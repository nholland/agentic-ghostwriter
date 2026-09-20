# Session review — the plate round 2, and a proof the inbox will not accept

**Desk:** the Archivist · **Clock:** 2026-09-20 18:00 · **Branch:** `claude/gateway-45bnh4`
**Window reviewed:** `eb3da38..HEAD` (`16f569b`) — 10 commits, 47 files, 1,511 insertions.
**Window the hook recorded:** `8c03c96 b5194cf` — 2 of those 10, excluding both Designer
rounds' start and the charset fix. Third instance; already filed as `#064`, not re-raised.
**Corpus:** 17,062 words, unchanged by this window (`git diff --stat eb3da38..HEAD -- CLAUDE.md .claude/`
is empty). `books/` untouched by any desk — Rule 8 held.
**Earlier review, not repeated:** `runs/retro/2026-09-20-plates-and-compile.md`.

---

## Proposed `FINDINGS.md` entry

### 2026-09-20 18:00 — The house's own proof standard is unfileable for a new check, and three items proved it in one sitting

The author said the plates were "slightly off mark" and "hard to understand the key
takeaway." The Reader Panel read all fifteen as a reader and returned keep 2, edit 8,
replace 2; two Designer desks applied the edits in parallel on disjoint file sets; the
Publisher checked every plate and caught one defect no checker sees. That work went
well and is described under *what worked*. Two things are worth the ledger.

**1. `inbox.py` cannot accept the proof `gw-retro.md` demands, for exactly the class
of proposal `gw-retro.md` was written to produce.** `gw-retro.md` lines 117-122 (71
words) say: "A proposal that adds or fixes a check closes on its fixture, never on a
grep for its own text... point `--applied-by` at `tests/run.py`." But `inbox.py --add`
runs `tests/prove.py` at **filing** time, and `prove.py` requires the named case to be
green on the current tree. A proposal to *add* a check names a case that does not exist
yet, so the filing is refused:

```
$ python3 tests/prove.py --file scripts/chapter_pdf_local.py --at eb3da38 \
      --case 'every html wrapper the house writes declares a charset'
prove: REFUSED - case '...' not found in tests/run.py's output
```

When the author said "file them," all three of the Archivist's proposals hit this and
fell back to greps: `#062` closes on `grep -q svgcheck scripts/land.py`, `#063` on
`grep -rq 'bottom band' tests/`, `#064` on `grep -rq 'second dispatch keeps the older
window start' tests/`. Every one is a grep for the change's own text — the precise
thing the brief calls a comment rather than a proof, and the thing that closed green
over two half-fixes on 2026-09-19.

The guard is right about the danger (an unproven red-then-green claim) and wrong about
the moment. At `--add` the fixture cannot exist; at `--close` it must. Lens: **what
broke** — a rule bypassed three times in one command is mis-placed, not disobeyed.
Related but distinct: `#048` (open) is `prove.py` unable to revert to a commit where
the file or function did not exist; this is the case not existing at all yet, and its
remedy is in `inbox.py`, not `prove.py`. Note also that the Archivist has no `Write`
tool and never applies, so it cannot write the fixture first: with the guard where it
is, the standard is unreachable by construction, not by laziness.

**2. The charset defect: the right pattern already existed 130 lines away in the same
file, and the fix landed as a comment.** Chromium sniffed `runs/ch11/plate.svg` wrong
and printed the title's curly apostrophe as three garbage glyphs, because
`svg_to_png`'s HTML wrapper declared no charset. The manuscript wrapper in the same
file (`chapter_pdf_local.py:302`) has carried `<meta charset='utf-8'>` all along.
Measured across every tracked non-test `.py` that writes a doctype:

```
at eb3da38: ['scripts/chapter_pdf_local.py:173']
at HEAD   : []
```

One offender, now zero — a one-line class with a one-line check available. What landed
instead was a 25-word comment. Lens: **what recurs** — this is the third fix of the day
(after `svgcheck`'s anchor precedence and the rasteriser's bottom band) to land on
inspection with nothing in `tests/` holding it, and the third is the cheapest of the
three to hold: `tests/run.py` already carries `sys_path_hardcode_cases()`, a
source-level scan of every tracked script with a negative control, written for exactly
this shape ("GAPS.md used to carry that as a sentence telling the next reader to
remember to check; a fixture does not need remembering").

**What worked, and should not be simplified away.** Two clean checkers and two Designer
rounds had passed these plates; a reader found ten of twelve wrong. `svgcheck.py` and
the renderer verify geometry; only the Reader Panel verified *meaning*, and its
cross-set diagnosis (the drawing states the disease, the caption stack carries the cure,
so the takeaway was never in the picture) is the answer to the author's sentence, not a
restatement of it. It is a read-only desk with no `Write` tool, so the review exists as
`runs/design/2026-09-20-plate-reader-review.md` only because the Publisher filed the
return verbatim — nothing in the corpus instructs that. It held here because the
downstream work was parallel sub-agents, which cannot read the parent's transcript and
so *had* to be briefed from a file. Worth knowing that the guarantee comes from that
coupling and not from a rule, before anyone relies on it for a review with no
downstream desk. The parallel split itself was clean: disjoint SVG sets, one desk
recompiling, no shared-file conflict.

**One trap, for whoever applies `#065`.** If the author rules that a plate's title is
the distillation's Mechanism word for word, the obvious check fails on typography, not
on titles: `runs/ch11/plate.svg` is `The Conversation She’s Never Heard` (curly) against
`The Conversation She's Never Heard` (straight) in the distillation, while `ch06` and
`ch07` use straight apostrophes. Eleven of twelve titles now match; that one differs by
one character. This needs no new item — two lines in `#065`'s **Checked** block.

---

## Suggestions, ranked

**1. Rule placement (type: rule edit / check placement).** Move `inbox.py`'s
`--prove-*` verification from `--add` to `--close`: record the three flags as a promise
at filing, and refuse the *close* unless `tests/prove.py` shows the named case red at
`--prove-at` and green now. Cost: unmeasured (code, not corpus; no rule words). **What
it deletes:** nothing, if accepted — and if declined, it deletes `gw-retro.md` lines
117-122, 71 words that instruct the Archivist to do something the tooling refuses. One
of the two must go; today they contradict each other three times over.

**2. New check with a caller (type: new check).** A `charset_cases()` in `tests/run.py`,
modelled on `sys_path_hardcode_cases()`: scan every tracked non-test `.py` for a written
`<!doctype html` with no `charset` within the same wrapper, plus a negative control that
reintroduces the pre-fix string. Cost: unmeasured until drafted (≈25 lines of test code;
corpus stays 17,062, `tests/` is not corpus). **What it deletes:** the 25-word comment at
`scripts/chapter_pdf_local.py:173-174`, which is the only thing currently holding this
knowledge.

**3. Amendment, no item (type: open item, already open).** Append the apostrophe
measurement above to `#065`'s **Checked** block, so the check written on the author's
yes normalises quotes instead of failing eleven-of-twelve-plus-one.

---

## Proposals, as commands

```
python3 scripts/inbox.py --add "inbox.py --add runs tests/prove.py at filing time, so a gw-retro proposal to ADD a check can never carry the proof gw-retro.md demands: the fixture case does not exist yet, and prove.py refuses a case it cannot find. All three items filed this session fell back to a grep for the change's own text - the exact thing the brief calls a comment rather than a proof. Should the --prove-* flags be recorded as a promise at --add and verified at --close, where the fixture must exist?" \
    --raised-by gw-retro --chapter 0 \
    --context "With the guard at --add, the standard is unreachable by construction, not by laziness: the Archivist has no Write tool and never applies, so it cannot write the fixture before filing. Every future proposal for a new check will close on a grep, which closed green over two half-fixes on 2026-09-19. Distinct from #048, which is prove.py failing on a file or function absent at --at; this is the case absent everywhere, and its remedy is in inbox.py." \
    --unblocks "Whether gw-retro.md lines 117-122 describe a workable close-condition or 71 words that must be cut" \
    --recommend "Move the verification to --close: store prove-file/at/case at --add unverified, and refuse --close unless prove.py shows the case red at --prove-at and green now" \
    --evidence "python3 tests/prove.py --file scripts/chapter_pdf_local.py --at eb3da38 --case 'every html wrapper the house writes declares a charset' -> prove: REFUSED - case not found in tests/run.py's output. Filed this session: #062 applied_by 'grep -q svgcheck scripts/land.py'; #063 'grep -rq bottom band tests/'; #064 'grep -rq second dispatch keeps the older window start tests/' - 3 of 3 are greps for their own text." \
    --applied-by "grep -q 'verified at --close' scripts/inbox.py"

python3 scripts/inbox.py --add "The plate rasteriser wrote an HTML wrapper with no charset, so Chromium sniffed runs/ch11/plate.svg and printed the title's curly apostrophe as three garbage glyphs - while the same file's manuscript wrapper had declared a charset all along. The fix landed as a 25-word comment. Should tests/run.py carry a source-level case that no tracked script writes a doctype without a charset?" \
    --raised-by gw-retro --chapter 0 \
    --context "Third fix of the day to land on inspection with nothing in tests/ holding it, and the cheapest of the three to hold. No checker sees a mojibake glyph: svgcheck reads geometry, the renderer reports correct dimensions, and only a human looking at the PNG caught it. The next wrapper anyone adds reintroduces it silently." \
    --unblocks "Whether the charset rule is a comment one reader has to notice or a case that runs on every commit" \
    --recommend "Yes: charset_cases() in tests/run.py on the sys_path_hardcode_cases() model - scan tracked non-test .py for a written doctype with no charset in the same wrapper, plus a negative control reintroducing the pre-fix string" \
    --evidence "Scan of every tracked non-test .py writing a doctype: at eb3da38 ['scripts/chapter_pdf_local.py:173']; at HEAD []. The compliant wrapper at scripts/chapter_pdf_local.py:302 predates the defect. runs/ch11/plate.svg and runs/ch12/plate.svg each hold 2 non-ASCII characters; ch06 holds 1." \
    --applied-by "grep -q 'declares a charset' tests/run.py"
```

Both `--applied-by` values are greps for their own text, for the reason finding 1 gives.
The first proposal is the one that makes the second one's proof honest.

---

## Looked at, found clean

- `books/` — untouched by any desk in the window; Rule 8 held through two parallel Designers.
- Corpus — 17,062 words, unchanged; no rule text was spent on this work.
- `#062`-`#067` — filed, each with context and evidence; `#065` and `#066` carry the panel's
  cross-set rulings rather than a desk deciding them silently. `#067` captured the round-2
  label calls. Nothing decided cold that should have gone to the author.
- The Reader Panel's per-plate edits against the round-2 SVGs: Ch7 retitled **The Private
  Tally**, Ch12 **The Thing With No Deadline**, Ch11 to its distillation line; Ch4 and Ch5
  now share one nail and one hole glyph, closing the contradiction the panel ranked third.
  Eleven of twelve titles match their Mechanism exactly; the twelfth differs by one
  apostrophe (above).
- `runs/log.md` — four entries, correct branch, no merge corruption of the kind repaired
  earlier today.
- Rule 15 — the reader PDF was regenerated wholesale under its dated name; no stale
  point-in-time artifact left claiming to be current.
