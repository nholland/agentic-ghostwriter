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
Measured 2026-09-20 in /home/user/agentic-ghostwriter: git rev-list --max-parents=0 main -> c74fe66; same for origin/main -> cbb7a37, fcb3fcb; 'git merge-base main HEAD' -> none; 'git merge-base origin/main HEAD' -> 1ccc0cf; 'git merge-base --is-ancestor c74fe66 origin/main' -> non-zero. git reflog show origin/main -> @{2} 4eb8325 'storing head', @{1} 9d8a346 'forced-update', @{0} 1ccc0cf 'fast-forward'. git reflog show main -> single entry, 'branch: Created from refs/remotes/origin/main' at 4eb8325. Local main's tip 4eb8325 is contained in origin/claude/book-resolution-script-u8ad59, origin/claude/dreamy-gates-52bn4v and origin/claude/gateway-sgjaao, so repointing loses nothing.
```

**What unblocks this:** Whether land() asserts 'git merge-base --is-ancestor main origin/main' before checkout, refusing with the remedy named in words, and whether say_status labels its comparison as being against origin/main
