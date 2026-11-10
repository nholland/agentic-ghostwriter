"""Meet hostility with kindness, frustration with patience, disconnection with warmth (Chapter 15).

Three small scenes with the same two people. He is the bold figure.
Hostility: her sharp remark goes past him. Frustration: the load that
was at her feet is now at his. Disconnection: her words reach him and he
says nothing back.
"""
from platekit import Plate, W, write

p = Plate(height=132, seed=127, title="Meet hostility with kindness, frustration with patience, disconnection with warmth")

FLOOR, S = 90, 0.82
COLS = [(54, "Hostility", "Kindness", "let it go"),
        (162, "Frustration", "Patience", "start helping first"),
        (270, "Disconnection", "Warmth", "let her talk")]
HEAD = FLOOR - 46 * 1.26 * S          # roughly the top of a head


def raw(pts, cls="line"):
    p.parts.append(f'<path class="ink {cls}" d="M' + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + '"/>')


def basket(x, cls):
    raw([(x - 8.5, FLOOR - 11), (x + 8.5, FLOOR - 11), (x + 6.4, FLOOR), (x - 6.4, FLOOR), (x - 8.5, FLOOR - 11)], cls)
    p.curve([(x - 7.3, FLOOR - 11), (x - 3, FLOOR - 16.5), (x + 2.5, FLOOR - 17), (x + 7.3, FLOOR - 11)], cls=cls)


for cx, hers, his, how in COLS:
    her_x, him_x = cx - 29, cx + 29
    p.straight(cx - 48, FLOOR, cx + 48, FLOOR)
    p.person(her_x, FLOOR, "woman", s=S)
    p.person(him_x, FLOOR, "man", s=S, cls="bold")

    if hers == "Hostility":                       # the zing goes over his shoulder and keeps going
        x0, y0, x1, y1 = her_x + 10, HEAD + 6, him_x + 19, HEAD - 17
        n = 13
        zig = [(x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n + (2.6 if i % 2 else -2.6) * (0 < i < n)) for i in range(n + 1)]
        raw(zig)
    elif hers == "Frustration":                   # the load moves from her feet to his
        basket(her_x + 20, "line dotted")
        basket(him_x - 19, "line")
    else:                                         # her words arrive; nothing comes back
        swell = p._noise(1.0, 26)
        for k in range(4):
            y = HEAD + 7 + k * 4.4
            p.stroke(lambda x, y=y: y + swell(x), her_x + 11 + k * 1.3, him_x - 12, wobble=0.15, step=3)

    p.label(cx, 9, hers, anchor="middle")
    p.label(cx, FLOOR + 15, his, anchor="middle")
    p.label(cx, FLOOR + 28, how, cls="ital", anchor="middle")

write(p, "plate-15-meet-hostility-with-kindness",
      deck="When your wife&#8217;s day turns sharp.",
      caption="&#8220;Was I the best part of her day?&#8221;")
