#!/usr/bin/env python3
"""
compile.py - assemble a reader-facing manuscript, and check what it produced.

WHY THIS IS A SCRIPT
    On 2026-09-15 the first compiled manuscript was assembled by a model
    following the ~200 words of assembly rules in /gw-compile's skill. It dropped
    both Part opening pages the range crossed. Nothing noticed: the skill's only
    mechanical check is a word-count delta against the previous compile, the two
    pages are about 120 words (0.5% of the book, under any noise floor), and it
    was the first compile so there was no previous one to compare against. The
    incumbent pipeline's own manuscript.md had both pages, so the replacement was
    quietly less complete than the thing it replaces - in a stage the incumbent
    had already solved.

    The verification that was done checked the two traps the skill tells stories
    about (apparatus leaking, the **Practice:** field) and not the requirement in
    the same skill that had no story attached. That is a model following prose,
    which is the failure LEARNINGS.md closes everywhere else with a script.

WHAT IT ASSERTS BEFORE IT CLAIMS SUCCESS
    Every Part opening the range crosses is present; one Practice section per
    in-range distillation; no apparatus; chapters in order. A delta is relative
    and cannot see a defect that is already in the baseline, so these are
    absolute checks against the outline and the files on disk.

USAGE
    python3 scripts/compile.py                 # everything refined
    python3 scripts/compile.py --to 11         # precursors through chapter 11
    python3 scripts/compile.py --from 1 --to 5
    python3 scripts/compile.py --no-pdf
"""

import argparse
import datetime
import io
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402

PRECURSORS = ["prologue", "introduction"]
APPARATUS = r"^#{1,6}\s*(Editor's Notes|Draft Notes|Notes for the Editor|Provenance|Conformance)"


def parts(outline_text):
    """[(numeral, title, first_ch, last_ch, opening_file)] from the outline itself."""
    out = []
    for m in re.finditer(r"^##\s*PART\s+([IVX]+)\s*[—-]\s*([^\n]+)\n(.*?)(?=^##\s*PART |\Z)",
                         outline_text, re.M | re.S):
        body = m.group(3)
        f = re.search(r"Reader-facing opening:\s*`([^`]+)`", body)
        chs = [int(x) for x in re.findall(r"^##\s*Chapter\s+(\d+)", body, re.M)]
        if chs:
            out.append((m.group(1), m.group(2).strip(), min(chs), max(chs),
                        f.group(1) if f else None))
    return out


def strip_apparatus(text):
    """Prose ends at the first apparatus heading - the boundary voice_check owns."""
    cut = re.search(APPARATUS, text, re.M | re.I)
    return (text[:cut.start()] if cut else text).rstrip()


def practice(dist_path):
    """The **Practice:** FIELD, never a '## Practice' heading. The old compile
    looked for the heading and silently dropped ten sections, 1,700 words."""
    if not os.path.isfile(dist_path):
        return None
    t = io.open(dist_path, encoding="utf-8").read()
    m = re.search(r"\*\*Practice:\*\*\s*(.+?)(?=\n\s*\n|\n\*\*|\Z)", t, re.S)
    return m.group(1).strip() if m and m.group(1).strip() else None


def main():
    ap = argparse.ArgumentParser(description="Assemble a reader-facing manuscript.")
    ap.add_argument("--from", dest="lo", type=int, default=1)
    ap.add_argument("--to", dest="hi", type=int)
    ap.add_argument("--no-pdf", action="store_true")
    a = ap.parse_args()

    root, _, _ = resolve_book.resolve(resolve_book.load_config())
    if not root:
        print("compile: no book repo resolvable.", file=sys.stderr)
        return 2
    rel = resolve_book.inspect(root, require_okf=True)["info"]["bookRootRelative"]
    B = os.path.join(root, rel)
    outline = io.open(os.path.join(B, "03-outline.md"), encoding="utf-8").read()

    have = []
    for n in range(a.lo, (a.hi or 99) + 1):
        if os.path.isfile(os.path.join(B, "chapters", "ch%02d" % n, "refined.md")):
            have.append(n)
    if not have:
        print("compile: no refined chapters in that range.", file=sys.stderr)
        return 1
    lo, hi = min(have), max(have)

    crossed = [p for p in parts(outline) if p[2] <= hi and p[3] >= lo]
    pieces, sections, missing_part_files = [], [], []

    for key in PRECURSORS:
        src = os.path.join(B, "chapters", key, "refined.md")
        if os.path.isfile(src):
            pieces.append(strip_apparatus(io.open(src, encoding="utf-8").read()))
            sections.append(key)

    for numeral, title, first, last, opening in crossed:
        if opening:
            path = os.path.join(B, opening)
            if os.path.isfile(path):
                pieces.append(strip_apparatus(io.open(path, encoding="utf-8").read()))
                sections.append("PART %s opening" % numeral)
            else:
                missing_part_files.append(opening)
        for n in [c for c in have if first <= c <= last]:
            d = os.path.join(B, "chapters", "ch%02d" % n)
            body = strip_apparatus(io.open(os.path.join(d, "refined.md"),
                                           encoding="utf-8").read())
            pr = practice(os.path.join(d, "distillation.md"))
            if pr:
                body += "\n\n## Putting It Into Practice\n\n" + pr + "\n"
            pieces.append(body)
            sections.append("ch%02d" % n)

    today = datetime.date.today().isoformat()
    header = (
        "<!-- Generated by scripts/compile.py. Do not edit by hand. -->\n"
        "<!-- Coverage: %s. Chapters: %d of %d in range %d-%d. -->\n"
        "<!-- Precursors: %s. Part openings: %d of %d crossed. Built: %s. -->\n\n"
        % (", ".join(sections), len([s for s in sections if s.startswith("ch")]),
           hi - lo + 1, lo, hi,
           ", ".join(p for p in PRECURSORS
                     if os.path.isfile(os.path.join(B, "chapters", p, "refined.md")))
           or "none",
           len([s for s in sections if s.startswith("PART")]), len(crossed), today))

    md = header + "\n\n\\pagebreak\n\n".join(pieces) + "\n"
    outdir = os.path.join(REPO, "runs", "manuscript")
    os.makedirs(outdir, exist_ok=True)
    stem = "prologue-ch%02d" % hi if lo == 1 else "ch%02d-ch%02d" % (lo, hi)
    md_path = os.path.join(outdir, "manuscript-%s-%s.md" % (stem, today))
    io.open(md_path, "w", encoding="utf-8").write(md)

    # --- assertions, before anything is called a success -------------------
    problems = list("missing Part opening file on disk: " + f for f in missing_part_files)
    for numeral, title, _, _, opening in crossed:
        if opening and opening not in missing_part_files:
            key = os.path.splitext(os.path.basename(opening))[0].split("-", 2)[-1]
            if key.replace("-", " ").lower() not in md.lower():
                problems.append("PART %s opening did not reach the manuscript" % numeral)
    want = sum(1 for n in have
               if practice(os.path.join(B, "chapters", "ch%02d" % n, "distillation.md")))
    got = md.count("## Putting It Into Practice")
    if got != want:
        problems.append("%d Practice sections, but %d chapters have one" % (got, want))
    if re.search(APPARATUS, md, re.M | re.I):
        problems.append("apparatus reached the manuscript")
    order = [int(x) for x in re.findall(r"^#\s*Chapter\s+(\d+)", md, re.M)]
    if order != sorted(order):
        problems.append("chapters are out of order: %s" % order)

    if problems:
        print("compile: %d problem(s); the manuscript was written but is NOT clean:"
              % len(problems))
        for p in problems:
            print("  x %s" % p)
        return 1

    words = len(md.split())
    print("compile: %s" % os.path.relpath(md_path, REPO))
    print("  %d sections, %d words" % (len(sections), words))
    print("  Part openings: %s"
          % (", ".join("PART %s" % p[0] for p in crossed) or "none crossed"))

    if a.no_pdf:
        return 0
    renderer = os.path.join(root, "scripts", "chapter_pdf.py")
    if not os.path.isfile(renderer):
        print("  no renderer in the book repo; markdown only.")
        return 0
    pdf_path = md_path.replace("manuscript-", "the-stoic-husband-").replace(".md", ".pdf")
    r = subprocess.run([sys.executable, renderer, "--markdown", md_path, pdf_path],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("  renderer failed:\n%s" % (r.stderr or r.stdout)[-400:])
        return 1
    print("  %s" % os.path.relpath(pdf_path, REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
