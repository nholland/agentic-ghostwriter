---
id: 035
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:28
applied_by: python3 tests/run.py
resolved: 2026-09-19 06:28
---

# runs/log.md restated the same file set on 39 of 117 entries, caused by the retro dispatch's forced second Stop pass logging the same cumulative session-start..HEAD diff. Skip the append when the new file set matches the last entry's?

session_log.py's diff is cumulative from session-start-sha, not incremental, so a Stop with no new work commit since the last entry reproduces the same list verbatim. The retro dispatch exits 2, forcing exactly this second Stop, every time it fires. Named in #030's own Context paragraph in 2026-09-18 with no close condition, so it was never fixed.

**Recommendation:** compare the current file set (minus runs/log.md) against the last '## ' block's file list; skip the append on a match

**Checked:**

```
python3 tests/run.py -> session_log_dedup_cases(): 3/3 pass, confirmed to fail without the fix (git stash the change, same fixture -> [FAIL]); existing runs/log.md cleaned of the 40 duplicate blocks it already had, 120 -> 80 entries, 4993 -> 3401 words
```

**What unblocks this:** runs/log.md stops restating itself and becomes the session memory it claims to be

**Resolution (2026-09-19 06:28):** Approved by the author, applied directly: fixed the guard, added a real fixture proving it (fails on the pre-fix script, passes on the fix), and cleaned the 40 existing duplicate blocks out of runs/log.md.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 06:29:** `python3 tests/run.py` now exits 0.
