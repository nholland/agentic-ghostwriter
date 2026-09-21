#!/usr/bin/env python3
"""Regenerate Part II's closing plate: tree rings that say growth, not age.

The landed plate is a complete disc of about thirty near-circular rings with a
clean outer edge, which is the end of a cut log. Three changes fix that without
giving up the rings:

  1. No outer edge. The rings run off all four sides of the drawing box, so the
     reader is looking at part of something larger that is still going out, not
     at a finished round of timber.
  2. The rings widen outward. Tight at the core, wider every year, so the field
     accelerates away from the centre: each year lays down more than the last.
  3. The rings are lumpy, not circular, and every ring carries the same lumps,
     which is what wood looks like and what a target does not.

Kept from the landed plate: the pith dot at the centre, the two bands of tight
years, and a scar the later rings close over.
"""
import math
import os
import random

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

W, H = 600, 900
BOX_L, BOX_R = 90.0, 510.0
BOX_T, BOX_B = 190.0, 640.0
INK = '#111111'
W_FIELD = 1.05              # ring weight, as landed
W_ACCENT = 1.35             # accent weight, as landed
CX, CY = 300.0, 415.0       # pith, on the canvas axis and the box's centre line

N = 24                      # rings
GAP_MIN, GAP_MAX = 8.0, 21.0
R_FIRST = 14.0
R_MAX = 322.0               # box corner is 307.6 from the pith: nothing closes

TIGHT = [(7, 9), (15, 17)]   # the hard years: rings that barely widened
TIGHT_FACTOR = 0.32
SCAR_RING = 11                # the year the wound was taken
SCAR_ANGLE = -1.05            # radians, upper right
SCAR_WIDTH = 0.26
SCAR_DEPTH = 26.0
SCAR_CLOSE = 4.0              # years over which the later rings close it


def radii():
    gaps = []
    for k in range(N - 1):
        g = GAP_MIN + (GAP_MAX - GAP_MIN) * (k / (N - 2))
        for a, b in TIGHT:
            if a <= k + 1 <= b:
                g *= TIGHT_FACTOR
        gaps.append(g)
    scale = (R_MAX - R_FIRST) / sum(gaps)
    rs, r = [R_FIRST], R_FIRST
    for g in gaps:
        r += g * scale
        rs.append(r)
    return rs


def ring_path(i, r, rnd, gap):
    """One year's outline. A shared lumpy profile so every ring belongs to the
    same trunk, a small per-ring wobble for the hand, and the scar."""
    pts = []
    steps = 240
    ph = [rnd.uniform(0, 2 * math.pi) for _ in range(3)]
    kink = 1.0
    for a, b in TIGHT:
        if a <= i <= b:
            kink = 2.0
    for k in range(steps + 1):
        t = 2 * math.pi * k / steps
        # the trunk's own lumps, the same on every ring
        shape = (0.042 * math.sin(2 * t + 0.6)
                 + 0.024 * math.sin(3 * t - 1.4))
        # the hand, and the kink of a hard year
        wob = kink * (0.55 * math.sin(3 * t + ph[0])
                      + 0.35 * math.sin(5 * t + ph[1])
                      + 0.22 * math.sin(9 * t + ph[2]))
        rr = r * (1.0 + shape) + wob
        if i >= SCAR_RING:
            d = abs(math.atan2(math.sin(t - (SCAR_ANGLE % (2 * math.pi))),
                               math.cos(t - (SCAR_ANGLE % (2 * math.pi)))))
            # never deeper than the year's own growth: the ring is pinched
            # toward the one inside it, never through it
            dep = min(SCAR_DEPTH, 0.85 * gap)
            rr -= (dep * math.exp(-((i - SCAR_RING) / SCAR_CLOSE) ** 2)
                   * math.exp(-(d / SCAR_WIDTH) ** 2))
        pts.append((CX + rr * math.cos(t), CY + rr * math.sin(t)))
    d = 'M ' + ' L '.join('%.1f %.1f' % p for p in pts) + ' Z'
    return d


def build(title='THE STURDY OAK', title_y=150.0, title_px=21):
    rnd = random.Random(7)
    rs = radii()
    accents = set()
    for a, b in TIGHT:
        accents.add(b + 1)      # the first wide year after each hard band

    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
             f'viewBox="0 0 {W} {H}" role="img" aria-label="The Sturdy Oak">')
    o.append('<style>')
    o.append(f'.ttl{{font:600 {title_px}px Georgia,"Times New Roman",serif;'
             'letter-spacing:.20em;text-anchor:middle}')
    o.append('.cap{font:italic 17px Georgia,"Times New Roman",serif;text-anchor:middle}')
    o.append('</style>')
    o.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    o.append('<defs><clipPath id="box"><rect x="%.0f" y="%.0f" width="%.0f" height="%.0f"/>'
             '</clipPath></defs>' % (BOX_L, BOX_T, BOX_R - BOX_L, BOX_B - BOX_T))
    o.append('<g clip-path="url(#box)">')
    for i, r in enumerate(rs):
        w = W_ACCENT if i in accents else W_FIELD
        gap = r - rs[i - 1] if i else r
        o.append(f'<path d="{ring_path(i, r, rnd, gap)}" fill="none" stroke="{INK}" '
                 f'stroke-width="{w}" stroke-linejoin="round"/>')
    o.append(f'<circle cx="{CX:.1f}" cy="{CY:.0f}" r="2.2" fill="{INK}"/>')
    o.append('</g>')
    o.append(f'<text class="ttl" x="{CX:.1f}" y="{title_y:.0f}" fill="{INK}">{title}</text>')
    o.append(f'<text class="cap" x="{CX:.1f}" y="730" fill="{INK}">'
             'The storm comes through,</text>')
    o.append(f'<text class="cap" x="{CX:.1f}" y="756" fill="{INK}">'
             'and in the morning the oak is still there.</text>')
    o.append('</svg>')
    return '\n'.join(o) + '\n'


if __name__ == '__main__':
    import sys
    name = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else 'plate-2-sturdy-oak.svg'
    px = int(sys.argv[sys.argv.index('--px') + 1]) if '--px' in sys.argv else 21
    rs = radii()
    print('radii: ' + ', '.join('%.0f' % r for r in rs))
    p = os.path.join(OUT_DIR, name)
    open(p, 'w', encoding='utf-8').write(build(title_px=px))
    print(p)
