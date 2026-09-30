"""Read current PDFs against their manifest sources; requires pypdf.

Run after compile_current.py. This reads artifacts without regenerating them.
"""
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
import sys
import unicodedata

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import compile as assembly
import chapter_pdf_local as renderer


def normal(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text).casefold() if c.isalnum())


class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.data = []; self.lists = []

    def handle_starttag(self, tag, attrs):
        if tag == 'ol': self.lists.append(0)
        if tag == 'li' and self.lists:
            self.lists[-1] += 1
            self.data.append(str(self.lists[-1]))

    def handle_endtag(self, tag):
        if tag == 'ol': self.lists.pop()

    def handle_data(self, text): self.data.append(text)


def expected(html):
    parser = Text(); parser.feed(html)
    return normal(' '.join(parser.data))


def pages(path):
    pdf = PdfReader(path)
    return [(normal(p.extract_text()), bool(p.images)) for p in pdf.pages]


def main():
    out = ROOT / 'output/compiled'
    manifest = json.loads((out / 'manifest.json').read_text())
    sources = manifest['source_sha256']
    for path, digest in sources.items():
        assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == digest, path + ': stale export'
    book = pages(out / 'book.pdf')
    joined = ''.join(t for t, _ in book)
    previous = -1
    count = 0
    for path in sources:
        if not path.endswith('/refined.md'): continue
        src = ROOT/path
        n, prose, dist = assembly.draft_inputs(src, src.with_name('distillation.md'))
        packet = pages(out / 'chapters' / f'ch{n:02}.pdf')
        ptext = ''.join(t for t, _ in packet)
        p = expected(renderer.format_headings(renderer.md_to_html(prose)))
        d = expected(renderer.distillation_html(dist, renderer.PRACTICE_KICKER))
        assert p in ptext and d in ptext, f'ch{n}: incomplete packet'
        assert p in joined and d in joined, f'ch{n}: incomplete book'
        pos = joined.index(p)
        assert previous < pos < joined.index(d, pos), f'ch{n}: wrong sequence'
        previous = joined.index(d, pos) + len(d) - 1
        heading = expected(renderer.format_headings(renderer.md_to_html(prose.splitlines()[0])))
        for label, content in [('packet', packet), ('book', book)]:
            starts = [i for i, (t, _) in enumerate(content) if heading in t]
            assert len(starts) == 1, f'ch{n} {label}: split or missing heading'
            start = starts[0]
            assert content[start][0].startswith(heading), f'ch{n} {label}: chapter does not start fresh'
            end = next(i for i in range(start, len(content)) if content[i][0].startswith(normal(renderer.PRACTICE_KICKER)))
            assert end > start and content[end-1][1], f'ch{n} {label}: plate not before distillation'
            assert sum(image for _, image in content[start:end]) == 1, f'ch{n} {label}: wrong plate count'
        assert all(t or image for t, image in packet), f'ch{n}: blank page'
        count += 1
    assert count and all(t or image for t, image in book), 'empty or blank book'
    print(f'{count}/{count} chapter PDFs and book sequences pass; full prose/distillations preserved, headings together, plates before distillations.')
    print(f'Book: {len(book)} pages; {sum(image for _, image in book)} plate pages; no blank pages.')


if __name__ == '__main__': main()
