---
id: 050
status: resolved
raised_by: Publisher
chapter: 0
opened: 2026-09-20 15:09
applied_by: python3 tests/run.py
resolved: 2026-09-20 15:09
---

# runs/log.md is one shared file two concurrent sessions' merges corrupted twice (2026-09-19 06:38 and 13:45 entries lost their file lists and Next lines), and next_action_streak() treated each gap as a change of direction - next.py reported 'unchanged for 6 log entries' when the true run was 13 of the last 14. Repair the two entries from git history and make the streak skip-and-count malformed entries instead of breaking on them?

The Archivist found this reviewing a window it pulled in via merge-main; I verified it independently before acting. The 06:38 entry had 9 files and no Next line where its pre-merge version (ae949db) had 10 files and a Next line; the 13:45 entry was a bare header where its pre-merge version (66b2f63) had 29 files and a Next line. next_action_streak() broke the streak on the first entry with no Next: line, undercounting a real 13-entry run as 6.

**Recommendation:** repair both entries from their pre-merge git history (recoverable, no data actually lost); change next_action_streak() to skip a Next-less entry and count how many it skipped, reporting the gap alongside the streak rather than silently undercounting

**Checked:**

```
Before: python3 -c 'import sys; sys.path.insert(0,"scripts"); import next; print(next.next_action_streak("/gw 13"))' -> 6. After repair+fix -> (13, 0), no gaps left in the last 14 entries. python3 tests/run.py -> 97/97, including a new case built against a synthetic fixture log with one malformed entry, mutation-tested by reverting only the skip-vs-break logic (keeping the tuple return so callers do not crash): reverted gives (2, 0), fixed gives (2, 1). Not routed through tests/prove.py: reverting the whole file to any commit before this fix changes next_action_streak's return signature from int to (int, int), which crashes every caller in streak_cases() rather than failing cleanly - the same class of gap #048 already names (prove.py cannot prove a fixture across an interface change), not a new one.
```

**What unblocks this:** whether the author sees an accurate count of how long the house has been away from the book

**Resolution (2026-09-20 15:09):** Applied directly - a live, undercounted number the house reports to the author every session, caused by data damage that was fully recoverable from git history.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-20 15:09:** `python3 tests/run.py` now exits 0.
