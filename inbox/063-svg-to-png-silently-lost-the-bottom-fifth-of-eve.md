---
id: 063
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 17:38
resolved: 2026-09-26 17:32
applied_by: python3 tests/export_safety_cases.py --render
---

# svg_to_png silently lost the bottom fifth of every plate capture while the PNG dimensions stayed correct. Should tests/run.py carry a raster fixture that counts ink in the bottom band?

Four desks each rediscovered this separately today, and it cost the Ch12 verdict PDF its plate's last three lines. The fix landed on inspection with no fixture, so the next renderer change can reintroduce it silently - a dimensions check would not catch it.

**Recommendation:** Yes: a 200x200 SVG with a black band at y=190, asserting dark pixels in rows 570..600 of the 3x capture, printing SKIP if the browser is absent

**Checked:**

```
old path (chrome --window-size): png 600x600, dark px in rows 570..600 = 0. new path (Playwright viewport): png 600x600, dark px in rows 570..600 = 18000. Both measured 2026-09-20 16:36 on an identical source SVG.
```

**What unblocks this:** Whether the rasteriser's correctness is proven by a re-runnable case or by a 77-word docstring

**Previous proof (retired; replaced by behavioral coverage):**

```sh
grep -rq 'bottom band' tests/
```

**Resolution (2026-09-26 17:32):** Approved. Bottom-edge raster coverage now counts ink at 2x and 3x, and capture waits for fonts. Chromium rendering cases pass. Evidence: runs/qa/2026-09-26-export-safety-ch01-ch13.md. No agent instructions changed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/export_safety_cases.py --render` exits 0.

**Applied, confirmed 2026-09-26 17:32:** `python3 tests/export_safety_cases.py --render` now exits 0.
