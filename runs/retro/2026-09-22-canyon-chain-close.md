# Retro — does the canyon correction chain terminate? (2026-09-22 22:46)

Window: `12c7fdfa597b47003f1b7115de8d3d5a0e3f8839..272474bddd2272b255b1fc0236e5647541e8a129`
(from `.claude/state/retro-window`; one substantive commit, `5d2802e`).

Fourth Archivist dispatch on the same Part I river plate. I was asked three
direct questions and not to re-derive the void arithmetic a fifth time. I did
not. Everything below is new measurement on questions the prior three retros
did not ask.

## Q2 first, because it decides Q1: was a safe quick fix available?

**No. And the reason is sharper than "it was hard."**

The Publisher tried one tightening (a uniform per-height width-ratio bound) and
abandoned it when it failed the plate's own legitimate geometry. I tried a
different family it had not tried — monotonic convergence, which needs no
calibrated threshold at all ("a canyon may not widen as it descends"). Both the
per-step and the cumulative form.

Span between the two wall polylines, measured at each of the 20 wall vertices:

| plate | top/bottom ratio | bottom span | max step widening | max cumulative widening |
|---|---|---|---|---|
| landed (known good) | 9.5:1 | 20.2 | **2.6** | **2.6** |
| draft (the defect #087 is about) | 2.0:1 | 92.3 | **0.0** | **0.0** |
| sharp flare (retro #3's counter-example) | — | 400.0 | 38.7 | 317.6 |
| gradual flare, +1/vertex below waterline | 4.8:1 | 40.2 | 4.6 | 4.6 |
| gradual flare, +0.5/vertex | 6.4:1 | 30.2 | 3.6 | 3.6 |

The decisive row is the second. **The draft scores 0.0 on both monotonicity
metrics — perfectly converging — while the landed plate scores 2.6.** Any
monotonicity bound, at any tolerance, ranks the defective draft as *cleaner than
the plate it regressed from*. It would pass the very plate #087 exists to reject.

That is not a calibration problem, it is a category error, and it explains the
width-ratio failure too. The defect #087 names is **taper flattening** (11:1
converging becomes 2:1 near-parallel). Flattening is still monotonic narrowing.
Every bound of the form "do not open up" — width ratio, per-step delta,
cumulative delta — measures *widening*, and is blind to flattening by
construction. The gradual-flare rows show the same thing from the other side: a
flare tuned to merely cancel the natural taper doubles the bottom span (20.2 to
40.2) while producing a 4.6 signal, against a legitimate plate's 2.6.

Resampling the r2 generator's own jitter (`rnd.uniform(-1.5, 1.5)` per wall per
vertex) across 2000 seeds puts the legitimate noise ceiling at 1.83 (median
0.00), so a window does exist between noise and the gradual flare — but it is
1.8x wide, calibrated against one observed plate whose jitter the current
generator cannot even reproduce (seed 11 resamples to 0.00, the landed file
measures 2.6), and it still does not catch the draft.

**Verdict: stopping the patch cycle was correct.** Two independent families of
quick fix fail, and the second fails in a way that proves no member of the
family can work. The rule this yields is not "try harder next time" but: *when a
proof has been patched twice and the third patch is a threshold rather than a
measurement of the thing the item actually names, stop and build the check.*

## Q1: would #090, built as recommended, close retro #3's hole?

Its proof is honestly red today — I ran it verbatim from the item's frontmatter:

```
landed: None  flared-to-400-units: None
EXIT=1
```

Red for the right reason: `plate_check.rows(part=1)` emits nine rows and none is
`canyon`. It is a genuine discrimination test (landed must be `ok`, mutant must
not), not a grep and not a tautology. The four substantive clauses of the
recommendation — derive the waterline from the file, assert the walls rather
than indexing them, measure by ink density, sample the full wall range — are
each correct and each addresses a real defect in the retired one-shot script.
**The recommendation's substance is sound. I looked for a flaw in it and did not
find one.**

The hole is not in the recommendation. It is in the **close condition**, and
there are two, both cheap because they are pre-build.

**(a) The proof admits an implementation that passes the original defect.**
`applied_by` requires only that the canyon row fail the *sharp* flare — 400
units, wildly non-monotonic, the easiest possible mutant. A canyon row
implemented as a monotonicity check satisfies #090's proof exactly and, per the
table above, scores the draft at 0.0 and calls it `ok`. #090 would then close
green while `runs/parts/plate-1-steady-river.svg` — the plate the entire chain
is about — passes. That is the sixth-instance shape #090 itself names, reproduced
in the item written to end it. The fix is one assertion, and the fixture is a
file that already exists on disk.

**(b) The proof only exercises `part=1`; the row is proposed "under `--part`".**
There are five part plates and two have landed. Polyline counts:

```
books/.../plate-1-steady-river.svg   polylines=3   paths=0
books/.../plate-2-sturdy-oak.svg     polylines=0   paths=30
runs/parts/plate-3-warm-sun.svg      polylines=42  paths=0
runs/parts/plate-4-fall-to-winter.svg polylines=24 paths=0
runs/parts/plate-5-spring-to-summer.svg polylines=22 paths=0
```

Plate 2 has **zero** polylines, so "the two widest polylines are the walls" has
nothing to assert on. Plate 3 has 42, none of them canyon walls. #090's proof
says nothing about what the row does on any of them. An implementation that
returns `ok` when it cannot identify walls passes #090 and vacuously green-lights
four plates — Rule 4's "a gate that cannot see is not a gate," which is how this
lineage started.

Neither is a reason to reopen the measurement. Both are amendments to a proof on
an item that has not been built yet, which is the cheapest moment they will ever
be available.

## Q3: is #087 still usable?

Barely, and it is the one thing here I would not leave alone.

`wc -w` on the open inbox: **#087 is 1025 words against a median open item of
229 and a previous maximum it now sets.** It carries three dated corrections; its
headline claim was filed, retracted, re-signed with the opposite sign, and then
gated; and its `applied_by` is documented in its own body as insufficient to
close it. The author is asked to rule on "redraw keeping the landed taper?" — a
one-line design question — after reading four paragraphs about which band was
measured.

It is not wrong and nothing in it should be deleted: the correction history is
the evidence that the numbers are now trustworthy. But the *ruling* and the
*forensics* are now the same document, and the ruling is underneath. This is
Rule 18 ("lead with what he must decide") applied to an inbox item rather than a
reply. I did not restructure it — rewriting another desk's filed item is not
mine to do, and the corrections are load-bearing.

## What worked

- Refusing the fourth one-shot patch. The evidence above says a fourth patch
  would have shipped a check that passes the original defect.
- Documenting the blind spot *inside* #087 rather than silently replacing the
  script. Retro #3's finding survived into the record where the next reader hits it.
- Surfacing the ink-density-vs-raw-area judgment. The sign of the headline number
  rested on an unstated choice; naming it is what let me test the taper claim
  independently of the void claim.
- `plate_check.rows()` being importable with a path argument. Every measurement in
  this review, and #090's own proof, is possible only because of that shape.

## Looked at and found clean

- #090's proof: re-run verbatim, red, red for the stated reason.
- The void arithmetic: not re-derived, per instruction. Nothing I measured
  contradicts it.
- #089: closed correctly in `b3b8aa5`; its replacement proof is not a tautology.
- `tests/run.py`: 107/107 as reported.
- Corpus 18,540 words (`CLAUDE.md` + agents + skills). Up from 17,017 on
  2026-09-19, but not from this window — `5d2802e` touches only `inbox/` and
  `runs/retro/`. Flagged for the next count, not charged here.
- `runs/log.md`, `.claude/state/retro-window`: window bounds correct and
  non-empty, the #030/#033 failure did not recur.
