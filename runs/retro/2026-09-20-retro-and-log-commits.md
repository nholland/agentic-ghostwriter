# Archivist — 2026-09-20 23:40 — window 88cfa346..dec7dd99

Two commits. One is the previous Archivist's own output (`908a2ef`: a retro doc
plus inbox #072 and #073). One is the Stop hook's bookkeeping (`dec7dd9`:
`runs/log.md`). No desk did any work in this window, and no rule was applied.

That is itself the finding.

---

## What broke — the retro loop is not cut at the root; it is cut at three
## quarters, and the fourth quarter is `inbox/`

`retro-check.sh` counts commits touching `bakeoff/ inbox/ scripts/ config/
books/ FINDINGS.md`. `runs/` was deliberately excluded, with the reason written
into the hook: *"NOT runs/: session-stop.sh writes and commits runs/log.md
itself, so watching it made the hook dispatch a retrospective on its own
bookkeeping."* Correct diagnosis, half a fix. The Archivist's retro doc goes to
`runs/retro/` (excluded), but its **inbox filings go to `inbox/` (watched)**, and
the inbox filing is the Archivist's only durable output — its charter requires
one. So every substantive retrospective guarantees the next dispatch, and that
dispatch's entire reviewable content is the previous retrospective.

Measured on the real windows:

```
88cfa346..dec7dd99  old_COUNT=1  -> 908a2ef "Archivist review of the PDF layout fix"
21b1f73..dfcb843    old_COUNT=1  -> 9332607 "Archivist: retro of round 4; #071 ..."
dfcb843..88cfa34    old_COUNT=1  -> 88cfa34 (the PDF fix: real work)
980e502..dfcb843    old_COUNT=2  -> b9a1a61 + f7736f3
```

Two of the last four dispatches were triggered by nothing but a prior
retrospective. This one is the second consecutive instance.

Both the hook's own comment and `FINDINGS.md` line 336 state the opposite:
*"That loop is cut at the root here — the Archivist never applies, and rule
paths are not watched."* The first clause is true and load-bearing (the ledger
cannot grow, because nothing is applied). The second is true but insufficient.
The loop survives in a weaker gauge: it cannot inflate the rules, but it can
spend sessions, and at ~15 dispatch markers in `.claude/state/` today against 5
retro docs written, session-spend is the live cost.

**Shape:** this is the `runs/` exclusion's own shape, recurring one path over —
a mechanism fixed for the instance that was noticed rather than for the class.
Same family as #030's four recurrences.

---

## What recurs — six consecutive `gw-retro` items now close on a grep, and
## #048 is why

The two items filed in this window close on greps of the implementation for the
fix's own text:

```
#072  grep -qi 'leaked.markup\|no.un-interpreted' scripts/package_check.py
#073  grep -qi 'page-break.*parity\|parity_rows' scripts/chapter_pdf.py
```

Both propose **adding a check.** The Archivist's charter forbids exactly this:
*"A proposal that adds or fixes a check closes on its fixture, never on a grep
for its own text,"* and `FINDINGS.md` records the cost — `grep -q 'spec_number'
voice_rules_check.py` closed green over two half-fixes, one of which crashed and
one of which passed the very defect it was written for.

Counting all `gw-retro` items by proof shape: #036–#044, #050, #053 close on
`python3 tests/run.py`. Then **#062, #063, #064, #071, #072, #073 — the six most
recent, unbroken — close on a grep.** Four of those six (#062, #071, #072, #073)
grep the implementation file itself, the strongest form of the forbidden shape.

This is not laziness, and that matters for the fix. `inbox.py` runs
`tests/prove.py` at `--add` time whenever `--applied-by` names `tests/run.py`,
and `tests/prove.py` cannot prove a case that does not exist yet — which is
every proposal, by definition. **#048 filed exactly this on 2026-09-19 13:56 and
is still open.** So the gate's only passable exit for a proposal that adds a
check is the shape the charter forbids. A rule and its enforcing tool point in
opposite directions, and the tool wins six times running.

**No new item is filed for this.** The fix is already filed, unruled, and a
seventh guard on this lineage is what `FINDINGS.md`'s 2026-09-19 07:11 entry
decided to stop adding. What is new is the price: #048 has been open for a day
and has silently degraded every `gw-retro` proposal filed since. That belongs in
front of the author as a number, not as another item.

---

## What worked

- **`retro-window` was correct this time.** `.claude/state/retro-window` reads
  `88cfa346... dec7dd99...`, exactly the dispatched range, and
  `retro-done-88cfa346f7e8` was created at 23:40. The prior hand-dispatch was
  also real: `retro-done-dfcb8434165d` exists at 23:34 with the matching window.
  **#071's staleness did not recur in this window** — asked, checked, clean.
- The Stop hook did not amend a published commit: `dec7dd9` landed as its own
  commit, as the branch-ancestor guard intends.
- `session_log.py`'s entry is accurate: right branch, right commit count, the
  three files named, `Next:` from the oracle.
- `inbox.py`'s empty-`--applied-by` refusal held — all three recent items carry
  one. The guard that exists works; the one that would have caught the grep
  shape is the one #048 blocks.

## What was missing / too hard

Nothing in this window. Two commits, one of them a bot.

## Context, not a finding

Corpus is **18,540 words** (`cat CLAUDE.md .claude/agents/*.md
.claude/skills/*/SKILL.md | wc -w`), against the 17,017 the brief records for
2026-09-19. No file in this window is in that glob; noted so the next count
starts from a true number.

---

## Proposal (one). The Publisher runs it on the author's yes; the Archivist
## applies nothing.

Priced: the replacement comment is **90 words** against the existing **94**
(net −4); the counting block goes from **8 words to 25** (net +17). Total +13
words to the hook, 0 to the corpus. It deletes the false half of the hook's
own loop-is-cut claim, which is the deletion it names.

Verified against four real windows before proposing:

```
88cfa346..dec7dd99  old=1 new=0   (this dispatch: would not have fired)
21b1f73..dfcb843    old=1 new=0   (the 22:06 dispatch: would not have fired)
dfcb843..88cfa34    old=1 new=1   (the PDF fix: still fires)
980e502..dfcb843    old=2 new=1   (real work, minus the retro commit: still fires)
```

No false negative on either real-work window.

Proof shape, stated honestly: `--applied-by` greps `tests/` rather than naming
`tests/run.py`, because #048 makes the latter refuse at filing time. A grep at
`tests/` is weaker than a fixture but stronger than a grep at `scripts/`: it
cannot be satisfied without a fixture landing in `tests/`, and `session-stop.sh`
runs `python3 tests/run.py` unconditionally every session. This is the seventh
consecutive grep-shaped proof and it is named as such in the item's own context.

```
python3 scripts/inbox.py --add "retro-check.sh watches inbox/, and the Archivist's only durable output is an inbox filing, so every substantive retrospective triggers one more whose entire subject is the previous retrospective. Two of the last four dispatches fired on nothing else. Should the count skip any commit carrying a runs/retro/ file?" \
    --raised-by gw-retro --chapter 0 \
    --context "The hook already excludes runs/ for this exact shape and closed only half of it; its own comment and FINDINGS line 336 both claim the loop is cut at the root, which is now false. The loop cannot grow the ledger - the Archivist never applies - but it spends sessions: 15 dispatch markers in .claude/state today against 5 retro docs written. Note for the record: --applied-by greps tests/ rather than naming tests/run.py because inbox.py runs prove.py at filing time and #048 makes that refuse for a case that does not exist yet. This is the seventh consecutive grep-shaped gw-retro proof for that reason." \
    --unblocks "Whether a retrospective can trigger the next retrospective, and whether the hook's 94-word loop comment drops to 90 with its false half removed" \
    --recommend "Yes: skip commits touching runs/retro/ when counting, prove it with a two-commit fixture in tests/run.py, and rewrite the loop comment to say three quarters cut rather than root" \
    --evidence "Ran the proposed count against four real windows: 88cfa346..dec7dd99 old=1 new=0 (only commit is 908a2ef, the prior retro); 21b1f73..dfcb843 old=1 new=0 (only commit is 9332607, the prior retro); dfcb843..88cfa34 old=1 new=1 (the PDF fix, still dispatches); 980e502..dfcb843 old=2 new=1 (real work kept, retro commit dropped). No false negative on either real-work window. Word counts: sed -n '5,12p' .claude/hooks/retro-check.sh | wc -w -> 94; replacement comment -> 90; current count line -> 8 words; replacement block -> 25." \
    --applied-by "grep -rq 'retro dispatch skips a commit carrying runs/retro/' tests/"
```

**Also recommended, no command:** put **#048** in front of the author before any
further `gw-retro` filing. It is the upstream of six degraded proofs and
counting.
