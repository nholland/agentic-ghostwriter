# Claim 3: Ch7, line 25. "Thirteen years of data on more than 7,000 couples"

Fact-Checker (gw-factchecker), inbox #114. Checked 2026-10-03 04:40 to 04:48.
Nothing inside `books/` was changed.

## The claim as printed

`books/the-stoic-husband/chapters/ch07/refined.md`, line 25:

> A separate, much larger study, thirteen years of data on more than 7,000
> couples, found something that points in the same direction. People who kept
> close track of what they were owed, expecting their giving to be matched
> back, saw their satisfaction erode over time. Most couples loosen that
> expectation naturally as the relationship deepens. The ones who don't tend to
> drift.

## Step (a): what the OKF and runs already held

**This claim is already sourced.** The digest missed it.

- `books/the-stoic-husband/okf/citations/park-et-al-2025-pay-me-back-exchange-orientation.md`
  (`status: verifiable`, `quote_form: paraphrase`, `evidence_source:
  database-abstract`, `chapter_slugs: [the-end-of-scorekeeping]`, which is
  Chapter 7's slug). Park, H. G., Johnson, M. D., Gordon, A. M., & Impett, E. A.
  (2025). "'Pay Me Back': Testing the Implications of Long-Term Changes and
  Partner Similarity in Exchange Orientation Within Intimate Relationships."
  *Personality and Social Psychology Bulletin*. DOI 10.1177/01461672251330700.
  Its 2026-09-08 external check (confidence medium) quotes the published
  abstract from PMC: 13 years of longitudinal data, a national sample of
  romantic couples in Germany, N = 7,293 couples; partners on average declined
  in exchange orientation; those who held on to it longer saw steeper declines
  in satisfaction. That check added a caveat: "German national sample, so say so
  rather than implying US data."
- `books/the-stoic-husband/chapters/ch07/research.md` line 44 assigns this
  concept to the claim.
- `books/the-stoic-husband/chapters/ch07/draft.md` line 50 (drafter's note)
  records the choice: "The Park et al. German study is paraphrased without the
  study name ('thirteen years of data on more than 7,000 couples') — no author
  names cited per the voice register."
- `runs/ch07/plate-notes.md` lines 43 and 118 keep the number off the plate,
  correctly.

## Step (b): checking the claim against the source

### What I actually saw, and through what

PMC and SAGE pages: refused by the proxy (403, organization policy). PsyPost:
403. PubMed article page: bot challenge, not attempted.

| Evidence | Kind | What it showed |
|---|---|---|
| PubMed citation matcher, `https://pubmed.ncbi.nlm.nih.gov/api/citmatch/?method=heuristic&raw-text=Park HG, Johnson MD, Gordon AM, Impett EA. Pay Me Back: ... Pers Soc Psychol Bull. 2025` | bibliographic record match | Exactly one record: **PMID 40326353**. The paper is indexed in PubMed under these authors, this title and this journal. |
| WebSearch: `Park Johnson Gordon Impett 2025 "Pay Me Back" exchange orientation 7,293 couples pairfam Personality and Social Psychology Bulletin` | search-synthesis | Returned the SAGE DOI page, the PMC page (PMC13310269) and PsyPost. Summary consistent with the concept: 13 years, national sample of couples in Germany, N = 7,293; general decline in exchange orientation; slower declines went with steeper declines in satisfaction; within-person increases predicted later decreases; no partner-similarity effects. First published online May 2025. |
| Existing concept's 2026-09-08 external check | abstract text, quoted in the concept | As above. That is the strongest evidence on file, and it is why the concept's `evidence_source` is `database-abstract`. |

### Line by line

| Printed | Source | Holds? |
|---|---|---|
| "a separate, much larger study" | 7,293 couples vs Pillemer's 700 individuals | Yes |
| "thirteen years of data" | longitudinal data spanning 13 years | Yes |
| "on more than 7,000 couples" | N = 7,293 couples | Yes |
| "People who kept close track of what they were owed, expecting their giving to be matched back" | exchange orientation: expecting direct reciprocation when giving a benefit | Yes, as a paraphrase. "Kept close track" is a gloss: the study measured an expectation, not literal record-keeping. Acceptable in this register |
| "saw their satisfaction erode over time" | slower declines in exchange orientation went with steeper declines in satisfaction; increases predicted later decreases | Yes. Strictly it is *faster* erosion, relative to others, and it is an association, not proof of cause. Fine for a paraphrase |
| "Most couples loosen that expectation naturally as the relationship deepens" | on average, exchange orientation declined over the relationship | Yes |
| "The ones who don't tend to drift." | satisfaction declined more steeply | Mostly. "Drift" reads as growing apart, which matches lower satisfaction. The study did not measure separation, so "drift" should not be read as breakup |

**Not disclosed in the prose:** the sample is German. The prose does not claim
American data, so this is not an error, but the 2026-09-08 check asked for it.
Author's call.

## Proposed status

| Citation | status | quote_form | evidence_source | Why |
|---|---|---|---|---|
| `park-et-al-2025-pay-me-back-exchange-orientation` (existing) | `verifiable` (no change) | `paraphrase` (no change) | `database-abstract` (no change) | Today's check added a PubMed record match (PMID 40326353) and consistent search results. No page was opened from here, so the evidence axis does not rise. Proposed revision records today's line-by-line check and the PMID: `concepts/park-et-al-2025-pay-me-back-exchange-orientation.md` |

Nothing is `verified`.

## Softened wordings

Not required: the claim is supported. One optional precision, for the author
only if he wants it, not a correction:

- To name the sample, as the 2026-09-08 check suggested: *"A separate, much
  larger study, thirteen years of data on more than 7,000 couples in Germany,
  found something that points in the same direction."* This is two words longer
  than the printed sentence.

## Recommended action

No prose change needed. Land the concept revision (adds the PMID and today's
line check). The German-sample note is the author's call.
