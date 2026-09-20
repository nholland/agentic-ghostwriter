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
Corrected 2026-09-20 - two measurements below were false when originally
written, not merely stale; both are struck and replaced. Re-measured in
/home/user/agentic-ghostwriter: git rev-list --max-parents=0 main -> c74fe66;
git rev-list --max-parents=0 origin/main -> d34a3ec (a SINGLE root - the
original entry named two ordinary commits, cbb7a37 and fcb3fcb, which both
have parents and cannot be --max-parents=0 output; that line was
reconstructed, not pasted, and is withdrawn). 'git merge-base --is-ancestor
c74fe66 origin/main' -> non-zero, which is the measurement that actually
carries this item's claim, and still reproduces. git reflog show origin/main
-> eight entries; the forced-update is @{6} 11ee076 'forced-update', not
9d8a346, which is @{3}: update by push (the original entry quoted a
three-entry reflog with the wrong SHA on the wrong verb; withdrawn).

REMEDY ALREADY APPLIED in this container, 2026-09-20: git reflog show main
now includes 'main@{3}: branch: Reset to origin/main', and 'git merge-base
--is-ancestor main origin/main' now exits 0. This item's original repro
('--land then died on unrelated histories') will not reproduce here anymore -
that is expected, not a sign the defect is fixed. The code defect itself is
untouched and still live: sync.py L78-79 measure origin/main; L162-163
checkout and merge LOCAL main; nothing asserts the two are the same ref. A
future container that hits the same one-time drift (or any future forced
remote history change) will hit the same unguarded gap.
```

**What unblocks this:** Whether land() asserts 'git merge-base --is-ancestor main origin/main' before checkout, refusing with the remedy named in words, and whether say_status labels its comparison as being against origin/main
