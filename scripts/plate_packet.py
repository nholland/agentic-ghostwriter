#!/usr/bin/env python3
"""Build the plate feedback packet: each plate on its own page, then its intent and takeaway.

Not the cold visual-only read runs/design/*-names-and-visual-summaries.md
gives (that document is deliberately blind, for testing whether the image
alone carries the argument). This is the opposite document: the author
showing others the intent, to get feedback on whether the plate delivers it.

Source of truth per plate, so nothing here is invented:
  - Plate title: this session's curated name
    (runs/design/2026-09-20-plate-names-and-visual-summaries.md), which
    already resolves the one open title/Mechanism mismatch (Ch5, #070).
  - Chapter plates: Mechanism, Conversation sentence and Lesson straight
    from books/the-stoic-husband/chapters/chNN/distillation.md - the same
    fields plate_brief.py extracts, read directly so every chapter is
    covered, not just the four with a brief on file.
  - Part plates: the Part's opening paragraph
    (books/the-stoic-husband/parts/part-N-*.md) as the intended sense, and
    the plate's own closing caption (read from the SVG) as the line it
    carries.

Reuses compile.py's plate discovery (chapter_plate/part_plate/parts) so the
page order and landed/draft status match the reader manuscript exactly, and
chapter_pdf_local.py's svg_to_png/CSS so the plate itself renders identically
to the shipped PDF.

USAGE
    python3 scripts/plate_packet.py --to 12
"""
import argparse
import datetime
import html as _html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import resolve_book  # noqa: E402
import compile as compilepy  # noqa: E402
from chapter_pdf_local import svg_to_png, md_inline, CHROME, FLAGS  # noqa: E402

NAMES_DOC = os.path.join(REPO, "runs", "design",
                          "2026-09-20-plate-names-and-visual-summaries.md")


def curated_names():
    """{'ch05': 'The Courage to Come Back', 'PART I': 'The Steady River', ...}
    parsed from the session's own naming pass, keyed the same way
    compile.py's plates list is. Each entry is a "## Title" section whose
    LAST non-blank line is a "*Chapter N*" / "*Part N ...*" tag - not
    necessarily the first italic line, since Ch5's entry carries an extra
    italic naming-note paragraph right after its heading (#070)."""
    text = open(NAMES_DOC, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        title = m.group(1).strip()
        lines = [ln for ln in m.group(2).strip().splitlines() if ln.strip()]
        if not lines:
            continue
        tag = lines[-1].strip().strip("*").strip()
        cm = re.match(r"Chapter (\d+)", tag)
        if cm:
            out["ch%02d" % int(cm.group(1))] = title
        pm = re.match(r"Part ([IVX]+)", tag)
        if pm:
            out["PART %s" % pm.group(1)] = title
    return out


def chapter_takeaway(B, n):
    """(mechanism, conversation, context, lesson) straight from the chapter's
    own distillation - the field plate_brief.py reads, read directly here so
    every chapter is covered, not only the four with a brief on file.

    `context` is the unlabelled paragraph the distillation puts between the
    Conversation sentence and the first **Label:** field. It is what the
    packet expands the one-line explanation into. Chapters differ on whether
    a blank line precedes it (Ch11 has none), so the span is bounded by the
    next label rather than by a paragraph break."""
    path = os.path.join(B, "chapters", "ch%02d" % n, "distillation.md")
    t = open(path, encoding="utf-8").read()
    mech = re.search(r"\*\*Mechanism:\*\*\s*(.+)", t)
    convo = re.search(r"\*\*Conversation sentence:\*\*\s*(.+)", t)
    lesson = re.search(r"\*\*Lesson:\*\*\s*(.+)", t)
    ctx = re.search(r"\*\*Conversation sentence:\*\*.*?\n(.*?)(?=\n\s*\*\*\w)", t, re.S)
    context = " ".join(ctx.group(1).split()) if ctx else ""
    return (mech.group(1).strip() if mech else "",
           convo.group(1).strip() if convo else "",
           context,
           lesson.group(1).strip() if lesson else "")


def part_takeaway(B, numeral):
    """(opening paragraph, closing caption) for a Part plate."""
    cand = [f for f in os.listdir(os.path.join(B, "parts"))
            if re.match(r"part-%d-" % compilepy.ROMAN[numeral], f)]
    opening = ""
    if cand:
        t = open(os.path.join(B, "parts", cand[0]), encoding="utf-8").read()
        m = re.search(r"\*(.+?)\*", t, re.S)
        opening = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    return opening


def svg_caption(svg_path):
    """The plate's closing line(s): every italic <text> element, in document
    order, joined - the Part plates split their one closing sentence across
    two consecutive italic lines (see plate-1-steady-river.svg)."""
    src = open(svg_path, encoding="utf-8").read()
    italics = re.findall(r'<text[^>]*font-style="italic"[^>]*>([^<]*)</text>', src)
    if italics:
        return " ".join(italics[-2:]) if len(italics) > 1 else italics[-1]
    texts = re.findall(r"<text[^>]*>([^<]*)</text>", src)
    return texts[-1] if texts else ""


CSS = """
@page { size: 6in 9in; margin: 0.75in 0.7in 0.8in 0.7in; }
html { -webkit-print-color-adjust: exact; }
body { font: 10.5pt/1.55 Georgia,'Liberation Serif',serif; color:#1a1a1a; margin:0; }
section.plate { page-break-after: always; text-align:center; min-height:7.3in;
    display:flex; flex-direction:column; align-items:center; justify-content:center; }
section.plate:first-of-type { }
section.plate img { max-width:100%; max-height:7in; height:auto; }
section.note { page-break-after: always; padding-top: 0.3in; }
section.note:last-of-type { page-break-after: auto; }
section.note .kicker { font:italic 9.5pt Georgia,serif; letter-spacing:.06em;
    color:#5a5a5a; text-align:center; margin:0 0 .3in; }
section.note h1 { font-size:19pt; font-weight:600; text-align:center; margin:0 0 .3in; }
section.note h2 { font:600 9.5pt Georgia,serif; letter-spacing:.14em; text-transform:uppercase;
    color:#5a5a5a; margin:.26in 0 .08in; border-bottom:.5pt solid #ddd; padding-bottom:.05in; }
section.note p { margin:0 0 .16in; text-align:left; }
section.note .mech { font:600 12pt Georgia,serif; letter-spacing:.06em; text-align:center; margin:0 0 .26in; }
section.note .convo { font:italic 12.5pt/1.5 Georgia,serif; text-align:center; margin:0 auto .1in; max-width:4.4in; }
"""


def note_page(kicker, title, rows):
    h = ['<section class="note">', '<p class="kicker">%s</p>' % md_inline(kicker),
        '<h1>%s</h1>' % md_inline(title)]
    for label, body, cls in rows:
        if not body:
            continue
        if cls:
            h.append('<p class="%s">%s</p>' % (cls, md_inline(body)))
        else:
            h.append('<h2>%s</h2><p>%s</p>' % (_html.escape(label), md_inline(body)))
    h.append('</section>')
    return "\n".join(h)


def main():
    ap = argparse.ArgumentParser(description="Build the plate feedback packet.")
    ap.add_argument("--to", type=int, default=12)
    ap.add_argument("--out")
    a = ap.parse_args()

    root, _, _ = resolve_book.resolve(resolve_book.load_config())
    if not root:
        print("plate_packet: no book repo resolvable.", file=sys.stderr)
        return 2
    rel = resolve_book.inspect(root, require_okf=True)["info"]["bookRootRelative"]
    B = os.path.join(root, rel)
    outline = open(os.path.join(B, "03-outline.md"), encoding="utf-8").read()
    names = curated_names()

    stamp = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    outdir = os.path.join(REPO, "runs", "manuscript")
    os.makedirs(outdir, exist_ok=True)
    out_pdf = a.out or os.path.join(
        outdir, "the-stoic-husband-plate-feedback-packet-ch01-ch%02d-%s.pdf" % (a.to, stamp))

    parts_list = compilepy.parts(outline)
    body = []
    n_plates, n_draft = 0, 0

    for n in range(1, a.to + 1):
        svg, landed = compilepy.chapter_plate(B, n)
        if not svg:
            print("  MISSING: ch%02d has no plate" % n)
            continue
        png = os.path.join(outdir, "packet-ch%02d.png" % n)
        w, h = svg_to_png(svg, png)
        n_plates += 1
        n_draft += 0 if landed else 1
        body.append('<section class="plate"><img src="%s" alt=""></section>'
                    % os.path.basename(png))
        title = names.get("ch%02d" % n, "Chapter %d" % n)
        mech, convo, context, lesson = chapter_takeaway(B, n)
        body.append(note_page(
            "Chapter %d" % n, title,
            [("", mech, "mech"), ("", convo, "convo"),
             ("What the plate is saying", context, None),
             ("Lesson - the takeaway", lesson, None)]))

        for numeral, ptitle, first_ch, last_ch, opening_f, closing in parts_list:
            if last_ch == n and last_ch <= a.to:
                svg, landed = compilepy.part_plate(B, numeral, closing)
                if not svg:
                    print("  MISSING: PART %s closing plate" % numeral)
                    continue
                png = os.path.join(outdir, "packet-part%s.png" % numeral)
                w, h = svg_to_png(svg, png)
                n_plates += 1
                n_draft += 0 if landed else 1
                body.append('<section class="plate"><img src="%s" alt=""></section>'
                            % os.path.basename(png))
                pname = names.get("PART %s" % numeral, "Part %s — %s" % (numeral, ptitle))
                opening = part_takeaway(B, numeral)
                cap = svg_caption(svg)
                body.append(note_page(
                    "Part %s closing plate" % numeral, pname,
                    [("The line it closes on", cap, "convo"),
                     ("What the Part sets up", opening, None)]))

    doc = ("<!doctype html><html><head><meta charset='utf-8'>"
          "<title>Plate feedback packet</title><style>%s</style></head>"
          "<body>%s</body></html>") % (CSS, "\n".join(body))
    html_path = os.path.splitext(out_pdf)[0] + ".html"
    open(html_path, "w", encoding="utf-8").write(doc)
    subprocess.run([CHROME, *FLAGS, "--no-pdf-header-footer",
                    "--print-to-pdf=%s" % out_pdf, "file://" + os.path.abspath(html_path)],
                   check=True, capture_output=True, timeout=180)
    size = os.path.getsize(out_pdf)
    print("  plates: %d (%d draft)" % (n_plates, n_draft))
    print("  html:   %s" % html_path)
    print("  pdf:    %s  (%d bytes)" % (out_pdf, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
