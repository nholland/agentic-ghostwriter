"""Use the house renderer and assembly helpers for this unapproved chapter copy."""
from pathlib import Path
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import chapter_pdf_local as renderer
import compile as assembly

run = ROOT / 'runs/ch13'
out = run / 'pdf/Chapter-13-Pursue-Her-After-You-Have-Her-author-review.pdf'
raw = (run / 'refined.md').read_text()
body = assembly.strip_apparatus(raw)
practice = assembly.practice(str(run / 'distillation.md'))
assert practice and "Editor's Notes" not in body
# The same practice field and page-break marker used by compile.py.
reader_md = body + '\n\n<div class="pb"></div>\n\n## Putting It Into Practice\n\n' + practice + '\n'
(run / 'pdf/ch13-author-review.md').write_text(reader_md)
renderer.CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
box = ET.parse(run / 'plate.svg').getroot().attrib['viewBox'].split()
with tempfile.TemporaryDirectory(prefix='ch13-pdf-chrome-') as profile:
    renderer.FLAGS = renderer.FLAGS + ['--user-data-dir=' + profile, '--no-first-run', '--disable-extensions']
    html = renderer.build(reader_md, None,
        [('END', str(run/'pdf/plate.png'), '', (float(box[2]), float(box[3])))],
        str(out), 'Chapter 13 — Author review, not yet approved', base_dir=str(run))
print(html)
print(out)
