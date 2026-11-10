"""The Conversation She's Never Heard (Chapter 11).

The whole argument is drawn where it actually happens: looping over his
head. She is standing right there. The only thing between them is a
dotted line, because none of it has been said.
"""
import math
from platekit import Plate, W, write

p = Plate(height=146, seed=103, title="The Conversation She&#8217;s Never Heard")

FLOOR = 128
HIM, HER = 62, 262

# the argument, going round and round
cx, cy = HIM + 2, 34
loop = []
for i in range(321):
    t = i / 320 * math.tau * 7
    rx = 19 + 7 * math.sin(0.61 * t + 0.5)
    ry = 11 + 4.5 * math.cos(0.43 * t)
    loop.append((cx + 3 * math.sin(0.29 * t) + rx * math.cos(t), cy + 1.5 * math.cos(0.37 * t) + ry * math.sin(t)))
p.curve(loop)
for k, (dx, dy) in enumerate(((1.5, 21), (0.5, 26))):          # it belongs to him
    p.dot(cx - 2 + dx, cy + dy, r=1.1 - 0.3 * k)

p.straight(HIM - 44, FLOOR, HER + 44, FLOOR)
p.person(HIM, FLOOR, "man")
p.person(HER, FLOOR, "woman")

# what has crossed the room so far
chest = FLOOR - 37
p.straight(HIM + 24, chest, HER - 26, chest, cls="bold dotted")
p.label((HIM + HER) / 2, chest - 8, "you haven&#8217;t told her", cls="ital", anchor="middle")

p.label(0, 9, "In your head")
p.label(HER, FLOOR - 70, "With her", anchor="middle")

write(p, "plate-11-the-conversation-shes-never-heard",
      deck="You keep arguing with her in your head.",
      caption="Tell her what&#8217;s bothering you.<br>Then listen.")
