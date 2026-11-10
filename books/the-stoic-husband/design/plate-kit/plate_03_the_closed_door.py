"""The Closed Door (Chapter 3).

One doorway, four times. What she brings is the light that comes through
it. Each defence swings the door a third of the way shut, and the light
on the floor narrows with it until there is none.
"""
from platekit import Plate, W, write

p = Plate(height=146, seed=31, title="The Closed Door")

COL = W / 4
FW, TOP, FLOOR = 46, 5, 93          # doorway width, lintel, threshold
SPILL = 25                          # how far the light reaches across the floor
STEPS = [("she brings something", 0.0),
         ("you defend", 1 / 3),
         ("she updates", 2 / 3),
         ("she stops", 1.0)]

prev_right = 0
for i, (name, shut) in enumerate(STEPS):
    cx = COL * (i + 0.5)
    left, right = cx - FW / 2, cx + FW / 2
    edge = right - FW * shut         # leading edge of the door

    # the floor runs between doorways, never across an open one
    p.straight(prev_right, FLOOR, left, FLOOR)
    prev_right = right

    # the doorway
    p.seg(left, FLOOR, left, TOP)
    p.seg(left, TOP, right, TOP)
    p.seg(right, TOP, right, FLOOR)

    # the door: tone from close vertical grain, then its leading edge
    x = right - 1.9
    while x > edge + 0.8:
        p.seg(x, TOP + 1.2, x, FLOOR, wobble=0.1)
        x -= 1.9
    if shut:
        p.straight(edge, FLOOR, right, FLOOR, cls="line")
        p.seg(edge, TOP, edge, FLOOR, cls="bold", wobble=0.08)
        p.dot(edge + 6.2, (TOP + FLOOR) / 2 + 4, r=1.0, clear=2.4)

    # what still comes through: light fanning out over the floor
    n = round((edge - left) / 3.7)
    for j in range(n):
        x0 = left + (edge - left) * (j + 0.5) / n
        lean = (x0 - (left + edge) / 2) * 0.5     # fans outward from the middle of the opening
        p.seg(x0, FLOOR + 2.5, x0 + lean, FLOOR + SPILL - p.rng.uniform(0, 5), wobble=0.12)

    p.label(cx, FLOOR + SPILL + 20, name, cls="ital", anchor="middle")

p.straight(prev_right, FLOOR, W, FLOOR)

write(p, "plate-03-the-closed-door",
      deck="Defend yourself enough times, and she stops bringing you the truth.",
      caption="She&#8217;s been keeping track longer than you know.")
