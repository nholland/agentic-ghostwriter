# Archivist — session close, 2026-09-23 01:30

Window: `55b16cb..ffd55a1` (from `.claude/state/retro-window`). Two commits:
`1c6cb26` (the Publisher's own self-review of the land) and `ffd55a1` (session log).
Diff touches `inbox/`, `runs/retro/`, `runs/log.md` only — **zero corpus words added.**

## 1. #047's prediction matches tonight's mechanism — confirmed

Spot-checked as asked. `inbox/047` names, in its Recommendation and since
2026-09-20: *"NAME `git branch -f main origin/main` as the remedy."* That is the
exact command run tonight. The body's diagnosis is the same shape, not a
superficial resemblance: `sync.py` L78-79 compute `behind_main`/`ahead_of_main`
against `origin/main`, L162-163 then `checkout`/`merge --ff-only` against *local*
`main`, and nothing asserts the two are the same ref. Tonight's failure was
precisely that divergence surfacing as `fatal: refusing to merge unrelated
histories`. Match confirmed. Appending the occurrence as evidence rather than
closing was the right call — closing wants his words.

## 2. #093 is accurate, its direction is right, its stated reason is not the deciding one

The fact is verified live: `dupes: ['053']`, two files. The recommended direction
(renumber the `log_check` item) is **correct** — but #093 justifies it by arrival
order ("arrived second, on main"), and that is the weaker of the two available
criteria. The deciding evidence is reference count:

- `#053` meaning the **inbox.py guard** item is cited in **seven** live places,
  three of them in shipped source and the ledger: `scripts/inbox.py:182`,
  `tests/run.py:840`, `FINDINGS.md:773`, `inbox/052:20`, `inbox/080:12`,
  `runs/retro/2026-09-21-retro-self-review-3.md:53`,
  `runs/retro/2026-09-20-retro-and-log-commits.md:67`.
- `#053` meaning the **log_check** item is cited in **zero** live places. Its only
  ID reference is the frozen commit message `b22137f`; `runs/log.md` names it by
  path, not ID.

So renumbering `log_check` breaks 0 references; renumbering the other breaks 7.
Arrival order agrees here by luck. Had the counts been reversed it would have
given the wrong answer — and "on main" is not even a distinguishing property
post-merge (`git branch --contains` puts both commits on both refs; only the
pre-merge parents distinguish them: `13332da` held one, `0c0264b` held both).
**Suggestion, not a new item:** append the reference count to #093 before he
rules. Evidence belongs in the item he reads, not in a second item.

## 3. The closing observation is not the backlog size

48 open + 1 ruled-not-applied, corpus 17,017 -> 18,540 across the session with
none of it from tonight. As a count, "open backlog, correctly triaged" is
accurate and not a finding. What *is* a finding sits underneath it:

**Two of the oldest open items have close-conditions that can never fire.**

    #046  applied_by: python3 tests/prove_inbox_duplicate.py      -> file does not exist
    #047  applied_by: python3 tests/prove_land_unrelated_main.py  -> file does not exist

`--applied-by` exists so that a yes closes itself and `next.py` surfaces the item
until it does. For these two, a yes closes nothing: the proof path is a file
nobody created. And for #047 a **working red proof already exists**, verified by
me just now at exit 1, honest red not a crash — at
`runs/retro/2026-09-22-proof-land-unrelated-main.py`, 38 lines, one directory away
from where its own item says it should be.

The Publisher's stated reason for leaving it unwired — *"that is implementation,
which is the author's to rule on"* — is a reasonable principle applied one step
too far. The *guard in `land()`* needs his ruling. The *proof* does not: it lands
red, stays red until he rules yes, and turns an unclosable item into a
self-closing one. Withholding the proof along with the fix defeats the mechanism
that was built to make his yes stick.

## What recurs

**Tonight is the fourth instance of the inbox-ID collision**, and `FINDINGS.md`
L672-679 already narrates the first three, ending: *"#046, the proposal for a
structural guard, was already open and unruled when it happened."* That sentence
is true again, verbatim.

The sharper recurrence is in the handling. **One commit, `1c6cb26`, contains both
the right response and the wrong one.** For #047 the Publisher appended the
recurrence as evidence and did not re-file. For #046 — same situation, an open
unruled item that predicted the exact event — he filed **#093 as new**, and #093
does not mention #046 once (`grep -c '046'` -> 0). #093's own recommendation,
*"add a duplicate-ID guard in the same commit,"* is #046's unblock condition
restated: *"whether `load_all()`/`next_id` gains a duplicate guard and `--close`
refuses an ambiguous N, with a two-duplicates fixture."*

#093 is not a pure duplicate — *which file gets renumbered* is genuinely new, and
that half should stay. Its guard half is #046 re-filed.

**No ninth guard is proposed.** FINDINGS 2026-09-19 07:11 decided to stop
hardening the `inbox.py --add` lineage; #052, #053 and #080 are all open on it;
the eighth layer was reverted for refusing legitimate filings. Adding a
"does an open item already ask this?" check would be that mistake a ninth time.
The fix here is not rule text and not a guard — it is that #046 has been right
for four days and cannot close itself.

## What worked

- `retro-window` gave correct bounds. The #030 collapse did not recur.
- Both live proofs are honestly red and terminate cleanly: `#093`'s duplicate scan
  exits 1 with `dupes: ['053']`; the land fixture exits 1 with the real
  `fatal: refusing to merge unrelated histories` and `GUARD PRESENT: False`.
  Neither is a grep; neither crashes.
- 113/113 fixtures pass, main's 6 absorbed by the merge.
- Zero corpus growth in this window. Every artifact went to `inbox/` or `runs/`.
- Appending the #047 occurrence rather than closing it, and rather than re-filing
  it, is the correct pattern. It is the pattern #093 needed.

## Looked at, clean

The log.md union merge, the `manual.html` regeneration, the reachability of the
22 commits, the plate chain, and rounds #075-#091 — all independently checked in
their own turns, not re-verified here. #092 is filed and unruled; not re-litigated.
