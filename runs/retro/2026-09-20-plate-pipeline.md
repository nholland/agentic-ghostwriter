# Session review — the plate pipeline, built and then run against its own predecessor

**Desk:** the Archivist · **Clock:** 2026-09-20 19:56 · **Branch:** `claude/gateway-45bnh4`
**Window reviewed:** `6ed70f1..HEAD` (`36baf54`) — 17 commits.
**Window the hook recorded:** `1418692 8785cb6` — 9 of those 17, excluding the pipeline
commit itself and the four commits that ran it. Fourth instance; filed as `#064`, not re-raised.
**Corpus:** **18,540** words (`cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w`),
up from 17,062 at 18:00 — **+1,478 in one window**, the largest single-session corpus
addition the ledger records. `.claude/skills/gw-plate/SKILL.md` 924 new; `gw-designer.md`
507 → 845; `gw-panel.md` 369 → 572; `gw-chapter/SKILL.md` +5 lines.
**Earlier reviews today, not repeated:** `runs/retro/2026-09-20-plates-and-compile.md`,
`runs/retro/2026-09-20-plate-round-2.md`.

---

## Proposed `FINDINGS.md` entry

### 2026-09-20 19:56 — The plate pipeline cost 1,478 corpus words and bought a measured 3-in-10 to 0-in-2; one item's proof is now falsely red, and three known failures have no route

The author said plates must stand on their own for a man who never read the chapter, and
named the stages himself: *formulate ideas, pick the best, draft, checks, persona input,
revisions, formatting*. That became `/gw-plate`, `plate_check.py` (eleven rows, including
an `ink` row that rasterises and counts margin pixels — the first check in the house that
looks at the *drawing* rather than the source), `plate_brief.py`, concepts mode in
`gw-designer`, and plate personas in `gw-panel`. It was then run.

**1. The pipeline's value is measured, not asserted — this is the rare session that got
its own counterfactual.** The same desk, the same standard, the same afternoon:

| Plates | Stage-5 standalone read |
|---|---|
| Ch8 and Ch12, through `/gw-plate` end to end | **2 PASS** (Ch12 first time; Ch8 on the one allowed revision) |
| The other ten, drawn first-idea-ships on 2026-09-20 | **7 PASS, 3 FAIL** (Ch2, Ch5, Ch6) |

Ch6's failure is the sharpest: the plate's fills were inverted, so the solid bar read as
*her* work and the ghost as his, and the drawing argued the self-pity position its own
subtitle exists to deny. Two clean checkers, two Designer rounds and a full reader review
had passed it. Only a cold reader with no chapter caught it. `FINDINGS.md` 2026-09-20 18:00
already says geometry checks verify form and only the Panel verifies meaning; this is that
finding with a denominator.

Which stages earned the 1,478 words is worth recording before anyone simplifies. **Stage 1
(three concepts, three carriers) and Stage 5 (the cold standalone read) did the work**:
Ch8's chosen concept still imported the chapter's Lesson as two printed Stoic tests, and
Stage 5 cut them. **Stage 2 (the Panel's cold pick) changed nothing yet** — it agreed with
the Designer independently on both Ch8 and Ch12. Two for two is agreement, not evidence of
redundancy; n=2. Recorded so that if it reaches five-for-five, the deletion has a number
waiting for it rather than an impression.

**2. `#062`'s proof command is falsely red: the work landed, better than asked, and the
item can never close.** `#062` asked whether `land.py` should run `svgcheck.py` before
copying a plate into `books/`. It now runs `plate_check.py`, which is a strict superset —
it flags the exact Ch12 defect on three rows where `svgcheck` flagged one:

```
$ python3 scripts/plate_check.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg --chapter 12
  [FAIL] geometry    MARGIN  y=340.0 'no deadline, nobody watching' -44..132
  [FAIL] anchor-attr text-anchor attribute on an element whose class also sets one; the class wins in the browser
  [FAIL] ink         rendered ink inside the 40px margin bands: left=396
$ grep -q svgcheck scripts/land.py ; echo $?
1
```

`applied_by: grep -q svgcheck scripts/land.py`. The behaviour is in `scripts/land.py:159-176`;
the grep names a symbol the implementation improved past. **This is the third instance of
the grep-for-its-own-text shape, and the first in the false-red direction** — 2026-09-19's
two half-fixes closed green on work not done; this one stays open on work done. Both come
from the same root, and the root is that a proof which does not run the behaviour is a
comment. `tests/run.py` has a case for `plate_check`'s anchor-attr row (line 200); nothing
tests that `land.py` refuses. The half of `#062` that is a fixture landed; the half that is
a caller did not get one.

**3. Three plates fail the house's own standard and nothing routes them.** The sweep's
verdicts on Ch2, Ch5 and Ch6 — including "send it back to the concept stage" for Ch5 — live
only in `runs/design/2026-09-20-plate-standalone-sweep.md`. No inbox item carries them
(`#061` and `#067` carry unrelated label calls on the same chapters). `next.py` reports 22
questions waiting; none is *three plates fail the standalone read*. The cause is structural
and in the skill: `/gw-plate` routes a Stage-5 failure to Stage 6 (revise), and only to the
inbox after a second failure (Rule 6). Run as a **sweep** over plates nobody is revising
today, a first failure has nowhere to go. The earlier reader review was routed into `#065`-`#067`
because per-chapter work followed it; this one had none, and fell out of the system of record.
Lens: **what was missing** — a stage the flow has no name for. Same shape as the ledger's
oldest complaint, a desk reporting something true into a file nobody greps.

**4. The harness caches desk definitions, so a definition edited this session ran as its
old text.** `gw-panel` was granted `Write` in `.claude/agents/gw-panel.md` and could not
write for its first three dispatches; the Publisher filed `plate-pick.md` x2 and the
standalone sweep by hand, each labelled *"Filed by the Publisher verbatim from the desk's
return (its Write tool was not live this session)."* That labelling is exactly right and is
why this is legible at all. The consequence is larger than one tool: **`gw-designer`'s new
concepts mode also ran under the cached definition**, so three concepts arrived because the
dispatch prompt asked for them, not because the desk's own text does. The session is
therefore not evidence that either edit works as written. `gw-panel.md:12-14` records the
incident for that one desk; nothing records the general rule.

**5. A `git mv` of `ttfwidth.py` broke `svgcheck.py` under a running desk**, which noticed
and repaired it. One-off, self-repaired, cost nothing. Worth one line because it is the
second instance today of the same shape as five parallel Designers each rediscovering one
tool defect (2026-09-20 16:37): **the parent mutates the tree while children are reading
it.** A lock would cost more than either instance did. Named, not proposed.

**What worked, and is load-bearing.**

- **`svgcheck.py`'s deletion was actually taken.** It is now a two-line shim pointing at
  `scripts/plate_check.py`. Proposed as S2 on 2026-09-16, unapplied for four days, applied
  here. An absorption that leaves both copies running is the usual outcome; this one did not.
- **The manual generator refused an empty cell.** `docs/manual.html` would not regenerate
  because `ttfwidth.py` had no docstring, so the scripts table had a blank. It refused rather
  than emitting a blank, and the fix was a docstring on the script — a check that improved
  the thing it documents. Cheap, silent, correct; do not simplify it away.
- **Rule 7 held under pressure.** The Designer reported "11 rows ok" three times and the
  Publisher ran `plate_check.py` itself each time. `tests/run.py`: 107/107.
- **Rule 8 held.** Zero desk writes under `books/` across 17 commits, with three known-bad
  landed plates and fixes in hand.
- **Rule 15 held.** The round-3 compile carries the clock in its filename and `plates-draft`
  in its coverage.
- **The Panel's own honesty rows.** The sweep names what it did *not* read and flags that two
  distillations were truncated in its grep, so two verdicts rest on less evidence than the
  other eight. A desk reporting the weakness of its own result is the behaviour the whole
  evidence axis exists to produce.

---

## Suggestions, ranked

**1. New check with a caller, plus its fixture (type: new check).** `land.py:159-176`
refuses a plate on a `plate_check` FAIL row, and nothing in `tests/` proves it. Add a case
that lands a chapter whose `runs/chNN/plate.svg` carries the anchor-attr defect and asserts
the copy is refused, plus a clean control that lands. Then correct `#062`'s `applied_by`
to name that case instead of a grep for a superseded symbol. **Deletes** the 37-word
comment at `scripts/land.py:161-163` carrying the `#062` rationale, and the false grep.
Cost: code, not corpus; corpus stays 18,540.

**2. Open item (type: open item).** A Stage-5 FAIL on a plate nobody is revising today has
no route. Recommended shape, zero corpus words: `next.py` reports any
`runs/chNN/plate-read.md` whose last verdict is not PASS, the way it already reports
chapters stopped at a stage. Ch2, Ch5 and Ch6 are the standing instances. **Names no
deletion**, which is why it is an open item and not a suggestion.

**3. Open item (type: open item).** A desk definition edited in session runs as its old
text until a new session. Recommended shape: `sync_plugin_layout.py` already copies
`.claude/agents/` to `agents/` — have it print, once, the desks whose text changed and the
sentence *these desks run the previous definition until a new session*. **Names no
deletion**; `gw-panel.md:12-14` records the incident but not the rule, and deleting those
three lines would lose the reason that desk has `Write`.

**Assessed and not proposed.** The +1,478 corpus words: large, but every word is a stage the
author named and the measured result is 3-in-10 to 0-in-2. No deletion is warranted yet; the
candidate, if one ever comes, is Stage 2. The `git mv` race (finding 5): self-repaired, no
mechanism cheaper than the cost. The Ch8 PASS with Panel edit 5 unmet (the left caption
centres under its column, not under the loaded pan): correctly routed to `#068` as cosmetic,
not decided silently.

---

## Proposals, as commands

```
python3 scripts/inbox.py --add "land.py now refuses a plate on a plate_check FAIL row, but nothing in tests/ proves it, and #062's applied_by greps for 'svgcheck' in land.py - which land.py no longer names, because plate_check superseded it. The item can never close on work that is already done. Should land.py's refusal get its own fixture case, and #062's proof be corrected to name it?" \
    --raised-by gw-retro --chapter 0 \
    --context "Third instance of the grep-for-its-own-text shape and the first false-red one: 2026-09-19's two half-fixes closed green on work not done; this stays open on work done better than asked. tests/run.py covers plate_check's anchor-attr row but nothing covers the caller, so the half of #062 that was a fixture landed and the half that was a caller did not." \
    --unblocks "Whether #062 can close, and whether land.py's plate refusal is held by a re-runnable case or by a 37-word comment" \
    --recommend "Yes: a case that lands a chapter whose plate carries the anchor-attr defect and asserts the copy is refused, plus a clean control that lands; then rewrite #062's applied_by to run that case and delete the comment at land.py:161-163" \
    --evidence "python3 scripts/plate_check.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg --chapter 12 -> three FAIL rows (geometry MARGIN, anchor-attr, ink left=396). grep -q svgcheck scripts/land.py -> exit 1. grep -in land in tests/run.py output -> no case names land.py. The behaviour is at scripts/land.py:159-176." \
    --applied-by "python3 tests/run.py 2>&1 | grep -q 'land.py refuses a plate that fails plate_check'" \
    --prove-file scripts/land.py --prove-at 6ed70f1~1 \
    --prove-case "land.py refuses a plate that fails plate_check"

python3 scripts/inbox.py --add "The Reader Panel's standalone sweep failed three plates (Ch2 broken line reads as going cold, Ch5 cannot stand alone and needs a new concept, Ch6 fills inverted so the plate reads as self-pity). Those verdicts live only in runs/design/2026-09-20-plate-standalone-sweep.md; no inbox item carries them and next.py does not surface them. Should next.py report any runs/chNN/plate-read.md whose last verdict is not PASS?" \
    --raised-by gw-retro --chapter 0 \
    --context "/gw-plate routes a Stage-5 failure to Stage 6 (revise) and only to the inbox after a second failure. Run as a sweep over plates nobody is revising that day, a first failure has nowhere to go. The earlier reader review reached you as #065-#067 only because per-chapter work followed it. Ch6's plate currently argues the self-pity position its own subtitle denies, and that is not on any list you read." \
    --unblocks "Whether a failed plate is state the oracle reports or a line in a runs/ file someone has to remember" \
    --recommend "Yes: next.py reads runs/chNN/plate-read.md the way it reads chapter stage files and names any chapter whose last plate verdict is not PASS. Zero corpus words." \
    --evidence "python3 scripts/next.py -> 'inbox: 22 question(s) waiting on you'; no item mentions the sweep. grep -ril 'standalone sweep|polarity|concept stage' inbox/ -> no matches. runs/design/2026-09-20-plate-standalone-sweep.md -> 'Seven PASS, three FAIL.'" \
    --applied-by "python3 tests/run.py 2>&1 | grep -q 'next.py names a chapter whose plate-read verdict is not PASS'" \
    --prove-file scripts/next.py --prove-at 6ed70f1~1 \
    --prove-case "next.py names a chapter whose plate-read verdict is not PASS"

python3 scripts/inbox.py --add "A desk definition edited during a session runs as its OLD text until a new session starts. gw-panel was granted Write and could not write for three dispatches; the Publisher filed its returns by hand. The larger consequence is that gw-designer's new concepts mode also ran cached, so this session is not evidence either edit works as written. Should sync_plugin_layout.py print, once, the desks whose definitions changed and that they run the previous text until a new session?" \
    --raised-by gw-retro --chapter 0 \
    --context "Every session that edits a desk and then dispatches it believes it is testing the new text. Today it announced itself because a missing tool is loud; concepts mode is quiet, and three concepts arrived because the dispatch prompt asked for them. gw-panel.md:12-14 records the incident for one desk; nothing records the rule, so the next quiet instance passes as a successful test." \
    --unblocks "Whether a definition edit is verified by the session that makes it or by the next one, and whether the Publisher should say so when reporting a desk that ran under a changed definition" \
    --recommend "Yes, and only that: one printed line from sync_plugin_layout.py naming the changed desks. No rule text - this is a fact about the harness, not a behaviour anyone can be told to remember." \
    --evidence "runs/ch08/plate-pick.md, runs/ch12/plate-pick.md and runs/design/2026-09-20-plate-standalone-sweep.md each carry 'Filed by the Publisher verbatim from the desk's return (its Write tool was not live this session)'. grep -n Write .claude/agents/gw-panel.md -> line 5 'tools: Read, Grep, Glob, Write'. git diff --stat 16f569b..HEAD -- .claude/ -> gw-designer.md +54, gw-panel.md +25, both dispatched the same session." \
    --applied-by "python3 scripts/sync_plugin_layout.py --help 2>&1 | grep -q 'changed definition'"
```

---

## Looked at, found clean

- **`books/`** — zero desk writes across 17 commits, with three landed plates known defective
  and their fixes sitting in `runs/`. Checked by diffstat.
- **Rule 5 / Rule 7** — the Designer self-reported "11 rows ok" three times; `plate_check.py`
  was run independently each time and agreed. No discrepancy.
- **Rule 12** — no `SKIP` reported as `PASS`; the sweep states what it did not read and flags
  two verdicts as resting on truncated context.
- **`tests/run.py`** — 107/107, including the anchor-attr case from `#062`.
- **`svgcheck.py`** — now a shim; the absorption's deletion was taken, not deferred.
- **Rule 15** — the round-3 compile is dated to the minute and labelled `plates-draft`.
- **The inbox** — `#068` carries four label-level calls from the Ch8/Ch12 runs rather than
  the Designer deciding them; nothing in those two runs was resolved cold.
- **The previous review's two proposals** (`inbox.py --prove` at `--close`; the charset case)
  are not in the inbox as of this window. Noted, not re-raised — the author has not been asked
  yet, and re-filing an unanswered proposal is how a ledger grows.
