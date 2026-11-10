"""Calm and strength make the marriage sound; warmth makes it a home (Chapter 16).

The same house twice. Its two bold walls are calm and strength, and on
the left that is all there is: sound, shut, dark. On the right the
window is lit, the door is open with light on the step, and there is
smoke from the chimney.
"""
import math
from platekit import Plate, W, write

p = Plate(height=166, seed=131, title="Calm and strength make the marriage sound; warmth makes it a home")
rng = p.rng

FLOOR, EAVES, APEX = 124, 78, 47
HALF = 38                                   # half the width of the house


def house(cx, warm):
    p.straight(cx - 58, FLOOR, cx + 58, FLOOR)
    # chimney first, so the roof line sits in front of it
    roof_y = lambda x: APEX + (x - cx) / (HALF + 9) * (EAVES - APEX)   # the roof line on the right slope
    p.seg(cx + 18, roof_y(cx + 18), cx + 18, APEX + 1)
    p.seg(cx + 27, roof_y(cx + 27), cx + 27, APEX + 1)
    p.seg(cx + 16.5, APEX + 1, cx + 28.5, APEX + 1)
    # roof
    p.seg(cx - HALF - 9, EAVES, cx, APEX, wobble=0.1)
    p.seg(cx, APEX, cx + HALF + 9, EAVES, wobble=0.1)
    p.seg(cx - HALF - 9, EAVES, cx + HALF + 9, EAVES, wobble=0.1)
    # the two walls: calm and strength
    p.seg(cx - HALF, EAVES, cx - HALF, FLOOR, cls="bold", wobble=0.06)
    p.seg(cx + HALF, EAVES, cx + HALF, FLOOR, cls="bold", wobble=0.06)
    # door and window
    dx0, dx1, dtop = cx - 21, cx - 6, FLOOR - 29
    wx0, wx1, wy0, wy1 = cx + 7, cx + 25, FLOOR - 33, FLOOR - 15
    p.seg(dx0, FLOOR, dx0, dtop, wobble=0.05)
    p.seg(dx0, dtop, dx1, dtop, wobble=0.05)
    p.seg(dx1, dtop, dx1, FLOOR, wobble=0.05)
    for a, b in (((wx0, wy0), (wx1, wy0)), ((wx1, wy0), (wx1, wy1)), ((wx1, wy1), (wx0, wy1)), ((wx0, wy1), (wx0, wy0))):
        p.seg(*a, *b, wobble=0.05)
    p.seg((wx0 + wx1) / 2, wy0, (wx0 + wx1) / 2, wy1, cls="hair", wobble=0.0)
    p.seg(wx0, (wy0 + wy1) / 2, wx1, (wy0 + wy1) / 2, cls="hair", wobble=0.0)

    if not warm:
        x = dx0 + 1.9                                      # a shut door, in close grain
        while x < dx1 - 0.6:
            p.seg(x, dtop + 1, x, FLOOR, cls="hair", wobble=0.05)
            x += 1.9
        p.dot(dx1 - 3.2, FLOOR - 13, r=0.9, clear=1.9)
        return

    # light from the window
    wcx, wcy = (wx0 + wx1) / 2, (wy0 + wy1) / 2
    for k in range(12):
        a = math.tau * k / 12 + 0.26
        r0, r1 = 14.5, 19 + (k % 2) * 2.5
        if wcy + r1 * math.sin(a) > FLOOR - 2 or wcx + r0 * math.cos(a) > cx + HALF - 2 or wcy + r1 * math.sin(a) < EAVES + 2:
            continue                                       # keep the rays inside the room
        p.seg(wcx + r0 * math.cos(a), wcy + r0 * math.sin(a), wcx + r1 * math.cos(a), wcy + r1 * math.sin(a), wobble=0.0)
    # the door stands open: light on the step
    for j in range(5):
        x0 = dx0 + (dx1 - dx0) * (j + 0.5) / 5
        lean = (x0 - (dx0 + dx1) / 2) * 0.55
        p.seg(x0, FLOOR + 2.4, x0 + lean, FLOOR + 12 - rng.uniform(0, 2.5), wobble=0.08)
    # smoke
    sx = cx + 22.5
    p.curve([(sx, APEX - 2), (sx - 3.2, APEX - 8), (sx + 2.6, APEX - 13), (sx - 2.4, APEX - 19), (sx + 3, APEX - 24.5)])
    p.label(cx - 2, EAVES - 6.5, "Warmth", anchor="middle")


for cx, over, under, warm in ((81, "calm alone can go cold", "structurally sound", False),
                              (243, "small, warm things", "a home", True)):
    house(cx, warm)
    p.label(cx - (18 if warm else 0), 9, over, cls="ital", anchor="middle")
    p.label(cx - HALF, FLOOR + 21, "Calm", anchor="middle")
    p.label(cx + HALF, FLOOR + 21, "Strength", anchor="middle")
    p.label(cx, FLOOR + 36, under, cls="ital", anchor="middle")

write(p, "plate-16-calm-strength-warmth",
      deck="Warmth is what the calm and the strength were for.",
      caption="At peace, at its best, and flourishing.")
