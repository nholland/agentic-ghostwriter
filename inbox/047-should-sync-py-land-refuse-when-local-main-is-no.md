---
id: 047
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 14:24
applied_by: python3 tests/prove_land_unrelated_main.py
---

# Should sync.py --land refuse when local main is not an ancestor of origin/main?

land() gates on status()'s behind_main/ahead_of_main, both computed against origin/main (sync.py L78-79), then runs 'git checkout main' and 'git merge --ff-only <branch>' against LOCAL main (L162-163). Nothing asserts the two are the same ref - that is the whole defect, and it needs no account of any specific incident to see. [The narrative of a 2026-09-19 --land failure that used to sit here was wrong four separate times across four corrections (a wrong forced-update SHA, a wrong cause, a wrong date, and finally a wrong ancestry claim that survived the third cut) and is removed rather than attempted a fifth. Nothing in this item's recommendation or status depends on it.] Same shape sync.py already records against itself at L50-52 (a false zero with no error, in the one script whose job it is to prevent that).

**Recommendation:** Add the assertion in land() and NAME 'git branch -f main origin/main' as the remedy without running it - the sandbox denied that command this session as Irreversible Local Destruction and the author ruled that the safeguard stays and the allowance is one-time. Register a case in tests/run.py that builds a throwaway repo with two unrelated roots.

**Checked:**

```
Corrected THREE times now (2026-09-20 14:24-ish, 15:0x, 15:16). The first two
corrections each tried to describe what git state existed at some past
moment and got it wrong - carrying forward a stale SHA, then mis-dating an
event by two days, then (second correction) misreading main's reflog as of
the wrong timestamp entirely. Every attempt to narrate history introduced a
new error while fixing the last one. The historical narrative is deleted
below rather than rewritten a fourth time - it was never load-bearing; the
defect stands on the code, not on a story about how this container got here.

Read directly, not measured against any point in time: sync.py L78-79
compute behind_main/ahead_of_main against origin/main; L162-163 then
checkout and merge-ff-only against LOCAL main. No line between them asserts
the two are the same ref. That is the whole defect, and it needs no history
to see.

CURRENT, re-run fresh 2026-09-20 15:16 (main at 8f1fbfe): git rev-list
--max-parents=0 main -> d34a3ec8fd2c04070287971b0c069fe0388ae7db; same for
origin/main. 'git merge-base --is-ancestor main origin/main' -> exit 0. Local
main and origin/main currently agree, so --land's own repro from 2026-09-19
('fatal: refusing to merge unrelated histories') will not reproduce in this
container today - that is a fact about today, not evidence the code defect
is fixed, and this item does not depend on reproducing it to stay open.
```

**What unblocks this:** Whether land() asserts 'git merge-base --is-ancestor main origin/main' before checkout, refusing with the remedy named in words, and whether say_status labels its comparison as being against origin/main

**Fifth occurrence, 2026-09-22 (Publisher, this time actually reproduced and diagnosed rather than narrated after the fact).** `python3 scripts/sync.py --land` failed with exactly the predicted error - `fatal: refusing to merge unrelated histories` - while landing 114 commits at the author's word. Diagnosed live: `git merge-base main origin/main` returned nothing; `git for-each-ref` confirmed all 22 of local `main`'s commits are permanently reachable on four other remote branches, so nothing was at risk; `git reflog show main` showed `main@{2}: branch: Created from refs/remotes/origin/main` - it was created correctly at some point, so the divergence is that `origin/main`'s own history was later replaced (its root `f335220` carries two parents in its raw object data - `git cat-file -p f335220` shows them - that are absent from this container's shallow/partial clone, which is why `git log` sees it as parentless). Applied the remedy this item already named on 2026-09-20 - `git branch -f main origin/main` - then retried `--land`, which then landed on `main` at `5de2ad0`. The Archivist's re-review found my own in-the-moment narration of *why* ("local main was never correctly tracking origin/main") was itself wrong per the reflog above, even though the action taken was correct; that is the sixth time this item's narrative layer has been wrong while the code-level diagnosis stayed right, which is the same lesson the four prior corrections already drew.

A reproducible fixture now exists (built by gw-retro, verified by the Publisher): `runs/retro/2026-09-22-proof-land-unrelated-main.py`, which builds an isolated throwaway repo with two unrelated roots and confirms `--land` fails the same way there - re-run fresh, exit 1, `fatal: refusing to merge unrelated histories`. It is not yet at this item's own `applied_by` path (`tests/prove_land_unrelated_main.py`, which does not exist) and has not been wired into `tests/run.py` or registered as a `plate_check`-style case - that is implementation, which is the author's to rule on, not something landed here ahead of his word.
