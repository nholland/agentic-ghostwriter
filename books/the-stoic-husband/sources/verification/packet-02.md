# Citation verification request — packet 2 of 5
### the-stoic-husband

You are checking quotations and claims for a nonfiction book. Accuracy matters
more than completeness. **A confident wrong answer here ends up printed.**

## The one rule that matters

**"NOT_FOUND" is a correct and welcome answer.** It is not a failure and it is
not a disappointment. Roughly a third of these may be unfindable, misattributed,
or subtly different from what is recorded below, and finding that out is the
entire point of the exercise. Do not stretch to confirm something. Do not
reason from what a source "would" say. Do not treat a quote appearing on
quote-aggregator sites, Goodreads, Pinterest, or a blog as evidence — those are
where misattributions breed, and several entries below are suspected to have
come from exactly there.

## What counts as evidence

- A scan, facsimile, or full-text edition of the actual work (archive.org,
  Project Gutenberg, Wikisource, Perseus, Standard Ebooks, a publisher's
  preview, Google Books page images).
- A journal's own page for a paper: abstract, DOI record, or full text.
- **Not** evidence: a quote site, a listicle, an AI summary, another chatbot,
  or "commonly attributed to."

If you can open the actual text, transcribe what you SEE. If your only access
is a secondary source, say so in `notes` and set `confidence` to low.

## Editions matter here

This book is standardizing on **public-domain translations**: George Long for
Marcus Aurelius and Epictetus, Richard Gummere (Loeb) for Seneca's letters.
Where an entry names a different translator, report BOTH: what the named
translator says, and what Long/Gummere say. Translations of the same passage
differ enough that a reader comparing editions will notice.

Report the **translator and year** every time. "Meditations 4.49" without an
edition is not a verified quote, because the wordings genuinely differ.

**Standing request, and it applies to every Marcus Aurelius and Epictetus entry
below regardless of what translator that entry names: give me George Long's
wording specifically.** Long is the house standard because he is public domain
and this book is self-published. Where an entry currently records Hays,
Farquharson, Haines, Carter, Matheson, or Oldfather, report that translator's
wording *and* Long's, clearly labelled. An entry confirmed only in a
copyrighted translation does not close, because the book cannot print it.

Long's Marcus Aurelius and Epictetus are both on Wikisource and archive.org in
full text.

## Output format

Return a JSON array, one object per entry, nothing else. Use exactly this shape:

```json
{
  "slug": "<the slug exactly as given>",
  "verdict": "CONFIRMED | DIFFERENT_WORDING | WRONG_LOCATOR | PARTIAL | NOT_FOUND | SOURCE_DOES_NOT_SAY_THIS | WRONG_ATTRIBUTION",
  "edition": "<translator/editor, publisher, year — or null>",
  "url": "<direct URL to the page you actually opened — or null>",
  "exact_text": "<what the source actually says, transcribed from what you saw — or null>",
  "surrounding_context": "<~40 words around it, so a reader can confirm you were on the right page — or null>",
  "locator": "<book/section/letter/page as the source numbers it — or null>",
  "notes": "<anything that would change the verdict; disagreements between editions; why not found>",
  "confidence": "high | medium | low"
}
```

Field notes:
- `exact_text` — transcribe it. Do not normalize punctuation, do not modernize
  spelling, do not fix what looks like an error. If the source has a dash, keep
  the dash. The book has a house rule about punctuation inside quotations and
  needs to know what the translator actually printed.
- `surrounding_context` — this is the anti-hallucination check. If you cannot
  produce it, you did not open the source, and the verdict should be NOT_FOUND.
- `WRONG_ATTRIBUTION` — the text exists but belongs to someone else, or to a
  different work by the same author. Say who or what in `notes`.
- `WRONG_LOCATOR` — **check this on every entry.** The wording is right but the
  book, section, or letter number we recorded is wrong. This is the single most
  common defect found so far: three of eight entries in one packet had the
  right words under the wrong number. Give the correct locator.
- `PARTIAL` — the wording is genuine but we have misrepresented how it appears:
  two separated passages spliced into one continuous quotation, a fragment
  presented as a whole sentence, a mid-sentence excerpt capitalized as if it
  began one. Say exactly what the source does instead.

---

## Entries


### `gunnysacking-stored-grievances`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Gunnysacking — Stored Grievances

**Source as recorded:** General usage term, corroborated across Wikipedia, counseling-practice blogs, and academic references to "joint gunnysacking" in relational conflict research. Sometimes attributed to George Bach (co-author of "The Intimate Enemy," 1968) but this attribution was not independently confirmed in this session's research.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** The term and mechanism are real and widely used in relationship-coaching and conflict-resolution contexts, but a single canonical originating source was not confirmed. Do not attribute the term to George Bach (or any other named originator) in prose without further verification — use it unattributed, the same treatment already given to the Nail Parable (see /okf/frameworks/the-nail-parable.md).

---

### `household-labor-and-caretaker-burden`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Household Labor Distribution and Caretaker Burden Research

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Author asked directly whether research exists on the feeling that a home-managing spouse's work never has a stopping point. Look for division-of-household-labor / cognitive-load research (e.g., Hochschild's "second shift" framing, or more recent studies on perceived fairness in household labor division and marital satisfaction). Must find framing that doesn't rely on "emotional labor," "mental load," or other terms 02-audience.md flags as off-register for this book's voice. Confirm a specific, citable study or finding before use.

---

### `jack-dill-1992-silencing-the-self`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Jack & Dill (1992) — The Silencing the Self Scale

**Source as recorded:** Jack, D. C., & Dill, D. (1992). The Silencing the Self Scale: Schemas of intimacy associated with depression in women. Psychology of Women Quarterly, 16(1), 97-106.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, foundational, heavily-cited scale — corroborated across SAGE, Wiley, ScienceDirect, and a 2025 Sex Roles narrative review citing 126 studies using the scale. Full original article not independently read this session. Important scope limit: the original scale and theory were built on women's depression risk, tied to traditional gender-role socialization — do not present it as a men's-specific finding. Frame it in prose as "the pattern researchers call self-silencing," not as a study of husbands, and flag the men's comparative literature (Sex Roles/ScienceDirect result on self-silencing in women and men) as a secondary, not primary, source for that extension.

---

### `marcus-aurelius-born-to-act`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — "You Weren't Born to Stay Under the Covers" (Meditations 5.1)

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:**

> "At dawn, when you have trouble getting out of bed, tell yourself: I have to go to work — as a human being. What do I have to complain about, if I'm going to do what I was born for, the things I came into the world to do?" — *Meditations* 5.1 (translation and exact wording to be confirmed against a physical copy)

**What is already known to be uncertain:** Meditations 5.1 is a real, well-known passage (Marcus talking himself out of bed at dawn, e.g. Hays' translation: "At dawn, when you have trouble getting out of bed, tell yourself: I have to go to work — as a human being. What do I have to complain about, if I'm going to do what I was born for...") The author's recalled phrasing is a paraphrase, not a verbatim quote. Author should confirm exact wording and translation against a physical copy before the chapter quotes it directly; until then, paraphrase rather than quote verbatim.

---

### `marcus-aurelius-concealing-thoughts`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — Meditations 12.4: Concealing Our Thoughts

**Source as recorded:** Widely attributed to Meditations, Book 12, section 4 (Gregory Hays translation). Located via secondary aggregation of search results, not a direct read of the primary text — WebFetch to primary classical-text hosts (Perseus, Wikisource) was blocked by this session's network policy.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Upgraded from unverified during /book-chapter-refine 9 (2026-08-01): book/section (12.4) and the Hays-translation wording are corroborated across multiple independent secondary sources (consistent match, meets the citation-manifest's WEB VERIFY bar), but no primary text or scanned original was directly read this session (WebFetch to Perseus/Wikisource blocked by network policy both times it was attempted). The manuscript quotes this without an em-dash (rendered with commas/periods instead) since the em-dash appearing in some secondary renderings hasn't been confirmed as the translator's own punctuation. Per CLAUDE.md Rule 11, status stays at `verifiable`, not `verified` — only the author can upgrade further, after confirming exact wording (and whether the em-dash is genuine) against their physical copy of Hays's translation.

---

### `marcus-aurelius-impermanence-and-gratitude`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — Impermanence and Gratitude in Meditations

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Specific passages have not yet been identified — the source material notes "the memento mori passages that are relevant to marriage rather than death broadly" still need to be located. Anchors Ch 25 and Ch 26. Do not invent passages (CLAUDE.md Rule 3).

---

### `marcus-aurelius-instruct-or-bear-with-them`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — "Either Instruct Them or Bear with Them"

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real primary source. Specific translation and exact wording should be confirmed and a specific edition selected before direct quoting. No URL fabricated.

---

### `marcus-aurelius-meditations-book7-no-repayment`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — Meditations Book 7: Against Seeking Credit or Repayment for Good Deeds

**Source as recorded:** Marcus Aurelius, Meditations, Book 7. Widely rendered across translations (George Long, Gregory Hays, Robin Hard); commonly cited around passage 7.73 in some numbering schemes, though numbering varies significantly by translation/edition.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:**

> "When you have done a good act and another has received it, why do you still look for a third thing besides — credit for having done good, or a return for it?"

**What is already known to be uncertain:** Real, locatable passage in Meditations Book 7 — the idea and approximate wording are well attested across multiple secondary sources, but exact verse numbering and the precise translated wording to use have NOT been confirmed against a specific edition. Different translations number Book 7 passages differently. A researcher must pick a specific translation (check which one the author owns/prefers — see CLAUDE.md Rule 11 on verifying against the author's physical copy), locate the exact passage number in that edition, and confirm verbatim wording before manuscript use.

---
