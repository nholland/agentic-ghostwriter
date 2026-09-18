---
id: 024
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-18 18:45
---

# tests/run.py scores 14/14 against a voice_rules_check.py that is simply broken. Add a baseline and a DRIFT fixture?

Nine of fourteen fixtures assert only that a subprocess exited non-zero, which is what a working check and a dead one have in common. Verified: with main() replaced by 'return 1', the suite still prints 14/14. So does a machine where the book does not resolve and the check exits 2 before reading anything. No fixture asserts the unmutated config PASSES - package_check has a negative control, voice_rules has none - and DRIFT, a spec_probe that no longer matches 01-voice.md and the check's founding purpose, has no fixture at all. The directory built yesterday to stop 'a proof that cannot be re-run is a comment' currently cannot fail.

**Recommendation:** Assert the pristine config exits 0 with no MISMATCH before mutating, assert each mutation is named in the output rather than merely non-zero, and add a DRIFT fixture. Drafted at 183 words and verified: 16/16 on a healthy repo, red against a broken check and against an unresolvable book.

**Checked:**

```
main() replaced with 'return 1' -> tests/run.py prints 14/14 fixtures pass. GW_BOOK_REPO=/nonexistent -> 14/14 fixtures pass. Publisher reproduced the first independently.
```

**What unblocks this:** Whether tests/ is evidence or decoration. Every future proposal closing on tests/run.py inherits this.
