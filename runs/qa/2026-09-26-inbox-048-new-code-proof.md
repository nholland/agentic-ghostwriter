# Inbox #048 — new-code proof support

Publisher implementation, 2026-09-26 18:19. Authority: “Let's keep processing the inbox.” No desk ran cold; no house instructions changed.

The proof tool now validates the historical commit and removes a source file from its disposable checkout when that file did not exist at the commit. A fixture must explicitly emit its named FAIL, then emit OK with the current implementation. A missing case or arbitrary crash remains a refusal. No new flag is needed. Crash diagnostics are now visible when a case is missing.

The two fixtures cited in #048 explicitly report absent source/function as failure. The absolute-import scan skips tracked paths absent from the working tree; otherwise the deliberate source removal crashed the suite before any case results were printed.

## Evidence

Eight disposable-repository regression cases cover absent file, absent function, invalid revision, missing case, unrelated crash, current failure, worktree cleanup, and preservation of the live source. Running these against the pre-change proof tool failed the absent-file case (and four refusal cases that previously crashed); the existing function case already worked with an explicit missing-function fixture. The repaired tool passes all eight.

Original historical reproductions, executed against the repaired live tree:

```text
prove: PROVED - 'okf_index: a row whose status contradicts the concept is caught' red=scripts/okf_index.py@8d5d7dac0fd9b96dc106d6262fb19395a6220a02 then green on the current tree
prove: PROVED - 'freshness: a checkout behind origin/main says how far' red=scripts/resolve_book.py@dd8ef60 then green on the current tree
```

Final `python3 tests/run.py` output:

```text
199/199 fixtures pass
```

`git diff --check` passed. #048 closed using `python3 tests/prove_new_code_cases.py`, which the inbox command reran successfully. Historical initial replay failed on the script scan described above; the final replay passed after that correction. This implements the engineering repair, not the record's broader suggestion that arbitrary crashes or absent fixture output should count as proof.
