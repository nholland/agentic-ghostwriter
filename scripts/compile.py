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
    python3 scripts/compile.py --plates        # embed chapter and Part plates
    python3 scripts/compile.py --draft runs/ch11/refined.md \
        --distillation runs/ch11/distillation.md  # full review package

PLATES
    --plates embeds each chapter's plate (runs/chNN/plate.svg, the Designer's
    output; land.py copies it to design/plates/ unchanged, so the run copy is
    the one source) after the chapter's prose, and each Part's closing plate
    after the Part's last in-range chapter. A closing plate the outline names
    comes from the book tree; one that exists only in runs/parts/ is a draft.
    A plate whose identical copy is not in the book tree is unapproved, and
    the output filename says "plates-draft" so a reader copy never carries an
    unapproved draft unlabelled (Rule 15: coverage in the filename).
"""

import argparse
import datetime
import filecmp
import glob
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
    """[(numeral, title, first_ch, last_ch, opening_file, closing_plate)] from the outline itself."""
    out = []
    for m in re.finditer(r"^##\s*PART\s+([IVX]+)\s*[—-]\s*([^\n]+)\n(.*?)(?=^##\s*PART |\Z)",
                         outline_text, re.M | re.S):
        body = m.group(3)
        f = re.search(r"Reader-facing opening:\s*`([^`]+)`", body)
        c = re.search(r"Reader-facing closing plate:\s*`([^`]+)`", body)
        chs = [int(x) for x in re.findall(r"^##\s*Chapter\s+(\d+)", body, re.M)]
        if chs:
            out.append((m.group(1), m.group(2).strip(), min(chs), max(chs),
                        f.group(1) if f else None, c.group(1) if c else None))
    return out


ROMAN = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}


def chapter_plate(B, n):
    """(svg_path, landed) or (None, False). Landed means an identical copy
    sits in design/plates/, which is exactly what land.py produces."""
    run = os.path.join(REPO, "runs", "ch%02d" % n, "plate.svg")
    if not os.path.isfile(run):
        return None, False
    for cand in glob.glob(os.path.join(B, "design", "plates", "*.svg")):
        if filecmp.cmp(run, cand, shallow=False):
            return run, True
    return run, False


def part_plate(B, numeral, closing):
    """(svg_path, landed) or (None, False): the outline's file if on disk,
    else a draft in runs/parts/."""
    if closing and os.path.isfile(os.path.join(B, closing)):
        return os.path.join(B, closing), True
    drafts = sorted(glob.glob(os.path.join(REPO, "runs", "parts",
                                           "plate-%d-*.svg" % ROMAN[numeral])))
    return (drafts[0], False) if drafts else (None, False)


def plate_block(kind, svg, md_dir, alt):
    rel = os.path.relpath(svg, md_dir).replace(os.sep, "/")
    tag = "figure" if kind == "chapter" else "div"
    return '<%s class="plate"><img src="%s" alt="%s"></%s>' % (tag, rel, alt, tag)


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


DIST_FIELDS = ("Mechanism", "Conversation sentence", "Lesson", "Challenge", "Practice")


def draft_inputs(draft_path, dist_path):
    """Read explicit review inputs; never infer a different draft's distillation."""
    with open(draft_path, encoding="utf-8") as f:
        prose = strip_apparatus(f.read()).strip()
    with open(dist_path, encoding="utf-8") as f:
        dist = strip_apparatus(f.read()).strip()
    chapter = re.match(r"# Chapter (\d+):[^\n]+", prose)
    distilled = re.match(r"# Chapter (\d+) Distillation\b", dist)
    if not chapter or not distilled or int(chapter.group(1)) != int(distilled.group(1)):
        raise ValueError("draft and full distillation must have matching Chapter N headings")
    if not prose.partition("\n")[2].strip():
        raise ValueError("draft has no chapter prose")
    for label in DIST_FIELDS:
        field = re.search(r"^\*\*" + re.escape(label) +
                          r":\*\*\s*(.*?)(?=^\*\*[A-Za-z][^\n]*?:\*\*|\Z)",
                          dist, re.M | re.S)
        if not field or not field.group(1).strip():
            raise ValueError("full distillation is missing " + label)
        if label == "Practice" and not re.search(r"^\d+\.\s+\S", field.group(1), re.M):
            raise ValueError("full distillation has no numbered practices")
    return int(chapter.group(1)), prose, dist


def assemble_draft(prose, dist):
    """Both H1 headings start fresh pages in the existing renderers."""
    return prose + "\n\n" + dist + "\n"


def draft_package_problems(md, prose, dist):
    """Compare with both requested sources, not just the assembled input itself."""
    problems = []
    if not md.startswith(prose + "\n\n"):
        problems.append("chapter prose missing, changed, or not first")
    if md[len(prose) + 2:] != dist + "\n":
        problems.append("requested full distillation missing, changed, or not last")
    if re.search(APPARATUS, md, re.M | re.I):
        problems.append("apparatus reached the draft package")
    return problems


def compile_draft(a):
    try:
        n, prose, dist = draft_inputs(a.draft, a.distillation)
        md = assemble_draft(prose, dist)
        problems = draft_package_problems(md, prose, dist)
        if problems:
            raise ValueError("; ".join(problems))
    except (OSError, ValueError) as exc:
        print("compile: draft package refused: %s" % exc, file=sys.stderr)
        return 1

    outdir = os.path.join(REPO, "output", "compiled", "assets", "chapters")
    os.makedirs(outdir, exist_ok=True)
    stem = "ch%02d-review-draft" % n
    md_path = os.path.join(outdir, stem + ".md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print("compile: %s" % os.path.relpath(md_path, REPO))
    print("  chapter %d followed by complete distillation; no editorial notes" % n)
    if a.no_pdf:
        return 0
    return render_package(REPO, md_path, os.path.join(REPO, "output", "compiled", "chapters", "ch%02d.pdf" % n),
                          "Chapter %d (review draft with full distillation)" % n)


def render_package(root, md_path, pdf_path, title):
    """Use the approved renderer, including full distillation and any current plate."""
    import chapter_pdf_local as renderer
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    text = io.open(md_path, encoding='utf-8').read()
    match = re.search(r'^# Chapter (\d+) Distillation\b', text, re.M)
    prose, dist = (text[:match.start()], text[match.start():]) if match else (text, None)
    plates = []
    if match:
        n = int(match.group(1))
        svg = os.path.join(root, 'runs', 'ch%02d' % n, 'plate.svg')
        if os.path.isfile(svg):
            png = os.path.join(os.path.dirname(pdf_path), 'ch%02d-plate.png' % n)
            box = renderer.svg_to_png(svg, png)
            plates.append(('END', png, '', box))
    try:
        renderer.build(prose, dist, plates, pdf_path, title, base_dir=os.path.dirname(md_path))
    except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
        print('  renderer failed: %s' % exc)
        return 1
    print("  %s" % os.path.relpath(pdf_path, REPO))
    return 0


def main():
    ap = argparse.ArgumentParser(description="Assemble a reader-facing manuscript.")
    ap.add_argument("--from", dest="lo", type=int)
    ap.add_argument("--to", dest="hi", type=int)
    ap.add_argument("--no-pdf", action="store_true")
    ap.add_argument("--plates", action="store_true",
                    help="embed chapter plates and Part closing plates")
    ap.add_argument("--include-run", type=int, action="append", default=[],
                    help="Explicitly include an unlanded chapter from runs/")
    ap.add_argument("--outdir", default=os.path.join(REPO, "output", "compiled", "assets"))
    ap.add_argument("--draft", help="explicit chapter Markdown for a review package")
    ap.add_argument("--distillation", help="full distillation Markdown, required with --draft")
    a = ap.parse_args()
    if a.draft or a.distillation:
        if not (a.draft and a.distillation):
            ap.error("--draft and --distillation must be supplied together")
        if a.lo is not None or a.hi is not None or a.plates or a.include_run:
            ap.error("draft packages cannot combine --from/--to/--plates")
        return compile_draft(a)
    a.lo = 1 if a.lo is None else a.lo

    root, _, _ = resolve_book.resolve(resolve_book.load_config())
    if not root:
        print("compile: no book repo resolvable.", file=sys.stderr)
        return 2
    rel = resolve_book.inspect(root, require_okf=True)["info"]["bookRootRelative"]
    B = os.path.join(root, rel)
    outline = io.open(os.path.join(B, "03-outline.md"), encoding="utf-8").read()

    def chapter_dir(n):
        return os.path.join(REPO, "runs", "ch%02d" % n) if n in a.include_run else os.path.join(B, "chapters", "ch%02d" % n)

    have = []
    for n in range(a.lo, (a.hi or 99) + 1):
        if os.path.isfile(os.path.join(chapter_dir(n), "refined.md")):
            have.append(n)
    if not have:
        print("compile: no refined chapters in that range.", file=sys.stderr)
        return 1
    lo, hi = min(have), max(have)

    crossed = [p for p in parts(outline) if p[2] <= hi and p[3] >= lo]
    pieces, sections, missing_part_files = [], [], []
    plates = []   # (label, svg, landed) in page order
    plate_missing = []
    outdir = os.path.abspath(a.outdir)
    os.makedirs(outdir, exist_ok=True)

    for key in PRECURSORS:
        src = os.path.join(B, "chapters", key, "refined.md")
        if os.path.isfile(src):
            pieces.append(strip_apparatus(io.open(src, encoding="utf-8").read()))
            sections.append(key)

    for numeral, title, first, last, opening, closing in crossed:
        if opening:
            path = os.path.join(B, opening)
            if os.path.isfile(path):
                pieces.append(strip_apparatus(io.open(path, encoding="utf-8").read()))
                sections.append("PART %s opening" % numeral)
            else:
                missing_part_files.append(opening)
        in_part = [c for c in have if first <= c <= last]
        for n in in_part:
            d = chapter_dir(n)
            body = strip_apparatus(io.open(os.path.join(d, "refined.md"),
                                           encoding="utf-8").read())
            if a.plates:
                svg, landed = chapter_plate(B, n)
                if svg:
                    body += "\n\n" + plate_block("chapter", svg, outdir,
                                                 "Plate, Chapter %d" % n)
                    plates.append(("ch%02d" % n, svg, landed))
                else:
                    plate_missing.append("ch%02d" % n)
            pr = practice(os.path.join(d, "distillation.md"))
            if pr:
                # The pb marker, not a "## Putting It Into Practice" heading
                # alone: a heading has no page-break CSS of its own (other
                # h2s appear inside chapter prose, e.g. the Introduction's
                # sub-sections, and must NOT force a break), so the section
                # needs its own explicit break point.
                body += "\n\n<div class=\"pb\"></div>\n\n## Putting It Into Practice\n\n" + pr + "\n"
            pieces.append(body)
            sections.append("ch%02d" % n)
        if a.plates and in_part:
            svg, landed = part_plate(B, numeral, closing)
            if svg:
                pieces.append(plate_block("part", svg, outdir,
                                          "Closing plate, Part %s" % numeral))
                sections.append("PART %s closing plate" % numeral)
                note = "" if in_part[-1] == last else " (after ch%02d; Part incomplete)" % in_part[-1]
                plates.append(("PART %s%s" % (numeral, note), svg, landed))
            else:
                plate_missing.append("PART %s closing" % numeral)

    # Date and clock: two compiles on one day went out under one name on
    # 2026-09-20 and the author read the older one as the newer. Rule 15.
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d-%H%M")
    header = (
        "<!-- Generated by scripts/compile.py. Do not edit by hand. -->\n"
        "<!-- Coverage: %s. Chapters: %d of %d in range %d-%d. -->\n"
        "<!-- Precursors: %s. Part openings: %d of %d crossed. Built: %s. -->\n"
        % (", ".join(sections), len([s for s in sections if s.startswith("ch")]),
           hi - lo + 1, lo, hi,
           ", ".join(p for p in PRECURSORS
                     if os.path.isfile(os.path.join(B, "chapters", p, "refined.md")))
           or "none",
           len([s for s in sections if s.startswith("PART") and "opening" in s]),
           len(crossed), today))
    if a.plates:
        header += ("<!-- Plates: %s. Missing: %s. -->\n"
                   % (", ".join("%s=%s" % (lab, "landed" if ok else "DRAFT")
                                for lab, _, ok in plates) or "none",
                      ", ".join(plate_missing) or "none"))
    header += "<!-- Unapproved chapter runs: %s. -->\n\n" % a.include_run

    # No manual page-break marker between pieces: every piece (a precursor,
    # a Part opening, a chapter) starts with its own h1, and h1 already
    # forces a fresh page in both renderers' CSS. The literal "\pagebreak"
    # text this used to insert here was never interpreted by either
    # renderer - neither has ever defined that token - so it printed
    # verbatim as visible text on the page instead of breaking anything.
    md = header + "\n\n".join(pieces) + "\n"
    stem = "prologue-ch%02d" % hi if lo == 1 else "ch%02d-ch%02d" % (lo, hi)
    if a.plates:
        stem += "-plates" + ("" if all(ok for _, _, ok in plates) else "-draft")
    md_path = os.path.join(outdir, "manuscript.md")
    io.open(md_path, "w", encoding="utf-8").write(md)

    # --- assertions, before anything is called a success -------------------
    problems = list("missing Part opening file on disk: " + f for f in missing_part_files)
    for numeral, title, _, _, opening, _ in crossed:
        if opening and opening not in missing_part_files:
            key = os.path.splitext(os.path.basename(opening))[0].split("-", 2)[-1]
            if key.replace("-", " ").lower() not in md.lower():
                problems.append("PART %s opening did not reach the manuscript" % numeral)
    want = sum(1 for n in have
               if practice(os.path.join(chapter_dir(n), "distillation.md")))
    got = md.count("## Putting It Into Practice")
    if got != want:
        problems.append("%d Practice sections, but %d chapters have one" % (got, want))
    if re.search(APPARATUS, md, re.M | re.I):
        problems.append("apparatus reached the manuscript")
    order = [int(x) for x in re.findall(r"^#\s*Chapter\s+(\d+)", md, re.M)]
    if order != sorted(order):
        problems.append("chapters are out of order: %s" % order)
    if a.plates:
        embedded = re.findall(r'class="plate"><img src="([^"]+)"', md)
        if len(embedded) != len(plates):
            problems.append("%d plates embedded, %d expected" % (len(embedded), len(plates)))
        for rel in embedded:
            if not os.path.isfile(os.path.join(outdir, rel)):
                problems.append("plate path does not resolve from the manuscript: " + rel)

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
    if a.plates:
        print("  plates: %d embedded (%d landed, %d draft); missing: %s"
              % (len(plates), sum(1 for p in plates if p[2]),
                 sum(1 for p in plates if not p[2]), ", ".join(plate_missing) or "none"))
        for lab, svg, ok in plates:
            print("    %-8s %-6s %s" % (lab, "landed" if ok else "DRAFT", os.path.relpath(svg, REPO)))

    if a.no_pdf:
        return 0
    pdf_path = os.path.join(os.path.dirname(outdir), "book.pdf")
    return render_package(root, md_path, pdf_path, "River, Oak, Sun: The Stoic Husband (%s)" % stem)


if __name__ == "__main__":
    sys.exit(main())
