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
# 2026-11-10: the frontispiece's file loses its pandoc heading (below); its contents entry is
# pointed at the title page instead, so the list opens on the title, once.
front = [i.filename for i, d in items if i.filename.endswith('.xhtml') and b'alt="Frontispiece' in d]
tpage = [i.filename for i, d in items if i.filename.endswith('.xhtml') and b'class="title-page"' in d]
for info, data in items:
    if info.filename == 'EPUB/nav.xhtml' and front and tpage:
        t = data.decode('utf-8')
        f, g = (x.split('EPUB/', 1)[1] for x in (front[0], tpage[0]))
        t = re.sub(r'href="' + re.escape(g) + r'(?:#[^"]*)?"', 'href="' + f + '"', t)   # one target, then dedupe
        t = re.sub(r'(<li[^>]*>\s*<a href="' + re.escape(f) + r'">[^<]*</a>\s*</li>)\s*<li[^>]*>\s*<a href="'
                   + re.escape(f) + r'">[^<]*</a>\s*</li>', r'\1', t)
        t = t.replace('href="' + f + '"', 'href="' + g + '"')
        xml.dom.minidom.parseString(t.encode('utf-8'))
        data = t.encode('utf-8')
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
        # 2026-11-10: pandoc names any content before the first heading after the book; on the
        # frontispiece that printed "RIVER. OAK. SUN." above the drawing. The title page follows.
        if 'alt="Frontispiece' in s:
            s, f = re.subn(r'<h1 class="unnumbered">[^<]*</h1>\s*', '', s, count=1)
        if 'class="title-page"' in s:   # the title page's subtitle and author keep their classes
            s = re.sub(r'(<h1 class="title-page">.*?</h1>\s*)<p>(.*?)</p>\s*<p>(.*?)</p>',
                       r'\1<p class="tp-sub">\2</p>\n<p class="tp-author">\3</p>', s, count=1, flags=re.S)
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
