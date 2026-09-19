---
id: 046
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 15:01
applied_by: python3 tests/prove_inbox_duplicate.py
---

# Two branches can allocate the same inbox number and nothing catches it. Should inbox.py refuse to operate on a duplicate ID?

This session's runs/parked.md P-002 collision was caught ONLY because parked.md is one file, so git raised a merge conflict. The inbox is one file per item, so the identical collision merges clean and silent. Independently reproduced this session in an isolated temp copy of scripts/+inbox/: two open items both id 045, then '--close 045 --resolution x' exits 0 and closes 045-branch-a.md, binding the ruling to whichever slug sorts first alphabetically rather than the item the author read; 045-branch-b.md stays open and next_id moves to 046, so both persist. 61/61 fixtures stay green because inbox_cases() has no duplicate-ID case - confirmed: all three 'duplicate' hits in tests/run.py are the session-log dedup test at L543/L551/L570. This is #043's shape (a proof bound to the wrong item) reached by a different road, and .claude/LEARNINGS.md already parked the same collision from the old pipeline as 'caught by hand, not by anything structural'. This is instance two. Filing note: this could NOT be filed with --applied-by 'python3 tests/run.py' because tests/prove.py correctly refused - the fixture case does not exist yet. The proof below must be written as part of the fix.

**Recommendation:** inbox.py raises on duplicate IDs at load; --close N exits non-zero naming both paths; add a duplicate-ID case to inbox_cases() in tests/run.py, built the same isolated way it already builds its fixture inbox, AND add tests/prove_inbox_duplicate.py reproducing the scenario in --evidence and asserting inbox.py exits non-zero. The proof script must fail today and pass only after the guard lands - do not write one that merely exits 0.

**Checked:**

```
Verified reproduction, this session: copytree(scripts/) into a temp dir, write inbox/045-branch-a.md and inbox/045-branch-b.md both with 'id: 045' and 'status: open', then run scripts/inbox.py --close 045 --resolution x with cwd=tmp. Result: exit 0, stdout 'inbox: closed #045 - 045-branch-a.md'. Expected after the fix: non-zero, naming both paths. Also: python3 scripts/inbox.py --add ... --applied-by 'python3 tests/run.py' --prove-case inbox_duplicate_id -> 'prove: REFUSED - case inbox_duplicate_id not found in tests/run.py output' (exit 2), which is why the applied-by below points at a script the fix must create.
```

**What unblocks this:** Whether load_all()/next_id gains a duplicate guard and --close refuses an ambiguous N, with a two-duplicates fixture
