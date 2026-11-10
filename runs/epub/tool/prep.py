"""Prepare output/compiled/assets/book.html for pandoc's EPUB writer.
Usage: python3 -I prep.py BOOK_HTML OUT_HTML REPO_ROOT
Keeps the house print look where an ePub can carry it (Designer review, runs/epub/epub-design-review.md)."""
import re, sys, os
src, dst, root = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(src, encoding='utf-8').read()
# 1. practice pages: kicker inside the title heading, demoted to h2 so it stays in its chapter
s, n = re.subn(r'<p class="kicker">Putting into Practice</p>\s*<h1>(.*?)</h1>',
               r'<h2 class="dist-title"><span class="kicker">Putting into Practice</span>\1</h2>', s, flags=re.S)
print('practice titles:', n)
# 2. chapter openings: small label above the title; colon hidden but kept for the contents list
s = re.sub(r'<h1 class="chapter-heading"><span class="num">(Chapter \d+)</span>\s*<strong class="chapter-title">(.*?)</strong>',
           r'<h1 class="chapter-heading"><span class="num">\1<span class="sep">: </span></span>\2', s, flags=re.S)
# 3. plates: alt text from the SVG's own label
def svg_label(png):
    m = re.match(r'runs-(ch\d\d)-plate\.png', png)
    cand = []
    if m: cand += [f'runs/{m.group(1)}/plate.svg']
    m = re.match(r'books-the-stoic-husband-parts-(plate-.*)\.png', png)
    if m: cand += [f'books/the-stoic-husband/parts/{m.group(1)}.svg']
    m = re.match(r'runs-parts-(plate-.*)\.png', png)
    if m: cand += [f'runs/parts/{m.group(1)}.svg', f'books/the-stoic-husband/parts/{m.group(1)}.svg']
    for c in cand:
        p = os.path.join(root, c)
        if os.path.exists(p):
            a = re.search(r'aria-label="([^"]*)"', open(p, encoding='utf-8').read())
            if a: return a.group(1)
    return None
def alt(m):
    tag, png = m.group(0), m.group(1)
    lab = svg_label(png)
    if lab: tag = re.sub(r'alt="[^"]*"', 'alt="' + lab.replace('"', "'") + '"', tag)
    return tag
s = re.sub(r'<img src="([^"]+)"[^>]*>', alt, s)
# 3b. plates on the reader's own page colour (author, 2026-11-10: "the plates don't match the book BG color").
# The print rasters are one ink (#111) on white paper, greyscale only. Each pixel is a mix of ink and
# paper, so alpha = (255 - grey) / (255 - 17) recovers the ink exactly; white, including the plate kit's
# .knock shapes that clear lines behind them, becomes transparent. Written next to OUT_HTML; build.sh
# puts that folder on pandoc's resource path.
def ink_only(m):
    tag, png = m.group(0), m.group(1)
    srcp = os.path.join(os.path.dirname(os.path.abspath(src)), png)
    if 'plate' not in png or not os.path.exists(srcp): return tag
    from PIL import Image
    import numpy as np
    g = np.asarray(Image.open(srcp).convert('L')).astype(np.float32)
    a = np.clip((255.0 - g) / (255.0 - 17.0), 0, 1)
    la = np.zeros(g.shape + (2,), np.uint8); la[..., 0] = 17; la[..., 1] = np.round(a * 255)
    out = 'ink-' + png
    Image.fromarray(la, 'LA').save(os.path.join(os.path.dirname(os.path.abspath(dst)), out), optimize=True)
    return tag.replace(f'src="{png}"', f'src="{out}"')
s = re.sub(r'<img src="([^"]+)"[^>]*>', ink_only, s)
print('plates made transparent:', s.count('src="ink-'))
# 4. Part closing pages: their own page, as in print. (Until 2026-11-10 this matched a <p> wrapper the
# compiled book never has: the plates sit in <div class="plate">, the closing text after <div class="pb">,
# and step 5 deleted both, so neither ever got its page.) Pandoc drops classes on <p> but keeps them on
# <div>, so these two survive step 5 as a placeholder tag and come back as classed divs.
s, n1 = re.subn(r'<div class="pb"></div>\s*(<p>.*?</p>)', r'<keep class="part-closing">\1</keep>', s, flags=re.S)
s, n2 = re.subn(r'<div class="plate">\s*(<img src="[^"]*parts[^"]*plate[^"]*"[^>]*>)\s*</div>',
                r'<keep class="closing-plate">\1</keep>', s)
print('Part closing texts:', n1, ' Part closing plates:', n2)
# 4b. title page (2026-11-10): the book's own page from title-page.md replaces pandoc's, which
#     printed a build date. Its title becomes the h1 that starts the title-page file.
s, ntp = re.subn(r'<div class="titlepage"><p class="tp-title">(.*?)</p>',
                 r'<h1 class="title-page">\1</h1><div class="titlepage">', s, count=1)
print('title page:', ntp)
# 5. flatten wrappers pandoc would otherwise hide from the contents list
s = s.replace('<div class="rule"></div>', '<hr/>')
s = re.sub(r'</?(?:div|section|article|main|header)\b[^>]*>', '', s)
s = s.replace('<keep ', '<div ').replace('</keep>', '</div>')
open(dst, 'w', encoding='utf-8').write(s)
print('alt texts from SVG:', len(re.findall(r'<img[^>]*alt="(?!Plate, )', s)))
