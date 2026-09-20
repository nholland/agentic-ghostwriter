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
Corrected twice now - first on 2026-09-20 14:24-ish (struck two false
measurements), and again 2026-09-20 15:0x after the Archivist found the first
correction had reproduced the same defect class it was fixing: it carried
forward a stale SHA without re-running the command, and dated an event two
days off. This block uses dated SHAs throughout instead of positional reflog
references (@{N}), which shift by one on every fetch or push and were already
wrong by the second correction.

HISTORICAL, at the time this item was originally filed (2026-09-20 ~14:20,
before local main had been reset): main's tip was 4eb8325 (per its reflog,
'branch: Created from refs/remotes/origin/main', 2026-09-14 11:38:04+00:00),
rooted at c74fe66 (git rev-list --max-parents=0 4eb8325). origin/main was
already rooted at d34a3ec. 'git merge-base --is-ancestor c74fe66 origin/main'
-> non-zero: two unrelated histories, which is the actual defect this item
reports and is unaffected by anything below.

CURRENT, re-run just now (2026-09-20, main at 8f1fbfe): git rev-list
--max-parents=0 main -> d34a3ec8fd2c04070287971b0c069fe0388ae7db. git
rev-list --max-parents=0 origin/main -> the same SHA. 'git merge-base
--is-ancestor main origin/main' -> exit 0. main's reflog shows the repointing
commit as 459ae3e, dated 2026-09-18 20:58:00+00:00 - 'branch: Reset to
origin/main' - which is BEFORE this item was ever filed, not something this
session did; the first correction's claim that the remedy was "already
applied in this container, 2026-09-20" mis-dated this by two days. This
item's original repro ('--land then died on unrelated histories') will not
reproduce today - expected, not a sign the code defect is fixed.

The code defect is unaffected by any of the above and is still live: sync.py
L78-79 measure origin/main; L162-163 checkout and merge LOCAL main; nothing
asserts the two are the same ref. A future container that hits the same
one-time drift, or any future forced remote history change, hits the same
unguarded gap.
```

**What unblocks this:** Whether land() asserts 'git merge-base --is-ancestor main origin/main' before checkout, refusing with the remedy named in words, and whether say_status labels its comparison as being against origin/main
