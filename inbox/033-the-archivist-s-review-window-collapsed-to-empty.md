---
id: 033
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 01:41
resolved: 2026-09-19 01:42
---

# The Archivist's review window collapsed to empty again (#030 recurrence) - fixed by writing retro-window before the dedupe pointer?

retro-check.sh wrote .claude/state/retro-last-sha to HEAD_SHA as part of the same dispatch block whose message told gw-retro to read that file as the window's start - so by the time gw-retro read it, dedupe and window start were the same variable, and the window it computed was always empty. #030's own fix closed on a grep for the variable's name, not on running the hook, which is why this recurred unnoticed since 2026-09-18.

**Recommendation:** write .claude/state/retro-window as "START HEAD_SHA" before touching retro-last-sha; gw-retro.md (both copies) reads retro-window first, falling back to retro-last-sha..HEAD only if absent

**Checked:**

```
git stash push -- .claude/hooks/retro-check.sh && python3 tests/run.py -> crashes, retro-window never written by the old hook; git stash pop && python3 tests/run.py -> 36/36 fixtures pass, including 5 new retro_window_cases() that build a real git repo, run the actual hook, and assert the window it writes contains the triggering commit
```

**What unblocks this:** the Archivist actually reviews the commits it is dispatched to review, rather than silently reviewing nothing every time, masked only when the Publisher pastes context by hand

**Resolution (2026-09-19 01:42):** Applied by the Publisher on the Archivist's finding, without waiting for a separate ruling - same pattern as this session's other well-evidenced small fixes (ttfwidth, #030 originally). Verified: the fixture crashes on the pre-fix hook and passes 36/36 on the fixed one.
