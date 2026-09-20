---
id: 053
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 15:33
applied_by: python3 tests/run.py
---

# inbox.py's tests/run.py proof guard was widened from gw-retro-only to every filer without a ruling, after FINDINGS 2026-09-19 07:11 decided to stop hardening this lineage - and while a smaller guard of the same class (#052) was correctly deferred to you in the same commit. Measured, the widening refused legitimate filings (a deletion proof, any not-yet-applied proposal, even a proposal to remove itself) and was evaded by trivial rewrites ('cd tests && python3 run.py'). Reverted to gw-retro scope. Ratify that reversion, or should it be widened again in words this time?

The widening was applied directly in the same commit that (correctly) deferred #052's smaller guard to you - an inconsistency that is itself the finding. #050's raised_by: Publisher dodge is real but is the same shape of accepted residual bypass the 2026-09-19 07:11 decision already lives with for the gw-retro proof lineage.

**Recommendation:** keep the reversion - the widening cost more (refusing legitimate proofs) than it bought (closing one already-caught dodge), and it was applied without your word in a session that had explicitly agreed to stop adding to this exact lineage

**Checked:**

```
Widened guard refused a legitimate deletion proof: --applied-by 'python3 tests/run.py && test ! -f books/x/callouts.md' -> exit 2, missing --prove-* flags, even though no fixture case is at stake. Evaded trivially: --applied-by 'cd tests && python3 run.py' -> accepted, exit 0. After reverting: python3 tests/run.py -> 98/98, including a new case confirming a non-gw-retro filer with a legitimate tests/run.py-citing proof is accepted again.
```

**What unblocks this:** whether inbox.py's tests/run.py proof requirement is scoped to gw-retro (as it stood before this session) or applies to every filer
