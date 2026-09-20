---
id: 047
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 14:24
applied_by: python3 tests/prove_land_unrelated_main.py
---

# Should sync.py --land refuse when local main is not an ancestor of origin/main?

land() gates on status()'s behind_main/ahead_of_main, both computed against origin/main (sync.py L78-79), then runs 'git checkout main' and 'git merge --ff-only <branch>' against LOCAL main (L162-163). Nothing asserts the two are the same ref. On 2026-09-19 --status reported '6 ahead, 0 behind' and --land then died on 'fatal: refusing to merge unrelated histories'. Root cause established 2026-09-20: this container cloned at origin/main=4eb8325 (2026-09-14) and created local main from it; the 2026-09-18 migration rewrote main's history on the remote, which arrived here as 'fetch origin --quiet: forced-update' to 9d8a346. Git updates the remote-tracking ref on a forced update but never moves a local branch, so local main stayed on a history the remote no longer has - confirmed: the original engine root c74fe66 is NOT an ancestor of origin/main. This is a one-time artifact of the migration and will not recur in fresh containers, but the reporting defect is permanent: every guard in land() measures a ref it does not touch. Same shape sync.py already records against itself at L50-52 (a false zero with no error, in the one script whose job it is to prevent that).

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
