# Substack and social register — The Stoic Husband

*Ported 2026-10-02 from the frozen pipeline's `/book-substack` (Playground-260420,
`.claude/commands/book-substack.md`, steps "Substack Voice Constitution", 4a, 4b),
on the author's word that session: "Lets do A first". This file adds only what
`01-voice.md` does not already say. Where `01-voice.md` speaks (bold cap, metaphor
cap, rhetorical-device cap, ending, no-pointer-to-the-book rule, the wife-as-threat
ban), it governs and is not repeated here. The Publicist reads both.*

## The register

**Write it the way he'd tell it to a friend on a Saturday morning.** The book is
contemplative and can afford to be. A Substack post has to be more fun than the
book: looser, funnier, a little irreverent, and worth forwarding. If the book is
the sermon, this is the story he tells afterwards that people actually repeat.

- **Start with the thing.** State the idea in sentence one or two, plainly, then
  hang a story, a joke or a surprising detail on it. Not a scene-setting runway.
- **Talk, don't compose.** Contractions, fragments, asides, a tangent that earns its
  keep. Say "kids" and "dishwasher", not "household" and "the evening". If a sentence
  sounds like something written, say it out loud and rewrite it until it sounds said.
- **Be specific to the point of being funny.** The weird real detail beats the
  tidy general one: the exact thing she said about the dishwasher, the third time
  you checked your phone. Humour comes from precision and from being honest about
  how men actually behave, aimed at "most of us", never at her.
- **Have an opinion.** State it flat. Don't wrap every claim in a soft landing.
- **At least one moment a reader would screenshot or text to a friend.**
- **End by stopping.** The last sentence is a concrete image, a joke or a plain
  fact. Not a moral, not an aphorism, not a callback that explains the point.
- **No invented "I".** The author's real stories exist only where his interview
  record or the OKF holds them. Otherwise stay in "you" and "most of us". Never
  fabricate a personal anecdote, and never turn a composite scene into "my wife".

**What reads as AI slop here, and is out:** "Picture it:", "Break that down:",
"Translation:", "Here's the thing:", "That's the difference", a colon-then-label
sentence, a tidy three-beat list, "Not X. It's Y." used as a drumbeat, a closing
line that sounds like a poster, a moral spelled out after the story already made it,
and any paragraph where every sentence is the same length. A post can pass every
count and still read like a brochure. The counts are a floor; the test is whether he
would be happy to have said it out loud.

Test: if sentence one could open the chapter's scene without stating the concept,
rewrite it until it is the concept statement.

## Self-contained, before the first sentence

The reader found this in an inbox or a search. They have not read the chapter, any
other post, or anything about Stoicism. Every term, philosopher, scene and framework
is introduced inside the post. A Stoic term is never used before a plain-English
description of it. A scene the chapter set up earlier is re-established, not
referenced. Marcus, Seneca and Epictetus each get one sentence of grounding at first
use. Test: could someone arriving from a search follow every sentence without
wondering what it refers to?

## Shape (400–600 words, five paragraphs at most)

A hook that states the idea, the story or case that makes it land, the Stoic point
in plain talk, one thing he can do tonight, and one closing sentence. No bullets, no
subheadings. `[PLACEHOLDER: ...]` stays. The application is observational ("the next
time she says something sharp, there's a half second..."), never a workbook prompt
("Tonight, pick one thing. Ask yourself...").

## Required in every post

- **A light Stoic tie-in**, one or two sentences, and it must be the concept, figure
  or text the source chapter itself uses for this material. A plausible generic
  substitute reads as "no real lesson".
- **Quote-gloss.** Any quote over about 15 words, or in period translation phrasing,
  is followed at once by a one-sentence plain-English gloss.
- **Bidirectionality** where the concept runs both ways (his mood to her and hers to
  him; his patterns and hers). Show both directions.
- **No one-sided casting.** Across the posts already saved for the chapter, one
  partner must not be the standing source of negative affect. Use categories that hit
  both partners: anxiety, fear, dread, grief, exhaustion.
- **No forward reference of any kind**, including phrasing inherited from the chapter
  ("the next chapter", "later"). The `01-voice.md` ban list governs; check the hook and
  the body, not only the close.

## Short-form counts beyond `voice_check.py`

- No em-dashes.
- "move, moves, moved, moving" at most once per post. Use the specific verb:
  travels, runs, lands, arrives, passes, spreads, shifts, enters, carries.
- No windup sentences ("Here's what I mean...", "Here's what this looks like...").
- A second-person imperative swapped for another imperative is not a register fix.
  Change the mood.
- Metaphor family: about 3 mentions in a 400–600 word post, counting every
  conjugation. Counted by script, never by feel.

## Cross-concept redundancy

Before drafting a concept, read the posts already saved for that chapter. Two concepts
from one chapter may share a source and theme. They must not share a core mechanism,
a practical tool or a near-duplicate closing line. Find the distinct angle first.

## Subject lines

Three options under 60 characters: one counterintuitive, one practical, one curious.
**Every option is anchored in his marriage, not in the mechanism.** He is a married
man scanning an inbox: does this name a real moment with her, or a real stake? A
Stoic's name, a term (prohairesis, equanimity) or the framework's label in the subject
line reads as a trivia headline. Miss: "The most useful word from a 2,000-year-old
slave". Hit: "What to do in the three seconds after she says something sharp". Miss:
"Trace one default back to its source". Hit: "Who taught you how to fight with her?"

## The file: one post, with the X and Facebook posts appended

Each concept is ONE file, `runs/marketing/chNN/NN-slug.md`, laid out so the Substack
post can be pushed or pasted whole and the two social posts cut and pasted straight
from the bottom:

```
# Title
**Chapter source:** ...   **Subject lines:** 1. ... 2. ... 3. ...
**Status:** Draft, awaiting author approval. Not posted.
---
<the Substack post, and nothing else>
<!-- END OF POST -->
## X
<the post, ready to paste; the link line is the literal text [Substack link]>
## Facebook
<the post, ready to paste, ends with the link line then the tags>
```

Everything between the first `---` and `<!-- END OF POST -->` is the post and is the
only part ever pushed to Substack. Nothing in the post body may refer to the X or
Facebook posts. Run the counted check on the post body only.

**X and Facebook** (`#Stoicism #HusbandLife #MarriedMan` on both): single posts,
never threads, 3–4 sentences, a provocative fragment and not a summary, in the same
casual voice as the post. X gets two or three options with genuinely different
angles (counterintuitive, story-led, practical); Facebook gets one, warmer. Each ends
with the link line, then the tags. **LinkedIn and Reddit are written only when he asks
for them**, in the formats the frozen pipeline used (LinkedIn: no tags, link in the
first comment; Reddit: lowercase `i`, fragments, `...` as a beat, 2–3 questions, no
pitch, 150–200 words, link as an afterthought in the first comment).

## Before showing him anything

Punchline-first. Self-contained. Stoic tie-in matches the chapter's anchor. Both
directions shown. No one-sided casting. Banned verbs, em-dashes and windups cleared.
Conversational throughout. 400–600 words. Then `voice_check.py --short-form` pasted
verbatim. Do not show a draft that still needs a fix.

## What he does by hand after approval (the house never posts)

Today: copy the post into Substack, strip any tag from the title, publish, pick the
auto-generated preview image, then paste the X and Facebook posts from the bottom of
the file, swapping `[Substack link]` for the live URL. Pushing the post to Substack as
a draft is a registered gap (`GAPS.md`), not a capability this house has yet.
