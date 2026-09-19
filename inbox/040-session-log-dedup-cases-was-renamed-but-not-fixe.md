---
id: 040
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 06:49
applied_by: python3 tests/run.py 2>&1 | grep -q '^\[ ok \] session_log dedups when the last entry itself lists runs/log.md'
resolved: 2026-09-19 06:49
---

# session_log_dedup_cases() was renamed but not fixed - its case named for the #039 defect passed against the pre-fix script unchanged, because entry 1 is written before runs/log.md is ever committed and so never lists it. Add the fourth-Stop case that actually needs a logged entry to already contain runs/log.md?

The 06:40 fix (stripping runs/log.md on both sides of the comparison) is correct. The fixture that was supposed to prove it discriminates does not: with only scripts/session_log.py reverted to the pre-fix commit, the renamed case still printed [ok]. This is the fourth instance of the same shape (#030's grep, voice_rules_check passing its own defect, the dedup half-fix, now the fixture written for that half-fix).

**Recommendation:** add a fourth run: commit the log a second time (this makes the last entry's own file list contain runs/log.md, the actual precondition), run again with no new work, assert it skips; rename the earlier case to what it actually tests

**Checked:**

```
reverted only scripts/session_log.py to c17f979 (git show c17f979:scripts/session_log.py), ran python3 tests/run.py: [ ok ] on the case named for the defect - proving it did not discriminate. Added the new case; same revert now gives: [FAIL] session_log dedups when the last entry itself lists runs/log.md  got: ('session_log: appended to runs/log.md (4 file(s), next: ?)\n', 3). Restored the fix: [ ok ], 53/53 fixtures pass.
```

**What unblocks this:** whether runs/log.md's dedup is proved or only asserted

**Resolution (2026-09-19 06:49):** Applied directly - reproduced the Archivist's finding independently before trusting it (confirmed the renamed case passes against the actual pre-fix script), then built and verified the real discriminating case.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/run.py 2>&1 | grep -q '^\[ ok \] session_log dedups when the last entry itself lists runs/log.md'` exits 0.

**Applied, confirmed 2026-09-19 06:49:** `python3 tests/run.py 2>&1 | grep -q '^\[ ok \] session_log dedups when the last entry itself lists runs/log.md'` now exits 0.
