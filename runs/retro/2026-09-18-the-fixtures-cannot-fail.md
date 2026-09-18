# Archivist Review — 2026-09-18 — the fixture directory certifies a check that does nothing

Scope: since `runs/retro/2026-09-18-the-checks-contain-the-defect.md`.
PROPOSALS ONLY (Rule 17). Filed as **#024–#027**.

## The one expensive thing

**`tests/run.py` scores 14/14 against a `voice_rules_check.py` that is broken.**
Not "misses a case" — broken. Reproduced by the Publisher:

```
# main() replaced with: print('totally broken'); return 1
$ python3 tests/run.py | tail -1
14/14 fixtures pass
```

It also passes 14/14 on a machine where the book does not resolve and the check
exits 2 before reading anything. **Nine of fourteen fixtures assert only that a
subprocess exited non-zero** — the one property a working check shares with a dead
one. `package_check` has a negative control (`good.html`); `voice_rules` has none.
No fixture asserts the unmutated config passes, and **DRIFT — the check's founding
purpose — has no fixture at all.**

The directory built yesterday to stop *"a proof that cannot be re-run is a
comment"* is currently a proof that cannot fail. **Same shape, one turn later:
the artifact of verification substituted for verification.**

## `package_check.py` still fails open — six for six

Every constructed input printed `[ ok ] … opens on: chapter`, exit 0:

| input | why it escapes |
|---|---|
| `class='dist distback'` single-quoted | regex is `class="([^"]*)"` |
| `<div class="dist">` container | only `<section>` is known |
| distillation nested inside the chapter section | last by index, mid-chapter on the page |
| `<h2>Editor&#39;s Notes</h2>` | entities not unescaped |
| `<h4>Draft Notes</h4>` | scan is h1–h3 |
| first section has no class, holds the distillation | `first = (sections[0] or "chapter")` |

**The last is not a straw case.** `chapter_pdf_local.py` emits the chapter as a
bare `<section>`, verified on the live artifact:

```
$ grep -o '<section[^>]*>' "runs/ch12/pdf/Chapter 12 - Romance Is a Discipline.html"
<section>
<section class="dist distback">
```

So `opens on: chapter` is **the default value of a variable, never a verified
claim**. This is the previous retro's headline — *"it prints the failure inside
its own PASS line"* — surviving the fix written for it. The regex was widened; the
fabricated default was not removed.

## `tests/run.py` can break the engine it tests

It mutates the tracked `config/house.json` in place. Verified, not reasoned:
restore is byte-identical and SIGINT-safe **when `finally` runs**. Killed between
mutation and restore, `em_dash_max` is left at 7.0 and `okf_gate.py` then prints
`BLOCKED. Do not write prose.` It leaves `config/house.json.testbak`, which
`.gitignore` does not cover. Two concurrent runs corrupted the file 12 times out
of 12. The run takes 0.297s and has no reason to touch a tracked file.

## The Stop hook guard skips in the case it exists for

`git diff --quiet HEAD -- scripts/ tests/`, across six states: pristine SKIPPED,
unstaged runs, staged runs, **COMMITTED SKIPPED** (the normal end of a session),
untracked new script SKIPPED, untracked new fixture SKIPPED, `house.json` edited
SKIPPED. The same hook already uses `git ls-files --others --exclude-standard`
twelve lines above for exactly the untracked case. **Deleting the guard is the fix.**

## Clean, checked, nothing found

The four `#020`–`#023` close-conditions were each true before closing. The three
original mutations are genuinely caught; Rule 8(e) rests on something real. The
four stored `package_check` fixtures all still fail correctly and the live
artifact still passes — the fixes landed, they are just narrower than the
directory claims. `distback-but-first.html` is an honest fixture.

**Minor:** `gw-retro.md` has an empty fence pair left at the end of the new
paragraph. **Not executed:** rendered PDF page order (no `pdftotext`).
