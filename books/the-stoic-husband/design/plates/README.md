# Plates

Nine draft plates. Each is traceable to an approved concept; none introduces
new claims. Stroke-based SVG using `currentColor`, same as `../marks/`.

| Plate | Source | Notes |
|---|---|---|
| `incomplete-husband.svg` | `okf/frameworks/the-river-the-oak-and-the-sun.md` — "The Danger of Becoming Only One" | Uses all three marks. See note below on the missing sixth pairing. |
| `virtue-question.svg` | `okf/frameworks/the-virtue-question.md` + Ch1's beat labels | Practical labels only. No cardinal virtue names. |
| `four-horsemen.svg` | `okf/citations/gottman-four-horsemen.md`, framing from Ch9 prose | Attributed. No statistics — see below. |
| `four-ds.svg` | `okf/frameworks/the-four-ds-defensive-response-taxonomy.md` | Definitions condensed; full text in the concept. |
| `small-rocks-big-rocks.svg` | `okf/frameworks/small-rocks-big-rocks.md` | The picture argues the "share of total volume" column. |
| `tipping-scale.svg` | `okf/frameworks/the-tipping-scale.md` | Replacement approved in inbox #054, 2026-10-01: uncounted accumulation versus weights named as they arrive. |
| `river-oak-sun.svg` | `okf/frameworks/the-river-the-oak-and-the-sun.md` — Schema + closing formula | The explainer. Definitions condensed from the source paragraphs; the formula is verbatim. |
| `three-second-window.svg` | Ch1 prose + `chapters/ch01/distillation.md` | **Chapter 1 main plate, titled The Gap** (inbox #056 approved 2026-10-01). The 0.5s / 2.5s split is Ch1's own: "that half-second where you're still somewhere between deciding and reacting... and then the two and a half seconds after." |
| `the-operating-system.svg` | `okf/frameworks/the-operating-system-trigger-meaning-autopilot.md` | **Inline visual**, preserved for later layout repair and chapter placement (inbox #056). Trigger + loaded meaning = one impression; the dashed span is the gap most men run straight through. |

## Three things a future reader should not have to rediscover

**The Incomplete Husband shows six failure modes, and the sixth has a
history worth keeping.** The original manifesto named five. Drawing the plate
exposed the asymmetry — the River-Sun edge had no mode on the River side —
which is a diagram catching something the prose had not. The sixth
("river without sun -> detached") was proposed to the author with supporting
language from `okf/frameworks/avoiding-unhappiness-breeds-apathy.md`,
approved on 2026-08-31, and written into
`okf/frameworks/the-river-the-oak-and-the-sun.md` *before* it was drawn.

That order is the rule, not a formality: concept first, plate second. The
reverse would make a diagram the source of book content that never went
through check-in.

**The Four Horsemen plate carries no numbers, and that is deliberate.**
`okf/citations/gottman-four-horsemen.md` is `status: unverified`, and its
verification note says specifics must be confirmed before appearing in the
manuscript. The four behavior names are not in dispute and already appear in
refined Ch9 prose; statistics, study dates, and sample sizes are exactly what
Rule 3 guards, so none are on the plate. The subtitle paraphrases Ch9's own
approved sentence rather than the research.

Related, unresolved: Ch9's editor's notes call this citation `verifiable`
while the concept says `unverified`. The concept is authoritative per Rule 11.
Ch9's note also points at `sources/citation-manifest.md`, retired as a
tombstone on 2026-08-14.

**The virtue labels are short on the plate and long in the prose, and that is
not a discrepancy.** Ch1's beat label stays "Brave enough to stay engaged";
the plate says BRAVE. A plate is a different register — label plus gloss — so
shortening here required no edit to a refined chapter. If the *chapter's*
labels ever change, that is `/book-feedback`, and it would ripple through
`the-virtue-question.md`, `four-virtues-applied-to-speaking.md`, and
`appendix/practice-guide.md`.

## Rejected during drafting

- **Tipping scale, first draft** — the beam missed the fulcrum, the weights
  floated above the pan, and the hanger geometry made the loaded side
  ambiguous. Caught by rendering.
- **Incomplete Husband, first draft** — marks were scaled too small to read as
  the same set used elsewhere, and the triangle's edges stopped short of the
  vertices so it read as three unrelated lines.
- **Incomplete Husband, element labels set beside the marks** — RIVER sat to
  the left of the river glyph and collided with it once the sixth mode
  (DETACHED) was added below. Nudging the label left did not fix it; the
  corner was carrying a mark, an element name, and a failure mode at once.
- **Incomplete Husband, PASSIVE and RIGID moved inside the triangle** — this
  bought space and broke the diagram's logic. Four modes sat outside their
  edge and two sat inside, so position stopped meaning anything and the
  reader had no rule to follow. Space is never worth an inconsistency the
  reader has to decode.

**The layout rule these two produced.** Every failure mode sits *outside*
its edge, on the side of the element it belongs to — six items, one rule,
and the triangle's interior stays empty. Element names sit radially outward
from their marks (RIVER upper-left, OAK upper-right, SUN below), so they
move away from the modes rather than competing with them. The result is
symmetric: three modes per side, matched pairs at matched heights.

Render every plate before committing it. Both defects above were invisible in
the markup.

## Status

**Draft, pending author review.** No command reads these. Not referenced by
`design-language.md`, which does not exist yet.

## Chapter title rule — approved 2026-10-01

A chapter plate uses its distillation’s Mechanism line word for word as its
visible title and accessible label; display capitalization may differ.
The author answered “yes” to inbox #065 and approved Chapter 7’s
“The Private Tally” and Chapter 12’s “The Thing With No Deadline.”
This title approval does not approve separate diagram redesigns.


## Chapter 1 arrangement — approved 2026-10-01

The window graphic is Chapter 1’s main plate, titled **The Gap** to match its
Mechanism. The title is updated in both the existing book SVG and the working
chapter SVG; their respective drawings are preserved.

**The Operating System** is an inline visual. Preserve its source SVG; repair
its layout and select its position when the chapter’s inline visuals are next
laid out. Its existing margin and em-dash issues remain pending that work.
It does not count as a second Chapter 1 plate. The author replied “Approved”
to this arrangement in inbox #056.


## Chapter plate style — approved 2026-10-01

The author replied “Yes” to the chapter-only style presented for inbox #059.
The Designer reads this section as the written reference for chapter plates.
Arc/Part plate style and placement are parked until the arcs are complete.

- **Black on white.** Use one dark ink, the existing `#1a1a1a` in
  `currentColor`, with opacity for lighter tones and a white background.
- **Georgia type throughout.** Keep a consistent hierarchy: the title is the
  most prominent text; the italic subtitle sits beneath it; labels identify
  the drawing; smaller italic captions provide brief supporting copy. Use
  the existing class hierarchy rather than introducing another type family.
- **Standard width, fitted height.** Chapter plates use the existing 640-unit
  width. Fit the height to the drawing and its necessary copy; do not add
  blank space solely to match another plate's height.
- **At most three line weights.** Use line weight to emphasize the drawing's
  main relationship and keep supporting marks quieter.
- **Explicit text alignment and rendered margins.** Set `text-anchor` in a
  class or inline style, consistent with the existing checker and the
  approved Chapter 12 label repair. Inspect the rendered image and run
  `plate_check.py` for clipping, margin spills and text/drawing alignment.

The title remains the distillation's Mechanism, with a matching accessible
label, under inbox #065. Inbox #066’s copy and drawn Lesson decisions are
recorded below. This style ruling does not ratify the entire
older proposal in runs/design/2026-09-20-plate-review.md, including its Part
rules, fixed aspect ratio, exact type sizes or older attribute-only wording.
Existing diagrams retain their individual review status.


## Chapter copy and drawn Lesson — approved 2026-10-01

For inbox #066, the author replied “approved” to the copy cap and drawn Lesson
rules, and to declining a fixed book-wide symbol dictionary.

- **Limit copy** to a subtitle, one short gloss per element, and one closing
  line. Labels identify elements; captions must not become a second explanation
  of the whole chapter. The counted `captions` row in `plate_check.py` fails
  excess italic lines on chapter plates. It budgets one line per bold label,
  plus subtitle and closing line; the Designer and Reader Panel also check
  whether each gloss belongs to its element.
- **Draw the Lesson and helpful response.** The image must convey what the man
  can do differently, through a mark or relationship the reader can see.
  The Reader Panel's standalone read checks this meaning; a passing caption
  count alone cannot certify it.
- **Use the chapter's metaphor and labels to establish symbol meanings.** A
  fixed book-wide dictionary for bars, dots, dashed outlines or the nail is
  declined. Make the meaning clear within each plate and preserve the approved
  visual style across the set.

These rules govern chapter-plate design and review. They do not approve
existing drawings or commission a bulk redraw. Arc/Part rules remain parked.
