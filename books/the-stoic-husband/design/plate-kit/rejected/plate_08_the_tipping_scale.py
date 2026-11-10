"""The Tipping Scale (Chapter 8).

Above: small things nobody named pile up in one pan as blank pebbles,
and the last one tips it. Below: the same small things, each named as it
landed and set down beside the scale. The names are the chapter's own
examples. The pans are empty and the beam is level.
"""
import math
from platekit import Plate, W, write

p = Plate(height=220, seed=83, title="The Tipping Scale")

CX, ARM, STAND = W / 2, 52, 58


def pan(ex, ey):
    """A pan hanging from the beam end; returns the y of its rim."""
    rim = ey + 30
    p.seg(ex, ey, ex - 17, rim, cls="hair", wobble=0.05)
    p.seg(ex, ey, ex + 17, rim, cls="hair", wobble=0.05)
    p.curve([(ex - 17, rim), (ex - 10, rim + 6.6), (ex, rim + 9.2), (ex + 10, rim + 6.6), (ex + 17, rim)])
    p.seg(ex - 17, rim, ex + 17, rim, wobble=0.05)
    return rim


def balance(apex_y, tilt_deg, ground=(CX - 34, CX + 34)):
    a = math.radians(tilt_deg)
    dx, dy = ARM * math.cos(a), ARM * math.sin(a)
    left, right = (CX - dx, apex_y + dy), (CX + dx, apex_y - dy)
    base = apex_y + STAND
    p.straight(ground[0], base, ground[1], base)
    p.seg(CX, apex_y, CX - 10, base)
    p.seg(CX, apex_y, CX + 10, base)
    p.seg(*left, *right, wobble=0.1)
    return (left[0], pan(*left)), (right[0], pan(*right)), base


# --- uncounted: blank pebbles, and the one that tips it -------------------
p.label(0, 9, "Uncounted")
(lx, rim), _, _ = balance(36, 15)
for r, n in enumerate((4, 3, 2)):
    for k in range(n):
        p.ring(lx + (k - (n - 1) / 2) * 5.4, rim - 2.8 - r * 4.6, 2.2, cls="line")
land = (lx, rim - 2.8 - 3 * 4.6 - 0.6)
p.curve([(lx - 22, 12), (lx - 16, 24), (lx - 8, 40), (land[0] - 1.6, land[1] - 5.5)], cls="line dotted")
p.dot(*land, r=2.8)

# --- named when it lands: each one set down with its name -----------------
Y2 = 124
p.label(0, Y2, "Named when it lands")
_, _, base = balance(Y2 + 22, 0, ground=(0, W))
NAMED = [(40, "a critique that stung"),
         (128, "a weekend of work"),
         (262, "a morning you kept the peace")]
for x, name in NAMED:
    p.dot(x, base - 2.6, r=2.6)
    p.label(x, base + 13, name, cls="ital", anchor="middle")

write(p, "plate-08-the-tipping-scale",
      deck="Unfairness rarely arrives as one moment.",
      caption="The last pebble is rarely the whole weight.")
