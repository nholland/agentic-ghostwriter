# Citation verification request — packet 4 of 5
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


### `pillemer-long-marriages-learn-to-fight`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Pillemer — Long Marriages Don't Avoid Fighting, They Learn to Fight

**Source as recorded:** Karl Pillemer, *30 Lessons for Loving: Advice from the Wisest Americans on Love, Relationships, and Marriage* (New York: Hudson Street Press, 2015); Cornell Marriage Advice Project. Cornell Chronicle, June 2015 (HTTP 403); ScienceDaily mirror sciencedaily.com/releases/2015/06/150617134613.htm.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, locatable source identified (Pillemer, *30 Lessons for Loving*, 2015 / Cornell Marriage Advice Project: 700+ individuals in marriages of 30/40/50+ years, ~400-person random national survey of Americans 65+ plus 300+ in-person interviews, average marriage 44 years). The "learn to fight, not avoid it" finding is a confirmed attributed summary, not a verbatim quote — exact quotes and page numbers still need verbatim confirmation before manuscript use (Cornell article returned 403; fetch ScienceDaily mirror). Do not invent statistics (CLAUDE.md Rule 3).

---

### `sell-tooby-cosmides-2009-recalibrational-anger`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Sell, Tooby & Cosmides (2009) — Formidability and the Logic of Human Anger

**Source as recorded:** Aaron Sell, John Tooby, Leda Cosmides, "Formidability and the logic of human anger," Proceedings of the National Academy of Sciences 106(35), 2009.

**Quote form:** none (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, published, peer-reviewed paper; the recalibrational theory of anger is described accurately in Ch4. No wording is quoted, so there is no verbatim claim to check -- what needs confirming before print is that any figure or specific finding the prose attributes to it actually appears in the paper.

---

### `seneca-calm-not-root-out-emotions`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Seneca — "Reason wishes to give calm to our emotions, not to root them out"

**Source as recorded:** Seneca, *De Ira* (On Anger), Book II, §3. Cited and translated in Shermin Kruse J.D., "The Stoic's Guide to Caring Deeply Without Losing Yourself," *Psychology Today* (blog: The Stoic Heart, the Human Whole), updated November 14, 2025: https://www.psychologytoday.com/us/blog/the-stoic-heart-the-human-whole/202510/the-stoics-guide-to-caring-deeply-without-losing

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:**

> Latin: "Ratio affectibus tranquillitatem dare vult, non tollere." English: "Reason wishes to give calm to our emotions, not to root them out."

**What is already known to be uncertain:** Real primary source confirmed with book and section number (De Ira, Book II, §3) via the Psychology Today article (Kruse, 2025), which gives both the Latin ("Ratio affectibus tranquillitatem dare vult, non tollere") and the English ("Reason wishes to give calm to our emotions, not to root them out"). The quote is reproduced here from the secondary source; a researcher should still fetch *De Ira* II.3 directly to confirm the exact Latin and choose the preferred English translation before manuscript use. Do not alter the quote or invent a source location (CLAUDE.md Rule 3).

---

### `seneca-de-beneficiis-against-keeping-accounts`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Seneca — De Beneficiis: Against Keeping Accounts of Benefits Given

**Source as recorded:** Lucius Annaeus Seneca, De Beneficiis (On Benefits). Available in Miriam Griffin & Brad Inwood's translation (University of Chicago Press, "The Complete Works of Lucius Annaeus Seneca") and in older public-domain translations (Project Gutenberg, Wikisource).

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, locatable classical source — the treatise exists and this is its known central teaching per secondary summaries. Exact book/chapter location and verbatim translated wording for any direct quote are NOT yet confirmed — web-fetch access to the full primary text was unavailable during this research pass. A researcher must locate the specific book/chapter (the treatise has 7 books) and pull a verbatim quote in a citable translation before this is used as anything more than a paraphrased reference. Do not present a fabricated quote (CLAUDE.md Rule 3).

---

### `seneca-de-ira-on-anger`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Seneca — De Ira (On Anger)

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Specific passages about anger in close relationships, especially from Book III, still need to be located and extracted. Anchors Ch 4 (anger is failed leadership). Primary source exists but exact usable passages are not yet identified — do not invent quotes (CLAUDE.md Rule 3).

---

### `seneca-letter-81-wages-of-a-good-deed`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Seneca — Letters to Lucilius, Letter 81: The Wages of a Good Deed

**Source as recorded:** Seneca, Epistulae Morales ad Lucilium (Letters to Lucilius), Letter 81 ("On Benefits"). Commonly rendered: "The reward for all the virtues lies in the virtues themselves... the wages of a good deed is to have done it."

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real Senecan letter on the theme of benefits and gratitude, with reasonable secondary corroboration (Modern Stoicism, Donald Robertson's site, The Marginalian all reference the same passage and theme). Exact translation and line wording still need author confirmation against a physical edition before print use, per CLAUDE.md Rule 11. A companion Musonius Rufus line ("the greatest reward for a good deed is to have done it") was found during the same search but rejected as a source for this book: it only appears on quote-aggregator sites (Goodreads, QuoteFancy) with no traceable primary passage, so it does not meet this project's sourcing bar.

---

### `seneca-weep-but-not-wail`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Seneca — "We May Weep, But We Must Not Wail"

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real primary source, available at Wikisource and classics.mit.edu. Exact wording and translation should be confirmed and a specific edition selected before direct quoting. No URL fabricated — locate the specific passage before use.

---

### `tawwab-set-boundaries-find-peace`

**Tier 2** — a claim asserted in the compiled manuscript

**What we think it is:** Tawwab — Set Boundaries, Find Peace (Boundary as What You Will Do)

**Source as recorded:** Nedra Glover Tawwab, Set Boundaries, Find Peace: A Guide to Reclaiming Yourself (TarcherPerigee, 2021). Confirmed via WebSearch this session (Penguin Random House listing, mindtools.com and readingraphics.com summaries) — the definition and six-types framing are accurately represented; the exact wording of Tawwab's script formula was not independently located this session and should be treated as a paraphrase, not a verbatim quote, until confirmed.

**Quote form:** unset (verbatim = the wording must match exactly; paraphrase = only the claim needs to hold)

**Wording we currently have:** none recorded — we need the source's own words.

**What is already known to be uncertain:** Real, well-known source by a licensed therapist — not a listicle. Core definition and six-boundary-types framing confirmed via secondary summaries. The specific "when X, I feel Y, I need Z, if it continues I will..." script structure is a widely-taught boundary-setting formula associated with Tawwab's work but its exact verbatim phrasing in the book was not confirmed this session — present it in the manuscript as a paraphrased structure ("a version of the formula boundary-setting books like Tawwab's teach"), not a direct quotation, until verified against a physical copy per CLAUDE.md Rule 11.

---
