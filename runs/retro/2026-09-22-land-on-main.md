# Archivist — 2026-09-22 23:13 — "Commit to main"

Window: `13332da..5de2ad0` (merge of `origin/main` @ `0c0264b` into
`claude/gateway-45bnh4`), plus the `--land` that followed.
`.claude/state/retro-window` read `4cc8a2c 13332da` — already stale, written
before the merge existed. Reviewed the merge on its parents instead.

## Verdict in one line

The three hand resolutions were all correct. The one thing that went wrong
tonight was **already filed as inbox #047 two days ago and never ruled on.**

---

## 1. `runs/log.md` — the union merge is correct

Verified independently of `log_check.py`, at heading level against both
parents (`13332da` ours, `0c0264b` theirs, base `91c2907`):

```
heading counts ours/theirs/result: 153 136 190
headings in OURS missing from RESULT:        []
headings in THEIRS missing from RESULT:      []
headings in RESULT from neither parent:      []
duplicate headings in RESULT:                []
out-of-order adjacent pairs in RESULT:       0
```

Nothing dropped, nothing invented, nothing duplicated, strictly chronological.
Main's 15:37 and 15:53 entries sit in the only positions their timestamps allow.

A naive whole-block union predicts 191, not 190. That gap is **not** a defect:
the base and our branch both carried one corrupted entry — `2026-09-20 14:29`
with two `**Next:**` blocks, a foreign 9-file tail welded onto its body — and
`origin/main` had already repaired it. The resolution took main's repaired
version. The orphaned tail's file references (`svgcheck.py`, `toolcheck.py`,
`tests/prove.py`) still appear in properly-headed entries in the result. So the
merge was not merely a correct union; it silently inherited a repair.

Caveat worth stating plainly: `log_check.py` passing does **not** establish any
of the above. Its union invariant excuses a lost heading whenever any surviving
entry has the same file set, and open item **#053** records that this excuse
already fires across branches on the live log and has never had a fixture.
Tonight it had nothing to catch. It was not the thing that made this merge safe.

## 2. `docs/manual.html` — regeneration was right, and lost nothing

Both sides changed **only the generated file**. Neither touched the authored
half:

```
git diff --stat 91c2907 0c0264b -- docs/ scripts/manual.py scripts/manual_content.py
 docs/manual.html | 3 ++-
git diff --stat 91c2907 13332da -- docs/ scripts/manual.py scripts/manual_content.py
 docs/manual.html | 13 +++++++++----
```

So there was no authored content on main's side to lose. Main's substantive
change was the `log_check.py` table row, which is *derived* from scanning
`scripts/` — regeneration reproduces it rather than dropping it, and the merged
file contains it. `manual.py --check` → `in sync`. Hand-merging a generated
file with an `inputs-digest` trailer would have been the error here.

## 3. `git branch -f main origin/main` — right action, wrong stated reason,
##    and the safety check that would have justified it was not run

**Nothing was lost.** The 22 commits under `4eb8325` are the repo's original
genesis history (2026-09-12 → 09-14, root `c74fe66`), and they are not merely
in the reflog and loose objects — they are permanently reachable from four
surviving remote refs:

```
  preserved on refs/remotes/origin/claude/book-resolution-script-u8ad59
  preserved on refs/remotes/origin/claude/dreamy-gates-52bn4v
  preserved on refs/remotes/origin/claude/gateway-iqyyso
  preserved on refs/remotes/origin/claude/gateway-sgjaao
```

That is the check that makes the force-update provably safe, and **it was not
run before acting.** The decision rested on a narrative instead — "this
container's local `main` was apparently never correctly tracking `origin/main`"
— and `main`'s own reflog contradicts it:

```
4eb8325 main@{2}: branch: Created from refs/remotes/origin/main
```

Local `main` *was* created correctly from `origin/main`. What actually happened
is that `origin/main` was itself replaced with an unrelated history: its root is
`f335220` (2026-09-18 19:12, "Merge origin/main: reconcile Ch12 inbox closures
and session log") — a commit with **zero parents** whose message describes a
merge. The local ref was stranded by a remote history rewrite, not by bad
tracking.

So: investigate-then-act was **not** satisfied. The act was correct and
reversible, and the conclusion happened to be right, but it was reached by a
story rather than by the one-line reachability test. This matters because
`FINDINGS.md` already records that this specific item's history has been
narrated wrongly four separate times (2026-09-20 15:37). Tonight produced a
fifth wrong narration of the same events. The lesson that keeps not landing is
that this defect needs no history at all.

## 4. `sync.py` has the latent bug, and it is already inbox #047

Real, confirmed by reading:

```python
# status(), L78-79 — measured against origin/main
"behind_main":   count(f"{branch}..origin/main")
"ahead_of_main": count(f"origin/main..{branch}")
...
# land(), L162-163 — acted against LOCAL main
run("checkout", "main", check=True)
run("merge", "--ff-only", s["branch"], check=True)
```

Every guard is evaluated on `origin/main`; the operation runs on local `main`.
Nothing asserts they are the same ref. Same shape the script already documents
against itself at L50-52 ("a false zero with no error, in the one script whose
job is to remove ambiguity").

**This was filed as #047 on 2026-09-20 14:24** — two days before tonight — with
the recommendation "add the assertion in `land()` and NAME
`git branch -f main origin/main` as the remedy". Its Checked block ends:

> "--land's own repro ... will not reproduce in this container today — that is
> a fact about today, not evidence the code defect is fixed."

Tonight it reproduced, cost a hand diagnosis, and was fixed by running exactly
the command #047 said to name. The proposal was right, was never ruled on, and
the predicted failure arrived on schedule.

Reproduced deterministically in a throwaway repo with two unrelated roots —
`runs/retro/2026-09-22-proof-land-unrelated-main.py`, currently RED:

```
--- land rc: 1
STDOUT: sync: land FAILED, back on 'feat':
fatal: refusing to merge unrelated histories
GUARD PRESENT: False
```

Note the predicate: an earlier version of this fixture went **green** on the
string "unrelated" in git's own failure output — passing on the very defect it
was written to catch. It now requires the refusal to arrive *before* checkout
and to name the remedy.

---

## Lenses

**What broke.** Nothing in the book. `--land` failed once on a known, filed,
unruled defect. Recovery worked: `land()`'s `except` returned the working tree
to `feat`, never stranding it on `main`.

**What was missing.** A reachability test before a force-update of a branch ref.
One line, `git for-each-ref refs/remotes | while read r; do git merge-base
--is-ancestor <sha> $r; done`, converts "I believe this is clutter" into
"nothing here is unique to this ref". It was available and not used.

**What was too hard.** Diagnosing local-vs-origin ref drift by hand, at the end
of a session, with `--land` giving only git's raw `fatal:`. That is the exact
cost #047 priced.

**What worked.** Regenerating the generated file rather than merging markup.
The chronological interleave of the log, which is genuinely correct. `land()`'s
failure path restoring the branch. `manual.py --check` and `log_check.py`'s
*structure* invariant both giving real signal. And `tests/run.py` going 107 →
113 by absorbing main's fixtures rather than colliding with them.

**What recurs.** Two open proposals predicted tonight in advance:
- **#047** predicted the `--land` failure. Unapplied. It happened.
- **#046** ("two branches can allocate the same inbox number and nothing
  catches it") — this merge produced exactly that. Two files now share ID 053:
  `inbox/053-inbox-py-s-tests-run-py-proof-guard-was-widened-.md` and
  `inbox/053-log-check-s-union-invariant-the-one-its-own-docs.md`, and
  `scripts/inbox.py` prints both as "#053".

The shape is no longer "the house fails to notice". The house noticed both,
correctly, days early. The shape now is **a backlog of correct unapplied
proposals**: 47 open items, and the two that came due this session were both
already in it. More rule text would not have helped; neither would another
finding. Only a ruling would have.

Corpus: 18,540 words (`cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md
| wc -w`), up from 17,017 on 2026-09-19. Nothing proposed here adds to it.
