# Editorial Standards

*Cross-book standards shared by every desk that touches prose. This file holds
what is true of any book this house produces; the book's own law - its voice,
its audience, its archetype - lives in `{bookRoot}/01-voice.md`, `02-audience.md`
and `04-archetype.md`, and outranks anything here. Where a rule has a number,
the number is enforced by `scripts/voice_check.py` from `config/house.json`;
this file explains the rule and does not restate the threshold.*

*Carried from the book repo's `book-chapter-refine.md` (Pass 4), `book-distill.md`
and `book-chapter-draft.md`, which held these standards inside three procedural
skills where the Line Editor, Anti-Slop Reader and Publicist could not all see
them. One copy, read by every desk, is the point.*

---

## 1. Anti-slop categories

Ten categories. A to E are vocabulary and construction; F to J are structural
and **counted**. A finding names its category, the exact sentence, an
approximate line, and a suggested replacement in the author's voice.

| Cat | Name | The tell | Who decides |
|---|---|---|---|
| **A** | AI vocabulary | *delve, tapestry, nuanced, leverage (verb), utilize, "it's worth noting," paramount, robust, seamless, multifaceted, "at the end of the day," "in today's world."* Mechanical swaps for plain words. | Line Editor applies |
| **B** | Hedging chains | Vague unattributed quantities ("many people," "some experts," "a number of studies") with no citation; hedges stacked three deep. | Flag for the author |
| **C** | Structural tells | Windup sentences that announce the next sentence ("Here's what this looks like in practice..."); summary callbacks ("As we've seen..."); "In this chapter we will"; *Furthermore / Moreover / Additionally*. | Line Editor applies the cut |
| **D** | Passive voice | An active subject exists and is hidden ("mistakes were made"). | Line Editor applies |
| **E** | Smoothness without substance | A claim carrying no concrete detail, name, date, number or example. | Flag for the author |
| **F** | Orphan one-liner overuse | Three or more consecutive single-sentence paragraphs with no multi-sentence build before them; a one-liner that neither resolves nor flips what precedes it; consecutive one-liners at a chapter opening before any scene exists. A single one-liner that lands a flip is the voice working, not slop. | **Always the author** |
| **G** | Bold as crutch | A bolded span doing emphasis work the sentence should do. The cap is one genuine pull-quote per piece. Bolded run-in section headers on their own line are a separate question the script reports separately. | Counted |
| **H** | Metaphor saturation | The chapter's anchor image, counted as a word family including conjugations, above its per-1,000-word cap. The drafter declares the family in Draft Notes; undeclared means unchecked, never passed. | Counted |
| **I** | Double ending | A sentence after the real close that restates, explains or qualifies it. The close is one sentence and nothing follows it. | Counted (candidate) |
| **J** | Rhetorical-device repetition | One sentence-shape more than twice in a piece: the reframe ("That's not X. That's Y."), the negated pair ("installed, not chosen"), the you-don't pivot, the colon-then-label. A mini-instance inside a larger sentence counts. | **Always the author** for the verdict; counted for candidates |

**Counted rules are counted.** After any revision claims to satisfy G to J, run
`scripts/voice_check.py` on the final text and paste its output. "I cut it from
about nine to three" is a claim; only the second number, from the script, makes
it true. Self-reported counts were wrong on three chapters of the first book and
once hid a live violation.

**The qualitative half** (the Anti-Slop Reader's) is not in this table because
it cannot be tabulated: invented foils, indirection where the plain noun would
do, scenes watched from outside, the spouse cast as a threat, universal claims
about all men. Those live in `gw-slopreader.md` and in the book's Never Do list.

## 2. Placeholders

Nothing is invented. A gap is marked, in one of two shapes, and carried
downstream unchanged:

- `[PLACEHOLDER: description — see /okf/citations/slug.md]` for a public fact,
  quotation, statistic or study. The link points at the gap-marker concept the
  Researcher created with `scripts/okf_new.py`; the Line Editor may resolve a
  public placeholder to `verifiable` **only with evidence that satisfies the
  transcription rule** (a page actually opened for a verbatim quotation), and
  never to `verified`.
- `[STORY NEEDED: description]` for the author's own material. No desk may
  fill this. It reaches the author through the inbox.

An older placeholder without a link is carried through as-is; a link is never
fabricated to tidy it.

## 3. Apparatus, and where prose ends

Every chapter file is prose followed by apparatus. The scripts cut at the
**first** of these headings and count nothing after it, so a desk must use
these exact headings and put nothing reader-facing below them:

`## Draft Notes` · `## Editor's Notes` · `## Spec Conformance` · `## Distillation`

**Draft Notes (the Ghostwriter) must carry** a `metaphor_family:` line listing
the anchor image's word family with conjugations; every placeholder and what
would resolve it; every place the draft wrote around a missing author detail;
any outline row it could not satisfy and why.

**Editor's Notes (the Line Editor) must carry** what changed and why, per pass;
the conformance table reproduced verbatim; the anti-slop flags by category; the
final `voice_check.py` output pasted, not restated; the length check against the
outline's target; every judgement call the author might reverse; remaining
placeholder counts; any structural flag.

## 4. The distillation

One per chapter, in exactly this shape, because `/gw-compile` and the book
repo's compile read the **fields** (not headings) to build the chapter's
"Putting It Into Practice" close. The first compile that looked for a
`## Practice` heading silently dropped ten sections and 1,700 words.

```markdown
# Chapter N Distillation — <Title>

**Mechanism:** <label: the chapter's permanent handle across the pipeline>
**Conversation sentence:** <what you would say if asked what this chapter is about>
<1–2 sentence full distillation>
**Lesson:** <one sentence>
**Challenge:** <one sentence: what makes the lesson hard in the moment>

**Practice:**
1. <concrete, imperative, no Stoic term without its gloss>
2. <...>
3. <optional third>
```

Derive it in four passes: the reader's default move; its hidden cost; the
Stoic flip; the practice. Then run the voice check on it. It sits beside the
prose in the manuscript and is held to the same bar.

## 5. The practice guide

`appendix/practice-guide.md` (or `runs/appendix/practice-guide.md` while the
house shadows) is reader-facing and **accumulates**. Each chapter appends one
section and never touches another's:

```markdown
## Chapter N — <Title>

1. <the chapter's Practice items, verbatim>
```

Plain imperatives. No reference to "the chapter" that assumes it is open.
Confirm after appending that every other section is still present; the file is
shared and a rewrite that loses a section does not error.

## 6. Short-form (Substack, social)

The chapter rules apply unchanged and bite harder: the metaphor cap is per
1,000 words, so three anchor mentions in a 500-word post already read as six.
No em-dashes. One bold at most. No Stoic quotation whose citation is below
`verifiable` with a non-search `evidence_source`. No statistic invented to make
a hook land: a fabricated number in a post is the worst failure in this system
made public and permanent. Social posts are single posts, not threads.

## 7. Conformance is a separate reader

The chapter's outline section is its commission. A desk that wrote or edited
the prose does not judge whether it met the commission; `gw-specchecker` does,
with only the outline section and the prose in front of it. Two verdicts, PASS
and FAIL, a quote behind every PASS, and no third state. An outline revision
note inside the section (an italic or block-quoted line recording that a
requirement was deliberately removed and why) is part of the spec: a source
named only there is not commissioned.
