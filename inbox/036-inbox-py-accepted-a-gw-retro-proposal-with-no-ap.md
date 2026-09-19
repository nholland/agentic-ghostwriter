---
id: 036
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:29
applied_by: python3 tests/run.py
resolved: 2026-09-19 06:29
---

# inbox.py accepted a gw-retro proposal with no --applied-by - 8 of the first 18 landed that way, because --add silently dropped the flag (only --close ever wrote it) and nothing forced the desk or the Publisher relaying it to notice. Refuse --add without it, and carry the value forward on --close?

gw-retro's own brief ends every proposal with --applied-by, but --add never read a.applied_by at all - it only mattered if repeated on --close. #033 and #034 both closed with no proof field for exactly this reason.

**Recommendation:** --add exits 2 for a gw-retro item missing --applied-by and records the value into the new item's frontmatter; --close falls back to that stored value when --applied-by isn't repeated

**Checked:**

```
python3 tests/run.py -> 3 new inbox_cases() rows: refuses a gw-retro --add with no --applied-by, records it in frontmatter, carries it forward on --close with no --applied-by repeated - all pass
```

**What unblocks this:** every future gw-retro proposal carries a re-runnable proof command with no reliance on the desk or Publisher remembering to repeat it at close time

**Resolution (2026-09-19 06:29):** Approved by the author, applied directly.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 06:29:** `python3 tests/run.py` now exits 0.
