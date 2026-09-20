# Session review — plates, the compile path, and two checks that said clean

**Desk:** the Archivist · **Clock:** 2026-09-20 16:37 · **Branch:** `claude/gateway-45bnh4`
**Window reviewed:** `14cf389..77b9ff7` — 5 commits, 2,966 insertions, 34 files.
**Window the hook recorded:** `98f171f 0a0e1da` — 2 of those 5. See finding 3.
**Corpus:** 17,062 words (`cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w`),
unchanged by this window: it touched `runs/` and `scripts/` only. No rule words were
spent to do the work.

---

## Proposed `FINDINGS.md` entry

### 2026-09-20 16:37 — Two plate checks reported clean on the defects they were written to catch, and both fixes landed without a fixture

The session built the reader PDF's plate path (`compile.py --plates`, plus the local
renderer taught to pass plate blocks through and rasterise them) and drew eleven new
chapter plates and three Part plates. Along the way it found that **both tools the
house uses to look at a plate were lying**, in the two shapes this ledger already
names.

**1. The checker trusted an attribute the browser ignores.** `runs/design/svgcheck.py`
read `text-anchor="start"` as final on a `<text>` whose CSS class already set
`text-anchor:middle`. In SVG a presentation attribute carries the specificity of no
selector, so the class wins and the browser centres the label. The checker modelled
an alignment no renderer uses. Consequence: `the-muscle-you-stopped-using.svg` —
landed in `books/` at the Ch12 verdict on 2026-09-18, the house's first chapter end
to end — prints a quarter of its gloss off the left edge of the artboard, and the
checker said `clean`. Run against the fixed checker now:

```
$ python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg
  MARGIN  y=340.0 'no deadline, nobody watching' -44..132
$ python3 runs/design/svgcheck.py runs/ch12/plate.svg
  clean
```

That pair is a known-right answer: the landed file must flag, the repaired file must
pass. Nothing in `tests/` holds it. The same commit also stopped the checker crashing
on `max()` of an empty set — a plate with no classed `<text>`, which is what every
Part closing plate is. **A check that crashed on its own honest state, and a check
that passed the very defect it was written for, both in one file, both fixed on
inspection alone.** `FINDINGS.md` 2026-09-18 ("the checks contain the defect", "the
fixtures cannot fail") is the same shape twice over.

**2. The rasteriser dropped a fixed band off the bottom of every capture.**
`chapter_pdf_local.svg_to_png` drove Chromium with `--screenshot` and
`--window-size=W,H`; the window includes chrome the viewport does not, so roughly the
last 20% of the canvas was never captured — while the PNG's pixel dimensions stayed
exactly right. A plausible number, no error, found only by running against a known
answer. Reproduced here in a controlled file, 200x200 with a black band at y=190:

```
old path (chrome --window-size):  png 600x600,  dark px in rows 570..600 = 0
new path (Playwright viewport):   png 600x600,  dark px in rows 570..600 = 18000
```

This is instance nine of the plausible-number shape. It cost the Ch12 verdict PDF its
plate's last three lines, and it cost four separate desks the same rediscovery.

**3. Five Designer desks ran in parallel and each found 1 and 2 separately.** That is
the visible cost of a tool defect that no fixture holds: the house paid for the same
discovery five times. The fix is not a coordination mechanism between desks; it is
that neither tool should have been able to ship wrong twice.

**4. The review window the hook recorded was 2 of this session's 5 commits.**
`retro-check.sh` writes `retro-window` on every dispatch, overwriting it. Two
dispatches fired this session with no review between them (`retro-done-14cf389…` and
`retro-done-98f171f…` both exist, `runs/retro/` holds nothing for today), so the first
window — `14cf389..98f171f`, the commit containing *both* tool fixes above — was
silently discarded. This review only saw the session because the Publisher passed the
bounds by hand, which is CLAUDE.md's "never determine state by reading files and
reasoning about them" running backwards. Reproduced against a temp repo:

```
after dispatch 1: window = 0362b3a fd7ef28
after dispatch 2: window = fd7ef28 3fc9533
session really spans: 0362b3a .. 3fc9533
commits the window now covers: 1 of 2
```

The hook's own comment claims "nothing is reviewed twice and nothing is skipped".
That holds only when every dispatch produces a review. This is the #030 lineage's
third instance — the review's window silently smaller than the session — and unlike
the 2026-09-19 07:11 decision to stop hardening the *freshness* guard, this one is
mechanically decidable: the window is under-inclusive, and preserving the oldest
un-consumed START is a two-line change with an existing harness
(`tests/run.py:retro_window_cases()`) to prove it in.

**What worked, and is load-bearing.** Eight inbox items (#054–#061) from cold desks,
every one routed rather than decided, and **no cold desk wrote inside `books/`** —
with defects sitting in `books/` and the fixes in hand, Rule 8 held under exactly the
pressure it exists for. `compile.py --plates` applied Rule 15 unprompted: a plate with
no identical copy in the book tree makes the output filename say `plates-draft`, so a
reader copy cannot carry an unapproved plate unlabelled. The plate review desk found
both tool defects the right way — dark-pixel counts and `ttfwidth` measurements
against the file's own viewBox, not by reading code. Two independent desks
(review, Ch5-8) each caught the landed Ch8 Tipping Scale drawing the opposite of its
own caption. And the `count=1` → global fix on the chapter kicker was found only
because a whole manuscript ran through a path built for one chapter.

**What recurred and was assessed but not proposed.** `svgcheck.py` still lives in
`runs/design/`, an output tree, with no caller — promoted as proposal S2 by the
2026-09-16 review, never applied, and four days later it passed a defect onto a landed
plate. That proposal predates `--applied-by`; it is the exact failure that flag exists
for, and it is being re-filed below as a check with a caller rather than a move.
`grep -c` returning exit 1 on an honest zero aborted two of the Publisher's `&&`
chains before the render step ran, twice; it cost two retries, produced no wrong
output, announced itself both times, and earns no rule text.

---

## Suggestions, ranked

**S1 — new check with a caller, plus its fixture.** `land.py` copies `runs/chNN/plate.svg`
into `books/<slug>/design/plates/` with no check of any kind (lines 159-168); the only
thing it refuses is a content mismatch. Run `svgcheck.py` on the plate before the
copy and refuse a MARGIN or COLLIDE row unless `--force`, naming the row in words.
Fixture: `tests/fixtures/plate-anchor-attr.svg` (a `<text class="cap" text-anchor="start">`
whose class says `middle` — must flag) and `plate-anchor-class.svg` (the same label
anchored in its class — must pass), so the case survives #055 landing and replacing
the defective plate in `books/`. **Deletes** the 73-word comment block now carrying
the precedence rule and the empty-set note in `svgcheck.py` prose — a proof that can
be re-run replaces a comment. Cost: unmeasured until drafted; the deletion is 73 words.

**S2 — new check (fixture only).** A raster case for `svg_to_png`: a 200x200 SVG with
ink in its last 10 units, rasterised, asserting dark pixels in the bottom band. The
old path returns 0 there with identical PNG dimensions, so the case discriminates,
and it is the only assertion that would have caught this — a dimensions check would
have passed. Playwright resolves at `/opt/node22/lib/node_modules`; if the browser is
absent the case must print SKIP, never pass (Rule 12). **Deletes** the 77-word
docstring in `svg_to_png` narrating the Chromium bug.

**S3 — fix, and a corpus deletion.** `retro-check.sh` preserves the oldest
un-consumed START: advance only when a commit touching `runs/retro/` falls inside the
window. Proved in `tests/run.py:retro_window_cases()`, which already drives the real
hook against a real repo — add a second dispatch with no review between and assert
the window still starts where the first one did. **Deletes** the 115-word paragraph in
`.claude/agents/gw-retro.md` warning the Archivist how to read the window, replaced by
52 words. Net corpus **−63**.

---

## The commands

```
python3 scripts/inbox.py --add "land.py copies a chapter plate into books/ with no check at all. Should it run runs/design/svgcheck.py first and refuse a MARGIN or COLLIDE row unless --force?" \
    --raised-by gw-retro --chapter 0 --context "The Ch12 plate landed on 2026-09-18 printing a quarter of its gloss off the artboard, past two gates. The checker existed, was right about the geometry, and nothing called it at the one moment a plate becomes permanent. Promoting it was already proposed on 2026-09-16 (S2) and never applied." \
    --unblocks "Whether a plate the checker flags can reach books/ without the author saying --force, and whether svgcheck.py gains its first behavioural fixture" \
    --recommend "Yes: call it in land.py before the copy, refuse on MARGIN/COLLIDE with the row printed, --force to override, and add the two-SVG fixture pair" \
    --evidence "python3 runs/design/svgcheck.py books/the-stoic-husband/design/plates/the-muscle-you-stopped-using.svg -> 'MARGIN y=340.0 no deadline, nobody watching -44..132'; same checker on runs/ch12/plate.svg -> 'clean'; grep -n plate scripts/land.py -> lines 159-168 copy the file with no check" \
    --applied-by "python3 tests/run.py 2>&1 | grep -q 'plate anchor'"

python3 scripts/inbox.py --add "svg_to_png silently lost the bottom fifth of every plate capture while the PNG dimensions stayed correct. Should tests/run.py carry a raster fixture that counts ink in the bottom band?" \
    --raised-by gw-retro --chapter 0 --context "Four desks each rediscovered this separately today, and it cost the Ch12 verdict PDF its plate's last three lines. The fix landed on inspection with no fixture, so the next renderer change can reintroduce it silently - a dimensions check would not catch it." \
    --unblocks "Whether the rasteriser's correctness is proven by a re-runnable case or by a 77-word docstring" \
    --recommend "Yes: a 200x200 SVG with a black band at y=190, asserting dark pixels in rows 570..600 of the 3x capture, printing SKIP if the browser is absent" \
    --evidence "old path (chrome --window-size): png 600x600, dark px in rows 570..600 = 0. new path (Playwright viewport): png 600x600, dark px in rows 570..600 = 18000. Both measured 2026-09-20 16:36 on an identical source SVG." \
    --applied-by "python3 tests/run.py 2>&1 | grep -q 'bottom band'"

python3 scripts/inbox.py --add "retro-check.sh overwrites retro-window on every dispatch, so when two dispatches fire before a review runs, the earlier window is discarded. This session's recorded window was 2 of 5 commits and excluded both tool fixes. Should the hook preserve the oldest un-consumed START?" \
    --raised-by gw-retro --chapter 0 --context "Third instance of #030's shape: the review window silently smaller than the session. This review only saw the work because the Publisher passed the bounds by hand. Unlike the freshness guard the 2026-09-19 07:11 entry stopped hardening, this is mechanically decidable - advance only when a commit touching runs/retro/ falls inside the window." \
    --unblocks "Whether the Archivist's window is an oracle or a file the Publisher has to correct by hand, and whether gw-retro.md's 115-word warning paragraph can be cut to 52" \
    --recommend "Yes: preserve START until a retro file lands inside the window, prove it in the existing retro_window_cases() harness, and cut the paragraph" \
    --evidence "Two dispatches against a temp repo with no review between: after dispatch 1 window = 0362b3a fd7ef28; after dispatch 2 window = fd7ef28 3fc9533; session spans 0362b3a..3fc9533; commits covered = 1 of 2. Live: .claude/state/retro-window read '98f171f 0a0e1da' against a session of 14cf389..77b9ff7." \
    --applied-by "python3 tests/run.py 2>&1 | grep -q 'second dispatch keeps the older window start'"
```

---

## Looked at, found clean

- **Rule 8.** Zero paths under `books/` in the whole window, with two landed plates
  known defective and both fixes sitting in `runs/`. Checked by diffstat, not assumed.
- **Rule 15.** `compile.py --plates` names its own coverage (`plates-draft`) when any
  embedded plate lacks an identical copy in the book tree.
- **Rule 5.** No self-reported counts in this window to disagree with a script.
- **The inbox.** 8 new items, all with `--unblocks` answerable cold; none resolved
  silently by a cold desk.
- **`tests/run.py`.** 98/98 pass. The suite is honest about what it covers; it simply
  covers neither plate tool.
- **Corpus.** 17,062 words, zero added by this window.
- **`GAPS.md`.** The renderer gap is recorded and unchanged; nothing here belongs in it.
