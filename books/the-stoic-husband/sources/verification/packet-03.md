# Citation verification request — packet 3 of 5
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


### `marcus-aurelius-on-correction-and-tolerance`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — Bad Breath, Tolerance, and the Virtue of Being Wrong (Meditations 5.28)

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:**

> "Art thou angry with him whose armpits stink? Art thou angry with him whose mouth smells foul? What good will this anger do thee? He has such a mouth, he has such armpits: it is necessary that such an emanation must come from such things." — Meditations 5.28 (translation to be confirmed)

**What is already known to be uncertain:** Meditations 5.28 is a real, frequently-cited passage — but translations vary significantly in wording (the version supplied reads in an older/public-domain style, likely Long's translation). Author should confirm the exact translation and wording against their physical copy before quoting directly. The Robertson attribution (How to Think Like a Roman Emperor, Ch6: The Virtue of Justice) should also be confirmed against a physical copy if Robertson is named in the book — if the chapter instead presents the "welcoming correction" reframe as a direct application of 5.28 without naming Robertson, that attribution check isn't needed.

---

### `marcus-aurelius-power-over-your-mind-condensation`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus Aurelius — "You Have Power Over Your Mind" (Modern Condensation)

**Source as recorded:** Commonly attributed to Marcus Aurelius, Meditations, loosely associated with Book 2 / Book 12. Not a verbatim line in any standard translation (Hays / Farquharson / Long).

**Quote form:** paraphrase (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:**

> "You have power over your mind, not outside events. Realize this, and you will find strength." — *Meditations* (uncited in text)

**What is already known to be uncertain:** This is the famous modern condensation of Meditations, not a verbatim line from any single standard translation. The manuscript claims no book or section for it, and none should be added. Treat as a widely-known paraphrase. Status is `unverified` rather than `verifiable` because the attribution itself -- not just the wording -- is unconfirmed against any primary text.

---

### `marcus-newhall-2000-displaced-aggression`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Marcus-Newhall et al. (2000) — Displaced Aggression Is Alive and Well

**Source as recorded:** Marcus-Newhall, A., Pedersen, W. C., Carlson, M., & Miller, N. (2000). Displaced aggression is alive and well: A meta-analytic review. Journal of Personality and Social Psychology, 78(4), 670-689.

**Quote form:** paraphrase (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Full text not retrieved this session (PubMed blocked by egress proxy; publicly hosted PDF mirrors not fetched). Effect size (+0.54) and the three moderator findings are consistent across the Semantic Scholar listing, a Wiley reference-work chapter, and a JSTAGE review. Confirm the effect size and the triggered-displaced-aggression framing against the primary before any figure appears in prose — and note that the book should almost certainly NOT print the number at all (see below). Author confirmation required per CLAUDE.md Rule 11.

---

### `musonius-rufus-on-marriage`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Musonius Rufus on Marriage

**Source as recorded:** https://sites.google.com/site/thestoiclife/the_teachers/musonius-rufus/lectures

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real primary source — Lectures III, IV, XIII, XIV. Researcher agents should fetch and extract direct quotes (the most vivid quotes on marriage as community of life and mutual devotion) for use as primary-source quotes, not paraphrase.

---

### `pillemer-communication-is-paramount`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Pillemer — Communication Is Paramount

**Source as recorded:** Karl Pillemer, *30 Lessons for Loving: Advice from the Wisest Americans on Love, Relationships, and Marriage* (New York: Hudson Street Press, 2015); Cornell Marriage Advice Project. Cornell Chronicle, June 2015 (news.cornell.edu/stories/2015/06/gerontologist-finds-formula-happy-marriage) — primary article returned HTTP 403; ScienceDaily mirror at sciencedaily.com/releases/2015/06/150617134613.htm.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, locatable source identified (Pillemer, *30 Lessons for Loving*, 2015 / Cornell Marriage Advice Project). Exact quotes and page numbers still need verbatim confirmation before manuscript use — the Cornell Chronicle article returned 403, so a researcher should fetch the ScienceDaily mirror for verbatim Pillemer quotes. The phrases "talk, talk, talk" and "most marital problems can be solved through open communication" are confirmed attributed *summaries* from secondary coverage, not direct quotes — do not present as quotations without fetching the primary source. Do not invent statistics (CLAUDE.md Rule 3).

---

### `pillemer-dont-keep-score`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Pillemer — Don't Keep Score

**Source as recorded:** Karl Pillemer, *30 Lessons for Loving: Advice from the Wisest Americans on Love, Relationships, and Marriage* (New York: Hudson Street Press, 2015); Cornell Marriage Advice Project. Cornell Chronicle, June 2015 (HTTP 403); ScienceDaily mirror sciencedaily.com/releases/2015/06/150617134613.htm.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, locatable source identified (Pillemer, *30 Lessons for Loving*, 2015 / Cornell Marriage Advice Project). The "don't keep score / give more than you get" finding is a confirmed attributed summary from the source, not a verbatim quote — exact quotes and page numbers still need verbatim confirmation before manuscript use (Cornell article returned 403; fetch ScienceDaily mirror). Do not invent statistics (CLAUDE.md Rule 3).

---

### `pillemer-five-major-stressors`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Pillemer — The Five Major Stressors in Long Marriages

**Source as recorded:** Karl Pillemer, *30 Lessons for Loving: Advice from the Wisest Americans on Love, Relationships, and Marriage* (Hudson Street Press / Plume, 2015); Cornell Marriage Advice Project — 700+ individuals in marriages of 30 to 50+ years, average 44 years, combining a national survey of Americans 65+ with 300+ in-person follow-up interviews. Local intake: `sources/articles/pillemer-cornell-marriage-advice.md`.

**Quote form:** none (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** The five-stressor framing was corroborated 2026-08-17 at publisher and book-description level (Penguin Random House, Barnes & Noble, Publishers Weekly listings all describe the book breaking conflict down by "five major stressors" with rules for in-laws and household labor). That is enough to cite the finding; it is NOT enough to quote. No verbatim wording was obtained — Cornell's own page returns HTTP 403 and this session's environment blocked external WebFetch entirely. `quote_form: none` is deliberate: cite the finding in prose, never a Pillemer quotation, until the author checks a physical copy. Do not attach percentages to it; none were confirmed (CLAUDE.md Rule 3).

---

### `pillemer-friendship-as-important-as-love`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Pillemer — Friendship as Important as Love

**Source as recorded:** Karl Pillemer, *30 Lessons for Loving: Advice from the Wisest Americans on Love, Relationships, and Marriage* (New York: Hudson Street Press, 2015); Cornell Marriage Advice Project. Cornell Chronicle, June 2015 (HTTP 403); ScienceDaily mirror sciencedaily.com/releases/2015/06/150617134613.htm.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, locatable source identified (Pillemer, *30 Lessons for Loving*, 2015 / Cornell Marriage Advice Project). The friendship finding is a confirmed attributed summary, not a verbatim quote — exact quotes and page numbers still need verbatim confirmation before manuscript use (Cornell article returned 403; fetch ScienceDaily mirror). Do not invent statistics (CLAUDE.md Rule 3).

---
