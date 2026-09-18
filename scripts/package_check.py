#!/usr/bin/env python3
"""package_check.py - check the artifact a reader actually receives.

WHY THIS EXISTS. Four defects reached the author in rendered output before this
existed: a blank plate, two overlapping labels, three formatting defects already
fixed once in the book repo's own renderer, and a PDF that opened on the
distillation. He found all four by opening the file, because no script in this
repo read a rendered artifact. Every gate stopped at markdown.
`gw-compile/SKILL.md` states the stake - "Nothing else in the house matters to a
reader" - and nothing executable stood behind the sentence.

The distillation case is the one that named the rule. `compile.py` lifts only the
Practice block out of a distillation and strips the rest, and the book's shipped
manuscript contains the word "distillation" zero times: it is working apparatus
that feeds the back-of-book practice guide. The renderer put it on page one. Two
parts of this repo disagreed about what a reader receives and nothing compared
them.

WHAT IT CANNOT DO. It reads the emitted HTML, not the rendered page, so it sees
ordering and apparatus and cannot see overlapping glyphs or a plate that renders
blank on someone else's machine. Those stay with the author and with
runs/design/svgcheck.py. A clean run here is not "the package is good"; it is
"the package does not have the three faults we have already shipped".

USAGE
    python3 scripts/package_check.py <package.html> [...]

EXIT
    0  every check passed
    1  at least one failed
    2  bad usage / unreadable input
"""
import re
import sys

# Headings that are working apparatus. A reader must never meet one.
APPARATUS = ("Draft Notes", "Editor's Notes", "Editors Notes", "Provenance",
             "Research Brief", "Brief Gaps", "Conformance")


def check(path):
    try:
        html = open(path, encoding="utf-8").read()
    except Exception as exc:
        return [f"UNREADABLE {path}: {exc}"], None

    fails = []
    sections = re.findall(r'<section(?:\s+class="([^"]*)")?>', html)
    first = (sections[0] or "chapter") if sections else None

    # 1. The package opens on the chapter, never on apparatus.
    if first is None:
        fails.append("no <section> found; cannot tell what the package opens on")
    elif "dist" in first and "distback" not in first:
        fails.append("opens on the distillation; the shipped manuscript has none")

    # 2. Any distillation is at the back and labelled as not-for-readers.
    if any("dist" in (c or "") for c in sections):
        if not any("distback" in (c or "") for c in sections):
            fails.append("a distillation section is not marked distback")
        if "Not part of the chapter" not in html:
            fails.append("apparatus present but not labelled as apparatus")

    # 3. No apparatus heading reached the reader.
    for word in APPARATUS:
        if re.search(r"<h[1-3][^>]*>[^<]*" + re.escape(word), html, re.I):
            fails.append(f"apparatus heading in reader output: {word!r}")

    return fails, first


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip().split("USAGE")[-1].strip(), file=sys.stderr)
        return 2
    bad = 0
    for path in argv[1:]:
        fails, first = check(path)
        if fails and fails[0].startswith("UNREADABLE"):
            print(f"[SKIP] {path}\n       {fails[0]}")
            return 2
        print(f"{'[FAIL]' if fails else '[ ok ]'} {path}")
        if first:
            print(f"       opens on: {first}")
        for f in fails:
            print(f"       {f}")
        bad += bool(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
