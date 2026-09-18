# Citation verification request — packet 5 of 5
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


### `wiesel-opposite-of-love-is-indifference`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Elie Wiesel — The Opposite of Love Is Indifference

**Source as recorded:** US News & World Report, October 27, 1986 interview. Corroborated across Quote Investigator, Goodreads, and multiple secondary sources. An earlier, closely related line appears in Wilhelm Stekel's "The Beloved Ego" (1921, trans. Rosalie Gabler), which Wiesel's 1986 phrasing likely echoes rather than originates outright.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Attribution and approximate date corroborated across independent secondary sources (Quote Investigator's own investigation is specifically reliable for tracing quote origins). Exact original magazine wording not independently read this session. Confirm final wording against the original US News & World Report piece or a reliable reprint before treating as a locked verbatim quote in print.

---
