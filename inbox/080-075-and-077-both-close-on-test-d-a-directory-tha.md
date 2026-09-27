---
id: 080
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:22
retired_applied_by: for f in inbox/075-*.md inbox/077-*.md; do grep -qE "^applied_by: *test -[def] [^ ]*$" "$f" && exit 1; done; exit 0
applied_by: python3 tests/manual_description_cases.py && python3 scripts/manual.py --check
resolved: 2026-09-26 13:18
---

# #075 and #077 both close on 'test -d' a directory that does not exist, so 'mkdir -p tests/fixtures/docstrings' closes #077 green while three rows of the published scripts table are still truncated mid-sentence. Should both be reissued with a proof that executes - #077's is already pasted inside #077 - rather than one satisfied by creating an empty directory?

inbox.py:185 fires the prove.py freshness gate only on the literal string 'tests/run.py', so naming a fixtures PATH evades it while looking more rigorous than the seven greps before it - and is strictly weaker, since a grep at least reads content. #075's own title says 'proved by a two-dated-docs fixture'; its close-condition never runs one. No ninth guard is proposed: FINDINGS 2026-09-19 07:11 decided to stop hardening this lineage, #052 and #053 are open on it, and the eighth layer was reverted for refusing legitimate filings while being evaded by 'cd tests && python3 run.py'. If this stays, the item written to stop a check closing over its own defect closes over its own defect.

**Recommendation:** Reissue both: #077 takes the command already in its own Checked block (exit non-zero while any purpose lacks terminal punctuation); #075 takes a two-dated-docs case in tests/run.py, whose harness #079 has already shown runs subprocesses against a temp repo

**Checked:**

```
grep '^applied_by:' inbox/075-*.md inbox/077-*.md -> 'test -d tests/fixtures/plate-names' and 'test -d tests/fixtures/docstrings'; neither directory exists (test -d exits 1), so both were accepted red. python3 -c "import sys;sys.path.insert(0,'scripts');import manual;print([s['name'] for s in manual.read_scripts() if not s['purpose'].endswith(('.','!','?'))])" -> ['land.py','toolcheck.py','ttfwidth.py'], live at docs/manual.html:556,573,574. 9 of the last 10 gw-retro applied_by values execute nothing (062,063,064,071,072,073,074 greps; 075,077 test -d; 079 is the sole exception). #078, filed in the same commit, reads config/house.json and asserts a value - the counter-example showing the problem is not short proofs. Proof below re-run on today's tree -> exit 1 (red); re-run against copies with the applied_by lines replaced -> exit 0 (green).
```

**What unblocks this:** Whether a gw-retro close-condition must run something, and whether #077 can be marked applied while land.py, toolcheck.py and ttfwidth.py still publish mid-sentence to readers

**Resolution (2026-09-26 13:18):** Author: "Approved" to repairing the actual descriptions and their completion evidence. #077 now closes on executable description cases and manual freshness, not directory existence. #075 was already retired as superseded on the author’s prior approval; its obsolete directory check remains historical only. This closes the weak-proof cleanup without recreating obsolete #075 code. No new global evidence rule added. Validation limitation: python3 tests/run.py stops in the existing plate checker on missing /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf; no full-suite pass claimed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/manual_description_cases.py && python3 scripts/manual.py --check` exits 0.

**Applied, confirmed 2026-09-26 13:18:** `python3 tests/manual_description_cases.py && python3 scripts/manual.py --check` now exits 0.
