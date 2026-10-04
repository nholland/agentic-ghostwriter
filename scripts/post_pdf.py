#!/usr/bin/env python3
"""post_pdf.py - phone-sized reading copy of anything the author must read: marketing drafts
(Substack post + X + Facebook) and plain markdown (proposals, reports).

Reuses chapter_pdf_local's markdown parser, stylesheet, Chromium and Playwright
discovery, so there is still one rendering implementation. Only the page differs:
4 x 7 in with larger type, because a 6 x 9 in chapter page shrinks to unreadable
on a phone screen. This is a reading copy for the author. It is not a chapter and
is never an export of record.

    python3 scripts/post_pdf.py OUT.pdf runs/marketing/ch02/05-*.md runs/marketing/ch02/06-*.md ...

A marketing input is laid out per marketing/substack-voice.md:
header, a line of ---, the post, <!-- END OF POST -->, then ## X and ## Facebook.
Any other markdown file (one starting with a '# Title' line) renders as plain text.
"""
import html as _html
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chapter_pdf_local as C  # noqa: E402

PHONE_CSS = """
@page { size: 4in 7in; margin: .42in .38in .5in .38in; }
body { font: 12.5pt/1.58 Georgia,'Liberation Serif',serif; }
h1.title { font-size: 19pt; line-height:1.2; margin:0 0 .1in; page-break-before: always; }
h1.title:first-of-type { page-break-before: avoid; }
.meta { font: italic 10pt/1.4 Georgia,serif; color:#5a5a5a; margin:0 0 .06in; }
.subj { font: 11pt/1.45 Georgia,serif; margin:.1in 0 .14in; padding:.08in .12in;
        border-left:2pt solid #c9c9c9; background:#f6f6f6; }
.subj b { font-weight:600; }
.social h2 { font:600 10pt Georgia,serif; letter-spacing:.14em; text-transform:uppercase;
        color:#5a5a5a; border-bottom:.5pt solid #ddd; padding-bottom:.04in;
        margin:.2in 0 .1in; page-break-before: always; }
.social h2 ~ h2 { page-break-before: avoid; }
.social p { font-size: 11.5pt; break-inside: avoid; page-break-inside: avoid; }
.social h2 { break-after: avoid; page-break-after: avoid; }
.endmark { text-align:center; color:#9a9a9a; letter-spacing:.3em; margin:.2in 0; }
"""


def split(md):
    m = re.search(r"\n---\n", md)
    head, rest = md[:m.start()], md[m.end():]
    post, _, social = rest.partition("<!-- END OF POST -->")
    return head, post.strip(), social.strip()


def header_html(head):
    title = re.search(r"^# (.+)$", head, re.M).group(1).strip()
    subs = re.findall(r"^\d\. (.+)$", head, re.M)
    if not subs:  # desks sometimes put them inline: **Subject lines:** 1. A 2. B 3. C
        m = re.search(r"\*\*Subject lines:\*\*\s*(.+?)(?=\n\*\*|\Z)", head, re.S)
        if m:
            subs = [x.strip() for x in re.split(r"(?:^|\s)\d\.\s+", m.group(1)) if x.strip()]
    status = re.search(r"\*\*Status:\*\*\s*(.+)", head)
    out = [f'<h1 class="title">{_html.escape(title)}</h1>']
    if status:
        out.append(f'<p class="meta">{_html.escape(status.group(1).strip())}</p>')
    if subs:
        out.append('<div class="subj"><b>Subject lines</b><br>' +
                   "<br>".join(f"{i}. {_html.escape(s)}" for i, s in enumerate(subs, 1)) + "</div>")
    return "".join(out)


def build(paths, out_pdf):
    body = []
    for p in paths:
        raw = open(p, encoding="utf-8").read()
        if "<!-- END OF POST -->" not in raw:  # plain document: a proposal, a report, anything to read
            m = re.match(r"\s*# (.+)\n", raw)
            title, rest = (m.group(1).strip(), raw[m.end():]) if m else (os.path.basename(p), raw)
            body.append(f'<h1 class="title">{_html.escape(title)}</h1>' + C.md_to_html(rest))
            continue
        head, post, social = split(raw)
        body.append(header_html(head))
        body.append(C.md_to_html(post))
        body.append('<div class="endmark">&#8226; &#8226; &#8226;</div>')
        # '#Stoicism' tags would parse as headings; keep them literal text.
        social = re.sub(r"^(#\w[^\n]*)$", lambda m: "\\" + m.group(1), social, flags=re.M)
        # a single newline inside a paragraph is a line the author copies separately;
        # the parser joins such lines with a space, so mark them first
        social = re.sub(r"(?<=\S)\n(?=\S)", " @@BR@@ ", social)
        social_html = C.md_to_html(social).replace("\\#", "#").replace(" @@BR@@ ", "<br>")
        body.append('<div class="social">' + social_html + "</div>")
    doc = (f"<!doctype html><html><head><meta charset='utf-8'><title>Draft reading copy</title>"
           f"<style>{C.CSS}\n{C.CHAPTER_CSS}\n{PHONE_CSS}</style></head><body>{''.join(body)}</body></html>")
    html_path = os.path.splitext(out_pdf)[0] + ".html"
    open(html_path, "w", encoding="utf-8").write(doc)
    subprocess.run(["node", "-e", C.PDF_JS, os.path.abspath(html_path), os.path.abspath(out_pdf), C.CHROME],
                   env=dict(os.environ, NODE_PATH=C.node_modules()),
                   check=True, capture_output=True, timeout=120)
    return html_path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    h = build(sys.argv[2:], sys.argv[1])
    print(f"post_pdf: wrote {sys.argv[1]} (supporting file {h})")
