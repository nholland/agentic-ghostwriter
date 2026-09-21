# Archivist review — 2026-09-21 01:05

**Window:** `f4f693c..6382166` (from `.claude/state/retro-window`), 2 commits:
`83bede5` (plate feedback packet) and `6382166` (Stop-hook session log).
Two further commits — `1543f17`, `84b7996` — landed after the hook dispatched
and are outside the reviewed window; that is #064/#071's known shape, not a
new finding.

## What happened

`scripts/plate_packet.py` (231 lines) built a new artifact: 14 plates, each on
its own page, each followed by its intent and takeaway. It reuses `compile.py`'s
plate discovery and `chapter_pdf_local.py`'s rasteriser **by import**, reads
per-plate text straight from each chapter's `distillation.md`, and invents
nothing — Ch5's page reproduces the open #070 mismatch verbatim rather than
reconciling it. 107/107 fixtures pass; nothing under `books/` was touched.

## Lens: what worked — name it before anything deletes it

**Two things, both load-bearing.**

1. The Stop hook's `DERIVED` drift block (`.claude/hooks/session-stop.sh:67-77`)
   flagged `docs/manual.html` as stale the moment a new script landed, and that
   produced a real same-session repair (`1543f17`), including a docstring reflow
   that had wrapped mid-sentence into the manual's scripts table. A check with a
   caller, catching a class of staleness nobody would have thought to look for.

2. `plate_packet.py` imports `compile.chapter_plate/part_plate/parts` and
   `chapter_pdf_local.svg_to_png/md_inline/CHROME/FLAGS` rather than copying
   them. That is the *answer* to the problem #073 is open about — two renderers
   kept in parity by hand, the parity claim unverifiable when made. This session
   shows the cheaper fix is import, not a parity fixture. Worth saying inside
   #073 rather than filing again.

## Lens: what recurs — Rule 15, third occurrence, now materialised

Rule 15 exists because three files in the book repo "each looked current." The
same shape is now live in `runs/manuscript/`, and it is not the
commit-the-PNGs-or-not inconsistency it looks like.

Measured:

```
$ md5sum runs/manuscript/*.png | sort | awk '{a[$1]=a[$1]" "$2} END{...}'
ch01-plate.png == packet-ch01.png      (all 14 pairs byte-identical)
...
duplicate PNG files (same bytes, different name): 14
$ du -ch runs/manuscript/packet-*.png | tail -1
1.9M    total          # of 3.8M tracked PNG in that directory
```

```
$ for f in runs/manuscript/*plates-draft*.html; do grep -o 'src="[^"]*\.png"' "$f" | md5sum; done
798c330df56f28b71ffd8b607b457b70  -   (x4 — four stamped HTMLs, one PNG set)
```

Four HTML files carry a clock in their names per Rule 15 (`...-1952.html`,
`...-2200.html`, `...-2330.html`, and round 1's). All four reference the same
**unstamped** raster names, which each compile overwrites: `eb3da38` wrote them,
`1be88a2` rewrote them, `c5690af` rewrote `ch07/08/09/12-plate.png` again after
the Ch8 and Ch12 redraws. So round 1's committed HTML, opened today, renders
round 3's plates while its sibling PDF embeds round 1's. The stamp in the
filename is now a claim the file cannot keep — Rule 15's exact failure, in a
directory Rule 15 was written to protect.

`plate_packet.py` inherited it and worked around it: it chose a `packet-`
prefix specifically so it would not clobber `compile.py`'s set, which is why
14 byte-identical duplicates exist. The workaround is the tell.

The PDFs are unaffected — Chrome embeds the images — which is what bounds the
severity and what suggests the fix. The PDF is the artifact that circulates;
the HTML and the PNGs are regenerable intermediates that currently lie.

## Lens: what was missing — a dated source hard-coded as if it were current

`plate_packet.py:45` pins the plate titles to one dated file:

```python
NAMES_DOC = os.path.join(REPO, "runs", "design",
                          "2026-09-20-plate-names-and-visual-summaries.md")
```

and `main()` falls back silently when a chapter is not in it:

```python
title = names.get("ch%02d" % n, "Chapter %d" % n)
```

Today every chapter resolves (verified: 12/12 titles, 12/12 Mechanism,
Conversation and Lesson fields non-empty), so this is latent, not live. But
#065, #069 and #070 are all open proposals to *retitle or redraw* plates. The
next naming pass produces a new dated file beside the old one; the old one still
exists and still parses, so `plate_packet.py` keeps using yesterday's titles and
says nothing. A missing plate prints `MISSING:`; a missing *title* prints a
packet page headed "Chapter 5". The packet is the one artifact built to go to
strangers.

`curated_names()` also already carries one scar from this document's shape —
Ch5's extra italic naming-note paragraph broke a first parse, fixed by taking
each section's last non-blank line as the tag. That heuristic is unproven by
any stored fixture, and `tests/run.py`'s own docstring is the standard it
misses: *"A check whose escape is not in this directory has not been proved;
it has been asserted."*

## Lens: what was too hard

Nothing this session. The script is a script, not a checklist; it ran once and
produced the artifact.

## Assessed and not filed

- `part_takeaway()`'s docstring promises `(opening paragraph, closing caption)`
  and returns a string. Cosmetic; costs nobody anything.
- `plate_packet.py` stamps with `datetime.utcnow()`; `compile.py:209` uses
  `datetime.now()`. Identical here (TZ is UTC) and a one-line divergence
  elsewhere. Not worth an item.
- No fixture for `plate_packet.py` — but #048 is open precisely because
  `tests/prove.py` cannot prove a fixture for a *new* file. This session is
  #048's second concrete instance, not a new finding. It belongs in #048's
  evidence, not in a new item.

## Corpus

18,540 words (`cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w`),
up from 17,017 on 2026-09-19. Neither proposal below adds a corpus word; one
deletes 3.8M of tracked bytes.

## Proposals

Two. Both are **new check with a caller** / **deletion**; neither adds a corpus
word. I apply nothing.

### A — the dated titles document, pinned as if it were current

```
python3 scripts/inbox.py --add "plate_packet.py pins plate titles to one hard-coded dated file (runs/design/2026-09-20-plate-names-and-visual-summaries.md) and falls back silently to 'Chapter N' for any chapter missing from it. Should curated_names() take the newest runs/design/*-plate-names-and-visual-summaries.md and refuse a silent fallback, proved by a two-dated-docs fixture?" \
    --raised-by gw-retro --chapter 0 \
    --context "#065, #069 and #070 are all open proposals to retitle or redraw plates. The next naming pass lands a new dated file beside the old one; the old one still exists and still parses, so the packet keeps yesterday's titles and says nothing. A missing plate prints MISSING; a missing title prints a page headed 'Chapter 5'. This is the one artifact built to go to strangers." \
    --unblocks "Whether the packet's titles follow the latest naming pass automatically, or the author has to remember to edit line 45 after every retitle" \
    --recommend "Glob newest-wins, and print MISSING-TITLE and exit non-zero rather than falling back - the same loudness chapter_plate() already gets" \
    --evidence "curated_names() resolves 12/12 today: ch01..ch12 all named, all Mechanism/Conversation/Lesson fields non-empty - so this is latent, not live. The pin is scripts/plate_packet.py:45-46 NAMES_DOC = os.path.join(REPO,'runs','design','2026-09-20-plate-names-and-visual-summaries.md'); the silent fallback is line 186 title = names.get('ch%02d' % n, 'Chapter %d' % n). ls runs/design/ shows four 2026-09-20-* documents already, one naming pass in. curated_names() also already carries one unproven scar: Ch5's extra italic naming-note paragraph broke the first parse, fixed by a last-non-blank-line heuristic with no stored fixture." \
    --applied-by "test -d tests/fixtures/plate-names && python3 tests/run.py"
```

Price: code, **unmeasured** (not drafted). Replaces the silent fallback at
line 186 and the hard-coded constant at line 45. Corpus: +0.

### B — four stamped HTMLs, one mutable raster set

```
python3 scripts/inbox.py --add "runs/manuscript/ commits 29 regenerable PNGs and 6 HTMLs whose stamped names now misrepresent their contents - four Rule-15-stamped HTMLs share one unstamped, repeatedly-overwritten PNG set. Should the rasters and HTML stop being tracked, leaving the self-contained PDF as the committed artifact?" \
    --raised-by gw-retro --chapter 0 \
    --context "Rule 15 exists because three files 'each looked current'. Round 1's committed HTML, opened today, renders round 3's Ch8 and Ch12 plates while its sibling PDF embeds round 1's. plate_packet.py inherited the collision and worked around it with a packet- prefix, which is why 14 byte-identical duplicate PNGs now exist. The workaround is the tell." \
    --unblocks "Whether a stamped filename in runs/manuscript/ can be trusted to show what it showed when it was made" \
    --recommend "gitignore runs/manuscript/*.png and *.html; keep the PDFs (Chrome embeds the images, so they are already self-contained and already correct) and keep README.md's table as the index" \
    --evidence "md5sum runs/manuscript/*.png grouped by hash: 14 byte-identical pairs, chNN-plate.png == packet-chNN.png for all 12 chapters plus both Part plates; 'duplicate PNG files (same bytes, different name): 14', 1.9M of 3.8M. All four *plates-draft*.html reference an identical PNG name list (md5 798c330df56f28b71ffd8b607b457b70 x4). git log on the rasters: eb3da38 wrote them, 1be88a2 rewrote them, c5690af rewrote ch07/08/09/12-plate.png again after the Ch8 and Ch12 redraws - while eb3da38's HTML is still tracked and still points at them. Tracked in runs/manuscript: 29 png (3.8M), 6 html (748K), 7 pdf." \
    --applied-by "test \$(git ls-files 'runs/manuscript/*.png' 'runs/manuscript/*.html' | wc -l) -eq 0 && python3 tests/run.py"
```

Price: +2 `.gitignore` lines, **deletes 35 tracked files / 4.5M** (29 PNG,
6 HTML). Corpus: +0.

Neither proof passes today: `tests/fixtures/plate-names` does not exist, and
35 files are tracked. Both are re-runnable and both fail for the right reason
before the work lands.
