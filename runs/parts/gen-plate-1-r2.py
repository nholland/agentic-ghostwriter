#!/usr/bin/env python3
"""Regenerate Part I's closing plate from the landed plate's own geometry.

Changes, and only these:
  1. A title, THE STEADY RIVER, in the chapter plates' display idiom.
  2. The canyon bottom opens to a floor, and the river is drawn across that
     floor wall to wall, so the two sides are joined by the water rather than
     separated by an empty gap.
  3. Optionally, stepped walls (one riser per stratum).

Everything else - canvas, ink, weights, strata count and spacing, drawing box,
caption text and position - is read off or copied from
books/the-stoic-husband/parts/plate-1-steady-river.svg.
"""
import math
import os
import random

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

W, H = 600, 900
BOX_L, BOX_R = 90, 510
BOX_T, BOX_B = 190.0, 640.0
N = 20                      # strata rows, as landed
INK = '#111111'
W_FIELD = 1.1               # strata weight, as landed
W_WALL = 1.6                # canyon wall weight, as landed
W_RIVER = 1.4               # river weight, as landed
CENTRE = 300.0

# Landed half-widths: 102.4 at the top stratum, 10.5 at the bottom one.
# The top is unchanged; the bottom opens to a 100px floor so the water can be
# drawn across it and touch both walls.
HALF_TOP = 102.4
HALF_BOT = 50.0


def wall_halfwidth(u, jitter):
    """u in 0..1 down the canyon. Concave: most of the narrowing happens in
    the upper half, the lower walls stand close to vertical, then a floor."""
    return HALF_TOP - (HALF_TOP - HALF_BOT) * (u ** 0.72) + jitter


def build(stepped=False, title='THE STEADY RIVER', title_y=150.0, title_px=21):
    rnd = random.Random(11)
    ys = [BOX_T + (BOX_B - BOX_T) * i / (N - 1) for i in range(N)]
    # the landed plate's walls are not smooth; keep a hand wobble of the same
    # amplitude (the landed left wall drifts back and forth by 1-2px)
    jl = [rnd.uniform(-1.6, 1.6) for _ in ys]
    jr = [rnd.uniform(-1.6, 1.6) for _ in ys]
    left, right = [], []
    for i, y in enumerate(ys):
        u = (y - BOX_T) / (BOX_B - BOX_T)
        left.append(CENTRE - wall_halfwidth(u, jl[i]))
        right.append(CENTRE + wall_halfwidth(u, jr[i]))

    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" role="img" aria-label="The Steady River">')
    o.append('<style>')
    o.append(f'.ttl{{font:600 {title_px}px Georgia,"Times New Roman",serif;'
             'letter-spacing:.20em;text-anchor:middle}')
    o.append('.cap{font:italic 17px Georgia,"Times New Roman",serif;text-anchor:middle}')
    o.append('</style>')
    o.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')

    for i, y in enumerate(ys):
        o.append(f'<line x1="{BOX_L}" y1="{y:.1f}" x2="{left[i]:.1f}" y2="{y:.1f}" '
                 f'stroke="{INK}" stroke-width="{W_FIELD}"/>')
        o.append(f'<line x1="{right[i]:.1f}" y1="{y:.1f}" x2="{BOX_R}" y2="{y:.1f}" '
                 f'stroke="{INK}" stroke-width="{W_FIELD}"/>')

    floor_y = BOX_B + 12.0
    if stepped:
        # one riser per stratum: the cut reads as taken a layer at a time
        for i in range(N - 1):
            o.append(f'<line x1="{left[i]:.1f}" y1="{ys[i]:.1f}" x2="{left[i]:.1f}" '
                     f'y2="{ys[i+1]:.1f}" stroke="{INK}" stroke-width="{W_WALL}"/>')
            o.append(f'<line x1="{right[i]:.1f}" y1="{ys[i]:.1f}" x2="{right[i]:.1f}" '
                     f'y2="{ys[i+1]:.1f}" stroke="{INK}" stroke-width="{W_WALL}"/>')
        o.append(f'<line x1="{left[-1]:.1f}" y1="{ys[-1]:.1f}" x2="{left[-1]:.1f}" '
                 f'y2="{floor_y:.1f}" stroke="{INK}" stroke-width="{W_WALL}"/>')
        o.append(f'<line x1="{right[-1]:.1f}" y1="{ys[-1]:.1f}" x2="{right[-1]:.1f}" '
                 f'y2="{floor_y:.1f}" stroke="{INK}" stroke-width="{W_WALL}"/>')
    else:
        lp = ' '.join(f'{left[i]:.1f},{ys[i]:.1f}' for i in range(N)) + f' {left[-1]:.1f},{floor_y:.1f}'
        rp = ' '.join(f'{right[i]:.1f},{ys[i]:.1f}' for i in range(N)) + f' {right[-1]:.1f},{floor_y:.1f}'
        o.append(f'<polyline points="{lp}" fill="none" stroke="{INK}" '
                 f'stroke-width="{W_WALL}" stroke-linejoin="round"/>')
        o.append(f'<polyline points="{rp}" fill="none" stroke="{INK}" '
                 f'stroke-width="{W_WALL}" stroke-linejoin="round"/>')

    # The water, drawn across the floor from wall to wall. Same weight and same
    # 48px wavelength as the landed plate's river; its two ends land exactly on
    # the foot of each wall, so the line that cut the rock also joins the sides.
    x0, x1 = left[-1], right[-1]
    span = x1 - x0
    cycles = round(span / 48.0)
    pts = []
    steps = 96
    for k in range(steps + 1):
        t = k / steps
        x = x0 + span * t
        y = floor_y - 2.2 * math.sin(2 * math.pi * cycles * t)
        pts.append(f'{x:.1f},{y:.1f}')
    o.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" '
             f'stroke-width="{W_RIVER}" stroke-linecap="round"/>')

    o.append(f'<text class="ttl" x="{CENTRE:.1f}" y="{title_y:.0f}" fill="{INK}">{title}</text>')
    o.append(f'<text class="cap" x="{CENTRE:.1f}" y="730" fill="{INK}">'
             "It's patient enough to cut a canyon out of rock,</text>")
    o.append(f'<text class="cap" x="{CENTRE:.1f}" y="756" fill="{INK}">'
             'one ordinary day at a time.</text>')
    o.append('</svg>')
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    import sys
    stepped = '--stepped' in sys.argv
    name = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else 'plate-1-steady-river.svg'
    px = int(sys.argv[sys.argv.index('--px') + 1]) if '--px' in sys.argv else 21
    p = os.path.join(OUT_DIR, name)
    open(p, 'w', encoding='utf-8').write(build(stepped=stepped, title_px=px))
    print(p)
