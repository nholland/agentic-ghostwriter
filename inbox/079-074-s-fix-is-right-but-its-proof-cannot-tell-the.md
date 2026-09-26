---
id: 079
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:18
applied_by: python3 tests/maintenance_batch_cases.py
resolved: 2026-09-26 18:27
---

# #074's fix is right but its proof cannot tell the fix from the non-fix: 'skip commits touching runs/retro/' as a pathspec exclusion still dispatches, because the retro's inbox filings are themselves watched. Should #074 close on a mixed-commit fixture in retro_window_cases() instead of a grep for its own sentence?

retro-check.sh never watched runs/, so ':!runs/retro/' is a no-op and the loop continues; only dropping the whole commit works. #074's applied_by greps tests/ for its own wording, which exits 0 over either implementation. Eight consecutive gw-retro items now carry grep-shaped proofs on the belief that #048 forbids fixtures here, but tests/run.py's retro_window_cases() already runs retro-check.sh against a real temp repo.

**Recommendation:** Yes: implement #074 as a commit-level filter, add a mixed commit (inbox/ + runs/retro/ in one commit) to retro_window_cases(), and close both items on the behavioural proof below rather than on grep

**Checked:**

```
Window 84b79969..0074d6e3, sole work commit f194db48 touches inbox/075, inbox/076, runs/retro/2026-09-21-plate-packet.md. WATCHED='bakeoff/ inbox/ scripts/ config/ books/ FINDINGS.md'. git rev-list --count 84b79969..0074d6e3 -- $WATCHED -> 1 (dispatches). Same with ':!runs/retro/' appended -> 1 (still dispatches). Commit-level filter dropping any commit containing a runs/retro/ path -> 0 (skipped). python3 tests/run.py -> 107/107 fixtures pass, exit 0, so tests/run.py alone as applied_by is tautological. tests/run.py:1270 already resolves .claude/hooks/retro-check.sh and runs it via subprocess against a temp git repo.
```

**What unblocks this:** Whether the retro loop's fix is verified by behaviour or by wording, and whether the eight-item grep-proof habit ends where a harness already exists

**Resolution (2026-09-26 18:27):** Closed on behavioral fixtures for report plus inbox commits, repeated review-only commits, and mixed report/production commits, replacing the historical one-shot proof.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/maintenance_batch_cases.py` exits 0.

**Applied, confirmed 2026-09-26 18:27:** `python3 tests/maintenance_batch_cases.py` now exits 0.
