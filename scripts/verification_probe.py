#!/usr/bin/env python3
"""Determine which citation-verification lane is available, by probing hosts.

WHY THIS EXISTS. Network reachability varies by environment: a local CLI
session on the author's laptop reaches every source host, while the cloud
container routes through an egress proxy that blocks essentially every
scholarly and literary host (Project Gutenberg, Wikisource, archive.org,
PubMed, Standard Ebooks, author-hosted PDFs) while permitting dev hosts.

The LLM must not decide this from context, memory, or a `progress.md` entry.
A session that "remembers" Gutenberg is blocked will keep believing it after
the author moves to his laptop, and the remembered note will be dated and
plausible — the exact failure mode CLAUDE.md Rule 9 exists for. This follows
the Rule 10 precedent instead: a script decides, the LLM reads the output.

WHAT IT PROBES, AND WHY CURL. `curl` reachability is a valid predictor of
`WebFetch` reachability — both traverse the same egress proxy. Verified
2026-09-07 across five hosts: `raw.githubusercontent.com` reachable by both,
`gutenberg.org` / `en.wikipedia.org` / `pubmed.ncbi.nlm.nih.gov` /
`standardebooks.org` / `websites.umich.edu` blocked by both.

WHAT IT CANNOT PROBE. `WebSearch` does not traverse the container's egress at
all, so curl says nothing about it. Treat it as available and degrade if the
tool errors. This is why a "can I reach the network?" boolean is the wrong
question and this script asks a per-host one instead.

Usage:
    python3 scripts/verification_probe.py books/the-stoic-husband
    python3 scripts/verification_probe.py books/the-stoic-husband --json
    python3 scripts/verification_probe.py --hosts standardebooks.org,pubmed.ncbi.nlm.nih.gov
"""

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

# Hosts that carry the kinds of source this pipeline cites. Probed by default
# so the report is meaningful even for a book whose ledger names no URLs yet.
CANONICAL_HOSTS = [
    # public-domain primary texts
    "standardebooks.org",
    "www.gutenberg.org",
    "en.wikisource.org",
    "archive.org",
    "classics.mit.edu",
    "www.perseus.tufts.edu",
    # journals / bibliographic
    "pubmed.ncbi.nlm.nih.gov",
    "doi.org",
    "www.sciencedirect.com",
    "link.springer.com",
    # trade books
    "books.google.com",
]

TIMEOUT_S = 12


def probe_host(host):
    """Return (host, reachable, detail). Reachable means the proxy let us out.

    Any HTTP response at all counts as reachable — a 403 or 404 from the origin
    still proves egress. Only a transport failure (curl exit non-zero, or the
    000 status the proxy produces on a block) counts as blocked.
    """
    url = host if host.startswith("http") else f"https://{host}/"
    try:
        res = subprocess.run(
            ["curl", "-sS", "-o", os.devnull, "-w", "%{http_code}",
             "--max-time", str(TIMEOUT_S), "-I", url],
            capture_output=True, text=True, timeout=TIMEOUT_S + 5,
        )
    except (subprocess.TimeoutExpired, OSError) as exc:
        return host, False, f"probe failed: {type(exc).__name__}"
    code = (res.stdout or "").strip()[-3:]
    if res.returncode != 0 or code in ("", "000"):
        return host, False, "blocked by egress proxy"
    return host, True, f"HTTP {code}"


def hosts_from_ledger(book_root):
    """Hosts named by the book's own citations, so the probe covers what it needs."""
    cdir = os.path.join(book_root, "okf", "citations")
    found = set()
    if not os.path.isdir(cdir):
        return found
    for name in sorted(os.listdir(cdir)):
        if not name.endswith(".md"):
            continue
        try:
            text = open(os.path.join(cdir, name), encoding="utf-8").read()
        except OSError:
            continue
        for m in re.finditer(r"https?://([A-Za-z0-9.\-]+)", text):
            host = m.group(1).lower().rstrip(".")
            if "." in host and not host.endswith((".md", ".py")):
                found.add(host)
    return found


def citation_axes(book_root):
    """(slug, quote_form, status) for every citation, for the lane summary."""
    cdir = os.path.join(book_root, "okf", "citations")
    out = []
    if not os.path.isdir(cdir) or yaml is None:
        return out
    for name in sorted(os.listdir(cdir)):
        if not name.endswith(".md"):
            continue
        text = open(os.path.join(cdir, name), encoding="utf-8").read()
        if not text.startswith("---"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict):
            continue
        out.append((
            name[:-3],
            str(fm.get("quote_form", "")).strip(),
            str(fm.get("status", "")).strip(),
        ))
    return out


def lane_for(quote_form, any_source_host_reachable):
    """Tier x reachability -> lane. See `.claude/OKF.md` transcription rule.

    The load-bearing cell is verbatim + blocked -> C, never B. Search may flag
    a defect in a quotation but may never close one.
    """
    if not quote_form:
        return "unknown"          # can't tier it; needs backfill first
    if quote_form == "verbatim":
        return "A" if any_source_host_reachable else "C"
    return "A" if any_source_host_reachable else "B"


LANE_TEXT = {
    "A": "fetch the page and transcribe (WebFetch)",
    "B": "WebSearch for claim support only; >=2 independent listings, never confidence: high",
    "C": "export a packet for a session with real web access; do NOT close from search",
    "unknown": "no quote_form recorded — cannot tier; backfill before verifying",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book_root", nargs="?")
    ap.add_argument("--hosts", help="comma-separated hosts to probe instead of the defaults")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    if args.hosts:
        hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    else:
        hosts = list(CANONICAL_HOSTS)
        if args.book_root:
            hosts = sorted(set(hosts) | hosts_from_ledger(args.book_root))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(probe_host, hosts))

    reach = {h: ok for h, ok, _ in results}
    detail = {h: d for h, _, d in results}
    # Source hosts are the ones that carry citable text. Dev hosts being
    # reachable tells us nothing about whether we can verify a quotation.
    source_hosts = [h for h in hosts if h in CANONICAL_HOSTS]
    any_source = any(reach.get(h) for h in source_hosts)

    payload = {
        "any_source_host_reachable": any_source,
        "reachable": sorted(h for h in hosts if reach.get(h)),
        "blocked": sorted(h for h in hosts if not reach.get(h)),
        "detail": detail,
        "default_lane": "A" if any_source else "B/C by tier",
        "note": "WebSearch is not probed here — it does not traverse the "
                "container egress proxy. Assume available; degrade if it errors.",
    }

    if args.book_root:
        lanes = {}
        for slug, qf, status in citation_axes(args.book_root):
            if status in ("verified", "superseded"):
                continue
            lanes.setdefault(lane_for(qf, any_source), []).append(slug)
        payload["lanes"] = {k: sorted(v) for k, v in lanes.items()}

    if args.as_json:
        print(json.dumps(payload, indent=2))
        return 0

    print(f"Source hosts reachable: {'YES' if any_source else 'NO'}")
    print(f"  reachable ({len(payload['reachable'])}): "
          + (", ".join(payload["reachable"]) or "none"))
    print(f"  blocked   ({len(payload['blocked'])}): "
          + (", ".join(payload["blocked"]) or "none"))
    print("\n" + payload["note"])
    for lane, slugs in sorted(payload.get("lanes", {}).items()):
        print(f"\nLane {lane} — {LANE_TEXT[lane]}")
        print(f"  {len(slugs)} citation(s)")
        for s in slugs[:8]:
            print(f"    - {s}")
        if len(slugs) > 8:
            print(f"    ... and {len(slugs) - 8} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
