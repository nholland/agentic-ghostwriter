#!/usr/bin/env python3
"""Render a chapter to PDF with headless Chromium.

WHY THIS EXISTS, and why it is not a second renderer in the sense
gw-compile/SKILL.md forbids: the book repo's `chapter_pdf.py` is the one
renderer and it cannot run in this container - weasyprint, pandoc and
wkhtmltopdf are all absent and pip cannot reach PyPI through the egress
proxy. This is a fallback that produces the reader package here, and it is
registered in GAPS.md as such. When the container can run the book's
renderer, this goes away.

Two choices are deliberate and worth stating:

  Plates are rasterised to high-DPI PNG rather than inlined as SVG. An SVG's
  labels become extractable text in a PDF, and the author listens to every
  chapter through a PDF-to-speech reader, which would read those labels aloud
  in the middle of a sentence. Raster keeps them printable and keeps them out
  of the audio.

  No running headers or footers, and no page numbers. Same reason: anything
  repeated on every page is read aloud on every page.
"""
import html as _html
import os
import re
import subprocess
import sys

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FLAGS = ["--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars"]


def md_inline(t):
    t = _html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
    t = re.sub(r"`([^`]+?)`", r"<code>\1</code>", t)
    # curly quotes and apostrophes, for print
    t = re.sub(r'"([^"]*)"', lambda m: "“" + m.group(1) + "”", t)
    t = t.replace("'", "’")
    return t


LABEL = re.compile(r"^\*\*[A-Z][A-Za-z ]{1,24}:\*\*")
DISPLAY_QUOTE = re.compile(r'^\*"(.+?)"\*\s*(?:\((.+)\))?\s*$')


def md_to_html(md):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s in ("---", "***", "___"):
            out.append('<hr class="beat">')
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{md_inline(m.group(2))}</h{lvl}>")
            i += 1
            continue
        if s.startswith("> "):
            buf = []
            while i < len(lines) and lines[i].strip().startswith("> "):
                buf.append(lines[i].strip()[2:])
                i += 1
            out.append("<blockquote><p>" + md_inline(" ".join(buf)) + "</p></blockquote>")
            continue
        if re.match(r"^\d+\.\s+", s):
            buf = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i].strip()):
                buf.append(re.sub(r"^\d+\.\s+", "", lines[i].strip()))
                i += 1
            out.append("<ol>" + "".join(f"<li>{md_inline(x)}</li>" for x in buf) + "</ol>")
            continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
                r"^(#{1,4}\s|>\s|---$|\d+\.\s)", lines[i].strip()):
            # A label line - "**Lesson:**", "**Challenge:**" - is its own
            # paragraph even when the source puts it on the very next line with
            # no blank between. Without this, Lesson and Challenge merge into
            # one block and the distillation reads as a wall.
            if buf and LABEL.match(lines[i].strip()):
                break
            buf.append(lines[i].strip())
            i += 1
        raw = " ".join(buf)

        # A paragraph that is nothing but an italicised quotation, optionally
        # followed by a parenthetical citation, is a display quote - the
        # chapter's Stoic anchor is written this way. Setting it as a
        # blockquote is what the author asked for when he asked that quotes be
        # formatted appropriately; left inline it reads as ordinary italics.
        q = DISPLAY_QUOTE.match(raw)
        if q:
            cite = f'<cite>{md_inline(q.group(2))}</cite>' if q.group(2) else ""
            out.append('<blockquote class="pull"><p>\u201c'
                       + md_inline(q.group(1)) + '\u201d</p>' + cite + "</blockquote>")
            continue

        para = md_inline(raw)
        cls = ' class="runin"' if para.startswith("<strong>") else ""
        out.append(f"<p{cls}>{para}</p>")
    return "\n".join(out)


def svg_to_png(svg_path, png_path, scale=3):
    src = open(svg_path, encoding="utf-8").read()
    m = re.search(r'viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)"', src)
    w, h = (float(m.group(1)), float(m.group(2))) if m else (640.0, 450.0)
    wrap = f"<!doctype html><style>*{{margin:0;padding:0}}body{{width:{w}px;height:{h}px}}svg{{display:block;width:{w}px;height:{h}px}}</style>{src}"
    tmp = png_path + ".html"
    open(tmp, "w", encoding="utf-8").write(wrap)
    subprocess.run(CHROME_CMD := [CHROME, *FLAGS,
                                  f"--screenshot={png_path}",
                                  f"--window-size={int(w)},{int(h)}",
                                  f"--force-device-scale-factor={scale}",
                                  "file://" + os.path.abspath(tmp)],
                   check=True, capture_output=True, timeout=120)
    os.remove(tmp)
    return w, h


CSS = """
@page { size: 6in 9in; margin: 0.75in 0.7in 0.8in 0.7in; }
html { -webkit-print-color-adjust: exact; }
body { font: 10.5pt/1.62 Georgia,'Liberation Serif',serif; color:#1a1a1a;
       margin:0; text-rendering:optimizeLegibility; hyphens:auto; }

/* ---- the distillation card, first page ---- */
.dist { page-break-after: always; }
.dist.distback { page-break-before: always; page-break-after: auto; }
.dist .kicker { font: italic 9.5pt Georgia,serif; letter-spacing:.06em;
        color:#5a5a5a; text-align:center; margin:0 0 .35in; }
.dist h1 { font-size:17pt; font-weight:600; letter-spacing:.01em;
        text-align:center; line-height:1.25; margin:0 0 .08in; }
.dist .rule { width:2.2in; height:0; border-top:.6pt solid #bdbdbd;
        margin:.18in auto .3in; }
.dist .mech { text-align:center; font: 600 11pt Georgia,serif;
        letter-spacing:.14em; text-transform:uppercase; margin:0 0 .06in; }
.dist .convo { font: italic 11.5pt/1.55 Georgia,serif; text-align:center;
        margin:0 auto .3in; max-width:4in; color:#2a2a2a; }
.dist p { margin:0 0 .16in; }
.dist h2 { font:600 9.5pt Georgia,serif; letter-spacing:.16em;
        text-transform:uppercase; color:#5a5a5a;
        margin:.28in 0 .1in; border-bottom:.5pt solid #ddd; padding-bottom:.05in; }
.dist ol { margin:0 0 .1in; padding-left:.24in; }
.dist li { margin:0 0 .11in; }

/* ---- chapter ---- */
h1 { font-size:20pt; font-weight:600; line-height:1.2; letter-spacing:.005em;
     margin:0 0 .06in; }
h1 .num { display:block; font:600 9.5pt Georgia,serif; letter-spacing:.2em;
     text-transform:uppercase; color:#6a6a6a; margin-bottom:.12in; }
h1 + hr.beat { display:none; }
p { margin:0 0 .13in; text-align:justify; }
p + p { text-indent:1.1em; }
p.runin, p.runin + p, blockquote + p, .plate + p, hr.beat + p { text-indent:0; }
p.runin { margin-top:.2in; }
p.runin strong { font-weight:600; letter-spacing:.01em; }
hr.beat { border:0; height:0; margin:.24in auto; width:1.1in;
     border-top:.6pt solid #cfcfcf; }
blockquote { margin:.22in .42in; padding-left:.2in; border-left:1.2pt solid #d4d4d4; }
blockquote.pull { margin:.26in .3in; padding:0 0 0 .22in;
     border-left:1.6pt solid #c9c9c9; page-break-inside:avoid; }
blockquote.pull p { font: italic 11pt/1.56 Georgia,serif; }
blockquote cite { display:block; font: normal 9pt Georgia,serif; font-style:normal;
     color:#6a6a6a; margin-top:.09in; letter-spacing:.02em; }
blockquote p { font: italic 10.5pt/1.55 Georgia,serif; color:#2f2f2f;
     text-align:left; text-indent:0; margin:0; }
em { font-style:italic; }
strong { font-weight:600; }

/* ---- plate ---- */
figure.plate { margin:.3in 0; text-align:center; page-break-inside:avoid; }
figure.plate img { max-width:100%; max-height:5.6in; height:auto; }
figure.plate figcaption { font: italic 9pt Georgia,serif; color:#6a6a6a;
     margin-top:.1in; }
.dropfirst::first-letter { font-size:1em; }
"""


def build(chapter_md, distillation_md, plates, out_pdf, title, dist_at="back"):
    body = []
    if distillation_md and dist_at == "front":
        d = md_to_html(distillation_md)
        d = re.sub(r"<h1>(.*?)</h1>",
                   lambda m: f'<p class="kicker">Chapter distillation</p><h1>{m.group(1)}</h1>'
                             f'<div class="rule"></div>', d, count=1)
        d = re.sub(r"<p><strong>Mechanism:</strong>\s*(.*?)</p>",
                   r'<p class="mech">\1</p>', d, count=1)
        d = re.sub(r"<p><strong>Conversation sentence:</strong>\s*(.*?)</p>",
                   r'<p class="convo">\1</p>', d, count=1)
        for lab in ("Lesson", "Challenge", "Practice"):
            d = re.sub(rf"<p><strong>{lab}:</strong>\s*(.*?)</p>",
                       rf'<h2>{lab}</h2><p>\1</p>', d)
            d = re.sub(rf"<p><strong>{lab}:</strong></p>", rf"<h2>{lab}</h2>", d)
            d = re.sub(rf"<p class=\"runin\"><strong>{lab}:</strong></p>", rf"<h2>{lab}</h2>", d)
        body.append(f'<section class="dist">{d}</section>')

    c = md_to_html(chapter_md)
    c = re.sub(r"<h1>Chapter (\d+): (.*?)</h1>",
               r'<h1><span class="num">Chapter \1</span>\2</h1>', c, count=1)
    for marker, png, cap, (w, h) in plates:
        fig = (f'<figure class="plate"><img src="{os.path.basename(png)}" '
               f'width="{int(w)}" height="{int(h)}" alt="">'
               + (f"<figcaption>{_html.escape(cap)}</figcaption>" if cap else "")
               + "</figure>")
        if marker == "END":
            c += fig
        else:
            c = c.replace(marker, fig + marker, 1)
    body.append(f"<section>{c}</section>")

    if distillation_md and dist_at == "back":
        d = md_to_html(distillation_md)
        d = re.sub(r"<h1>(.*?)</h1>",
                   lambda m: '<p class="kicker">Not part of the chapter &middot; '
                             'working notes</p><h1>' + m.group(1) + '</h1>'
                             '<div class="rule"></div>', d, count=1)
        d = re.sub(r"<p><strong>Mechanism:</strong>\s*(.*?)</p>",
                   r'<p class="mech">\1</p>', d, count=1)
        d = re.sub(r"<p><strong>Conversation sentence:</strong>\s*(.*?)</p>",
                   r'<p class="convo">\1</p>', d, count=1)
        for lab in ("Lesson", "Challenge", "Practice"):
            d = re.sub(rf"<p><strong>{lab}:</strong>\s*(.*?)</p>", rf'<h2>{lab}</h2><p>\1</p>', d)
            d = re.sub(rf"<p><strong>{lab}:</strong></p>", rf"<h2>{lab}</h2>", d)
            d = re.sub(rf'<p class="runin"><strong>{lab}:</strong></p>', rf"<h2>{lab}</h2>", d)
        body.append(f'<section class="dist distback">{d}</section>')

    doc = (f"<!doctype html><html><head><meta charset='utf-8'>"
           f"<title>{_html.escape(title)}</title><style>{CSS}</style></head>"
           f"<body>{''.join(body)}</body></html>")
    html_path = os.path.splitext(out_pdf)[0] + ".html"
    open(html_path, "w", encoding="utf-8").write(doc)
    subprocess.run([CHROME, *FLAGS, "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf}", "file://" + os.path.abspath(html_path)],
                   check=True, capture_output=True, timeout=180)
    return html_path


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Render a chapter to PDF via headless Chromium.")
    ap.add_argument("--chapter", required=True)
    ap.add_argument("--distillation")
    ap.add_argument("--distillation-at", choices=["front", "back"], default="back",
                    help="The shipped manuscript carries no distillation at all - it is "
                         "working apparatus that feeds the back-of-book practice guide. "
                         "Default back, and labelled, so a reader copy never opens on it.")
    ap.add_argument("--plate", action="append", default=[],
                    help="SVG[::marker][::caption]; marker END appends at the end")
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", default="Chapter")
    a = ap.parse_args()

    if not os.path.exists(CHROME):
        print(f"chapter_pdf_local: no chromium at {CHROME}", file=sys.stderr)
        return 2

    outdir = os.path.dirname(os.path.abspath(a.out)) or "."
    os.makedirs(outdir, exist_ok=True)

    plates = []
    for spec in a.plate:
        parts = spec.split("::")
        svg = parts[0]
        marker = parts[1] if len(parts) > 1 and parts[1] else "END"
        cap = parts[2] if len(parts) > 2 else ""
        png = os.path.join(outdir, os.path.splitext(os.path.basename(svg))[0] + ".png")
        w, h = svg_to_png(svg, png)
        plates.append((marker, png, cap, (w, h)))
        print(f"  plate rasterised: {os.path.basename(png)}  {int(w)}x{int(h)} @3x")

    chapter = open(a.chapter, encoding="utf-8").read()
    dist = open(a.distillation, encoding="utf-8").read() if a.distillation else None
    html_path = build(chapter, dist, plates, a.out, a.title, a.distillation_at)
    size = os.path.getsize(a.out)
    print(f"  html:  {html_path}")
    print(f"  pdf:   {a.out}  ({size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
