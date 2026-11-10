"""Shared scenery for the frontispiece: the same oak and sun as the interludes, at any size."""
import math


def oak(p, cx, ground, scale=1.0, depth=6, roots=0):
    """A broad bare oak standing at (cx, ground). roots=N also grows roots to depth N."""
    rng = p.rng

    def limb(x, y, angle, length, d, up=True):
        sign = -1 if up else 1
        bend = rng.uniform(-0.22, 0.22)
        pts = []
        for i in range(5):
            t = i / 4
            a = angle + bend * t
            pts.append((x + math.sin(a) * length * t, y + sign * math.cos(a) * length * t))
        heavy = d - (6 - depth)
        p.curve(pts, cls="bold" if d >= depth - 1 else "line" if d >= depth - 3 else "hair")
        if d == 0:
            return
        ex, ey = pts[-1]
        kids = 3 if d >= depth - 2 and rng.random() < 0.55 else 2
        spread = 0.62 if up else 0.8
        for k in range(kids):
            a = (angle + bend) * 0.82 + (k - (kids - 1) / 2) * spread + rng.uniform(-0.16, 0.16)
            if up:
                a += 0.10 * math.copysign(1, a) if abs(a) < 1.25 else 0
                a = max(-1.75, min(1.75, a))
            else:
                a = max(-1.42, min(1.42, a))
            limb(ex, ey, a, length * rng.uniform(0.66, 0.78), d - 1, up)

    top = ground - 54 * scale
    lines = 9 if scale > 0.75 else 7
    for i in range(lines):
        off = (i - (lines - 1) / 2) * 3.3 * scale * 9 / lines
        def flare(y, off=off):
            low = max(0, (y - (ground - 16 * scale)) / (16 * scale)) ** 2
            high = max(0, (top + 14 * scale - y) / (14 * scale)) ** 2
            return off * (1 + 1.5 * low + 0.6 * high)
        n = 9
        pts = [(cx + flare(top + (ground - top) * j / n) + rng.uniform(-0.2, 0.2), top + (ground - top) * j / n) for j in range(n + 1)]
        p.curve(pts, cls="bold" if i in (0, lines - 1) else "line")
    for a, ln in ((-1.02, 50), (-0.36, 46), (0.30, 47), (0.98, 50)):
        limb(cx + a * 13 * scale, top + (2 + abs(a) * 3) * scale, a, ln * scale, depth)
    if roots:
        for a, ln in ((-1.12, 40), (-0.42, 36), (0.38, 36), (1.08, 40)):
            limb(cx + a * 17 * scale, ground + 1, a, ln * scale, roots, up=False)


def sun(p, cx, cy, r, skip=lambda a: False, rays=36, long=19, short=11):
    """The sun as a bold ring with alternating rays. skip(angle) leaves a ray out."""
    p.parts.append(f'<circle class="ink bold knock" cx="{cx}" cy="{cy}" r="{r}"/>')
    for k in range(rays):
        a = math.tau * k / rays
        if skip(a):
            continue
        r1 = r + (long if k % 2 else short)
        p.seg(cx + (r + 6) * math.cos(a), cy + (r + 6) * math.sin(a), cx + r1 * math.cos(a), cy + r1 * math.sin(a), wobble=0.0)
