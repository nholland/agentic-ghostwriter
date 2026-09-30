# Chapter 13 provisional plate notes

Designer desk. Draft-stage SVG from cold-panel pick B. This is the author's requested prototype from draft.md, not a claim of completed refinement or final mechanism approval.

## Drawing and source

The river continues from remembered dating answers to present interest. Its two bands remain at a constant separation; no divergent path or distance marker implies spouses growing apart. Present interest has stronger type than remembered answers. The closing line makes receiving her answer warmly explicit.

Removed both the vertical double arrow and the faint vertical line, so no marks pass through copy. Replaced the water subtitle with the exact draft sentence “Some things matter more to her now.” The Panel's proposed “Her answer now may be different” was not used because it was not draft copy.

Visible copy (40 words total):

- “Keep learning what matters to her” (6): substring of “You keep learning what matters to her.” Provisional exact title.
- “Some things matter more to her now.” (7): She's still becoming section.
- “when you were dating” (4): When learning felt finished section.
- “now” (1): current-choice language throughout the draft.
- “the answers you already had” (5): When learning felt finished section, split over two lines.
- “Be interested in her answer.” (5): draft section heading, split over two lines.
- “She's still becoming. You've changed too.” (6): two exact draft sentences combined into one line.
- “Let yourself be pleased for her.” (6): opening scene.

The copy totals **40 words**, counted as 6 + 7 + 4 + 1 + 5 + 5 + 6 + 6. Apostrophe-bearing words count as one.

House style follows the existing plates: Georgia/serif, #1a1a1a, white canvas, thin strokes, centered text, restrained italic subordinate copy. Larger body text supports phone reading.

## Format checklist

- [x] Centered text lies on x=320 or the shared x=168 / x=472 columns.
- [x] River drawing is centered within the canvas.
- [x] Canvas is 640 × 560.
- [x] Five italic lines meet the checker cap of five.
- [x] Text anchoring is in CSS classes, never bare attributes.
- [x] SVG rendered through the Publisher's Sharp helper; PNG viewed. Text is readable and no line crosses text.

## Local counted check

Command: `python3 runs/ch13/check-plate-local.py runs/ch13/plate.svg --chapter 13`.

```text
runs/ch13/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x560
  [WARN] title       no distillation.md with a Mechanism line found for ch13
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    5 italic lines against a cap of 5 (3 labels + subtitle + closing line)
  [ ok ] alignment   10 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed:    at require (node:internal/modules/helpers:191:16)
    at [eval]:3:22
    at ru
```

The title warning is expected because this authorized draft prototype has a provisional plate-distillation.md, not distillation.md. It has not been suppressed by inventing refinement artifacts. The checker's rendering backend failed, but `node runs/ch13/render-plate.cjs runs/ch13/plate.svg runs/ch13/pdf/plate.png` succeeded, and that output was viewed. Independent Publisher review and the final standalone panel read remain pending.

## Single panel revision — current SVG

Preserved the original cold read as `plate-read-round1.md`. Applied its underlying findings while retaining the exact provisional mechanism title and draft-only language. Its suggested invented title and subtitle were not used.

- Moved “She's still becoming. You've changed too.” into the prominent subtitle.
- Removed “Some things matter more to her now.” to avoid the implication of increased demands.
- Grouped “Ask what happened next.”, “Be interested in her answer.”, and “Let yourself be pleased for her.” into one present-interest column, with receiving her answer warmly adjacent to asking.
- Removed the second river pair. The remaining river carries continuity from dating to now, not a distance between spouses.
- Preserved source-grounded remembered-answer copy in the quieter left column.

Current copy supersedes the first-draft inventory above: 37 words (title 6; becoming subtitle 6; dating label 4; now 1; remembered answers 5; ask 4; interested 5; pleased 6). Twelve SVG text elements; five italic lines. Current column axes remain 168 and 472, with title/subtitle at 320; width remains 640. All format checklist entries still hold. Rendered and inspected during revision; the only subsequent formatting fix reduced the dating header from 21 to 19 px to meet the checker's margin bound.

Final revision check:

```text
runs/ch13/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x560
  [WARN] title       no distillation.md with a Mechanism line found for ch13
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    5 italic lines against a cap of 5 (3 labels + subtitle + closing line)
  [ ok ] alignment   12 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed:    at require (node:internal/modules/helpers:191:16)
    at [eval]:3:22
    at ru
```

Sharp render succeeded after the final font correction. The same expected provisional-title and unavailable-checker-render warnings remain. Independent Publisher verification and fresh cold read are pending. No further design round is claimed or performed here.

## Direct author revision — arrows, balance, and takeaway

The author requested directional arrowheads on the water lines, a separator and centered bottom takeaway following the established plates, and relief from the previous right-heavy composition. This direct author instruction authorizes the present revision beyond the earlier panel cycle. Preserved its predecessor as `plate-before-author-revision.svg`.

Revisited the actual `virtue-question.svg` and `four-ds.svg` for thin rules and shared alignments, alongside the previously read `river-oak-sun.svg` with its centered full-width conclusion. The new drawing has two equally styled, equal-height columns at x=176 and x=464. Each has a short heading and exactly two body lines. Both wavy paths have visible rightward arrowheads. The column copy ends at the same baseline, so the lower half no longer belongs to the right column.

A thin separator spans x=64..576 at y=351. Beneath it, both takeaway lines are centered at x=320: “Choosing her keeps happening” (a contiguous phrase from the draft) and “Let yourself be pleased for her.” This joins continued choosing with warm reception. Removed “Be interested in her answer.” to reduce redundant copy. Canvas shortened to 640 × 480.

Current copy: 36 words, counted as title 6 + becoming subtitle 6 + dating heading 4 + now 1 + remembered answers 5 + follow-up question 4 + continued choosing 4 + pleased for her 6. Every phrase remains draft-grounded. No refined artifact was available at this handoff, and none was invented.

Current format checklist: all centered text uses x=320 or shared symmetric columns; drawing centered; width 640; three italic lines under cap four; anchors in CSS; explicit fills; no em-dash or numbers. Sharp rendered successfully. The drawing was inspected during this revision; the final adjustment shortened the first takeaway to remove an unclear “that life” reference and pass the margin check.

```text
runs/ch13/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x480
  [WARN] title       no distillation.md with a Mechanism line found for ch13
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    3 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   10 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [WARN] ink         render failed, unchecked: svg_to_png: playwright capture failed:    at require (node:internal/modules/helpers:191:16)
    at [eval]:3:22
    at ru
```

Expected provisional-title and checker-render warnings remain; Sharp output is `pdf/plate.png`. Parent Publisher independently reviews this author-directed version.

## Final source synchronization and Publisher checks

2026-09-23T07:00:23.371201-05:00

Actual refined prose and distillation now exist. Publisher retained the Designer layout and replaced the draft-only choosing phrase with one exact-source takeaway: “The effort that follows / deserves just as much of you.” The brief was regenerated from final sources. Final cold read passed in plate-read-author-revision.md. All geometry, source, title, caption, alignment, and rendered-ink checks pass; see final-gates.txt. The previous provisional warnings above are historical. No book landing yet.

## Author correction — curiosity while dating (current plate)

2026-09-23. Supersedes the historical remembered-answer interpretation above. The author correctly observed that dating involved curiosity about answers not yet known. Replaced the left column with the chapter's exact phrase “you wanted to hear / what she thought.” The right column remains “Ask what / happened next.” The two arrows now connect early curiosity to continued interest, while the becoming subtitle and sustained-effort takeaway carry the chapter's reason for continuing. No claim remains that he already had the answers during dating.

Preserved the established 640 × 480 canvas, Georgia, ink color, thin strokes, two centered columns at x=176 and x=464, arrowheads, separator, and centered takeaway. Source: refined.md, paragraph beginning “That's the pre-commitment paradox.” Every visible phrase remains chapter-grounded; the mechanism title matches distillation.md exactly. The author's correction is recorded in plate-brief.md.

- [x] Ten centered text elements use the center axis or symmetric shared columns.
- [x] Drawing block remains centered; both arrows remain visible.
- [x] Three italic lines are within the cap of four.
- [x] No bare text-anchor attributes, em-dashes, or numbers.
- [x] Sharp rendered to pdf/plate.png; image visually inspected, with no clipped copy or collisions.

Independent Publisher check and cold Panel read remain pending. Designer local check:

```text
runs/ch13/plate.svg
  [ ok ] charset     valid UTF-8, no mojibake
  [ ok ] geometry    no margin or collision rows
  [ ok ] anchor-attr anchors set in classes or inline styles only
  [ ok ] em-dash     none
  [ ok ] digits      none
  [ ok ] canvas      640x480
  [ ok ] title       title 'Keep learning what matters to her' / aria-label 'Keep learning what matters to her' vs Mechanism 'Keep learning what matters to her'
  [ ok ] grounded    every run of three or more words is the chapter's
  [ ok ] captions    3 italic lines against a cap of 4 (2 labels + subtitle + closing line)
  [ ok ] alignment   10 centred texts on the axis or a shared column; 1 drawing blocks centred or mirrored
  [ ok ] ink         no rendered ink inside the 40px margin bands (dark px {'left': 0, 'right': 0, 'top': 0, 'bottom': 0})
```
