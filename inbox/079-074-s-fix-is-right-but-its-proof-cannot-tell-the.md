---
id: 079
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:18
applied_by: R=$(git rev-parse --show-toplevel); T=$(mktemp -d); git -C "$R" worktree add -q --detach "$T" 0074d6e3 >/dev/null 2>&1; mkdir -p "$T/.claude/state"; echo 84b79969b60fbad3f61147b68f4dbbc01b0deeff > "$T/.claude/state/retro-last-sha"; rc=0; CLAUDE_PROJECT_DIR="$T" bash "$R/.claude/hooks/retro-check.sh" >/dev/null 2>&1 || rc=$?; git -C "$R" worktree remove --force "$T" >/dev/null 2>&1; test "$rc" -ne 2
---

# #074's fix is right but its proof cannot tell the fix from the non-fix: 'skip commits touching runs/retro/' as a pathspec exclusion still dispatches, because the retro's inbox filings are themselves watched. Should #074 close on a mixed-commit fixture in retro_window_cases() instead of a grep for its own sentence?

retro-check.sh never watched runs/, so ':!runs/retro/' is a no-op and the loop continues; only dropping the whole commit works. #074's applied_by greps tests/ for its own wording, which exits 0 over either implementation. Eight consecutive gw-retro items now carry grep-shaped proofs on the belief that #048 forbids fixtures here, but tests/run.py's retro_window_cases() already runs retro-check.sh against a real temp repo.

**Recommendation:** Yes: implement #074 as a commit-level filter, add a mixed commit (inbox/ + runs/retro/ in one commit) to retro_window_cases(), and close both items on the behavioural proof below rather than on grep

**Checked:**

```
Window 84b79969..0074d6e3, sole work commit f194db48 touches inbox/075, inbox/076, runs/retro/2026-09-21-plate-packet.md. WATCHED='bakeoff/ inbox/ scripts/ config/ books/ FINDINGS.md'. git rev-list --count 84b79969..0074d6e3 -- $WATCHED -> 1 (dispatches). Same with ':!runs/retro/' appended -> 1 (still dispatches). Commit-level filter dropping any commit containing a runs/retro/ path -> 0 (skipped). python3 tests/run.py -> 107/107 fixtures pass, exit 0, so tests/run.py alone as applied_by is tautological. tests/run.py:1270 already resolves .claude/hooks/retro-check.sh and runs it via subprocess against a temp git repo.
```

**What unblocks this:** Whether the retro loop's fix is verified by behaviour or by wording, and whether the eight-item grep-proof habit ends where a harness already exists
