"""The Tipping Scale, alternative (Chapter 8): what breaks the surface.

Left: small things nobody counted have been settling on the riverbed for
a long time. The mound is under water, so none of it shows, until the
last pebble lands on top and breaks the surface. That one is all he sees.
Right: the same number of pebbles, each named as it landed. They lie in
one layer and the water stays calm.
"""
from platekit import Plate, W, write

p = Plate(height=112, seed=89, title="The Tipping Scale")
rng = p.rng

SURFACE, BED = 60, 100
PANELS = {"left": (6, 152), "right": (172, 318)}
R, DX, DY = 3.3, 7.3, 6.2


def water(x0, x1, keep_clear):
    """Still water: a few short strokes between surface and bed."""
    for _ in range(9):
        x, y = rng.uniform(x0 + 6, x1 - 22), rng.uniform(SURFACE + 8, BED - 9)
        if keep_clear(x + 7, y):
            continue
        p.straight(x, y, x + rng.uniform(9, 16), y, cls="hair")


def bed(x0, x1):
    floor = p._noise(0.7, 55)
    p.stroke(lambda x: BED + floor(x), x0, x1, wobble=0.15)


# --- uncounted: the mound nobody saw, and the one pebble that shows -------
x0, x1 = PANELS["left"]
cx = (x0 + x1) / 2
ROWS = 7
top_y = BED - R - (ROWS - 1) * DY
water(x0, x1, lambda x, y: abs(x - cx) < (BED - y) * 0.62 + 16)
bed(x0, x1)
for r in range(ROWS - 1):
    n = ROWS - r
    for k in range(n):
        p.ring(cx + (k - (n - 1) / 2) * DX + rng.uniform(-0.5, 0.5), BED - R - r * DY + rng.uniform(-0.3, 0.3),
               round(R + rng.uniform(-0.35, 0.25), 2), cls="line")
p.dot(cx, top_y, r=R + 0.3)                                    # the last pebble
calm = p._noise(0.35, 40)
p.stroke(lambda x: SURFACE + calm(x), x0, cx - 13, wobble=0.1)
p.stroke(lambda x: SURFACE + calm(x), cx + 13, x1, wobble=0.1)
for s in (-1, 1):                                              # the surface lifting around it
    p.curve([(cx + s * 13, SURFACE + calm(cx + s * 13)), (cx + s * 8.5, SURFACE - 0.9), (cx + s * 4.6, SURFACE - 2.2)])
p.label(cx, 9, "Uncounted", anchor="middle")
p.label(cx, SURFACE - 13, "the last pebble", cls="ital", anchor="middle")

# --- named when it lands: nothing piles up --------------------------------
x0, x1 = PANELS["right"]
cx2 = (x0 + x1) / 2
water(x0, x1, lambda x, y: y > BED - 14)
bed(x0, x1)
calm2 = p._noise(0.35, 40)
p.stroke(lambda x: SURFACE + calm2(x), x0, x1, wobble=0.1)
N = 11
for k in range(N):
    p.dot(x0 + 14 + (x1 - x0 - 28) * k / (N - 1) + rng.uniform(-1.6, 1.6), BED - R + 0.2, r=round(R + rng.uniform(-0.4, 0.2), 2))
p.label(cx2, 9, "Named when it lands", anchor="middle")

write(p, "plate-08-the-tipping-scale-alt",
      deck="Unfairness rarely arrives as one moment.",
      caption="The last pebble is rarely the whole weight.")
