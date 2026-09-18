# Citation verification request — packet 1 of 5
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


### `cloud-townsend-boundaries`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Cloud & Townsend — Boundaries (Property-Line Metaphor)

**Source as recorded:** Henry Cloud & John Townsend, Boundaries: When to Say Yes, How to Say No to Take Control of Your Life (Zondervan, 1992; updated edition 2017). Confirmed via WebSearch this session (Wisconsin Lutheran Seminary summary, achology.com book overview, cloudtownsend.com) — the property-line metaphor, the "responsible to vs. responsible for" distinction, and the Law of Sowing and Reaping are all accurately represented.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, well-known, credentialed source (both authors are clinical psychologists) — this is not a listicle. Core concepts confirmed accurate via secondary summaries this session. Exact page numbers and verbatim wording of any direct quote still need confirmation against a physical/primary copy before manuscript use, per CLAUDE.md Rule 11 — cite the book by name and paraphrase the concepts rather than quoting verbatim until then, the same treatment already given to Glover's "No More Mr. Nice Guy" in Chapter 9.

---

### `epictetus-discourses-2-18-test-the-impression`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Epictetus — Discourses II.18: Put the Impression to the Test

**Source as recorded:** Epictetus, Discourses II.18. Widely circulated modern rendering; no single canonical translator is attached to this exact phrasing.

**Quote form:** paraphrase (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:**

> "Don't let the force of an impression when it first hits you knock you off your feet; just say to it, 'Hold on a moment; let me see who you are and what you represent. Let me put you to the test.'" — Epictetus, *Discourses* II.18

**What is already known to be uncertain:** The underlying passage (Discourses II.18, on not being carried away by a first impression) is real and locatable. The wording in the manuscript is a widely circulated modern rendering rather than a specific published translation, so no verbatim claim is being made and no translator can be credited. Author should confirm against a published translation before any pass treats it as a direct quotation.

---

### `epictetus-enchiridion-33-disciplined-speech`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Epictetus — Enchiridion 33: Disciplined, Not Total, Silence

**Source as recorded:** Enchiridion (Epictetus), chapter 33. Located via secondary aggregation (Perseus Digital Library indexing, MIT Classics summary) — WebFetch to the primary hosted texts was blocked by this session's network policy.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Upgraded from unverified during /book-chapter-refine 9 (2026-08-01): the chapter and its general content (restraint from gossip, trivial topics, blaming/praising/comparing others; speaking only when occasion genuinely calls for it) are corroborated across multiple independent secondary sources. The manuscript paraphrases this content rather than quoting a specific translation verbatim (logged as AI PARAPHRASE, not WEB VERIFY, in sources/citation-manifest.md, since there's no single exact wording being claimed as a direct quote). If a future revision wants a direct quotation instead of a paraphrase, confirm exact translation and wording (Elizabeth Carter's public-domain translation is the likely candidate) against primary text first.

---

### `epictetus-smoke-in-the-room`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Epictetus — "Smoke in the Room" Passage

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** The exact source location in the Discourses has not yet been identified. Needed as context for Ch 21 (endurance vs. cowardice). Do not invent the passage or its wording (CLAUDE.md Rule 3) — locate the exact source first.

---

### `glover-no-more-mr-nice-guy`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Glover — No More Mr. Nice Guy (Nice Guy Syndrome)

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Confirm the book's actual title/publication details (Robert Glover, "No More Mr. Nice Guy," 1st ed. 2003), and confirm the specific claims used in prose — particularly the "covert contract" mechanism (unstated expectation of reciprocity for compliance) — against the source text rather than secondhand summaries, before using as a named reference in the chapter. This is popular psychology, not peer-reviewed research; per CLAUDE.md Rule 3, verify it's being represented accurately and not presented with more evidentiary weight than a single author's clinical framework warrants.

---

### `gottman-four-horsemen`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Gottman — The Four Horsemen

**Source as recorded:** https://www.gottman.com/blog/the-four-horsemen-recognizing-criticism-contempt-defensiveness-and-stonewalling/

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** URL and specific statistics/study dates must be confirmed by a researcher agent before this appears in the manuscript. Do not resolve with fabricated numbers (CLAUDE.md Rule 3).

---

### `gottman-repair-attempts`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Gottman — Repair Attempts

**Source as recorded:** https://www.gottman.com/blog/r-is-for-repair/

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** URL and the underlying research (study details, what counts as a "repair attempt," predictive strength) must be confirmed by a researcher agent before this appears in the manuscript. Do not resolve with fabricated details (CLAUDE.md Rule 3).

---

### `gottman-turning-toward-bids`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Gottman — Bids for Connection and the Turning-Toward Rate (86% vs. 33%)

**Source as recorded:** Primary source is Gottman's own popular work, principally John M. Gottman & Joan DeClaire, The Relationship Cure (Crown, 2001), drawing on the Gottman "Love Lab" apartment-lab observational studies. Exact study, sample, and publication for the 86%/33% figures NOT yet pinned to a peer-reviewed citation.

**Quote form:** paraphrase (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** DO NOT put the numbers in prose until the primary is pinned down. What needs confirming: which study the 86%/33% figures come from, the sample and follow-up interval, and whether the figures are reported in a peer-reviewed paper or only in the trade books. Related caution: the widely repeated "94% divorce prediction accuracy" claim attached to Gottman's work is a known overclaim (it describes post-hoc model fit, not prospective prediction) and must NOT be used in this book under any framing. Author confirmation still required per CLAUDE.md Rule 11.

---
