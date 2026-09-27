---
id: 062
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 17:38
resolved: 2026-09-26 17:32
applied_by: python3 tests/export_safety_cases.py
---

# land.py copies a chapter plate into books/ with no check at all. Should it run runs/design/svgcheck.py first and refuse a MARGIN or COLLIDE row unless --force?

The Ch12 plate landed on 2026-09-18 printing a quarter of its gloss off the artboard, past two gates. The checker existed, was right about the geometry, and nothing called it at the one moment a plate becomes permanent. Promoting it was already proposed on 2026-09-16 (S2) and never applied.

**Recommendation:** Yes: call it in land.py before the copy, refuse on MARGIN/COLLIDE with the row printed, --force to override, and add the two-SVG fixture pair

**Checked:**

```
python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg -> 'MARGIN y=340.0 no deadline, nobody watching -44..132'; same checker on runs/ch12/plate.svg -> 'clean'; grep -n plate scripts/land.py -> lines 159-168 copy the file with no check
```

**What unblocks this:** Whether a plate the checker flags can reach books/ without the author saying --force, and whether svgcheck.py gains its first behavioural fixture

**Previous proof (retired; replaced by behavioral coverage):**

```sh
grep -q plate_check scripts/land.py
```

**Resolution (2026-09-26 17:32):** Approved. Keep complexity in scripts rather than agents. The actual landing gate now has clean/failing/force behavioral coverage; resolved book/run paths and portable DejaVu metrics are verified. Evidence: runs/qa/2026-09-26-export-safety-ch01-ch13.md. No agent instructions changed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/export_safety_cases.py` exits 0.

**Applied, confirmed 2026-09-26 17:32:** `python3 tests/export_safety_cases.py` now exits 0.
