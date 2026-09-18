---
id: 027
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 18:45
---

# Delete the Stop hook's fixture guard and run the fixtures unconditionally?

The guard is 'git diff --quiet HEAD -- scripts/ tests/'. Tested across six tree states it skips in five of them, including the most common one: after the author commits the very check he edited, which is the normal end of a session. It also misses a brand-new untracked script, a brand-new untracked fixture, and any change to config/house.json, which is the input to nine of the fourteen fixtures. The same hook file already uses 'git ls-files --others --exclude-standard' twelve lines above for exactly the untracked case.

**Recommendation:** Delete the guard. It gates a 0.297 second command and costs 41 words. This is a deletion, so its close-condition is necessarily textual - there is no fixture for the absence of code.

**Checked:**

```
pristine clean: SKIPPED. unstaged: runs. staged: runs. COMMITTED: SKIPPED. untracked script: SKIPPED. untracked fixture: SKIPPED. house.json edited: SKIPPED.
```

**What unblocks this:** Whether the fixtures run at the end of the session that changed a check.
