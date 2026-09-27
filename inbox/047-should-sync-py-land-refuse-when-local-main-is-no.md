---
id: 047
status: resolved
raised_by: gw-retro
chapter: 0
opened: 2026-09-20 14:24
applied_by: python3 tests/prove_land_unrelated_main.py
resolved: 2026-09-26 13:53
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

**Resolution (2026-09-26 13:53):** Author: "Approved" to the landing safeguard, not to landing this branch. sync.land now confirms local main is an ancestor of origin/main before pushing, checking out or merging. It refuses missing, unrelated, ahead and diverged local main without altering refs and explains the manual recovery choice; it never resets the branch automatically. Four unsafe-history cases failed against the pre-fix implementation and now pass; equal and behind controls still land in disposable repositories using only a local bare remote. No live main was changed. Completion condition: python3 tests/prove_land_unrelated_main.py. Full-suite limitation: tests/run.py still stops in the existing plate checker because /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf is absent on this Mac. No full-suite pass claimed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 tests/prove_land_unrelated_main.py` exits 0.

**Applied, confirmed 2026-09-26 13:53:** `python3 tests/prove_land_unrelated_main.py` now exits 0.
