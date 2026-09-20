#!/usr/bin/env python3
"""
plate_check.py - the counted check for a plate SVG.

WHY THIS IS A SCRIPT
    On 2026-09-20 the plates were checked by runs/design/svgcheck.py, which
    measured text collisions and margins and nothing else. The author then saw,
    in one reading, everything it could not see: a block off centre, a label
    the chapter never says, a title that is not the chapter's mechanism, three
    garbage glyphs where an apostrophe should be, and a plate that only makes
    sense to someone who read the chapter. Two of those are a reader's call and
    stay with the Reader Panel. The rest are counted here.

WHAT IT REPORTS
    One row per check, [ ok ] / [WARN] / [FAIL]. A FAIL is a defect no plate
    ships with. A WARN is reported for the author or the Publisher to judge;
    it never blocks. Two rows (title, captions) are WARN until the author
    ratifies inbox #065 and #066, after which they become FAIL: see LEVELS.

USAGE
    python3 scripts/plate_check.py runs/ch08/plate.svg --chapter 8
    python3 scripts/plate_check.py runs/parts/plate-3-warm-sun.svg --part 3
    python3 scripts/plate_check.py a.svg b.svg          # geometry rows only
"""
import argparse
import glob
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from ttfwidth import metrics, width  # noqa: E402

# Measure against the WIDEST plausible serif fallback, not the narrowest.
# The CSS says "Georgia,serif"; where Georgia is absent the generic serif is
# commonly DejaVu Serif, which runs ~40-50% wider than Liberation for lowercase.
# That gap is what put two glosses on top of each other on the Ch1 plate.
D = '/usr/share/fonts/truetype/dejavu/DejaVuSerif%s.ttf'
FONTS = None
CLEARANCE = 10.0   # px; touching is a defect, not a pass
LEFT = 44

# WARN until the author ratifies the rule, FAIL after. Inbox #065 (title is
# the distillation's Mechanism line) and #066 (the caption cap).
LEVELS = {"title": "WARN", "captions": "WARN"}

CHAPTER_WIDTH = 640
PART_CANVAS = (600, 900)


def fonts():
    global FONTS
    if FONTS is None:
        FONTS = {'reg': metrics(D % ''), 'ita': metrics(D % ''), 'bold': metrics(D % '-Bold')}
    return FONTS


def classes(s):
    cls = {}
    for m in re.finditer(r'\.(\w+)\{([^}]*)\}', s):
        b = m.group(2)
        sz = re.search(r'(\d+(?:\.\d+)?)px', b)
        ls = re.search(r'letter-spacing:\.?(\d+)em', b)
        ta = re.search(r'text-anchor:(\w+)', b)
        cls[m.group(1)] = dict(size=float(sz.group(1)) if sz else 12,
                               ls=float('.' + ls.group(1)) if ls else 0,
                               anchor=ta.group(1) if ta else 'start',
                               italic='italic' in b,
                               bold=('600' in b or '700' in b),
                               sets_anchor=ta is not None)
    return cls


def texts(s):
    """Every <text> with its resolved class, anchor, size and position."""
    cls = classes(s)
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', s):
        attrs, t = m.group(1), m.group(2)
        cm = re.search(r'class="(\w+)"', attrs)
        c = cm.group(1) if cm else ''
        k = cls.get(c, dict(size=12, ls=0, anchor='start', italic=False, bold=False, sets_anchor=False))
        anch = k['anchor']
        # SVG precedence: inline style > stylesheet class > presentation
        # attribute. The Ch12 plate set text-anchor="start" on an element whose
        # class says middle; the browser centred it off the left edge while
        # the old checker, reading the attribute as final, reported clean.
        ist = re.search(r'style="[^"]*text-anchor:\s*(\w+)', attrs)
        ia = re.search(r'text-anchor="(\w+)"', attrs)
        if ist:
            anch = ist.group(1)
        elif ia and not k['sets_anchor']:
            anch = ia.group(1)
        size = k['size']
        isz = re.search(r'style="[^"]*font-size:\s*([\d.]+)px', attrs)
        if isz:
            size = float(isz.group(1))
        xm = re.search(r'\bx="([\d.]+)"', attrs)
        ym = re.search(r'\by="([\d.]+)"', attrs)
        x = float(xm.group(1)) if xm else 0.0
        y = float(ym.group(1)) if ym else 0.0
        fo = fonts()['ita'] if k['italic'] else (fonts()['bold'] if k['bold'] else fonts()['reg'])
        w = width(t, size, k['ls'], *fo)
        l = x - w / 2 if anch == 'middle' else (x - w if anch == 'end' else x)
        out.append(dict(cls=c, text=t, x=x, y=y, l=l, r=l + w, size=size, anchor=anch,
                        italic=k['italic'], bold=k['bold'], attr_anchor=bool(ia),
                        attr_conflict=bool(ia) and k['sets_anchor'] and not ist))
    return out


def viewbox(s):
    m = re.search(r'viewBox="([^"]+)"', s)
    return [float(v) for v in m.group(1).split()] if m else [0, 0, 640, 430]


def geometry(bx, vb, left=LEFT):
    """The original svgcheck rows: margins, same-line collisions, baseline."""
    right = vb[2] - left
    issues = []
    for b in bx:
        if b['l'] < left - 0.5 or b['r'] > right + 0.5:
            issues.append(f"MARGIN  y={b['y']:>5} '{b['text'][:34]}' {b['l']:.0f}..{b['r']:.0f}")
    for i, a in enumerate(bx):
        for c in bx[i + 1:]:
            if abs(a['y'] - c['y']) < max(a['size'], c['size']) * 0.9:
                if a['l'] < c['r'] + CLEARANCE and c['l'] < a['r'] + CLEARANCE:
                    ov = min(a['r'], c['r']) - max(a['l'], c['l'])
                    issues.append(f"COLLIDE y={a['y']:>5} '{a['text'][:26]}' [{a['l']:.0f}..{a['r']:.0f}] "
                                  f"x '{c['text'][:26]}' [{c['l']:.0f}..{c['r']:.0f}]  overlap {ov:.0f}px")
    lowest = max((b['y'] for b in bx), default=0)
    if lowest > vb[3] - 6:
        issues.append(f"VIEWBOX lowest baseline {lowest} vs height {vb[3]}")
    return issues


NUM = r'-?\d+(?:\.\d+)?'


def drawing_groups(s, vb):
    """Approximate bounding boxes of the top-level <g> elements that draw
    (rect, line, circle, path), for the alignment row. Text is excluded."""
    groups = []
    depth = 0
    start = None
    for m in re.finditer(r'<g\b[^>]*>|</g>', s):
        if m.group(0).startswith('<g'):
            if depth == 0:
                start = m.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0 and start is not None:
                groups.append(s[start:m.end()])
                start = None
    out = []
    for g in groups:
        xs = []
        for r in re.finditer(r'<rect\b[^>]*>', g):
            x = re.search(r'\bx="(%s)"' % NUM, r.group(0))
            w = re.search(r'\bwidth="(%s)"' % NUM, r.group(0))
            if x and w:
                xs += [float(x.group(1)), float(x.group(1)) + float(w.group(1))]
        for r in re.finditer(r'<line\b[^>]*>', g):
            for k in ('x1', 'x2'):
                v = re.search(r'\b%s="(%s)"' % (k, NUM), r.group(0))
                if v:
                    xs.append(float(v.group(1)))
        for r in re.finditer(r'<circle\b[^>]*>', g):
            cx = re.search(r'\bcx="(%s)"' % NUM, r.group(0))
            rr = re.search(r'\br="(%s)"' % NUM, r.group(0))
            if cx and rr:
                xs += [float(cx.group(1)) - float(rr.group(1)), float(cx.group(1)) + float(rr.group(1))]
        for r in re.finditer(r'\bd="([^"]+)"', g):
            xs += path_xs(r.group(1))
        if xs:
            lo, hi = min(xs), max(xs)
            # the white ground rect spans the canvas and is not a drawing
            if lo <= 0.5 and hi >= vb[2] - 0.5:
                continue
            out.append((lo, hi))
    return out


def path_xs(d):
    """x extents of a path: absolute and relative M/L/H/V and the pairs that
    follow them. Curves are approximated by their control points."""
    xs = []
    cx = cy = 0.0
    cmd = None
    toks = re.findall(r'[MmLlHhVvCcSsQqTtAaZz]|%s' % NUM, d)
    i = 0
    nums = []
    while i < len(toks):
        t = toks[i]
        if re.match(r'[A-Za-z]', t):
            cmd = t
            i += 1
            continue
        nums = []
        while i < len(toks) and not re.match(r'[A-Za-z]', toks[i]):
            nums.append(float(toks[i]))
            i += 1
        if cmd in ('M', 'L', 'T'):
            for j in range(0, len(nums) - 1, 2):
                cx, cy = nums[j], nums[j + 1]
                xs.append(cx)
        elif cmd in ('m', 'l', 't'):
            for j in range(0, len(nums) - 1, 2):
                cx += nums[j]
                cy += nums[j + 1]
                xs.append(cx)
        elif cmd == 'H':
            for n in nums:
                cx = n
                xs.append(cx)
        elif cmd == 'h':
            for n in nums:
                cx += n
                xs.append(cx)
        elif cmd == 'V':
            for n in nums:
                cy = n
        elif cmd == 'v':
            for n in nums:
                cy += n
        elif cmd in ('C', 'S', 'Q'):
            for j in range(0, len(nums) - 1, 2):
                xs.append(nums[j])
                cx, cy = nums[j], nums[j + 1]
        elif cmd in ('c', 's', 'q'):
            step = 6 if cmd == 'c' else 4
            for j in range(0, len(nums) - step + 1, step):
                for k in range(0, step, 2):
                    xs.append(cx + nums[j + k])
                cx += nums[j + step - 2]
                cy += nums[j + step - 1]
        elif cmd in ('A', 'a'):
            for j in range(0, len(nums) - 6, 7):
                if cmd == 'A':
                    cx, cy = nums[j + 5], nums[j + 6]
                else:
                    cx += nums[j + 5]
                    cy += nums[j + 6]
                xs.append(cx)
    return xs


def normalise(t):
    t = t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    t = re.sub(r"[^a-z0-9' ]+", ' ', t.lower())
    return re.sub(r'\s+', ' ', t).strip()


def mechanism_line(chapter_dir_candidates):
    for d in chapter_dir_candidates:
        p = os.path.join(d, 'distillation.md')
        if os.path.isfile(p):
            m = re.search(r'^\*\*Mechanism:\*\*\s*(.+?)\s*$', io.open(p, encoding='utf-8').read(), re.M)
            if m:
                return m.group(1), p
    return None, None


def corpus(chapter_dir_candidates, run_dir):
    parts = []
    for d in chapter_dir_candidates:
        for name in ('refined.md', 'distillation.md'):
            p = os.path.join(d, name)
            if os.path.isfile(p):
                parts.append(io.open(p, encoding='utf-8').read())
    brief = os.path.join(run_dir, 'plate-brief.md')
    if os.path.isfile(brief):
        parts.append(io.open(brief, encoding='utf-8').read())
    return normalise('\n'.join(parts))


def rows(svg_path, chapter=None, part=None, book_root=None, runs_root=None, render=False):
    """[(status, name, detail)] where status is 'ok', 'WARN' or 'FAIL'.
    render=True adds the ink row, which rasterises the plate (a few seconds)."""
    out = []
    raw = open(svg_path, 'rb').read()
    try:
        s = raw.decode('utf-8')
        bad = 'â€' in s or '�' in s
        out.append(('FAIL' if bad else 'ok', 'charset',
                    'mojibake sequence in the file' if bad else 'valid UTF-8, no mojibake'))
    except UnicodeDecodeError as e:
        s = raw.decode('latin-1')
        out.append(('FAIL', 'charset', f'not UTF-8: {e}'))
    vb = viewbox(s)
    bx = texts(s)

    geo = geometry(bx, vb)
    out.append(('FAIL' if geo else 'ok', 'geometry', '; '.join(geo) if geo else 'no margin or collision rows'))

    conflict = [b['text'][:30] for b in bx if b['attr_conflict']]
    bare = [b['text'][:30] for b in bx if b['attr_anchor'] and not b['attr_conflict']]
    if conflict:
        out.append(('FAIL', 'anchor-attr',
                    'text-anchor attribute on an element whose class also sets one; the class wins in the browser: '
                    + ', '.join(repr(a) for a in conflict)))
    elif bare:
        out.append(('WARN', 'anchor-attr',
                    'text-anchor as a bare attribute (set it in a class or inline style): ' + ', '.join(repr(a) for a in bare)))
    else:
        out.append(('ok', 'anchor-attr', 'anchors set in classes or inline styles only'))

    runs = [b['text'] for b in bx]
    em = [t[:30] for t in runs if '—' in t]
    out.append(('FAIL' if em else 'ok', 'em-dash', ', '.join(repr(t) for t in em) if em else 'none'))
    dg = [t[:30] for t in runs if re.search(r'\d', t)]
    out.append(('WARN' if dg else 'ok', 'digits',
                'numbers on a plate get quoted back: ' + ', '.join(repr(t) for t in dg) if dg else 'none'))

    if part is not None:
        good = (vb[2], vb[3]) == PART_CANVAS
        out.append(('ok' if good else 'WARN', 'canvas',
                    f'{vb[2]:.0f}x{vb[3]:.0f}' + ('' if good else f' (Part plates are {PART_CANVAS[0]}x{PART_CANVAS[1]})')))
    else:
        good = vb[2] == CHAPTER_WIDTH
        out.append(('ok' if good else 'WARN', 'canvas',
                    f'{vb[2]:.0f}x{vb[3]:.0f}' + ('' if good else f' (chapter plates are {CHAPTER_WIDTH} wide)')))

    if chapter is not None:
        book_root = book_root or default_book_root()
        runs_root = runs_root or os.path.join(REPO, 'runs')
        tag = 'ch%02d' % chapter
        cands = [os.path.join(runs_root, tag), os.path.join(book_root, 'chapters', tag)]
        mech, src = mechanism_line(cands)
        ttl = next((b['text'] for b in bx if b['cls'] == 'ttl'), '')
        aria = re.search(r'aria-label="([^"]*)"', s)
        aria = aria.group(1) if aria else ''
        if mech is None:
            out.append(('WARN', 'title', 'no distillation.md with a Mechanism line found for ' + tag))
        else:
            same = normalise(ttl) == normalise(mech) and normalise(aria) == normalise(mech)
            out.append(('ok' if same else LEVELS['title'], 'title',
                        f'title {ttl!r} / aria-label {aria!r} vs Mechanism {mech!r}'
                        + ('' if same else ' (differs; inbox #065)')))

        corp = corpus(cands, os.path.join(runs_root, tag))
        loose = []
        for t in runs:
            words = normalise(t).split()
            if len(words) < 3:
                continue
            hit = any(' '.join(words[i:i + 3]) in corp for i in range(len(words) - 2))
            if not hit:
                loose.append(t[:40])
        out.append(('WARN' if loose else 'ok', 'grounded',
                    'no three-word run of these appears in the chapter, its distillation or plate-brief.md: '
                    + ', '.join(repr(t) for t in loose) if loose else 'every run of three or more words is the chapter\'s'))

    labels = sum(1 for b in bx if b['bold'] and not b['italic'] and b['cls'] != 'ttl')
    italics = sum(1 for b in bx if b['italic'])
    cap = labels + 2   # a subtitle, one gloss per labelled element, one closing line
    over = italics > cap
    out.append(('ok' if not over else LEVELS['captions'], 'captions',
                f'{italics} italic lines against a cap of {cap} ({labels} labels + subtitle + closing line)'
                + ('' if not over else ' (over; inbox #066)')))

    mids = [b for b in bx if b['anchor'] == 'middle']
    centre = vb[2] / 2
    stray = []
    for b in mids:
        if abs(b['x'] - centre) <= 1:
            continue
        if any(o is not b and abs(o['x'] - b['x']) <= 2 for o in mids):
            continue
        stray.append(f"'{b['text'][:24]}' x={b['x']:.0f}")
    lone = []
    groups = drawing_groups(s, vb)
    for lo, hi in groups:
        cx = (lo + hi) / 2
        off = cx - centre
        if abs(off) <= 0.06 * vb[2]:
            continue
        if hi - lo < 0.1 * vb[2]:
            # a column of small marks (the checkboxes on Ch12, an arrowhead)
            # sits at the margin on purpose; only a block can be off centre
            continue
        if any(abs(b['x'] - cx) <= 4 for b in mids):
            continue
        mirrored = any(abs(((l2 + h2) / 2 - centre) + off) <= 0.15 * vb[2] for l2, h2 in groups if (l2, h2) != (lo, hi))
        if mirrored:
            continue
        lone.append(f'block {lo:.0f}..{hi:.0f} centred at {cx:.0f}')
    det = []
    if stray:
        det.append('centred text on no shared axis: ' + ', '.join(stray))
    if lone:
        det.append('drawing off centre with no mirror and no text on its axis: ' + ', '.join(lone))
    out.append(('WARN' if det else 'ok', 'alignment', '; '.join(det) if det else
                f'{len(mids)} centred texts on the axis or a shared column; {len(groups)} drawing blocks centred or mirrored'))

    if render:
        margin = 60 if part is not None else 40
        try:
            bands = ink(svg_path, margin=margin)
            hot = {k: v for k, v in bands.items() if v > 40}   # antialiasing noise is under 40 px at 3x
            out.append(('FAIL' if hot else 'ok', 'ink',
                        'rendered ink inside the %dpx margin bands: %s' % (margin, ', '.join('%s=%d' % kv for kv in hot.items()))
                        if hot else 'no rendered ink inside the %dpx margin bands (dark px %s)' % (margin, bands)))
        except Exception as e:
            out.append(('WARN', 'ink', 'render failed, unchecked: %s' % str(e)[:120]))
    return out


def png_rows(path):
    """Decode an 8-bit non-interlaced RGB/RGBA PNG (what Chromium writes) into
    rows of pixel tuples, with no image library: none is installable here."""
    import struct
    import zlib
    d = open(path, 'rb').read()
    assert d[:8] == b'\x89PNG\r\n\x1a\n', 'not a PNG'
    pos, idat, w, h, bpp = 8, [], 0, 0, 0
    while pos < len(d):
        ln, typ = struct.unpack('>I4s', d[pos:pos + 8])
        body = d[pos + 8:pos + 8 + ln]
        if typ == b'IHDR':
            w, h, depth, ctype = struct.unpack('>IIBB', body[:10])
            assert depth == 8 and ctype in (2, 6) and body[12] == 0, 'unsupported PNG layout'
            bpp = 3 if ctype == 2 else 4
        elif typ == b'IDAT':
            idat.append(body)
        pos += 12 + ln
    raw = zlib.decompress(b''.join(idat))
    stride = w * bpp
    rows, prev = [], bytearray(stride)
    p = 0
    for _ in range(h):
        f = raw[p]
        cur = bytearray(raw[p + 1:p + 1 + stride])
        p += 1 + stride
        for i in range(stride):
            a = cur[i - bpp] if i >= bpp else 0
            b = prev[i]
            c = prev[i - bpp] if i >= bpp else 0
            if f == 1:
                cur[i] = (cur[i] + a) & 255
            elif f == 2:
                cur[i] = (cur[i] + b) & 255
            elif f == 3:
                cur[i] = (cur[i] + (a + b) // 2) & 255
            elif f == 4:
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                cur[i] = (cur[i] + pr) & 255
        rows.append(bytes(cur))
        prev = cur
    return w, h, bpp, rows


def ink(svg_path, margin=40, scale=3, tmp=None):
    """Render the plate and count dark pixels in the four margin bands. The
    Ch9 right label overshot its grid by 11px in the real render while the
    font-estimate rows passed it; the Designer caught it by measuring ink."""
    from chapter_pdf_local import svg_to_png
    tmp = tmp or os.path.join(os.environ.get('TMPDIR', '/tmp'), 'plate-ink-%d.png' % os.getpid())
    svg_to_png(svg_path, tmp, scale=scale)
    w, h, bpp, rows = png_rows(tmp)
    try:
        os.remove(tmp)
    except OSError:
        pass
    m = margin * scale
    bands = {'left': 0, 'right': 0, 'top': 0, 'bottom': 0}
    for y, row in enumerate(rows):
        for x in range(w):
            r, g, b = row[x * bpp], row[x * bpp + 1], row[x * bpp + 2]
            if r + g + b < 384:
                if x < m:
                    bands['left'] += 1
                elif x >= w - m:
                    bands['right'] += 1
                if y < 4 * scale:
                    bands['top'] += 1
                elif y >= h - 4 * scale:
                    bands['bottom'] += 1
    return bands


def default_book_root():
    try:
        import resolve_book
        root, _, _ = resolve_book.resolve(resolve_book.load_config())
        rel = resolve_book.inspect(root, require_okf=False)['info']['bookRootRelative']
        return os.path.join(root, rel)
    except Exception:
        return os.path.join(REPO, 'books', 'the-stoic-husband')


def legacy(paths):
    """The old svgcheck.py output, for the notes and inbox checks that name it."""
    for p in paths:
        s = open(p, encoding='utf-8').read()
        iss = geometry(texts(s), viewbox(s))
        print(f"\n{p}")
        print("  " + ("\n  ".join(iss) if iss else "clean"))


def main(argv=None):
    ap = argparse.ArgumentParser(description='The counted check for a plate SVG.')
    ap.add_argument('svg', nargs='+')
    ap.add_argument('--chapter', type=int)
    ap.add_argument('--part', type=int)
    ap.add_argument('--book-root')
    ap.add_argument('--runs-root')
    ap.add_argument('--no-render', action='store_true',
                    help='skip the ink row (the render takes a few seconds per plate)')
    a = ap.parse_args(argv)
    bad = 0
    for p in a.svg:
        print(p)
        for status, name, detail in rows(p, a.chapter, a.part, a.book_root, a.runs_root, render=not a.no_render):
            tag = {'ok': '[ ok ]', 'WARN': '[WARN]', 'FAIL': '[FAIL]'}[status]
            print(f'  {tag} {name:<11} {detail}')
            if status == 'FAIL':
                bad += 1
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
