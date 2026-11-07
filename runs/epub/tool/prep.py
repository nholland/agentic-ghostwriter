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
# 4. Part closing plates: their own page
s = re.sub(r'<p>(\s*<img src="[^"]*parts[^"]*plate[^"]*"[^>]*>\s*)</p>', r'<p class="closing-plate">\1</p>', s)
# 5. flatten wrappers pandoc would otherwise hide from the contents list
s = s.replace('<div class="rule"></div>', '<hr/>')
s = re.sub(r'</?(?:div|section|article|main|header)\b[^>]*>', '', s)
open(dst, 'w', encoding='utf-8').write(s)
print('alt texts from SVG:', len(re.findall(r'<img[^>]*alt="(?!Plate, )', s)))
