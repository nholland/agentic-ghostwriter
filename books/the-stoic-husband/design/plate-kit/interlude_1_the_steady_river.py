"""Interlude, Part I: the steady river.

"It doesn't fight the stone in its path. It goes around it, and it goes
on." A river crosses the page between two banks. Three stones sit in
it. The current parts, passes, and closes up again.
"""
import math
from platekit import Plate, W, write_interlude

p = Plate(height=292, seed=211, title="The steady river")
rng = p.rng

S0, S1 = 2, 322                         # the river runs the full width
HALF = 60                               # half its breadth
N = 19                                  # lines of current
STONES = [(74, -15, 14), (172, 15, 19), (256, -11, 12)]     # along, across, radius


def centre(s):
    """The river's course: one slow bend."""
    return 146 + 30 * math.sin((s - 30) / 300 * math.tau * 0.85)


def across(base, s):
    """Where the line that starts at `base` across the river sits once it has reached s."""
    v = base
    for ss, sv, r in STONES:
        d = base - sv
        reach = (r + 5) * math.exp(-abs(d) / (1.45 * r))
        length = 1.2 * r if s < ss else 3.2 * r                 # parts late, closes slowly
        v += math.copysign(reach, d if d else 1) * math.exp(-((s - ss) / length) ** 2)
    limit = HALF + 28                                          # ease everything back inside the banks
    return limit * math.tanh(v / limit)


def page(s, v):
    return (s, centre(s) + v)


# the current
for i in range(N):
    base = -HALF + 7 + (2 * HALF - 14) * i / (N - 1)
    tremor = p._noise(0.35, 90)
    s = S0 + rng.uniform(0, 14)
    while s < S1 - 6:                                           # drawn in long strokes with short breaths
        end = min(s + rng.uniform(95, 210), S1 - rng.uniform(0, 10))
        pts, t = [], s
        while t <= end:
            pts.append(page(t, across(base, t) + tremor(t)))
            t += 4
        if len(pts) > 2:
            p.curve(pts)
        s = end + rng.uniform(4, 7)

# the banks, and the ground beyond them
for side in (-1, 1):
    edge = p._noise(1.6, 80)
    p.stroke(lambda s, side=side: centre(s) + side * (HALF + 5 + edge(s)), S0, S1, wobble=0.2)
    edge2 = p._noise(2.2, 60)
    s = S0 + 4
    while s < S1 - 20:                                          # a broken second line: the bank's rise
        e = s + rng.uniform(18, 44)
        p.stroke(lambda x, side=side: centre(x) + side * (HALF + 12 + edge2(x)), s, min(e, S1), cls="hair", wobble=0.2)
        s = e + rng.uniform(10, 26)
    for _ in range(17):                                         # grass
        gx = rng.uniform(S0 + 4, S1 - 4)
        gy = centre(gx) + side * (HALF + rng.uniform(20, 56))
        for k in (-1, 0, 1):
            p.straight(gx + k * 1.6, gy, gx + k * 3.0 + rng.uniform(-0.6, 0.6), gy - rng.uniform(3.2, 5.2), cls="hair")

# the stones
for ss, sv, r in STONES:
    cx, cy = page(ss, sv)
    k = 14
    lump = [rng.uniform(-0.1, 0.1) for _ in range(k)]
    ring = []
    for j in range(k + 1):
        t = math.tau * j / k
        rr = r * (1 + lump[j % k])
        ring.append((cx + rr * 1.12 * math.cos(t), cy + rr * 0.84 * math.sin(t)))
    p.curve(ring, cls="bold knock")
    p.curve([(cx - r * 0.5, cy - r * 0.42), (cx - r * 0.05, cy - r * 0.56), (cx + r * 0.45, cy - r * 0.4)], cls="hair")

write_interlude(p, "interlude-1-the-steady-river",
                "The stone drops in,<br>and the current keeps its pace.")
