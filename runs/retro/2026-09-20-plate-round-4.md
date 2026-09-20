# Session review — 2026-09-20 22:03 — round 4: Ch2, Ch6 edited, Ch5 rebuilt

**Window:** `980e502..HEAD` (12 work commits, `45e31f9`..`bf34a11`), branch
`claude/gateway-45bnh4`. Bounds passed by the Publisher by hand. See finding 1 —
that hand-off is the session's finding, not its footnote.

**Fourth Archivist dispatch today.** The three earlier reviews are
`2026-09-20-plate-pipeline.md`, `-plate-round-2.md`, `-plates-and-compile.md`.
Nothing here repeats their proposals; two of this session's candidates were
dropped on inspection because they already carry an inbox number.

---

## 1. The review window was stale by an entire session (what broke · what recurs)

`.claude/state/retro-window` read:

```
4ea3575994dd9d1ad1523b6f844451fcb91d9743 980e502e2eac0d0498b26966feb681d4ea4acf44
```

That window was **already reviewed**. `git log --oneline 4ea3575..980e502` returns
three commits, one of which is `f7736f3 Archivist: retro of the plate pipeline` —
the review of that very span. This session's twelve commits (`45e31f9`..`bf34a11`)
fall entirely **outside** it.

`gw-retro.md` lines 24-31 instruct this desk, in 103 words, that the pair in
`retro-window` "is the review's actual bounds" and that `retro-last-sha`..HEAD is
the fallback **only if `retro-window` is absent.** Followed literally, this review
would have re-read the previous session, found the retrospective of it sitting in
the window, and reported on work three hours old while Ch2, Ch5 and Ch6 went
unexamined. It did not, only because the Publisher passed `0b8dfa7`..HEAD in the
dispatch prompt — the second consecutive session in which the window's correctness
depended on a human remembering to override the oracle.

**Why it was stale:** `retro-check.sh` writes `retro-window` only when it
dispatches. This dispatch came from the Publisher, mid-session, not from the Stop
hook. The file's mtime is 19:58; the session ran to 22:03. Nothing marks a window
consumed, so a consumed window reads exactly like a fresh one.

**Shape.** This is the fourth instance of #030: *the review window silently
describes something other than the session.* Instances one and two were the
collapse-to-empty (fixed, then recurred because the fix closed on a grep).
Instance three is open as **#064** — two dispatches firing before a review,
discarding the earlier START.

**#064's recommendation would not have prevented today.** It proposes advancing
START only once "a commit touching `runs/retro/` falls inside the window."
`f7736f3` *is* such a commit and *is* inside `4ea3575..980e502`, so that window
is consumed under #064's own rule — and the file still names it, because no hook
ran to replace it. #064 fixes which START survives a double dispatch; it does not
make a consumed window announce itself.

**The mechanically decidable fact both cases share:** if the recorded window's end
is not HEAD, the span it names was reviewed and the unreviewed span is
`end..HEAD`. That single derivation covers #064's case and today's, and it removes
the reason the desk was ever told to reason about three state files.

**Proposed:** `scripts/retro_window.py`, printing `START HEAD`, called by
`gw-retro.md` in place of its 103-word warning paragraph. Priced below. Proved in
the existing `retro_window_cases()` harness (`tests/run.py:1261`), which already
runs the real hook against a repo it controls — the right place, because the last
fix of this shape closed on a grep and the defect recurred.

## 2. The Ch5 notes header states a title the plate does not carry (what broke, minor)

`runs/ch05/plate-notes.md` line 3:

```
**File:** `runs/ch05/plate.svg` · **Title (aria-label):** The Remaining Nails · **New drawing.**
```

The SVG's actual aria-label:

```
aria-label="The courage to come back: the same fight twice, once with the real
thing left unsaid and once with it said"
```

The same file's own body (lines 214-222) explains the divergence correctly and at
length, and the pasted check row on line 253 prints the real value. Only the
hand-written header is stale — written from the brief before the deliberate
retitle, never revisited.

**Cost this round: none.** The body carried the truth, the WARN fired, #070 was
filed, the author has the decision. But the shape is Rule 5's — *a field a desk
transcribes by hand, disagreeing with the artifact and with the script's own
output in the same file* — applied to a string instead of a count. `plate_check.py`
already parses the aria-label for its `title` row; comparing it to the header the
notes declare is a widening of an existing check, not a new one.

**Typed as an open item, not a suggestion,** because it names no deletion: no rule
text anywhere specifies that header (it appears in neither `gw-plate/SKILL.md` nor
`gw-designer.md`), so there is nothing to cut in exchange. Recorded here so the
third instance is not discovered as if it were the first.

## 3. What worked, and is load-bearing

**The Designer flagged rather than fixed.** The chapter's distillation still names
the Mechanism "The Remaining Nails" — Ch04's image, deliberately absent from the
new concept. The Designer took Ch5's own beat heading verbatim, declared the
divergence, marked its own WARN **expected**, named it "not the Designer's to
resolve," and filed #070. It did not edit
`books/the-stoic-husband/chapters/ch05/distillation.md`. Rule 8 held here
structurally, not by good manners: the file is under `books/` and a cold desk
cannot write there. Second time today this exact situation produced a flag instead
of a silent repair (Ch7/Ch12 in the prior session). **A later simplification that
touches Rule 8's cold-desk boundary should know this is what it is holding up.**

**The Panel reached the same flag from the other side.** `plate-pick.md`'s
"Carried forward for the author" arrives at the title problem independently, and
goes further than the Designer by naming the two candidate replacements from the
chapter's own beat headings. #070 is better posed for it.

**`--from 6` did what it was designed to do.** Ch2 and Ch6 each ran one stage-6
pass from the sweep's own edit list and each passed the Panel's cold read first
try. That *is* the resume path exercised — entering the pipeline at a named stage
on a prior desk's written findings. The dispatch note wondered whether `--from`
was "actually exercised as designed"; it was, twice, successfully. No proposal.

## 4. Assessed and deliberately not proposed

**The Panel's pick has agreed with the Designer 2 for 2** (Ch8/Ch12 prior session,
Ch5 today), with no cost yet paid for disagreement. The tempting finding is that
stage 2 is ceremony. **It is not supportable, on two grounds.** n=2 is not a rate.
More to the point, the pick is not where stage 2 paid this run: `plate-pick.md`'s
value was the skeptic column — A named as "the most dangerous of the three: it
hands a defensive man the shrinking," a reading the Designer's own notes do not
contain — plus the runner-up repair notes and the title flag that fed #070. A
desk whose *ranking* is redundant but whose *reasoning* is load-bearing is not a
deletion candidate; it is a desk whose output format might eventually narrow.
**Recorded so it can be judged at n=6, not re-litigated from scratch each round.**

**#070 is the third instance of the question #065 already asks** (is a plate titled
by the distillation's Mechanism? — open since 17:46, with Ch7 and Ch12 as
instances one and two). A general item left unruled accrues per-chapter
duplicates. This is the author's queue depth, not a defect in the house, and
`plate_check.py:48` already routes the WARN through `LEVELS` so the rows become
FAIL the moment he ratifies. No proposal; noted because a fifth instance would
change the assessment.

## 5. Looked at and found clean

- `git log --stat`/`--diff` across all twelve work commits; no unwatched path
  written, no book-tree write by a cold desk, no landing without the Publisher.
- `runs/ch05/plate-brief.md`, `plate-concepts.md`, `plate-pick.md`,
  `plate-notes.md`, `plate-read.md` — the full stage 1-6 apparatus present and in
  `runs/`, none of it in `books/`.
- Ch5's standalone read: PASS against the distillation, with the Conversation
  sentence's "becomes small" reproduced in the stranger's own words, and the
  Ch04 nail/fence-post imagery confirmed absent as instructed.
- `plate_check.py` re-run reasoning verified against the pasted rows; the single
  WARN is the title row and is the expected one. No FAIL anywhere in the round.
- Rule 15 honoured: the compile is
  `the-stoic-husband-prologue-ch12-plates-draft-2026-09-20-2200.pdf` — coverage
  and clock both in the filename.
- `inbox.py` — #070 filed with context and unblocks; #069 closed out by the
  author's batching instruction being executed in the order he gave.
- `FINDINGS.md`, `.claude/LEARNINGS.md`, `GAPS.md` read for shape. Nothing in this
  session matches a GAPS entry.
- **Corpus: 18,540 words** (`cat CLAUDE.md .claude/agents/*.md
  .claude/skills/*/SKILL.md | wc -w`), against 17,017 on 2026-09-19 and 16,904 at
  end-of-day 2026-09-18. **Up 1,523 words in a day.** The plate pipeline is most
  of it and has earned its place; but this is the first day the corpus grew by
  more than the whole Archivist definition, and the next review should say so
  again if it grows again. The one proposal below is net negative by design.

---

## Suggestions

### S1 — new check with a caller, plus a simplification (net -41 words of rule text)

**Type:** new check with a caller · simplification.
**Changes:** adds `scripts/retro_window.py` as the single oracle for the review's
bounds; adds a staleness case to `retro_window_cases()` in `tests/run.py`.
**Deletes:** `gw-retro.md` lines 24-31 — **103 words**, measured:
`sed -n '24,31p' .claude/agents/gw-retro.md | wc -w` → `103`.
**Replaces with** — 62 words, measured, drafted in full:

```
- `git log --stat` and `git diff` for the window: run
  `python3 scripts/retro_window.py`, which prints `START HEAD` and is the only
  oracle for the review's bounds. If the recorded window's end is not HEAD, that
  span was already reviewed and the unreviewed one is its end..HEAD. Never read
  the state files and reason about them; that is how #030 recurred four times.
```

**Net rule text: -41 words.** The script itself is **unmeasured** — it is not
drafted, and this desk does not write it. Its logic is three lines.

**Why this and not more rule text:** the current paragraph is already the second
attempt to fix #030 with prose. Prose lost twice. The fact is decidable from two
SHAs.

```
python3 scripts/inbox.py --add "retro-window is never marked consumed, so a review dispatched by the Publisher rather than the Stop hook reads a window that was already reviewed. Today it named 4ea3575..980e502 - a span containing f7736f3, the retrospective OF that span - while this session's twelve commits sat outside it. Should scripts/retro_window.py become the single oracle, deriving the bounds as end..HEAD whenever the recorded window's end is not HEAD?" \
    --raised-by gw-retro --chapter 0 \
    --context "Fourth instance of #030's shape and the second consecutive session where the window was correct only because the Publisher passed it by hand in the dispatch prompt. Distinct from #064, whose fix does not cover this: #064 advances START when a runs/retro/ commit falls inside the window, and f7736f3 is exactly that, so today's window is consumed under #064's own rule and the file still names it. gw-retro.md spends 103 words telling the desk to trust that file." \
    --unblocks "Whether the Archivist's bounds are computed or hand-carried, and whether gw-retro.md lines 24-31 drop from 103 words to 62" \
    --recommend "Yes: add scripts/retro_window.py printing START HEAD, derive end..HEAD when the recorded end is not HEAD, call it from gw-retro.md in place of the paragraph, and prove it in retro_window_cases()" \
    --evidence "cat .claude/state/retro-window -> '4ea3575994dd9d1ad1523b6f844451fcb91d9743 980e502e2eac0d0498b26966feb681d4ea4acf44'; git log --oneline 4ea3575..980e502 -> '980e502 auto: session log 2026-09-20 19:58 / f7736f3 Archivist: retro of the plate pipeline; #062's proof corrected; #069 routes the three sweep failures / 36baf54 Reader Panel: Ch8 second cold read, PASS'; git log --oneline 980e502..HEAD | wc -l -> 13; sed -n '24,31p' .claude/agents/gw-retro.md | wc -w -> 103" \
    --applied-by "python3 tests/run.py" \
    --prove-file "tests/run.py" \
    --prove-at "bf34a11b0596327b9d14dbe1a9de35da1cad4d89" \
    --prove-case "retro window: a recorded window whose end is not HEAD reports end..HEAD, not its own stale pair"
```

### S2 — open item (names no deletion, so it is not a suggestion)

The Ch5 notes header declares a title the SVG does not carry. `plate_check.py`
already reads both values for its `title` row. Widening that row to compare the
notes' declared title against the aria-label would cost one comparison and close
on a case in the existing `plate_check_cases()` harness — but no rule text
anywhere specifies the header, so there is nothing to delete in exchange, and by
this desk's own standard that makes it an open item. **Raise it if a third
instance appears; do not file it now.**

---

## Bottom line

One proposal, net negative in rule text, on the failure that would have silently
made this review worthless. One open item held back deliberately. Two temptations
(cutting stage 2, chasing the #065 duplicates) assessed and declined with the
counts written down so the next review inherits them rather than re-deriving them.
