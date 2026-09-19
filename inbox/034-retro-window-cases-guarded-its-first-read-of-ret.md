---
id: 034
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 01:48
resolved: 2026-09-19 01:48
---

# retro_window_cases() guarded its first read of retro-window and not its second, so a regression tracebacks instead of reporting - and it never asserted the dispatch message carries the range. Guard the second read and add that assertion?

tests/run.py's window2 = open(window_path).read().split() had no os.path.exists guard, unlike the first read above it. On a regression retro_window_cases() would raise before returning, discarding the rows it already computed and printing a traceback instead of a named [FAIL] - #021's shape, inside the fixture written to end that shape. It also never checked the one channel the Publisher actually reads: whether the dispatch message text carries the range.

**Recommendation:** guard window2 the same way window is guarded; add a row asserting f'{start_sha}..{head_sha}' in r.stderr

**Checked:**

```
git archive 1062b73^ into scratch + copy new tests/run.py -> CRASH: FileNotFoundError, zero rows reported; after the fix: python3 tests/run.py -> 37/37 fixtures pass
```

**What unblocks this:** a regression in retro-check.sh reports as a named failure instead of aborting the whole suite, and the dispatch-message channel is covered

**Resolution (2026-09-19 01:48):** Applied directly - a bug in code from two commits ago, small, well-evidenced by the Archivist, same pattern as this session's other proactive small fixes.
