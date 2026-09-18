---
id: 030
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 20:18
---

# The Archivist's review window silently halved this session. Should it read .claude/state/retro-last-sha instead of session-start-sha?

session-start-sha is rewritten by every SessionStart, including a resumed thread. It moved at 20:01 to a commit four into this session, so the prescribed review window covered 8 commits and missed 6 - including both book-repo constitution writes, the metaphor-cap application, and all four proposal fixes (#024-#027). Only the Publisher's hand-written list of ten items in the dispatch prompt saved this review. retro-done-<sha> is keyed to the same moving value, so one session can be reviewed twice on overlapping ranges, and session_log.py restated the same commit list eight times in 18 minutes for the same reason.

**Recommendation:** retro-check.sh writes .claude/state/retro-last-sha after it fires; the gw-retro brief reads that file and falls back to session-start-sha only when it is absent. Leave session-start-sha alone - the branch-hygiene hook needs it.

**Checked:**

```
git log --oneline $(cat .claude/state/session-start-sha)..HEAD | wc -l -> 8 commits in the visible window; git log 273d4d9..<session-start-sha> shows 5 more commits (82b833b, 3f16531, 8b8ddbe, f335220, 9dde2aa) that the prescribed window would have missed.
```

**What unblocks this:** The Archivist reads the whole session without being handed a manifest by hand, and runs/log.md stops restating itself.
