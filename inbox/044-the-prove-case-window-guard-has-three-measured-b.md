---
id: 044
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 07:18
applied_by: python3 tests/run.py
resolved: 2026-09-19 07:18
---

# The --prove-case window guard has three measured bypasses (rename an old case, reuse this window's own case, or corrupt .claude/state/retro-window to silently disable the check) that no next layer mechanically closes - stop hardening this lineage, make the residual visible instead, and move to Chapter 13?

Seven rounds (#036, #039, #040, #041, #042, #043, this one) each built a guard the next review broke inside ten minutes. Verified independently: (a) renaming four words of an existing discriminating case reopens the mascot attack, exit 0; (b) reusing this window's own just-added case (no rename needed) reopens it too, exit 0; (c) corrupting retro-window to a garbage SHA silently disabled the check entirely with no output, exit 0 - and all three state files are gitignored, so a fresh clone has it off by default. Binding an English proposal to a fixture is a semantic judgment a script cannot make. 70+ commits since 2026-09-18 12:00 have gone into this machinery while next.py has read '/gw 13' the whole time.

**Recommendation:** stop adding layers. Land only the honesty edit: inbox.py prints a NOTE when the freshness check can't run (window absent, or unreadable at the pointed-to commit) instead of silently skipping; tests/prove.py's USAGE note is replaced with a WHAT THIS DOES NOT DO section naming all three residual holes and saying explicitly not to add an eighth layer. Then /gw 13.

**Checked:**

```
Mutation-tested: reverted scripts/inbox.py to c0e39e1 (before this change) -> [FAIL] on the new NOTE case, got exit 0 with no warning printed; restored -> [ ok ]. python3 tests/prove.py --file scripts/inbox.py --at c0e39e1 --case 'inbox says the freshness check did not run when the window is unreadable' -> PROVED, exit 0. Full suite: 61/61. Corpus (cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w) unchanged at 17,017 - everything landed in tests/ and scripts/.
```

**What unblocks this:** whether the next session hardens this further or drafts Chapter 13

**Resolution (2026-09-19 07:18):** Applied directly - the Archivist gave a genuine, well-evidenced recommendation to stop hardening this lineage and make its known limits honest instead, verified independently before acting. Agreed: three deliberate-effort bypasses that show up in a diff are an acceptable residual; the machinery already catches the failure mode that happened by accident twice. Moving to Chapter 13.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 07:18:** `python3 tests/run.py` now exits 0.
