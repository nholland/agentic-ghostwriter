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
Corrected 2026-09-20 15:16 - "After repair+fix -> (13, 0)" below was wrong when
written: 13 was carried forward from the Archivist's prior review prose rather
than re-run, inside the very item whose subject is that exact habit. Re-run
just now against runs/log.md at commit 61c6e17 (this item's own fix, before
the next commit added another log entry): (26, 0), not (13, 0). Confirmed
independently: `git show 61c6e17:runs/log.md` copied into an isolated tmp
root and run through next_action_streak - (26, 0). At HEAD today the number
has moved further (more sessions have logged /gw 13 since); the durable claim
is "no gap remains unaccounted for in the trailing run," not a specific count.

Before: python3 -c 'import sys; sys.path.insert(0,"scripts"); import next; print(next.next_action_streak("/gw 13"))' -> 6. After repair+fix, measured at 61c6e17 -> (26, 0), no gaps left in the trailing run. python3 tests/run.py -> 97/97.

Also corrected 2026-09-20 15:16 - the fixture named below did not actually
test the fix. Its malformed entry sat next to a genuine different-command
entry (/gw 5), so break-on-missing and skip-on-missing both returned (2, 1) -
verified by reverting only the continue-vs-break line and re-running: suite
still 97/97, this case still [ ok ]. Reshaped the fixture to place the gap
between two matching entries on both sides (now asserts (4, 1)); reverting
that same line now correctly fails: got (2, 1), [FAIL]. Also added a
tolerant int-or-tuple unpack so the case is no longer exempt from
tests/prove.py the way this item originally (and wrongly) argued: `python3
tests/prove.py --file scripts/next.py --at bd43509 --case "next: a malformed
log entry is skipped, not read as a direction change"` -> PROVED, exit 0.
```

**What unblocks this:** whether the author sees an accurate count of how long the house has been away from the book

**Resolution (2026-09-20 15:09):** Applied directly - a live, undercounted number the house reports to the author every session, caused by data damage that was fully recoverable from git history.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-20 15:09:** `python3 tests/run.py` now exits 0.
