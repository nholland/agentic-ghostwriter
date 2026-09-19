---
id: 039
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:39
applied_by: python3 tests/run.py 2>&1 | grep -q '^\[ ok \] session_log skips when the last entry listed runs/log.md itself'
resolved: 2026-09-19 06:39
---

# session_log.py's dedup guard strips runs/log.md from the current file set but not from the last entry's, so the two sets differ by exactly that one element and never match once the log is in the cumulative diff - it wrote a duplicate on its first real Stop. Strip both sides, and add the case the fixture was missing?

The guard landed 2026-09-19 06:29 and produced two identical 06:30 entries in the same session. session_log_dedup_cases() passed because its synthetic repo never committed runs/log.md between runs, which is the one thing the real Stop hook always does.

**Recommendation:** return set(...) - {'runs/log.md'} from last_entry_files(); extend the fixture with a commit of runs/log.md between the first and second run

**Checked:**

```
reproduced independently (git status before the log commit showed no pollution; before the fix, the same sequence via tests/run.py's own methodology printed 'session_log: appended' on the second run instead of 'same file set'); after the fix, python3 tests/run.py -> 50/50, including the new case 'session_log skips when the last entry listed runs/log.md itself'
```

**What unblocks this:** whether runs/log.md stops re-accumulating the duplicate blocks that were just cleaned out of it, twice now

**Resolution (2026-09-19 06:39):** Applied directly - a genuine regression in this session's own prior fix, reproduced independently before trusting the Archivist's report, then corrected with a fixture that actually exercises the real sequence.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py 2>&1 | grep -q '^\[ ok \] session_log skips when the last entry listed runs/log.md itself'` exits 0.

**Applied, confirmed 2026-09-19 06:39:** `python3 tests/run.py 2>&1 | grep -q '^\[ ok \] session_log skips when the last entry listed runs/log.md itself'` now exits 0.
