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
"""


def format_headings(html):
    return re.sub(r'<h1>Chapter (\d+): (.*?)</h1>',
                  r'<h1 class="chapter-heading"><span class="num">Chapter \1</span>\n'
                  r'<strong class="chapter-title">\2</strong></h1>', html)
