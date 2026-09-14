#!/usr/bin/env python3
"""
practice_sync.py - prove the practice guide still quotes the distillations.

WHY THIS EXISTS
    Three artifacts carry a chapter's practices: chapters/chNN/distillation.md
    (the pipeline handle), the compiled manuscript's "Putting It Into Practice"
    close (generated from it), and appendix/practice-guide.md (the back-of-book
    guide). The author ruled on 2026-09-14 that the guide carries practices
    only, taken verbatim from the distillation.

    Verbatim was not decorative. Measured the same day across all eleven
    refined chapters: ten guide entries matched their distillation exactly and
    Chapter 1 did not - the manuscript asked the reader "What's this actually
    about for me right now, and how do I want to respond?" while the guide
    asked "Am I being the best husband I can be right now?" Two different
    questions under one practice, shipped, for weeks, in an artifact nobody
    owned.

    That measurement was an ad-hoc command typed once. The rule that replaced
    it was a paragraph in an agent file. Neither runs on its own, and the
    ledger's own conclusion applies: no amount of rule text fixes this; what
    is missing is a check that runs without being remembered. So this is that
    check, and it has callers - /gw-refine step 4 and /gw-qa.

WHAT IT IS HONEST ABOUT
    A chapter with no guide section yet is reported MISSING, not PASS. A
    chapter whose distillation has no Practice block is reported UNCHECKED.
    Neither is a pass, and both are named.

USAGE
    python3 scripts/practice_sync.py                # every chapter, runs/ tree
    python3 scripts/practice_sync.py 12             # one chapter
    python3 scripts/practice_sync.py --book         # the book repo's tree
    python3 scripts/practice_sync.py --json

EXIT CODES
    0  every guide practice byte-identical to its distillation's
    1  at least one divergence, or a section is MISSING
    2  bad usage, or nothing to compare
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402

ITEM = re.compile(r"^[ \t]*\d+\.[ \t]+(.*?)(?=^[ \t]*\d+\.[ \t]|\Z)", re.M | re.S)
SECTION = re.compile(r"^##[ \t]+Chapter[ \t]+(\d+)[^\n]*$\n(.*?)(?=^##[ \t]+Chapter[ \t]|\Z)",
                     re.M | re.S)
# The tag the guide now carries. Stripped before comparing: it is the guide's
# own addition, not a change to the author's words.
TAG = re.compile(r"^\*\*(?:Proactive|Reactive)\.\*\*\s*")


def norm(item):
    """Collapse whitespace and drop the Proactive/Reactive tag.

    Byte-identical is the intent, but a markdown list re-wrapped at a different
    column is the same words. Comparing collapsed whitespace catches a reworded
    practice - the defect that actually happened - without failing on a rewrap.
    """
    return re.sub(r"\s+", " ", TAG.sub("", item.strip())).strip()


def items(text):
    return [norm(m) for m in ITEM.findall(text) if norm(m)]


def practices_from_distillation(path):
    try:
        raw = open(path, encoding="utf-8").read()
    except Exception:
        return None
    if "**Practice:**" not in raw:
        return None
    return items(raw.split("**Practice:**")[-1])


def main():
    ap = argparse.ArgumentParser(description="Guide practices vs distillation practices.")
    ap.add_argument("chapter", nargs="?", help="one chapter number; omit for all")
    ap.add_argument("--book", action="store_true",
                    help="check the book repo's tree instead of this repo's runs/")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.book:
        cfg = resolve_book.load_config()
        repo_root, _, _ = resolve_book.resolve(cfg)
        if not repo_root:
            print("practice_sync: no book repo resolvable - run scripts/resolve_book.py",
                  file=sys.stderr)
            return 2
        root = resolve_book.inspect(repo_root, require_okf=False)["info"].get("bookRoot")
        if not root:
            print("practice_sync: no bookRoot", file=sys.stderr)
            return 2
        guide = os.path.join(root, "appendix", "practice-guide.md")
        chdir = os.path.join(root, "chapters")
        label = "book repo"
    else:
        root = os.path.join(REPO, "runs")
        guide = os.path.join(root, "appendix", "practice-guide.md")
        chdir = root
        label = "runs/"

    if not os.path.isfile(guide):
        print(f"practice_sync: no practice guide at {guide} - nothing to compare "
              f"({label}). UNCHECKED, not passed.", file=sys.stderr)
        return 2

    sections = dict(SECTION.findall(open(guide, encoding="utf-8").read()))
    wanted = [a.chapter.lstrip("0")] if a.chapter else sorted(sections, key=int)
    if not wanted:
        print(f"practice_sync: the guide has no chapter sections yet ({label}). "
              f"UNCHECKED, not passed.", file=sys.stderr)
        return 2

    rows, bad = [], 0
    for n in wanted:
        num = int(n)
        dist = os.path.join(chdir, f"ch{num:02d}", "distillation.md")
        g = items(sections[n]) if n in sections else None
        d = practices_from_distillation(dist)
        if g is None:
            status, note = "MISSING", f"no '## Chapter {num}' section in the guide"
            bad += 1
        elif d is None:
            status, note = "UNCHECKED", f"no **Practice:** block in {os.path.relpath(dist, REPO)}"
        elif g == d:
            status, note = "PASS", f"{len(g)} practice(s) identical"
        else:
            status, note = "FAIL", f"guide {len(g)} item(s), distillation {len(d)}"
            bad += 1
            for i in range(max(len(g), len(d))):
                gi, di = (g[i] if i < len(g) else None), (d[i] if i < len(d) else None)
                if gi != di:
                    note += (f"\n      item {i + 1} diverges"
                             f"\n        guide:        {(gi or '(absent)')[:110]}"
                             f"\n        distillation: {(di or '(absent)')[:110]}")
        rows.append({"chapter": num, "status": status, "note": note})

    if a.json:
        print(json.dumps({"source": label, "rows": rows}, indent=2))
        return 1 if bad else 0

    print(f"practice_sync: {os.path.relpath(guide, REPO)} vs each chapter's distillation ({label})")
    for r in rows:
        print(f"  [{r['status']:<9}] Chapter {r['chapter']:<3} {r['note']}")
    unchecked = [r["chapter"] for r in rows if r["status"] == "UNCHECKED"]
    print(f"\n  RESULT: {'FAIL' if bad else 'PASS'} on {len(rows)} chapter(s)")
    if unchecked:
        print(f"  UNCHECKED (not passed): chapter(s) {', '.join(map(str, unchecked))}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
