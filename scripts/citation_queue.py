#!/usr/bin/env python3
"""Regenerate the citation verification queue from the OKF citation ledger.

This replaces `sources/citation-manifest.md`, which was retired 2026-08-14.
That file was described by CLAUDE.md Rule 11 as "a derived, human-readable
table regenerated from those concepts", but nothing regenerated it and it
held quote-level data that existed nowhere else. So it was neither derived
nor maintained, and it drifted: its "Author Verification Queue" read "None
at this time" while seven concepts required a physical-copy check, and ten
of its fourteen quote rows had no concept counterpart at all.

This script closes that gap by making the derived view actually derived.
Every field it prints comes from `okf/citations/*.md` frontmatter, so the
queue cannot disagree with the ledger. Run it after any citation status
changes; it rewrites the output file wholesale.

Two independent axes are reported, because conflating them is what made the
old manifest's single status column lossy:

  status      unverified -> verifiable -> verified   (how confirmed is it?)
              Only the author may set `verified`, per CLAUDE.md Rule 11.
  quote_form  verbatim | paraphrase | none           (what needs checking?)
              A verbatim quote needs wording and punctuation checked against
              the edition. A paraphrase needs only the underlying idea
              confirmed. `none` means the source is cited, never quoted.

Usage:
    python3 scripts/citation_queue.py books/the-stoic-husband
    python3 scripts/citation_queue.py books/the-stoic-husband --check
"""

import argparse
import glob
import os
import re
import sys
from datetime import date

STATUS_ORDER = ["unverified", "verifiable", "verified", "superseded"]
OUTPUT_NAME = "citation-queue.md"


def parse_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    try:
        import yaml

        return yaml.safe_load(m.group(1)) or {}
    except ImportError:
        # Minimal fallback so the queue still builds without pyyaml installed.
        out = {}
        for line in m.group(1).splitlines():
            f = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if f and f.group(2) and not f.group(2).startswith(">"):
                out[f.group(1)] = f.group(2).strip().strip('"')
        return out


def collect(book_root):
    rows = []
    for path in sorted(glob.glob(os.path.join(book_root, "okf/citations/*.md"))):
        fm = parse_frontmatter(path)
        slug = os.path.basename(path)[:-3]
        chapters = fm.get("chapter_slugs") or []
        if isinstance(chapters, str):
            chapters = [c.strip() for c in chapters.strip("[]").split(",") if c.strip()]
        rows.append(
            {
                "slug": slug,
                "title": str(fm.get("title", slug)).strip('"'),
                "status": str(fm.get("status", "unspecified")).strip(),
                "quote_form": str(fm.get("quote_form", "—")).strip(),
                "chapters": chapters,
                "note": " ".join(str(fm.get("verification_note", "")).split()),
            }
        )
    return rows


def render(rows, book_root):
    by_status = {s: [r for r in rows if r["status"] == s] for s in STATUS_ORDER}
    other = [r for r in rows if r["status"] not in STATUS_ORDER]
    needs_you = by_status["unverified"] + by_status["verifiable"]

    L = []
    L.append("# Citation Verification Queue")
    L.append("")
    L.append(
        "> **Generated file — do not edit by hand.** Regenerate with "
        "`python3 scripts/citation_queue.py {}`.".format(book_root)
    )
    L.append(
        "> Every field is read from `okf/citations/*.md` frontmatter, which is "
        "canonical per CLAUDE.md Rule 11."
    )
    L.append(
        "> Edit the concept file, then re-run this script. Replaces the retired "
        "`sources/citation-manifest.md`."
    )
    L.append("")
    L.append(f"*Last generated: {date.today().isoformat()} — {len(rows)} citations.*")
    L.append("")
    L.append("## Where things stand")
    L.append("")
    L.append("| Status | Count | Meaning |")
    L.append("|---|---|---|")
    L.append(
        f"| `unverified` | {len(by_status['unverified'])} | Not yet confirmed against any source. |"
    )
    L.append(
        f"| `verifiable` | {len(by_status['verifiable'])} | Confirmed, but not by you. Still needs your physical-copy check before print. |"
    )
    L.append(
        f"| `verified` | {len(by_status['verified'])} | You confirmed it against your own copy. |"
    )
    L.append(
        f"| `superseded` | {len(by_status['superseded'])} | Replaced by a better source; no action. |"
    )
    if other:
        L.append(f"| *(no status)* | {len(other)} | Malformed frontmatter — fix these. |")
    L.append("")
    L.append(
        f"**{len(needs_you)} citations still need your attention** before publication."
    )
    L.append("")

    L.append("## Needs your physical copy")
    L.append("")
    L.append(
        "Sorted verbatim-quotes-first: those need exact wording *and* punctuation "
        "checked against the edition. Paraphrases need only the underlying idea "
        "confirmed."
    )
    L.append("")
    for form in ("verbatim", "paraphrase", "none", "—"):
        group = [r for r in needs_you if r["quote_form"] == form]
        if not group:
            continue
        heading = {
            "verbatim": "Verbatim quotes — check wording and punctuation",
            "paraphrase": "Paraphrases — check the idea, not the wording",
            "none": "Cited, never quoted — check the finding, not a quote",
            "—": "No `quote_form` recorded — needs one",
        }[form]
        L.append(f"### {heading} ({len(group)})")
        L.append("")
        L.append("| Citation | Status | Chapters | What's needed |")
        L.append("|---|---|---|---|")
        for r in sorted(group, key=lambda x: (x["status"], x["slug"])):
            note = r["note"] or "—"
            if len(note) > 300:
                note = note[:297] + "…"
            chaps = ", ".join(r["chapters"]) if r["chapters"] else "—"
            L.append(
                f"| [{r['title']}](okf/citations/{r['slug']}.md) | `{r['status']}` | {chaps} | {note} |"
            )
        L.append("")

    done = by_status["verified"] + by_status["superseded"]
    if done:
        L.append("## Settled — no action needed")
        L.append("")
        for r in sorted(done, key=lambda x: x["slug"]):
            L.append(
                f"- [{r['title']}](okf/citations/{r['slug']}.md) — `{r['status']}`"
            )
        L.append("")

    if other:
        L.append("## Malformed — missing or unrecognized `status`")
        L.append("")
        for r in other:
            L.append(f"- `okf/citations/{r['slug']}.md` — status: `{r['status']}`")
        L.append("")

    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("book_root", nargs="?", default="books/the-stoic-husband")
    ap.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if the file on disk differs from what would be generated",
    )
    args = ap.parse_args()

    rows = collect(args.book_root)
    if not rows:
        sys.stderr.write(f"no citations found under {args.book_root}/okf/citations/\n")
        return 1

    out_path = os.path.join(args.book_root, OUTPUT_NAME)
    content = render(rows, args.book_root)

    if args.check:
        current = open(out_path).read() if os.path.exists(out_path) else ""
        # ignore the generated-date line when comparing
        strip = lambda t: re.sub(r"\*Last generated: .*?\n", "", t)
        if strip(current) != strip(content):
            sys.stderr.write(
                f"{out_path} is stale. Run: python3 scripts/citation_queue.py {args.book_root}\n"
            )
            return 1
        print(f"{out_path} is current ({len(rows)} citations).")
        return 0

    open(out_path, "w", encoding="utf-8").write(content)
    needs = sum(1 for r in rows if r["status"] in ("unverified", "verifiable"))
    print(f"wrote {out_path} — {len(rows)} citations, {needs} awaiting author verification")
    return 0


if __name__ == "__main__":
    sys.exit(main())
