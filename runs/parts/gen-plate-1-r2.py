#!/usr/bin/env python3
"""Regenerate Part I's closing plate from the landed plate's own geometry.

Two changes, and only these:

  1. A title, THE STEADY RIVER, in the chapter plates' display idiom.
  2. The canyon is full of the river. The landed plate drew the canyon as an
     empty notch with a thread of water floating under it, which reads as a
     rift between two sides. Here the same horizontal layers carry on straight
     through the rock and go wavy where they cross the cut: the channel the
     water made is the channel the water runs in, and the surface line joins
     the two walls instead of standing between them.

Everything else - canvas, ink, weights, strata count and spacing, drawing box,
caption text and position - is copied from
books/the-stoic-husband/parts/plate-1-steady-river.svg.
"""
import math
import os
import random

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

W, H = 600, 900
BOX_L, BOX_R = 90.0, 510.0
BOX_T, BOX_B = 190.0, 640.0
N = 20                      # strata rows, as landed
INK = '#111111'
W_FIELD = 1.1               # strata weight, as landed
W_WALL = 1.6                # canyon wall weight, as landed
W_RIVER = 1.4               # river weight, as landed
CENTRE = 300.0

HALF_TOP = 102.4            # the landed top stratum's half-gap, unchanged
HALF_SLOT = 62.0            # the channel below the waterline
WATERLINE = 13              # first row that carries water
WAVELEN = 62.0
AMPL = 3.6


def half_widths(rnd):
    ys = [BOX_T + (BOX_B - BOX_T) * i / (N - 1) for i in range(N)]
    hw = []
    for i in range(N):
        if i <= WATERLINE:
            u = i / WATERLINE
            h = HALF_TOP - (HALF_TOP - HALF_SLOT) * (u ** 0.60)
        else:
            h = HALF_SLOT
        hw.append(h)
    jl = [rnd.uniform(-1.5, 1.5) for _ in range(N)]
    jr = [rnd.uniform(-1.5, 1.5) for _ in range(N)]
    left = [CENTRE - hw[i] + jl[i] for i in range(N)]
    right = [CENTRE + hw[i] + jr[i] for i in range(N)]
    return ys, left, right


def wave(x0, x1, y, rnd):
    span = x1 - x0
    cycles = max(1.0, round(span / WAVELEN * 2) / 2.0)
    ph = rnd.uniform(0, 2 * math.pi)
    pts = []
    steps = 64
    for k in range(steps + 1):
        t = k / steps
        x = x0 + span * t
        # the ends sit on the rock, so the water meets both walls
        env = math.sin(math.pi * t) ** 0.35
        y2 = y - AMPL * env * math.sin(2 * math.pi * cycles * t + ph)
        pts.append(f'{x:.1f},{y2:.1f}')
    return ' '.join(pts)


def build(title='THE STEADY RIVER', title_y=150.0, title_px=21):
    rnd = random.Random(11)
    ys, left, right = half_widths(rnd)

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
        o.append(f'<line x1="{BOX_L:.0f}" y1="{y:.1f}" x2="{left[i]:.1f}" y2="{y:.1f}" '
                 f'stroke="{INK}" stroke-width="{W_FIELD}"/>')
        o.append(f'<line x1="{right[i]:.1f}" y1="{y:.1f}" x2="{BOX_R:.0f}" y2="{y:.1f}" '
                 f'stroke="{INK}" stroke-width="{W_FIELD}"/>')

    # the cliff, drawn only where there is air: it stops at the waterline
    lp = ' '.join(f'{left[i]:.1f},{ys[i]:.1f}' for i in range(WATERLINE + 1))
    rp = ' '.join(f'{right[i]:.1f},{ys[i]:.1f}' for i in range(WATERLINE + 1))
    o.append(f'<polyline points="{lp}" fill="none" stroke="{INK}" '
             f'stroke-width="{W_WALL}" stroke-linejoin="round"/>')
    o.append(f'<polyline points="{rp}" fill="none" stroke="{INK}" '
             f'stroke-width="{W_WALL}" stroke-linejoin="round"/>')

    # the water, one line per layer, filling the channel it cut
    for i in range(WATERLINE, N):
        o.append(f'<polyline points="{wave(left[i], right[i], ys[i], rnd)}" fill="none" '
                 f'stroke="{INK}" stroke-width="{W_RIVER}" stroke-linecap="round"/>')

    o.append(f'<text class="ttl" x="{CENTRE:.1f}" y="{title_y:.0f}" fill="{INK}">{title}</text>')
    o.append(f'<text class="cap" x="{CENTRE:.1f}" y="730" fill="{INK}">'
             "It's patient enough to cut a canyon out of rock,</text>")
    o.append(f'<text class="cap" x="{CENTRE:.1f}" y="756" fill="{INK}">'
             'one ordinary day at a time.</text>')
    o.append('</svg>')
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    import sys
    name = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else 'plate-1-steady-river.svg'
    px = int(sys.argv[sys.argv.index('--px') + 1]) if '--px' in sys.argv else 21
    p = os.path.join(OUT_DIR, name)
    open(p, 'w', encoding='utf-8').write(build(title_px=px))
    print(p)
