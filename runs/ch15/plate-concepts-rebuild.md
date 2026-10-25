# Chapter 15 plate concepts, rebuild (D and E)

Designer (gw-designer), concepts mode. Clock read 2026-10-25 19:25. Two concepts on the rebuilt Mechanism, both showing all three pairs. Sources read: `runs/ch15/plate-brief.md` (regenerated today), `runs/ch15/distillation.md`, the prose above Editor's Notes in `runs/ch15/refined.md`, the plates `runs/ch12/plate.svg`, `runs/ch13/plate.svg`, `runs/ch14/plate.svg` and `runs/ch15/plate.svg`, the earlier panel reads `runs/ch15/plate-pick.md` and `plate-read*.md`, and the approved style in `books/the-stoic-husband/design/plates/README.md`.

Files: `runs/ch15/concepts/concept-d.svg` and `.png`, `runs/ch15/concepts/concept-e.svg` and `.png` (rendered with the repo's `chapter_pdf_local.svg_to_png`, Playwright, scale 2). `runs/ch15/plate.svg` and `books/` were not touched.

**Title (Mechanism, word for word):** Meet hostility with kindness, frustration with patience, disconnection with warmth. It is the same in the visible title and the aria-label.

**Conversation sentence (what the stranger must take away):** When your wife's day turns sharp, meet hostility with kindness, frustration with patience, and disconnection with warmth, and ask yourself each day whether you were the best part of her day.

**Style matched:** 640 wide, height fitted to the drawing (D 600, E 470). One ink, #1a1a1a through currentColor, on white, with opacity for the quiet tones. Georgia, serif throughout, using the Ch12/Ch15 class hierarchy: semibold letterspaced capitals for labels, a faint capital weight for the quiet side (`lblr`, as in the current Ch15 plate), italic glosses, a semibold italic for the closing question (`capq`, as in the current Ch15 plate). Three line weights: 1.4 quiet, 2 standard, 3.2 carrier, the same as the current Ch15 plate, plus the 0.8 hairline rule the Ch12 plate uses. Every anchor is set in a class or an inline style.

**The lesson from the earlier reads, applied to both:** every heavy carrier stroke starts at YOU and ends at her, with the arrowhead on her side. Nothing heavy travels from her to him, so a stranger should not read "she hands me chores." Neither concept draws a chore box, which is the drawing that invited the round-4 misreading.

## D. Three exchanges, one steady answer

**Carrier:** three rows between two posts, YOU on the left and HER on the right. In each row her edge arrives faint, from her to you, and its shape names the test: a jagged line (hostility), a line that keeps looping back on itself (frustration), and a dashed line that breaks off before it reaches you (disconnection). Under each one, his reply goes back as one heavy, smooth arc from YOU to HER, named for the virtue. Patience has one extra mark: three dots before the arc starts, which is the pause before he answers. The bottom line asks the daily question.

**A stranger sees this and takes away:** Whatever shape her edge comes in, sharp, tangled or cut off, what you send back is smooth and goes to her: kindness, patience, warmth. Then ask whether you were the best part of her day.

**Copy, counted:** 8 bold labels, 5 italic lines (cap 10; the caller's limit of 7 also holds).

| Text | Kind | Source |
|---|---|---|
| Meet hostility with kindness, frustration with patience, disconnection with warmth | title | Mechanism, distillation |
| When your wife's day turns sharp | subtitle | Conversation sentence, distillation |
| YOU, HER | labels | chapter's own words |
| HOSTILITY, FRUSTRATION, DISCONNECTION | quiet labels | Mechanism |
| KINDNESS, PATIENCE, WARMTH | labels | Mechanism |
| a little slight, a cutting remark | gloss, hostility | prose: "A zing is a little slight, a cutting remark." |
| two tired people | gloss, frustration | prose: "That's two tired people." |
| a sign that she is feeling strained | gloss, disconnection | prose: "just a sign that she is feeling strained" |
| "Was I the best part of her day?" | closing line | prose: "So ask yourself, each day: 'Was I the best part of her day?'" |

**Main risk:** the three heavy arcs look the same, so a skeptic may read "same reply to everything" and miss what kindness, patience and warmth each look like in practice. The plate shows the direction and the steadiness of his answer, not its content. The pause dots are the only thing that makes patience different, and they may be too small to see on a phone. Second risk: as in the earlier rounds, every edge starts with her, so a defensive man may read "she starts it, I absorb it." The glosses help here: "two tired people" puts him in the frustration too.

**Validation question:** without the chapter, does a reader see the heavy arc as something he gives her, or only as him not fighting back?

## E. Her day, held up three times

**Carrier:** her day as one line across the page, labelled HER DAY. It turns sharp three times, and each V is named for its test above the line. Below sits his steady line, YOU. From it, three heavy arrows rise and meet the bottom of each V, so the drawing shows him holding her day up at the moment it drops. Under each arrow is the virtue and one concrete thing to do. The closing question sits below the drawing.

**A stranger sees this and takes away:** Her day will dip, sharp, tired, cut off. Each time, you push up from underneath, with kindness, patience or warmth, and at night you ask whether you were the best part of it.

**Copy, counted:** 8 bold labels, 5 italic lines (cap 10; the caller's limit of 7 also holds).

| Text | Kind | Source |
|---|---|---|
| title, subtitle | as D | as D |
| HER DAY, YOU | labels | prose: "talk about her day", "the best part of her day" |
| HOSTILITY, FRUSTRATION, DISCONNECTION | quiet labels | Mechanism |
| KINDNESS, PATIENCE, WARMTH | labels | Mechanism |
| let it go | gloss, kindness | distillation: "If it isn't, let it go." |
| start helping first | gloss, patience | distillation, Practice 2: "Start helping first." |
| let her talk | gloss, warmth | distillation: "and let her talk" |
| "Was I the best part of her day?" | closing line | prose, as D |

**Main risk:** "her day as a line" can read as a mood chart, and a skeptic may hear "managing her moods is your job." The chapter's frame is that she is strained and his reply is his choice; the plate does not show that he is tired too (the Lesson's "even when you're tired too"). Second risk: an arrow tip meeting a V tip might be read as his push causing the dip. The arrowheads point up and sit under each dip, which should read as support, but a panel should test it. "let it go" may read as passive without the chapter's "If it isn't".

**Validation question:** without the chapter, does a reader see the arrows as him lifting her day, or as something he aims at her?

## How D and E differ

D is about the exchange: what comes at you and what you send back, row by row, so "meet X with Y" is drawn as a reply. E is about her day: three drops in one day and his three lifts, so "best part of her day" is built into the drawing and not only into the caption. D draws the reply more strongly; E draws the Lesson (what to do) and the daily audit more strongly.

## For the author to rule on

1. **The title does not fit as a display title.** The Mechanism is 83 characters, and `plate_check.py` reads only the first `ttl` text element and does not read `<tspan>`. On one line it fits the 552px measure only at 11px with no letter-spacing (measured against DejaVu Serif Bold: 541px at 11px, 590px at 12px). So in both concepts the title is smaller than the labels, which reverses the approved hierarchy ("the title is the most prominent text"), and it will be small on a phone. The three pairs are still readable at full label size in the drawing. Options: (a) accept a small single-line title for this chapter; (b) the Publisher extends `plate_check.py` so a title can be set over two or three lines, one per pair. That is a tooling change and needs an inbox item, not a Designer edit.
2. Both concepts use the faint `lblr` weight for the three tests, which makes her side quieter than his. Earlier readers called that blame ("she's mild, you're the aggressor") when it was used for his zings. Here the faint ink belongs to her edge and the heavy ink to his kindness, which is the reverse, but the Panel should check it.

## plate_check.py, verbatim

```
runs/ch15/concepts/concept-d.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x600
  [ ok ] title       title 'Meet hostility with kindness, frustration with patience, disconnection with warmth' / aria-label 'Meet hostility with kindness, frustration with patience, disconnection with warmth' vs Mechanism 'Meet hostility with kindness, frustration with patience, disconnection with warmth'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    5 italic lines against a cap of 10 (8 labels + subtitle + closing line)
  [ ok ] alignment   12 centred texts on the axis or a shared column; 11 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
  [WARN] raster-current preview missing or differs from source at its own scale
runs/ch15/concepts/concept-e.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x470
  [ ok ] title       title 'Meet hostility with kindness, frustration with patience, disconnection with warmth' / aria-label 'Meet hostility with kindness, frustration with patience, disconnection with warmth' vs Mechanism 'Meet hostility with kindness, frustration with patience, disconnection with warmth'
  [ ok ] grounded    each text has a three-word match in permitted source copy
  [ ok ] captions    5 italic lines against a cap of 10 (8 labels + subtitle + closing line)
  [ ok ] alignment   12 centred texts on the axis or a shared column; 4 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
  [WARN] raster-current preview missing or differs from source at its own scale
```

The `raster-current` WARN compares against `runs/ch15/pdf/plate.png`, the preview for the current plate, not these concept files. It does not apply to a concept.
