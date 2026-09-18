# Marks

Four SVG marks. Every line in them traces to a sentence already approved in
`okf/frameworks/the-river-the-oak-and-the-sun.md` or the Part pages — nothing
here was designed to look good first and justified afterward.

## Derivation

| Mark | Source sentence | What the drawing had to carry |
|---|---|---|
| `river.svg` | *"It doesn't fight the stone in its path. It goes around it, and it goes on."* (`parts/part-1-steady-river.md`) | The stone is the point. Water alone would be a generic wave glyph; the current parting and continuing past a fixed obstacle is the actual idea. |
| `oak.svg` | *"The oak's strength isn't announced; it's revealed when weight is placed on it."* — "load-bearing" | A broad crown over a visibly sturdy trunk. A thin trunk reads as decorative and contradicts the sentence. |
| `sun.svg` | *"The sun is warm, and it gives that warmth away. That's the whole of its work. It doesn't wait to feel like it, and it doesn't wait to be asked."* (`parts/part-3-warm-sun.md`) | Rays are even and unbroken in all directions. The evenness is the meaning: warmth is not rationed or conditional. |
| `ornament.svg` | The closing formula — *"When life changes, flow. When life becomes heavy, stand. When life becomes ordinary, bring warmth."* | Three strokes, one per element, in book order. Using a single element's mark (an oak leaf, say) as the house ornament would privilege one of three things the book insists are inseparable. |

## Two rejected drafts, and why

Recorded so the same mistakes don't get re-made.

1. **River as two streamlines parting around a centered circle** — symmetric
   bowing around a central dot reads unmistakably as an **eye**. Replaced with
   stacked waves interrupted by a solid stone.
2. **Oak as a single-stroke trunk under a thin dome** — reads as a **floor
   lamp**, and a spindly trunk actively contradicts "load-bearing." Replaced
   with a lobed crown over a tapered two-stroke trunk.

Both were caught by rendering them, not by reading the markup. Render before
committing to a mark.

## Technical

- `viewBox="0 0 64 64"` (`0 0 120 24` for the ornament), stroke-based, no fills
  except the river's stone.
- `stroke="currentColor"` throughout, so a mark inherits its context — dark on
  ivory, light on charcoal, no second file needed. This is what lets one set
  serve both design directions.
- Stroke width 2.5 at 64px. Below ~28px the river's three waves start to fill
  in; use the sun or oak where a very small mark is needed.
- No text, no gradients, no external references — safe to scale to foil
  stamping or down to a favicon.

## Status

**Draft, pending author review.** Not referenced by any command yet. These are
proposals, not locked artifacts.
