---
id: 063
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 17:38
applied_by: grep -rq 'bottom band' tests/
---

# svg_to_png silently lost the bottom fifth of every plate capture while the PNG dimensions stayed correct. Should tests/run.py carry a raster fixture that counts ink in the bottom band?

Four desks each rediscovered this separately today, and it cost the Ch12 verdict PDF its plate's last three lines. The fix landed on inspection with no fixture, so the next renderer change can reintroduce it silently - a dimensions check would not catch it.

**Recommendation:** Yes: a 200x200 SVG with a black band at y=190, asserting dark pixels in rows 570..600 of the 3x capture, printing SKIP if the browser is absent

**Checked:**

```
old path (chrome --window-size): png 600x600, dark px in rows 570..600 = 0. new path (Playwright viewport): png 600x600, dark px in rows 570..600 = 18000. Both measured 2026-09-20 16:36 on an identical source SVG.
```

**What unblocks this:** Whether the rasteriser's correctness is proven by a re-runnable case or by a 77-word docstring
