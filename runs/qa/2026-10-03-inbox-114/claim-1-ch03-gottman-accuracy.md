# Claim 1: Ch3, line 43. Gottman's prediction accuracy

Fact-Checker (gw-factchecker), inbox #114. Checked 2026-10-03 04:40 to 04:48.
Nothing inside `books/` was changed.

## The claim as printed

`books/the-stoic-husband/chapters/ch03/refined.md`, line 43 (same text in
`refined-prev.md` line 43):

> John Gottman spent decades in a research lab watching couples argue. His team
> could predict which marriages would survive, just from watching how two people
> fight. They did it with above 90 percent accuracy, from samples as short as
> three minutes. His work puts defensiveness alongside contempt, stonewalling,
> and criticism as the behaviors most likely to end a marriage.

That is three separate claims:

| # | Sub-claim | Verdict |
|---|---|---|
| 1a | Defensiveness is one of four behaviors (with contempt, stonewalling, criticism) most predictive of divorce | **Sourced.** Existing concept, `verifiable` |
| 1b | "above 90 percent accuracy, from samples as short as three minutes" | **Not supportable as printed.** It joins two different findings, and the OKF already bars the number |
| 1c | "His team could predict which marriages would survive" | Partly supported. The studies were prospective, but the accuracy does not hold up when tested on new couples (see below). Minor; optional softening offered |

## Step (a): what the OKF and runs already held

The digest was wrong to say there was nothing. The OKF has a concept for this
passage, and that concept **forbids the number the prose prints**:

- `books/the-stoic-husband/okf/citations/gottman-four-horsemen.md`
  (`status: verifiable`, `quote_form: paraphrase`, `evidence_source: page-text`).
  Its `# Status` section says: "The 90%+ accuracy figure is confirmed as
  unusable, not merely absent - do not attach a divorce-prediction percentage
  to this citation." Its body records why: the figure comes from equations
  fitted and tested on the same couples, and when Heyman & Slep (2001) tested
  that kind of equation on fresh couples, positive predictive value fell to
  roughly 21-29%. The 2026-09-06 external check repeated the bar: "do not
  attach a universal divorce-prediction percentage to this."
- `books/the-stoic-husband/okf/citations/gottman-turning-toward-bids.md` and
  `okf/index.md` line 156 bar the related "94% accuracy" claim as "a known
  overclaim".
- `books/the-stoic-husband/chapters/ch03/research.md` line 15/18: the brief
  asked only for the Four Horsemen anchor ("RESEARCH NEEDED (fetch and verify
  URL above)"). It never asked for, or supplied, an accuracy figure or a
  three-minute figure.
- `runs/ch03/` holds plate files only. No research there.
- No concept anywhere in the OKF mentions "three minutes", Carrère, or
  thin-slice prediction (grep for `three minutes|3 minutes|carr[eè]re|first
  three minutes|thin.?slice`: no hits outside unrelated newlywed studies).

**Second defect found in passing:** `gottman-four-horsemen.md` lists
`chapter_slugs: [how-to-fight-without-becoming-small,
repair-quickly-love-deliberately, silence-is-not-peace]`. It does not list
Chapter 3's slug, `stop-defending-yourself`, even though its own body says
"defensiveness (Ch 3)". That is why a slug-based lookup for Chapter 3 would
miss the very concept that bars this number.

## Step (b): what the literature supports

### What I actually saw, and through what

Reachability was probed, not assumed (`scripts/verification_probe.py`,
2026-10-03 04:40): reachable hosts were archive.org, books.google.com,
classics.mit.edu, doi.org, en.wikisource.org, link.springer.com,
pubmed.ncbi.nlm.nih.gov, standardebooks.org, perseus.tufts.edu,
sciencedirect.com. In practice every page that carries these papers was refused
by the egress proxy (403 on CONNECT, organization policy): Wiley Online
Library, PMC, gottman.com, johngottman.net, washington.edu, ProQuest, Semantic
Scholar, academia.edu, web.archive.org. PubMed article pages answer with a
proof-of-work bot challenge, which I did not attempt to defeat. Google Books
in-book search redirects to a Google CAPTCHA.

**No source page was opened for this claim.** The evidence is:

| Evidence | Kind | What it showed |
|---|---|---|
| PubMed citation matcher, `https://pubmed.ncbi.nlm.nih.gov/api/citmatch/?method=heuristic&raw-text=...` | bibliographic record match | My full citation string for Carrère & Gottman (1999), *Family Process* 38(3):293-301, matched exactly one record, **PMID 10526767**. The title itself states the design: "Predicting divorce among newlyweds from the first three minutes of a marital conflict discussion." |
| Same matcher, Gottman & Levenson (1992), *JPSP* 63(2):221-33 | bibliographic record match | Matched **PMID 1403613**. Confirms the primary paper already recorded in `gottman-four-horsemen.md`. |
| WebSearch, 4 queries (listed below) | search-synthesis | Consistent across results: 124 newlywed couples; conflict discussion coded with SPAFF; first three minutes predicted divorce over six years. One summary gave an accuracy of 87.4%. **I did not see that number on any page and do not rely on it.** Separately, search summaries attribute "91 percent accuracy, averaged over three studies" to Gottman's book *The Seven Principles for Making Marriage Work* (1999), and "96 percent of the time you can predict the outcome of a *conversation* from its first three minutes" to the same book. Heyman & Slep (2001): on a held-out half, positive predictive value dropped from 65% to 29%, and to 21% at a realistic divorce rate. |

Search queries run (2026-10-03):
1. `Carrère Gottman 1999 "Predicting divorce among newlyweds from the first three minutes of a marital conflict discussion" Family Process`
2. `Carrère Gottman 1999 first three minutes newlyweds divorce prediction accuracy percent startup SPAFF 124 couples six years abstract`
3. `Heyman Slep 2001 "hazards of predicting divorce without crossvalidation" positive predictive value Gottman accuracy`
4. `Gottman "91 percent" OR "91%" accuracy predict divorce Seven Principles where does figure come from`
5. `Gottman "96 percent" first three minutes conversation outcome harsh startup Seven Principles`

URLs the searches returned and that I could **not** open (403): 
https://onlinelibrary.wiley.com/doi/10.1111/j.1545-5300.1999.00293.x ,
https://www.johngottman.net/wp-content/uploads/2011/05/Predicting-Divorce-among-Newlyweds-from-the-First-Three-Minutes-of-a-Marital-Conflict-Discussion.pdf ,
https://washington.edu/news/1999/09/27/first-three-minutes-of-discussion-about-on-going-area-of-marital-conflict-are-predictive-of-divorce-for-newlyweds ,
https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1741-3737.2001.00473.x ,
https://www.gottman.com/wp-content/uploads/EmpiricalBasis-Update3.pdf .

### What the source supports

- A real, peer-reviewed paper predicted divorce among newlyweds from **the first
  three minutes** of a conflict discussion (Carrère & Gottman, 1999). The title,
  confirmed by PubMed's own record match, says so. "Samples as short as three
  minutes" is therefore traceable to a real paper.
- Gottman's popular writing claims accuracy above 90% (91% per search
  summaries of *Seven Principles*; the OKF notes popular sources often repeat
  "93.6%"). Neither figure was seen on a page, and neither is tied, in anything
  I found, to a three-minute sample.
- Defensiveness as one of the Four Horsemen: sourced, see 1a.

### What the source does not support

- **"Above 90 percent accuracy, from samples as short as three minutes."** I
  found no source that reports above-90% divorce prediction from a three-minute
  sample. The three-minute paper is one study; the above-90% figures come from
  others. The sentence welds them. A likely origin, unconfirmed: the *Seven
  Principles* line about predicting a *conversation's* outcome from its first
  three minutes (96%) read as predicting a *marriage's* outcome.
- **Any above-90% figure at all.** The OKF has already ruled it out, for a
  documented reason: the high figures are fitted and scored on the same
  couples. On fresh couples the hit rate is far lower (Heyman & Slep, 2001).
  The prose prints the exact number the ledger says the book must not use.
- I could not trace the 87.4% figure to a page either, so it must not be used
  as a replacement.

**Plainly: the "above 90 percent" number cannot be traced to the three-minute
study, and the OKF had already barred it before Chapter 3 printed it.**

## Proposed status

| Citation | status | quote_form | evidence_source | Why |
|---|---|---|---|---|
| `gottman-four-horsemen` (existing, sub-claim 1a) | `verifiable` (no change) | `paraphrase` (no change) | `page-text` (no change, from the 2026-09-06 external check) | The four behaviors are confirmed on the Gottman Institute page. Proposed revision adds the Ch3 slug and records this defect: `concepts/gottman-four-horsemen.md` |
| `carrere-gottman-1999-first-three-minutes` (new draft) | `verifiable` | `paraphrase` | `database-abstract` | Real and locatable: PubMed record PMID 10526767 matched the full citation, and the title states the three-minute design. Supports *only* "three minutes predicted divorce in one study of newlyweds". No accuracy figure established. Draft: `concepts/carrere-gottman-1999-first-three-minutes.md` |
| The printed sentence, "above 90 percent accuracy, from samples as short as three minutes" | **not supportable** | n/a | n/a | No source joins the two halves; the number is barred by the existing ledger |

Nothing is `verified`. Only the author can set that, against his own copy.

## Candidate softened wordings for the author

Original sentence (15 words): *"They did it with above 90 percent accuracy, from
samples as short as three minutes."*

Each option keeps the paragraph's next sentence ("His work puts defensiveness
alongside...") unchanged. Word counts were checked by script.

1. **Cut the sentence** (0 words). The paragraph still reads cleanly:
   "...just from watching how two people fight. His work puts defensiveness
   alongside contempt..." No number, nothing to source. Safest.
2. *"In one study, the first three minutes of a fight told them a lot."*
   (14 words) Keeps the three minutes, which Carrère & Gottman (1999) supports.
   Drops the percentage.
3. *"Even the first three minutes of a single argument gave them something to go on."*
   (15 words) Same support as option 2, a little warmer in rhythm.

Optional, lower priority. The sentence before it, *"His team could predict
which marriages would survive, just from watching how two people fight."* (15
words), claims more than the cross-validation evidence allows. If the author
wants it tighter: *"His team learned to spot marriages in trouble just from watching
two people fight."* (14 words).

## Recommended action

Soften at the next `/gw-edit` of Chapter 3, using one of the options above,
with the author's approval of the exact words first. Land the
`gottman-four-horsemen.md` revision (adds `stop-defending-yourself` to
`chapter_slugs`) and, if option 2 or 3 is chosen, the new Carrère & Gottman
concept. Proposed defect entry: `proposed-citation-defects.md`, #14.
