---
id: 042
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:58
applied_by: python3 tests/run.py
resolved: 2026-09-19 06:58
---

# The #041 [FAIL]-substring guard was gameable - an item whose --evidence read 'I did not run anything. [FAIL] is a string I typed.' was accepted, exit 0, and the guard's own green fixture passed a hand-written literal with no run behind it. Replace it with tests/prove.py running the red pass mechanically?

Fifth instance of one shape this session: an attestation field records belief, not fact, and #039/#040's failure mode was sincere error, not omission - against that, a substring check is the weakest proof in the lineage, not the strongest. Verified before building the fix: python3 scripts/inbox.py --add ... --evidence 'I did not run anything. [FAIL] is a string I typed.' --applied-by 'python3 tests/run.py' -> opened, exit 0.

**Recommendation:** add tests/prove.py: reverts --prove-file to --prove-at in a throwaway git worktree (never the live tree - avoids racing the Stop hook's auto-commit), runs the worktree's own tests/run.py, confirms --prove-case is [FAIL], restores the file, confirms [ ok ]. inbox.py --add now shells out to it instead of grepping --evidence for a typed string.

**Checked:**

```
python3 tests/prove.py --file scripts/session_log.py --at c17f979 --case 'session_log dedups when the last entry itself lists runs/log.md' -> PROVED, exit 0. Same file/commit with the non-discriminating case name -> REFUSED, exit 2. Re-ran the fabrication attack against the new inbox.py: refused for missing --prove-* flags, exit 2. python3 tests/run.py -> 57/57, including prove_cases()'s 5 new fixtures built against a synthetic repo (not real commit history, so nothing here depends on a specific SHA staying reachable).
```

**What unblocks this:** whether 'was this proof seen to fail' is measured by the machine or attested by the agent that wrote it

**Resolution (2026-09-19 06:58):** Applied directly - the Archivist demonstrated the prior guard was gameable with a concrete fabrication, verified independently before building the fix, then built and proved the mechanical replacement both directions.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py` exits 0.

**Applied, confirmed 2026-09-19 06:58:** `python3 tests/run.py` now exits 0.
