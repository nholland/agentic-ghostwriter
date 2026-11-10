"""Post-process pandoc's EPUB so nothing inside a chapter can start a new page.
Usage: python3 -I post.py EPUB
Designer, 2026-11-10 (runs/epub/epub-design-review.md, "2026-11-10"). The author's phone reader put
every beat of Chapter 1 ("Logical.", "Kind.", ...) on a page of its own, though epub.css asks for no
break there. Pandoc's EPUB writer always wraps each heading's run in <section>, and some readers start
a page at every <section> or every heading regardless of the publisher's CSS. So, after pandoc:
  1. every <section> becomes a <div> with the same id, class and epub:type (nav links still resolve);
  2. the in-chapter heads (h2.beat-heading, the Introduction's bare h2s, "Practice") become
     <p role="heading" aria-level="2"> with the text in <strong>, so they stay headings for screen
     readers but give a reader nothing to break on. Chapter and Part titles (h1) and the practice
     title (h2.dist-title, which follows a full-page plate) keep their heading elements.
The zip is rewritten with mimetype first and stored, as the OCF spec requires."""
import re, sys, zipfile, os, xml.dom.minidom
path = sys.argv[1]
zin = zipfile.ZipFile(path)
items = [(i, zin.read(i.filename)) for i in zin.infolist()]
zin.close()
n_sec = n_beat = n_prac = 0
out = []
for info, data in items:
    name = info.filename
    if name.startswith('EPUB/text/') and name.endswith('.xhtml'):
        s = data.decode('utf-8')
        s, a = re.subn(r'<section\b', '<div', s); s, b = re.subn(r'</section>', '</div>', s)
        assert a == b, (name, a, b)
        n_sec += a
        s, c = re.subn(r'<h2 class="beat-heading">(.*?)</h2>',
                       r'<p class="beat-heading" role="heading" aria-level="2"><strong>\1</strong></p>', s, flags=re.S)
        s, d = re.subn(r'<h2>(Practice)</h2>',
                       r'<p class="practice-label" role="heading" aria-level="2"><strong>\1</strong></p>', s)
        s, e = re.subn(r'<h2>(.*?)</h2>',   # the Introduction's unclassed beat heads
                       r'<p class="beat-heading" role="heading" aria-level="2"><strong>\1</strong></p>', s, flags=re.S)
        n_beat += c + e; n_prac += d
        left = re.findall(r'<h2(?! class="dist-title")[^>]*>.*?</h2>', s, flags=re.S)
        assert not left, (name, left[:3])
        xml.dom.minidom.parseString(s.encode('utf-8'))   # every file must still be well-formed
        data = s.encode('utf-8')
    out.append((info, data))
tmp = path + '.tmp'
with zipfile.ZipFile(tmp, 'w') as z:
    z.writestr(zipfile.ZipInfo('mimetype'), b'application/epub+zip', compress_type=zipfile.ZIP_STORED)
    for info, data in out:
        if info.filename == 'mimetype': continue
        z.writestr(info.filename, data, compress_type=zipfile.ZIP_DEFLATED)
os.replace(tmp, path)
print(f'post: {n_sec} sections -> div, {n_beat} beat heads and {n_prac} Practice labels -> p[role=heading]')
