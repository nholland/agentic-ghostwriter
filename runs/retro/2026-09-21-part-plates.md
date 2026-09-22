# Archivist — Part I and Part II plate drafts

**Window:** `cbcaaf32a13733ca0f3544f899f2d7cfe6e15e72..3a7ac886ad07614b727233b341ef230255798d9e`
(read from `.claude/state/retro-window`; `496d4bb` confirmed an ancestor of the
window start and therefore outside it)
**Reviewed:** 2026-09-21 12:53
**Commits:** `a2d90c0` (in-flight generators and variants), `ecb6285` (the plate
drafts), `29a5acf` (the prior Archivist's output), three session logs.
**Corpus:** 18,540 words. Nothing proposed here adds to it.

---

## 1. The canyon's empty wedge did not shrink. Measured, it grew 9%.

*Lens: what broke, and the window's own named error shape.*

The desk's note says the canyon "is a channel with the river running in it
rather than an empty notch," and the Publisher's summary carried it forward as
"the river now fills the canyon rather than leaving an empty wedge." Neither
measured it.

Rasterised both plates at scale 2 and integrated the open white span across the
canyon, row by row, from the top of the drawing box to the waterline — the band
that is genuinely empty in both files:

```
draft void 32033.0 landed void 29444.5
```

The void above the waterline is **9% larger in the draft than in the landed
plate it replaces.** Filling the lower canyon worked; what paid for it was the
profile. The desk's own note records the reshape — half-width 96 at the top
falling to 46 at the floor on a 0.62 exponent — and that reshape widened the
mid-section. Span across the canyon at x=300, in viewBox units:

```
y=    300    350    375    400    425
landed 135.5  109.0   98.0   83.0   66.0
draft  148.0  138.0  132.5  129.0  125.5
```

The landed plate tapers 191.5 → 17.5, about 10.9:1, and the eye follows it to a
point: a cut. The draft tapers 182.5 → 93.5, about 2:1, a near-parallel-sided
slot. Below y≈290 the draft's void is wider than the landed plate's at every
height. A parallel white slot between two striped blocks is closer to "a gap
opening between two sides" — the fault the desk set out to repair — than the
converging wedge was.

The water itself is sound: the 15px pitch against the rock's 23.7px does read as
a different substance, the surface line does join the two walls, and the water
does run off the bottom edge. The instruction was half-executed and reported as
whole.

## 2. The clipPath escalation names a mechanism this pipeline does not have, and its reassurance was never run

*Lens: what broke; what recurs — this is open #085's shape, second instance, same
desk, same session.*

The desk wrote: *"`chapter_pdf.py` renders it correctly here, but if any
downstream tool flattens or re-serialises the SVG, that is the one feature that
could be dropped."* Three separate problems.

**It cannot have rendered it.** `compile.py:part_plate()` returns the landed book
file whenever one exists and only falls back to `runs/parts/` when it does not.
Parts I and II are landed. Run:

```
$ python3 scripts/compile.py --from 1 --to 4 --plates --no-pdf
  plates: 5 embedded (1 landed, 4 draft); missing: none
    PART I (after ch04; Part incomplete) landed books/the-stoic-husband/parts/plate-1-steady-river.svg
```

The compile path reaches the **landed** plate — no clipPath, no title. The draft
is unreachable by it. The newest packet agrees: `runs/manuscript/the-stoic-
husband-plate-feedback-packet-ch01-ch12-2026-09-21-1250.html` contains 0
occurrences of `clipPath` and no Part-plate reference at all.

**The named mechanism does not exist here.** No `ElementTree`, `lxml`, `minidom`
or `BeautifulSoup` appears anywhere in `scripts/*.py`. `compile.py` embeds plates
as `<img src="...svg">` and never parses them. Nothing in this repo re-serialises
SVG. The real exposure is a renderer, not a re-serialiser: `chapter_pdf.py:346`
hands the page to WeasyPrint, whose own SVG engine is the one component that
might not honour `clip-path` — and WeasyPrint is not installed in this container,
so no one has tested it.

**The consequence is worse than "restores the cut log."** Stripped the
`clip-path` attribute and rendered. The rings bleed across the whole page and
strike through the title and both caption lines. It is an unreadable page, not a
worse reading.

## 3. What worked, and the one row that read clean over it

*Lens: what worked.*

`plate_check.py` catches the clip drop:

```
$ python3 scripts/plate_check.py <clip stripped> --part 2
  [FAIL] ink         rendered ink inside the 60px margin bands: left=9832, right=10681
EXIT=1
```

That is a real guard doing real work on a defect nobody had drawn yet, and it is
load-bearing. Name it before anything simplifies it away.

In the same run, `geometry` reported `no margin or collision rows` on a page with
ink drawn through three lines of type. That is by construction: `geometry()`
compares text boxes only to other text boxes (`for i, a in enumerate(bx): for c
in bx[i+1:]`). There is no ink-versus-text row. The `ink` row caught this
instance only because the bleed also breached the margin; a clip drop that stayed
inside the margins would strike the type and pass all nine rows. Recorded, not
filed — it is contingent on a clip drop, and the caller gap below is the cheaper
fix.

**The structural gap is a caller, not a check.** `plate_check` only ever runs on a
source SVG a human names. Nothing runs it on the file `compile.py` selected, and
`compile.py` already knows which file that is — it collects
`plates.append((label, svg, landed))` and prints the list. Same shape as open
`#062` one door over (`land.py` copies a chapter plate into `books/` with no
check at all).

Also worked: both drafts clear the `anchor-attr` WARN and the `0 italic lines`
reading that both landed plates still carry. Verified independently on all four
files. The `<style>` block did what the desk said it did.

## 4. The desk's recommended home for the new sentence breaks a rule in the file it was citing

*Lens: what was missing.*

The desk checked its proposed sentence against two of `parts/README.md`'s hard
rules — marriage vocabulary and caption-verbatim — and concluded the Part I page
is "the natural home... the caption rule stands unbroken." It did not check the
third, four bullets above the one it quoted: **"Length: 62-66 words. All five sit
in that band on purpose."**

```
62  part-1-steady-river.md      62  part-2-sturdy-oak.md      66  part-3-warm-sun.md
63  part-4-fall-to-winter.md    66  part-5-spring-to-summer.md
```

Part I sits at 62, the floor of the band. "The canyon is not the damage. It is
what the ordinary days built." is 12 words, putting the page at 74. The desk's
preferred resolution is unexecutable as written; the sentence would have to
replace text, not append to it.

## 5. The corpus claim is confirmed — and this is the opposite of last window's shape

*Lens: what worked.*

Verified independently. `canyon` appears 6 times under `books/`, but only once in
reader-facing prose: Part I's last sentence, duplicated into `manuscript.md:180`.
The other four are apparatus — `parts/README.md:57` and `progress.md` ×3. The
desk's "exactly one place in the whole corpus, the Part I page's last sentence,
which is already the caption" is right about everything that matters.

I also searched the *concept* rather than the word, since that is where a missed
source would hide. "ordinary day(s)" appears at `manuscript.md:60` and `:156`;
neither ties the canyon to anything the marriage gained. There is no sourceable
phrase the desk missed. **The desk searched what it held instead of reaching for
what it remembered, and then declined to invent.** That is the correction to last
window's finding actually working, and it should be recorded as such.

One flaw in the justification, same shape as §2: the desk cited *"Ch23's 'The
Marriage You Build Every Day'"*. It is **Chapter 24** (`03-outline.md:456`);
Chapter 23 is "The Difference Between Endurance and Cowardice" (`:434`). Ch24 is
also unwritten — the manuscript runs Prologue–Ch12 — so that half of the evidence
is an outline title, not prose. The other half, Part V's "Stand in the summer you
built," is solid and reader-facing, and carries the point on its own.

## 6. Sizing the three escalations

1. **Title vs README — correctly sized, and a genuine blocker.** The "Form rules"
   list has no line permitting a title, and the caption rule says the plate
   "reprints the book's own words; it adds none." Both drafts now carry a third
   text element the contract does not describe. Needs the author's word before
   either lands.
2. **Parts III–V titles — oversized as stated, and overlaps an open item.** None
   of plates 3, 4 or 5 is landed in `books/`; all three are drafts in
   `runs/parts/`. The furniture stops at Part II in the book whether or not the
   drafts get titles, so titles are the smaller half of that problem. `#060` is
   already open on Part plates III–V. Evidence there, not a new item.
3. **clipPath — correctly raised, wrongly aimed, understated.** See §2.

## 7. The committed scaffolding was right, and only the rasters match #076

*Lens: what worked.*

Re-ran both generators. Each reproduces its committed SVG byte for byte:

```
plate1 reproducible:  IDENTICAL
plate2 reproducible:  IDENTICAL
(git status --short runs/parts/ : clean)
```

The generator is the source and the SVG is the output, so committing them mid-
flight in an ephemeral container was correct, and they are re-readable in the
only sense that matters — they run. The A/B variants were **deleted** in the same
window (`p1-smooth.svg`, `p1-stepped.svg`, −144 lines). That is a tidy round, not
accumulation.

The two rasters are a different matter. `oak.png` (278 KB) and `river.png`
(79 KB) are unstamped regenerable output whose names will silently misrepresent
their contents the moment a generator is re-run — `#076`'s shape, now in a second
directory. Evidence for `#076`, not a new item.

---

## Looked at and found clean

- Window bounds read from the state file, not reconstructed; `496d4bb` checked
  with `git merge-base --is-ancestor` and confirmed outside.
- Nothing under `books/` was touched by `ecb6285`. Confirmed against the diffstat.
- `plate_check --part 1` and `--part 2` on both drafts: all nine rows ok, exit 0.
  The Publisher's report of this was accurate.
- Both captions verbatim against their Part pages; both titles verbatim against
  the Part page headings.
- No marriage vocabulary in either draft or in the proposed sentence.
- Corpus 18,540 words, unchanged by anything proposed here.
