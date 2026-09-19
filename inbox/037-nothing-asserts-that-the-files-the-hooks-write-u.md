---
id: 037
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:29
applied_by: python3 tests/run.py
resolved: 2026-09-19 06:29
---

# Nothing asserts that the files the hooks write under .claude/state/ are gitignored - retro-window was introduced without its line and caught only because a review happened to run. Add a fixture that checks every hook-written state file against .gitignore?

The ignore line is a per-file manual step with no check behind it. This particular miss cost nothing - the same miss on session-start-sha cost five empty auto-commits on 2026-09-14, which is why the .gitignore comment names that incident at all.

**Recommendation:** parse $STATE/<name> out of .claude/hooks/*.sh and assert git check-ignore on each

**Checked:**

```
python3 tests/run.py -> state_ignore_cases(): 4/4 pass (retro-done-probe, retro-last-sha, retro-window, session-start-sha)
```

**What unblocks this:** a hook can gain a new state file without the author or a review having to remember the .gitignore line

**Resolution (2026-09-19 06:29):** Approved by the author, applied directly.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 06:29:** `python3 tests/run.py` now exits 0.
