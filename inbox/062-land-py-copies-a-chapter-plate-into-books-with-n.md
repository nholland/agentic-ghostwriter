---
id: 062
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 17:38
applied_by: grep -q svgcheck scripts/land.py
---

# land.py copies a chapter plate into books/ with no check at all. Should it run runs/design/svgcheck.py first and refuse a MARGIN or COLLIDE row unless --force?

The Ch12 plate landed on 2026-09-18 printing a quarter of its gloss off the artboard, past two gates. The checker existed, was right about the geometry, and nothing called it at the one moment a plate becomes permanent. Promoting it was already proposed on 2026-09-16 (S2) and never applied.

**Recommendation:** Yes: call it in land.py before the copy, refuse on MARGIN/COLLIDE with the row printed, --force to override, and add the two-SVG fixture pair

**Checked:**

```
python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg -> 'MARGIN y=340.0 no deadline, nobody watching -44..132'; same checker on runs/ch12/plate.svg -> 'clean'; grep -n plate scripts/land.py -> lines 159-168 copy the file with no check
```

**What unblocks this:** Whether a plate the checker flags can reach books/ without the author saying --force, and whether svgcheck.py gains its first behavioural fixture
