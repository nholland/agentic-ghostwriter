# Archivist — the correction of the correction

**Window:** `5b2ca55fdf4c9c703bb87007ab7882eac7559aaf..12c7fdfa597b47003f1b7115de8d3d5a0e3f8839`
(from `.claude/state/retro-window`)
**Reviewed:** 2026-09-22 22:36
**Substantive commit:** `b3b8aa5` — corrects #087 and #089.
**Corpus:** 18,540 words. Nothing proposed here adds to it.

---

## 1. The correction is right. I reproduced it on a fourth method.

Read both SVGs directly, integrated the wall polylines by fine trapezoid
(20,000 steps) rather than by per-scanline sum — no shared code with the raster
scan, the Archivist's integral, or the Publisher's polyline sum:

```
EACH TO ITS OWN EXTENT (the corrected definition)
  draft  void 190->405 = 32764.1
  landed void 190->640 = 39852.0
  draft/landed = 82.2%  (change -17.8%)
TAPER  span(300)/span(400)
  draft  span300=149.3 span400=129.8 ratio=1.150
  landed span300=136.8 span400=84.4  ratio=1.620
```

Exact agreement to the tenth with what `b3b8aa5` filed.

**The landed plate really has no water above the box floor.** Not inferred —
counted. It holds three polylines total: two walls (y=190..640) and one wave at
y=647.8..652.2. The draft holds eighteen: two walls and sixteen wave rows from
y=402.0 to y=632.2. The band `190..400` therefore did fit one artifact and not
the other, exactly as the correction says.

**One thing the correction rests on that it never argued, and that holds.** The
whole sign of the result depends on treating the draft's watered canyon as
*filled* rather than as 91% white pixels. Weight the lower canyon by its own ink
fraction instead and the draft's white goes to **+41.2%** against the landed
plate — a third number, a third sign, from the same correct arithmetic. So the
band was never the only judgment in play; "textured means not void" is the other
one, and it was silent. It happens to be defensible, and I checked why: the
water strokes sit at **9.33% ink density against the rock stripes' 4.65%**. The
water is twice as dense as the rock it runs between. A region denser than the
rock does not read as empty white. The correction stands — but it stands on that
ratio, not on the band, and nothing in #087 says so.

## 2. The replacement proof for #087 closes green on a catastrophic plate

This is the finding. #087's new `applied_by` asserts two things:
`void(draft,190,405) <= void(landed,190,640)` and `span(300)/span(400) >= 1.5`.
Both samples are **above y=405**. The item's own headline complains that *"below
y~290 the draft canyon is wider than the landed one at every height."* The proof
never looks below the waterline.

Built the half-fix that follows #087's own recommendation literally — "keep the
landed taper above the waterline and widen only below it" — and overdid the
widening:

```
span at y=640: half-fix 400.0   landed 20.2   (page 600 wide, box 90..510)
left wall exits at x=100.0, right at x=500.0

=== #087 proof against the over-widened half-fix ===
void: draft=29988.8 landed=39852.0 not_grown=True
taper: span300=136.8 span400=84.4 ratio=1.62 converges=True
exit 0   <-- the item CLOSES GREEN
```

A plate whose canyon flares to twenty times the landed width and runs its walls
to the drawing-box margins — the "gap opening between two sides" the redraw was
commissioned to kill, in its purest form — satisfies both assertions and closes
#087 as applied. (A first mutant that kept the draft's 1.15 taper was correctly
caught; the taper row does work. It is the unwatched region below it that does
not.)

**The shape.** FINDINGS already records five instances: #030's grep,
`voice_rules_check` passing its own defect, the dedup half-fix, the fixture
written for that half-fix, the unproven proof-of-proof. This is the sixth — and
it was introduced in the same commit that removed the fifth-shaped defect from
#089. The Archivist diagnosed "a check that closes green on a check that never
fires" in #089 and wrote one for #087 four lines later.

**Two smaller faults in the same proof.** `405` is a hardcoded magic number, not
derived from the file, so any redraw that moves the waterline silently
mismeasures; and the walls are taken by polyline *index* (`wp(p,0)`, `wp(p,1)`)
with no assertion that what was grabbed is a wall, so a decorative polyline
added above them produces confident garbage rather than an error.

## 3. What is actually missing: the measurement has no home

Three bespoke measurement scripts have now been written for this one plate — a
raster scanline scan, a geometric integral, a wall-polyline integral — and none
of them landed anywhere runnable. `plate_check.py` reports nine rows on this
file (`charset, geometry, anchor-attr, em-dash, digits, canvas, captions,
alignment, ink`) and not one of them can see a canyon. The only surviving copy
of the measurement is a 25-line string inside an inbox item's YAML, and it is
deleted the moment the item closes.

That is why the blind spot in §2 is structural rather than careless. A proof
written once, to close one item, is optimised to be red today — not to be right
about every plate. A row in `plate_check` with a fixture is optimised to be
right, because the next plate runs through it.

## 4. Is hand-editing an open inbox item good practice? Mostly yes, with one gap.

Asked directly, so answered plainly: **the evidence correcting itself before it
reaches the author is the mechanism working, and it should keep working that
way.** The alternative — filing #090 "actually #087 was wrong" — is how the old
ledger went from 739 to 6,026 words. Preserving the original numbers under a
dated Correction rather than deleting them is the right call, and matches what
`runs/ch04/plate-notes.md` did earlier in the day.

The erosion worry does not survive the record. #087 has had exactly **two**
committed headlines, not three (`f1ffc1e`, then `b3b8aa5`); the third statement
was in chat, which is not the ledger. Two states, both readable, the superseded
one still on the page.

The real gap is narrower and mechanical: `inbox.py` has `--add` and `--close`
and nothing else, so the amendment was a hand edit of YAML frontmatter with no
uniqueness assertion (Rule 11) and no re-validation that the new `applied_by`
still parses the way `inbox.py` parses it. The Publisher did extract and run
both proofs before committing — the right discipline — but that discipline was
prose, not mechanism, and §2 shows what prose-level discipline catches and what
it misses: it confirmed both proofs *execute*, which they do, and could not
confirm either one *discriminates*. I am not proposing `--amend`. An undrafted
command is unmeasured, and the failure it would have caught is the one §2's
fixture catches anyway.

## 5. #089's proof: sound in shape, with one unstated assumption

The mutation proof is correctly built against the implementation's idiom — the
title row is `WARN`-not-`FAIL` until #065 ratifies it (`LEVELS = {"title":
"WARN", ...}` in `plate_check.py`), and the proof's `sb not in (None,'ok')`
tolerates that. Verified red today for the stated reason: no title row fires
under `--part`, both copies read `None`.

One caveat. The proof's "matching" title is `THE STEADY RIVER`. The Part page's
actual H1 is `# PART I — THE STEADY RIVER`. So the proof quietly requires the
future title row to strip the `PART I — ` prefix before comparing. If whoever
implements it compares the full H1, a correct fix leaves #089 red forever. This
fails safe (the item stays open rather than closing wrongly), and the fix is one
clause in the Recommendation line, not an item.

## 6. What worked

- **The re-review caught a real error in its own house's work, and the Publisher
  did not take it on faith** — a third derivation, from raw geometry, sharing no
  code with either prior method. That is why my fourth method agreed to the
  tenth rather than inheriting a mistake.
- **Preserving superseded numbers under a dated Correction** rather than
  rewriting them. Both #087 and #089 remain auditable; I reconstructed the whole
  sequence from the files without reading a single commit message.
- **The taper row in #087's proof genuinely discriminates.** My first mutant was
  designed to slip past and did not. Threshold 1.5 is not arbitrary — it
  separates 1.150 from 1.620 — though the headroom is asymmetric: only 8% below
  the one known-good sample, so an honest redraw landing at 1.45 fails. Worth
  knowing; not worth an item until it happens.
- **It cannot be run against the landed plate by mistake**, which was the worry
  raised. Both paths are hardcoded and the taper is always read from the draft.

## 7. Looked at and found clean

- `12c7fdf` is the Stop hook's session log. No content.
- 107/107 fixtures pass, confirmed by the commit and unchanged by anything here.
- No `books/` path was written this window. Rule 8 intact.
- Corpus 18,540 words, unchanged by `b3b8aa5` — the commit touched only `inbox/`
  and `runs/retro/`.
- Both corrected `applied_by` strings parse and execute, and both exit 1 today,
  as the commit message claims. Re-ran both; reproduced.
- No open item re-filed. #048, #060, #062, #065, #070–#089 left alone.

## 8. What a human still has to look at

The fixture in §2 cannot see whether the plate is *good*, only whether the
canyon reopened. A narrow hairline crack — span 30 at y=300, 15 at y=400 —
satisfies a small void and a 2.0 taper and is not a canyon either. Geometry can
bound the defect; it cannot certify the drawing. Someone has to render
`runs/parts/plate-1-steady-river.svg` and look at it before it lands.
