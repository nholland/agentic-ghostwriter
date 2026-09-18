---
id: 030
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 20:18
resolved: 2026-09-18 23:47
applied_by: grep -q retro-last-sha .claude/hooks/retro-check.sh && grep -q retro-last-sha .claude/agents/gw-retro.md && grep -q retro-last-sha agents/gw-retro.md
---

# The Archivist's review window silently halved this session. Should it read .claude/state/retro-last-sha instead of session-start-sha?

session-start-sha is rewritten by every SessionStart, including a resumed thread. It moved at 20:01 to a commit four into this session, so the prescribed review window covered 8 commits and missed 6 - including both book-repo constitution writes, the metaphor-cap application, and all four proposal fixes (#024-#027). Only the Publisher's hand-written list of ten items in the dispatch prompt saved this review. retro-done-<sha> is keyed to the same moving value, so one session can be reviewed twice on overlapping ranges, and session_log.py restated the same commit list eight times in 18 minutes for the same reason.

**Recommendation:** retro-check.sh writes .claude/state/retro-last-sha after it fires; the gw-retro brief reads that file and falls back to session-start-sha only when it is absent. Leave session-start-sha alone - the branch-hygiene hook needs it.

**Checked:**

```
git log --oneline $(cat .claude/state/session-start-sha)..HEAD | wc -l -> 8 commits in the visible window; git log 273d4d9..<session-start-sha> shows 5 more commits (82b833b, 3f16531, 8b8ddbe, f335220, 9dde2aa) that the prescribed window would have missed.
```

**What unblocks this:** The Archivist reads the whole session without being handed a manifest by hand, and runs/log.md stops restating itself.

**Resolution (2026-09-18 23:47):** fix everything that is outstanding

**Not applied yet.** This ruling lands outside this repo. It closes when `grep -q retro-last-sha .claude/hooks/retro-check.sh && grep -q retro-last-sha .claude/agents/gw-retro.md && grep -q retro-last-sha agents/gw-retro.md` exits 0.

**Applied, confirmed 2026-09-18 23:47:** `grep -q retro-last-sha .claude/hooks/retro-check.sh && grep -q retro-last-sha .claude/agents/gw-retro.md && grep -q retro-last-sha agents/gw-retro.md` now exits 0.
