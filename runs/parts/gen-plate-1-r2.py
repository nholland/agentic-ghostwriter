#!/usr/bin/env python3
"""Regenerate Part I's closing plate from the landed plate's own geometry.

Two changes, and only these:

  1. A title, THE STEADY RIVER, in the chapter plates' display idiom.
  2. The canyon holds the river. The landed plate drew the cut as an empty
     notch with a thread of water floating beneath it, which at a glance is a
     rift widening between two sides. Here the cut is a channel with the water
     running in it: what the ordinary days took out is what the river now runs
     through, and the surface line joins the two walls rather than standing
     between them.

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

HALF_TOP = 96.0            # the landed plate's top half-gap, near enough
HALF_BOT = 46.0             # the channel at the canyon floor
TAPER = 0.62                # <1: the shoulders fall away early, the gorge is sheer

WATER_TOP = 405.0           # the surface
WATER_GAP = 15.0            # water is a tighter texture than rock: its own thing
AMPL = 3.0
WAVELEN = 30.0


def halfwidth(y):
    u = (y - BOX_T) / (BOX_B - BOX_T)
    return HALF_TOP - (HALF_TOP - HALF_BOT) * (u ** TAPER)


def wave(y, rnd, amp=None):
    amp = AMPL if amp is None else amp
    h = halfwidth(y)
    x0, x1 = CENTRE - h, CENTRE + h
    span = x1 - x0
    cycles = max(1.5, round(span / WAVELEN * 2) / 2.0)
    ph = rnd.uniform(0, 2 * math.pi)
    pts = []
    steps = 60
    for k in range(steps + 1):
        t = k / steps
        env = math.sin(math.pi * t) ** 0.3     # the ends settle onto the rock
        y2 = y - amp * env * math.sin(2 * math.pi * cycles * t + ph)
        pts.append(f'{x0 + span * t:.1f},{y2:.1f}')
    return ' '.join(pts)


def build(title='THE STEADY RIVER', title_y=150.0, title_px=21):
    rnd = random.Random(11)
    ys = [BOX_T + (BOX_B - BOX_T) * i / (N - 1) for i in range(N)]
    jl = [rnd.uniform(-1.5, 1.5) for _ in range(N)]
    jr = [rnd.uniform(-1.5, 1.5) for _ in range(N)]
    left = [CENTRE - halfwidth(y) + jl[i] for i, y in enumerate(ys)]
    right = [CENTRE + halfwidth(y) + jr[i] for i, y in enumerate(ys)]

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

    lp = ' '.join(f'{left[i]:.1f},{ys[i]:.1f}' for i in range(N))
    rp = ' '.join(f'{right[i]:.1f},{ys[i]:.1f}' for i in range(N))
    o.append(f'<polyline points="{lp}" fill="none" stroke="{INK}" '
             f'stroke-width="{W_WALL}" stroke-linejoin="round"/>')
    o.append(f'<polyline points="{rp}" fill="none" stroke="{INK}" '
             f'stroke-width="{W_WALL}" stroke-linejoin="round"/>')

    y = WATER_TOP
    first = True
    while y <= BOX_B + 0.5:
        o.append(f'<polyline points="{wave(y, rnd, AMPL if first else AMPL * 0.72)}" '
                 f'fill="none" stroke="{INK}" stroke-width="{W_RIVER}" stroke-linecap="round"/>')
        first = False
        y += WATER_GAP

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
    for k in ('HALF_TOP', 'HALF_BOT', 'TAPER', 'WATER_TOP', 'WATER_GAP', 'AMPL', 'WAVELEN'):
        f = '--' + k.lower()
        if f in sys.argv:
            globals()[k] = float(sys.argv[sys.argv.index(f) + 1])
    p = os.path.join(OUT_DIR, name)
    open(p, 'w', encoding='utf-8').write(build(title_px=px))
    print(p)
