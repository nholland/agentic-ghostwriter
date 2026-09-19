#!/usr/bin/env python3
"""
okf_index.py - reconcile okf/index.md with the concepts on disk.

WHY THIS IS A RECONCILER AND NOT A GENERATOR
    The obvious fix for an index that has drifted is to generate it. That is
    wrong here, and measurably so: of 89 citation rows, 73 carry editorial
    annotation that exists nowhere else - which chapter a source anchors, an
    effect size, a warning that the figures are not pinned to a primary - and
    all 87 framework and story rows carry a one-line gloss of the same kind.
    Seven titles are deliberate shortenings of a longer frontmatter title.
    Regenerating index.md from frontmatter would delete 249 hand-written lines
    and churn seven more, which is a worse failure than the drift it fixes.

    So this script owns exactly what is mechanically true - which concepts
    exist, and what status each citation carries - and never touches a word a
    person wrote. Membership and status are derived; annotation is preserved.

WHAT DRIFTS, AND WHY THE OLD CHECK COULD NOT SEE IT
    okf_validate.py compares COUNTS per type ("index.md lists 89 citations but
    112 exist on disk"). A count cannot see a row whose status contradicts the
    concept it points at, and on 2026-09-19 thirteen rows did - six of them
    claiming BETTER evidence than the file carries, which is Rule 4's
    overclaim sitting inside the book's own rollup. This reports per concept.

USAGE
    python3 scripts/okf_index.py            # report drift, exit 1 if any
    python3 scripts/okf_index.py --check    # same; the name okf_gate.py uses
    python3 scripts/okf_index.py --fix      # apply, then re-report
    python3 scripts/okf_index.py --json

EXIT CODES
    0  index and disk agree
    1  drift (or, with --fix, drift that --fix cannot repair on its own)
    2  could not run: no book, no index, unreadable frontmatter
"""

import argparse
import glob
import json
import os
import re
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402

# Sections this script owns, in index.md's own order. A type absent from
# index.md is reported, never invented: the section blurbs are hand-written and
# this script does not write prose.
TYPES = ["frameworks", "stories", "citations", "signals"]
STATUS_TYPES = {"citations"}          # only citations carry a status in the row
ROW = re.compile(r'^- \[(?P<title>.+?)\]\(/(?P<type>\w+)/(?P<name>[^)]+\.md)\)(?P<tail>.*)$', re.M)


def frontmatter(path):
    """Parse a concept's YAML frontmatter, or raise with the path named."""
    text = open(path, encoding="utf-8").read()
    parts = text.split("---")
    if len(parts) < 3:
        raise ValueError(f"{path}: no YAML frontmatter")
    return yaml.safe_load(parts[1]) or {}


def read_index(okf):
    path = os.path.join(okf, "index.md")
    if not os.path.isfile(path):
        return None, None
    return path, open(path, encoding="utf-8").read()


def survey(okf, text):
    """What the index lists, and what is on disk, per type."""
    listed = {t: {} for t in TYPES}
    for m in ROW.finditer(text):
        if m.group("type") in listed:
            listed[m.group("type")][m.group("name")] = {
                "title": m.group("title"), "tail": m.group("tail"), "row": m.group(0)}
    disk = {}
    for t in TYPES:
        disk[t] = {}
        for p in sorted(glob.glob(os.path.join(okf, t, "*.md"))):
            fm = frontmatter(p)
            disk[t][os.path.basename(p)] = {
                "title": str(fm.get("title", "")).strip(),
                "status": str(fm.get("status", "")).strip()}
    return listed, disk


def diff(listed, disk):
    missing, orphan, status = [], [], []
    for t in TYPES:
        for name, d in disk[t].items():
            if name not in listed[t]:
                missing.append({"type": t, "name": name, **d})
        for name in listed[t]:
            if name not in disk[t]:
                orphan.append({"type": t, "name": name, "title": listed[t][name]["title"]})
        if t in STATUS_TYPES:
            for name, row in listed[t].items():
                if name not in disk[t]:
                    continue
                m = re.search(r'status:\s*(\w+)', row["tail"])
                shown = m.group(1) if m else None
                real = disk[t][name]["status"]
                if real and shown != real:
                    status.append({"type": t, "name": name, "index": shown,
                                   "file": real, "row": row["row"]})
    return missing, orphan, status


def apply_fix(path, text, missing, orphan, status):
    """Append missing rows at the end of their section, drop orphan rows, and
    rewrite ONLY the status token of a disagreeing row. Every edit asserts its
    match count before writing (CLAUDE.md Rule 11); an ambiguous one is left
    alone and reported rather than guessed at."""
    unfixed = []

    for s in status:
        # Replace the status token in this row only, keeping the annotation
        # that follows it. Anchored on the row's own link, which is unique.
        pat = re.compile(r'(\]\(/%s/%s\)[^\n]*?status:\s*)(\w+)'
                         % (re.escape(s["type"]), re.escape(s["name"])))
        if len(pat.findall(text)) != 1:
            unfixed.append(f"status {s['name']}: {len(pat.findall(text))} matches, not 1")
            continue
        text = pat.sub(lambda m: m.group(1) + s["file"], text, count=1)

    for o in orphan:
        pat = re.compile(r'^- \[[^\]]*\]\(/%s/%s\)[^\n]*\n'
                         % (re.escape(o["type"]), re.escape(o["name"])), re.M)
        if len(pat.findall(text)) != 1:
            unfixed.append(f"orphan {o['name']}: not uniquely matched")
            continue
        text = pat.sub("", text, count=1)

    # Append per section, at the end of that section's existing rows. A new row
    # carries no gloss: the annotations here are editorial claims about the
    # book, and inventing one would be a claim nobody made (Rule 2, Rule 9).
    for t in TYPES:
        rows = [m for m in missing if m["type"] == t]
        if not rows:
            continue
        new = "".join(
            "- [%s](/%s/%s)%s\n" % (r["title"], t, r["name"],
                                    " — status: %s" % r["status"] if t in STATUS_TYPES and r["status"] else "")
            for r in sorted(rows, key=lambda r: r["title"]))
        last = None
        for m in ROW.finditer(text):
            if m.group("type") == t:
                last = m
        if last:
            text = text[:last.end() + 1] + new + text[last.end() + 1:]
        else:
            # No rows of this type yet: put them under the type's own heading,
            # after its blurb, leaving the blurb itself untouched.
            h = re.search(r'^## %s\s*$' % t.capitalize(), text, re.M)
            if not h:
                unfixed.append(f"{t}: no rows and no '## {t.capitalize()}' heading to add them under")
                continue
            nxt = re.search(r'^## ', text[h.end():], re.M)
            end = h.end() + (nxt.start() if nxt else len(text) - h.end())
            text = text[:end] + new + "\n" + text[end:]

    open(path, "w", encoding="utf-8").write(text)
    return unfixed


def main():
    ap = argparse.ArgumentParser(description="Reconcile okf/index.md with the concepts on disk.")
    ap.add_argument("--check", action="store_true", help="report only (the default)")
    ap.add_argument("--fix", action="store_true", help="apply what can be applied, then re-report")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("book_root", nargs="?", help="defaults to the resolved book")
    a = ap.parse_args()

    root = a.book_root
    if not root:
        repo, _, _ = resolve_book.resolve(resolve_book.load_config())
        if not repo:
            print("okf_index: no book repo resolvable - run scripts/resolve_book.py",
                  file=sys.stderr)
            return 2
        root = resolve_book.inspect(repo, require_okf=False)["info"].get("bookRoot")
    okf = os.path.join(root, "okf")
    path, text = read_index(okf)
    if not path:
        print(f"okf_index: no index.md under {okf}", file=sys.stderr)
        return 2

    try:
        listed, disk = survey(okf, text)
    except Exception as exc:
        print(f"okf_index: {exc}", file=sys.stderr)
        return 2

    missing, orphan, status = diff(listed, disk)
    unfixed = []
    if a.fix and (missing or orphan or status):
        unfixed = apply_fix(path, text, missing, orphan, status)
        _, text = read_index(okf)
        listed, disk = survey(okf, text)
        missing, orphan, status = diff(listed, disk)

    out = {"index": path, "missing": missing, "orphan": orphan,
           "status_mismatch": status, "unfixed": unfixed}
    if a.json:
        print(json.dumps(out, indent=2))
        return 1 if (missing or orphan or status or unfixed) else 0

    if not (missing or orphan or status or unfixed):
        counts = ", ".join("%d %s" % (len(disk[t]), t) for t in TYPES)
        print(f"okf_index: index.md agrees with the bundle ({counts}).")
        return 0

    print(f"okf_index: DRIFT in {path}")
    if missing:
        print(f"\n  on disk, absent from the index ({len(missing)}):")
        for m in missing:
            print(f"    + {m['type']}/{m['name']}")
    if orphan:
        print(f"\n  listed, but no such concept on disk ({len(orphan)}):")
        for o in orphan:
            print(f"    - {o['type']}/{o['name']}")
    if status:
        print(f"\n  status in the row disagrees with the concept ({len(status)}):")
        for s in status:
            worse = " <- index OVERSTATES the evidence" if (
                s["index"], s["file"]) in (("verifiable", "unverified"), ("verified", "verifiable"),
                                           ("verified", "unverified")) else ""
            print(f"    ! {s['name']}: index says {s['index']}, file says {s['file']}{worse}")
    if unfixed:
        print(f"\n  --fix could not repair ({len(unfixed)}) - left alone, not guessed at:")
        for u in unfixed:
            print(f"    ? {u}")
    if not a.fix:
        print("\n  Apply with: python3 scripts/okf_index.py --fix")
        print("  A new row is appended with no gloss: the annotations in this file are")
        print("  editorial claims about the book, and this script does not write those.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
