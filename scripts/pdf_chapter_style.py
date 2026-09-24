"""Chapter opening shared by both PDF backends; ordinary words for speech readers."""
import re

CSS = """
h1.chapter-heading { font-family: Georgia, 'Times New Roman', serif;
  font-size:20pt; font-weight:700; line-height:1.25; letter-spacing:normal;
  margin:0 0 .30in; padding:0; border:0; text-indent:0;
  break-after:avoid; page-break-after:avoid; }
h1.chapter-heading .num { display:block; font-size:10pt; font-weight:400;
  letter-spacing:normal; text-transform:none; color:#444; margin:0 0 .12in; }
h1.chapter-heading .chapter-title { display:block; font-size:20pt;
  font-weight:700; letter-spacing:normal; text-transform:none; }
h1 + p, h1 + hr + p, h2 + p, h3 + p { text-indent:0; }
/* Shared reading format: ordinary paragraphs are flush left, never indented. */
p, p + p, p.runin, p.runin + p { text-indent:0; text-align:left; }
h2.beat-heading { font:700 11pt/1.35 Georgia,'Times New Roman',serif;
  letter-spacing:normal; text-transform:none; color:inherit;
  margin:.20in 0 .10in; padding:0; border:0;
  break-after:avoid; page-break-after:avoid; }
"""


def format_headings(html):
    # Older prose stores subsection labels as bold run-ins. Give them a real
    # block boundary in either backend; colon-prefixed metadata stays intact.
    html = re.sub(
        r'<p(?: class="runin")?><strong>([^<:]+\.)</strong>\s+([^<]|<em>)',
        r'<h2 class="beat-heading">\1</h2>\n<p>\2', html)
    html = re.sub(r'<p(?: class="runin")?><strong>([^<:]+)</strong></p>',
                  r'<h2 class="beat-heading">\1</h2>', html)
    html = re.sub(r'<p class="beat-label">(.*?)</p>',
                  r'<h2 class="beat-heading">\1</h2>', html)
    return re.sub(r'<h1>Chapter (\d+): (.*?)</h1>',
                  r'<h1 class="chapter-heading"><span class="num">Chapter \1</span>\n'
                  r'<strong class="chapter-title">\2</strong></h1>', html)
