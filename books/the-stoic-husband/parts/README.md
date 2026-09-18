# Part Openings

The five reader-facing section pages. One page precedes the first chapter
of each Part: a title and a single italic paragraph, nothing else.

These are **hand-authored, locked artifacts**, the same as the Introduction.
No skill generates them. Revise via `/book-feedback part-N`, never by
regenerating from scratch.

## The framework

Every page follows the same form:

1. **The turn** — one sentence naming what this is, plainly.
2. **The behavior** — two to four sentences of what it does in nature.
3. **The durable fact** — one sentence stating what's true regardless.
4. Nothing follows the last sentence. There is no closing standard line.

**Stance differs by Part, deliberately:**

- **I–III describe the element in nature.** Third person. No "you."
  Each introduces one element.
- **IV–V speak to the man.** Second person. IV cautions, V aspires.
  Each names all three elements rather than introducing a new one.

**Hard rules:**

- **No marriage vocabulary on any page.** No wife, no dinner table, no
  fight, no years married. Nature and the man, nothing else. The reader
  makes the connection himself; that is what makes these read as section
  pages instead of chapter openings.
- **Every sentence must carry an inferable lesson for the reader.** A
  sentence that exists for rhythm alone gets cut. This is how "and nothing
  grows in the dark" was removed from Part III.
- **No negative social proof**, per `01-voice.md`'s Never Do list, where
  this rule now lives for the whole book. Cut from Part V on 2026-08-23.
- **Length: 62–66 words.** All five sit in that band on purpose.

## Closing plates

Added 2026-09-11. A Part may also carry a **closing plate**: a full-page
illustration after the Part's last chapter, before the next Part's opening.
Parts I and II have one; the set is meant to reach five, since furniture
that stops at Part III reads as an accident (the same lesson as #27).

Stored at `parts/plate-N-<slug>.svg`, pointed to from `03-outline.md` by
``*Reader-facing closing plate: `parts/<file>`*`` under the Part header,
tracked in the manifest as `stages.parts.<N-slug>.closing`, and emitted by
`/book-compile` Step 2.7. `scripts/chapter_pdf.py` gives each one a page.

**Form rules, so the plates work as a set:**

- **Black line on white, one weight.** No color, no fill, no shading. Print
  interiors are grayscale; line art is the safe bet and the honest one.
- **One abstract image of time laid down in layers,** with one irregularity
  that carries a sentence already on that Part's opening page. Part I is
  canyon strata cut by a thin river: the days. Part II is tree rings with two
  bands of tight years and one scar the later rings closed over: the years.
  The image is not a picture of the element; it is the element's durable
  fact, drawn.
- **The caption is the opening page's last sentence, verbatim.** The plate
  reprints the book's own words; it adds none. Removing the caption is one
  edit and was left as an open call for the author.
- **No marriage vocabulary, same as the opening pages.** The rule above
  applies to the image too: nothing domestic, nothing human.
- **6x9 proportion** (600x900 viewBox), matching the trim.

The opening page describes the element before the reader has lived the
chapters; the plate shows the same element after. That gap is the point.

## Why IV and V are seasons, not elements

Parts I–III are things the husband *is*. Parts IV and V are what happens
to him and what he's aiming at, so they can't take an element name without
diluting River/Oak/Sun into a set of five.

Naming them as *movements* ("Fall to Winter," not "The Winter") puts the
direction of travel in the title, where a reader gets it on a flip-through.
On a contents page the reader sees three nouns and two movements and
perceives two different kinds of thing immediately.

Both season pages name the river, the oak, and the sun explicitly. That is
the payoff of the set, and it means the three elements reach the reader on
all five pages.

## Cross-page references

Part V's "No summer is the last one" deliberately answers Part IV's "No
winter is the last one." Part pages are a set and should talk to each
other. This is not the cross-chapter reference pattern that parking-lot
item #25 concerns.
