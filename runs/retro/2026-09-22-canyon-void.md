# Archivist — the canyon void re-verification

**Window:** `8c2c26c78c2d15e63e036bdd1fb04e5930e3b03a..5b2ca55fdf4c9c703bb87007ab7882eac7559aaf`
(read from `.claude/state/retro-window`, not reconstructed)
**Reviewed:** 2026-09-22 22:24
**Commits:** `f1ffc1e` (the re-verification and four inbox writes), `c78a64b`
(the prior retro doc), `5b2ca55` (session log).
**Corpus:** 18,540 words. Nothing proposed here adds to it.

---

## 1. The re-verification is real. The band it inherited is not.

*Lens: what worked, then what broke underneath it.*

**The number is confirmed, by a method that shares no code with it.** The filed
proof rasterises at scale 2 and walks pixels. I integrated the wall polylines
straight out of the SVG — no rasteriser, no threshold, no seed pixel:

```
                        raster scan      geometric integral
draft  void 190-400        32033.0                 32117.1
landed void 190-400        29444.5                 29572.5
ratio                       1.0879                  1.0861
```

0.3% apart on two independent paths. The 8.8% is not a shared bug. I also
instrumented the filed scan for its one silent failure mode — `if d(x,y):
continue`, which contributes zero for any row whose centre pixel is dark and
says nothing — and it fired on **no rows** in either plate. And the band is not
cherry-picked: moving its floor from y=390 to y=405 moves the ratio only
1.074 → 1.093.

**On the worry that a single column at x=300 mismeasures a non-vertical wall:
it does not, and that is a misreading of the code.** x=300 is a *seed*. Each row
expands left and right from it to the first dark pixel and adds that horizontal
span. Summing spans over rows is an area integral by Cavalieri; slanted walls are
handled exactly, which is why my geometric integral agrees. The seed only selects
*which* white region, not how it is measured.

**What neither run checked is the band's denominator.** `190..400` is "above the
waterline." The draft has a waterline at y=405. **The landed plate has none** —
its single wave sits at y≈650, below the drawing box floor at y=640. So the band
is defined by a feature that exists in one of the two artifacts. Measured instead
to each plate's own waterline, over the whole drawing box:

```
empty white, draft  190 -> 405 (its waterline)      32764.1
empty white, landed 190 -> 640 (box floor; no water inside the canyon at all)
                                                     39852.0
draft empty white is 82.2% of landed  ->  it SHRANK 17.8%
```

And the lower canyon is not white in the draft. Ink density inside the canyon
walls, y 405-640:

```
draft  canyon interior   9.09% ink      draft  rock field  3.83%
landed canyon interior   0.00% ink      landed rock field  3.84%
```

The draft's channel carries **2.4x the ink of the rock around it**. The landed
plate's carries literally none, across ~10,280 square units.

So the desk's claim — "the cut is a channel with the water running in it rather
than an empty notch" — is true, and measurable, and #087 currently tells the
author the opposite: *"the redraw was meant to remove the empty wedge, but
measured, the open white above the waterline is 9% larger, not smaller."* True of
the band. False of the plate.

**The taper defect is real and survives all of this.** 11:1 converging to 2:1
near-parallel is a genuine shape regression and was correctly seen. It just is
not the same claim as "the void grew," and the number attached to the headline
argues against the whole-plate measurement.

**The shape.** FINDINGS 2026-09-19 07:03: *"the mechanism was sound and only the
binding was missing."* Same here. The measurement was sound; what was unbound was
the comparison window. Two independent derivations agreeing confirms arithmetic
and cannot confirm a denominator, because the second run re-derived the *method*,
which is where the band lives. Cross-session re-verification is a real guard
against fabrication and no guard at all against a shared frame.

## 2. #087's recommendation is a ten-line edit. Built and measured, not guessed.

*Lens: what was too hard — it was not.*

`runs/parts/gen-plate-1-r2.py` is the source; the SVG is output. Both walls are
20-point polylines built from one function, and the strata lines and every water
wave derive from those same two lists. So "keep the landed taper above the
waterline and widen only below it" is one function body, not a redraw.

Replaced `halfwidth()` with a piecewise version — the landed plate's ten
half-widths above y=403.2, a gentle widening below — in a scratchpad copy,
regenerated, measured:

```
void above waterline (190-400):
   landed    29572.5   (+0.0%)
   draft     32117.1   (+8.6%)
   variant   29387.6   (-0.6%)

span by height:      y=300   y=350   y=375   y=400
   landed            136.8   110.5    99.2    84.4
   draft             149.3   139.1   133.9   129.8
   variant           135.7   110.4    98.7    84.4
```

The converging taper is restored to within a unit at every height, the void lands
*below* the landed plate's, and the river still fills the channel below the
waterline. `plate_check.py --part 1` on the variant: all nine rows ok, exit 0.

It is achievable, it is cheap, and #087's own proof command goes green on it.

## 3. #089 closes on the presence of a row, not on the row working

*Lens: what recurs.*

#089's proof is:

```
git show 3a7ac88:books/.../plate-1-steady-river.svg > /tmp/p1.svg \
  && python3 scripts/plate_check.py /tmp/p1.svg --part 1 | grep -qE '\[[^]]+\]\s+title\s'
```

`[[^]]+]` matches `[ ok ]` and `[FAIL]` equally, and it runs against the
**title-less landed plate**. A `title` row that prints `[ ok ]` on a plate with no
title at all closes this green. That is the ledger's own named half-fix — FINDINGS
records a check that passed the very defect it was written for, and the standing
instruction is that a proposal adding a check closes on a fixture, never on a grep
for the check's own output. This one greps for its own output.

Cheap correction: point it at a plate whose `.ttl` does not match its Part page
heading and require exit 1.

## 4. Sizing the four writes

- **#087 — real defect, wrong headline.** The taper finding stands; the void claim
  reverses on the whole plate. Re-aim it (§1). Its proof executes and is honestly
  red (exit 1 confirmed). One soft spot: it closes on `draft <= landed` in the
  band, so copying the landed file back over the draft also closes it green — an
  acceptable outcome of the question as asked, so recorded, not filed.
- **#088 — correctly sized, keep as written.** A real caller gap, names its
  overlap with #062 itself, and its proof runs `compile.py` and counts verdict
  lines. Executes, red, asserts behaviour. Nothing to change.
- **#089 — correctly sized, wrong proof.** See §3. Adjacent to #065 (chapter plate
  titles = the distillation's Mechanism); the `--part` title row and the
  `--chapter` title row are the same row, so #065 is worth naming inside it. Not a
  duplicate.
- **#076 and #085 evidence appendices — correct calls.** `oak.png` and `river.png`
  are unstamped regenerable renders of SVGs still under revision: #076's shape
  exactly, in a second directory. "Renders correctly here" plus a named mechanism
  (SVG re-serialisation) that appears nowhere in `scripts/` is #085's shape
  exactly. Both belong as evidence, not as new items. Verified independently.
- No duplication against #048, #060, #062, #065, #070-#086.

## 5. Recorded, not filed

Nothing in this repo can compare two plates. Every plate-to-plate comparison so
far has been a throwaway `python3 -c` pasted into an inbox item, which is how the
same hand-rolled band got invented twice and questioned zero times. A
`plate_check --against <svg>` row would fix the class. I have not drafted it, it
names no deletion, and the inbox already carries 43 open items — so it is an
observation here, not a forty-fourth.

---

## Looked at and found clean

- Window bounds read from `.claude/state/retro-window`; the pair matched the three
  commits reviewed.
- Nothing under `books/` touched anywhere in the window. `git diff --stat` empty.
- Corpus 18,540 words, unchanged; nothing proposed here adds to it.
- All three filed proofs (#087, #088, #089) execute and exit 1 today. No
  tautologies, none touches `tests/run.py`, so #080's freshness gate is not
  implicated.
- The raster scan's silent-row-drop path instrumented: zero rows dropped in either
  plate. The number is clean.
- Band sensitivity swept y=390..405: ratio stable 1.074-1.093. Not cherry-picked.
- Both generators still reproduce their committed SVGs; `git status runs/parts/`
  clean.
