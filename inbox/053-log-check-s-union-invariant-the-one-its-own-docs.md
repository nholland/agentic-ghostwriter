---
id: 053
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 15:52
applied_by: python3 -c 'import sys;sys.path.insert(0,"scripts");import log_check as L;q=chr(96);b=lambda h:"## "+h+"\n- "+q+"i/a.md"+q+"\n- "+q+"i/b.md"+q+"\n\n**Next:** x\n";g="2026-09-18 18:34 - "+q+"branch-A"+q+" - 2 commit(s) this session";t="2026-09-16 15:28 - "+q+"branch-B"+q+" - 2 commit(s) this session";sys.exit(1) if not hasattr(L,"lost_entries") else sys.exit(0 if g in L.lost_entries({g:b(g)},{t:b(t)}) else 1)'
---

# log_check's union invariant - the one its own docstring calls 'the one that matters' - has never had a fixture, and the content-based excuse it gained in 6a95d23 already fires across branches on the live log. Should union_breaches be split into a pure lost_entries(parent_entries, current_entries) that fixtures can call, with the excuse narrowed to a same-branch restatement?

All 104 fixtures exercise structure_breaches and entries; 'grep -n union tests/run.py' returns nothing. That is why the check could ship not running for a whole commit, and why its predicate could be weakened in the same commit with no test. session_log.py's real dedup compares only against the immediately preceding entry (last_entry_files), but the check's excuse is global - strictly wider than the behaviour it was written to permit. Measured on the live log, that gap is not theoretical: it is already excusing an entry across two branches and two days. No file reference is currently lost (unique=0 on every collision), so this is hardening, not data loss - it should be done after Chapter 13, not before.

**Recommendation:** Yes, but not now: after Chapter 13 lands, split out the pure predicate, narrow the excuse to same-branch, fixture the cross-branch coincidence in both directions, and restore 2026-09-18 18:34 tmjrgm rather than exempting it.

**Checked:**

```
$ grep -n 'union' tests/run.py   ->   (no output: the union invariant has no fixture)
$ python3 tests/run.py | tail -1   ->   104/104 fixtures pass
$ python3 scripts/log_check.py   ->   log_check: 133 entries intact - structure ok, union checked against every merge parent.
Measured against runs/log.md at 6a95d23: entries=133, distinct file-sets=105, entries whose file-set is NOT unique=44 (33%), collision pairs non-adjacent=15 of 28, collision groups spanning more than one branch=1.
Replaying union_breaches at 6a95d23 with the excuse disabled: a headings-only rule reports 3 missing; the content excuse clears all 3. Of those, '2026-09-18 18:34 - claude/gateway-tmjrgm - ? commit(s) this session' (4 files) is cleared by '2026-09-16 15:28 - claude/gateway-iqyyso - ? commit(s) this session' - a different branch, two days earlier. The other two are same-branch and would survive a narrowed rule.
Verified clean and needing no action: both LEGACY_MALFORMED entries are carried by 85 and 57 of the commits touching runs/log.md and are well-formed in 0 of them; the 9 entries restored in 6a95d23 recover 0 unique file references, confirming that commit's own correction of the prior review.
Filed without --applied-by naming tests/run.py because open item #048 blocks it: $ python3 tests/prove.py --file scripts/log_check.py --at 6a95d23 --case 'cross-branch'   ->   prove: REFUSED - case 'cross-branch' not found in tests/run.py's output (exit 2). Fifth occurrence, and the first that blocks the Archivist from filing. The proof below is the same fixture inlined so it stays re-runnable; the fixture belongs in tests/run.py once #048 is ruled.
```

**What unblocks this:** Whether log_check gains a pure lost_entries(parent_entries, current_entries) -> sorted missing headings, whether the excuse additionally requires the same branch, and whether the one entry that narrowing then reports is restored rather than exempted as a third LEGACY_MALFORMED
