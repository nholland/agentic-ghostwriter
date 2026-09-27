---
id: 048
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 13:56
applied_by: python3 tests/prove_new_code_cases.py
resolved: 2026-09-26 18:19
---

# tests/prove.py cannot prove a fixture for a NEW file or a new function: reverting --file to --at either deletes the function the case calls (the case crashes and prove.py reports 'case not found') or the file does not exist at that commit and git show exits 128. Should it treat a crash-or-absent case at --at as red, or take a --new flag?

Hit twice on 2026-09-19 proving this session's own work. 'freshness: a checkout behind origin/main says how far' is REFUSED because reverting scripts/resolve_book.py removes freshness() entirely, so the case raises instead of printing [FAIL] - which is a stronger red than the one prove.py accepts. 'okf_index: a row whose status contradicts the concept is caught' dies with CalledProcessError because scripts/okf_index.py did not exist at the pre-fix commit. Two of five new checks this session therefore have fixtures that pass but carry no mechanical proof, which is exactly the gap tests/prove.py was built to close.

**Recommendation:** Treat a case that is absent or raises at --at as RED when it is present and green on the current tree, and say which of the two it was; a case that is absent at --at because the fixture itself is new is the normal shape for new code, not a refusal.

**Checked:**

```
python3 tests/prove.py --file scripts/resolve_book.py --at dd8ef60 --case 'freshness: a checkout behind origin/main says how far' -> prove: REFUSED - case not found in tests/run.py's output; python3 tests/prove.py --file scripts/okf_index.py --at 8d5d7da --case 'okf_index: a row whose status contradicts the concept is caught' -> subprocess.CalledProcessError: ('git','show','8d5d7da:scripts/okf_index.py') returned non-zero exit status 128
```

**What unblocks this:** whether a new script or a new function can carry the same proof an edited one does, or whether new code is permanently exempt from the standard the house just adopted

**Resolution (2026-09-26 18:19):** Implemented under the author request to continue processing the inbox. New source files are removed only in the disposable historical checkout; a valid revision and explicit named FAIL followed by current OK remain required. The two original fixtures now report missing code explicitly; arbitrary crashes and missing cases remain refused. Both original historical proof commands report PROVED. All 199 fixtures pass. Evidence: runs/qa/2026-09-26-inbox-048-new-code-proof.md.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/prove_new_code_cases.py` exits 0.

**Applied, confirmed 2026-09-26 18:19:** `python3 tests/prove_new_code_cases.py` now exits 0.
