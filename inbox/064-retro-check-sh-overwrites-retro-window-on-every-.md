---
id: 064
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 17:38
applied_by: grep -rq 'second dispatch keeps the older window start' tests/
---

# retro-check.sh overwrites retro-window on every dispatch, so when two dispatches fire before a review runs, the earlier window is discarded. This session's recorded window was 2 of 5 commits and excluded both tool fixes. Should the hook preserve the oldest un-consumed START?

Third instance of #030's shape: the review window silently smaller than the session. This review only saw the work because the Publisher passed the bounds by hand. Unlike the freshness guard the 2026-09-19 07:11 entry stopped hardening, this is mechanically decidable - advance only when a commit touching runs/retro/ falls inside the window.

**Recommendation:** Yes: preserve START until a retro file lands inside the window, prove it in the existing retro_window_cases() harness, and cut the paragraph

**Checked:**

```
Two dispatches against a temp repo with no review between: after dispatch 1 window = 0362b3a fd7ef28; after dispatch 2 window = fd7ef28 3fc9533; session spans 0362b3a..3fc9533; commits covered = 1 of 2. Live: .claude/state/retro-window read '98f171f 0a0e1da' against a session of 14cf389..77b9ff7.
```

**What unblocks this:** Whether the Archivist's window is an oracle or a file the Publisher has to correct by hand, and whether gw-retro.md's 115-word warning paragraph can be cut to 52
