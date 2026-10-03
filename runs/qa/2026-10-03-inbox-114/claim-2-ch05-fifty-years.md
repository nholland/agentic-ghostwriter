# Claim 2: Ch5, line 53. "The couples who stay married for fifty years"

Fact-Checker (gw-factchecker), inbox #114. Checked 2026-10-03 04:40 to 04:48.
Nothing inside `books/` was changed.

## The claim as printed

`books/the-stoic-husband/chapters/ch05/refined.md`, line 53 (same in
`refined-prev.md`; `draft.md` line 43 had "They just learned"):

> The couples who stay married for fifty years didn't avoid fighting. They
> learned, over thousands of small fights, that most of them didn't need a
> verdict. The fight about the dishes. The cold drive home. ...

Two sentences carry the factual weight:

| # | Sub-claim | Verdict |
|---|---|---|
| 2a | Couples in very long marriages did not avoid fighting | **Sourced**, book-level paraphrase of Pillemer. Existing concept, `verifiable` |
| 2b | They learned, over thousands of small fights, that most of them didn't need a verdict | **Not located in any source.** Stated as a fact about long-married couples; reads as the author's own conclusion |

## Step (a): what the OKF and runs already held

The digest missed an existing concept:

- `books/the-stoic-husband/okf/citations/pillemer-long-marriages-learn-to-fight.md`
  (`status: verifiable`, `quote_form: paraphrase`, `evidence_source:
  search-synthesis`, `chapter_slugs: [how-to-fight-without-becoming-small]`,
  which is Chapter 5's slug). Its body names the printed first sentence as
  "Usable framing: 'The couples who stay married for fifty years didn't avoid
  fighting.'" Its 2026-09-08 external check (confidence **low**) found the
  learn-to-fight framing "consistent with the book's described content but ...
  not located as a specific passage in any source opened here. It is a
  book-level paraphrase and should stay one."
- `books/the-stoic-husband/chapters/ch05/research.md`, Claim 4 (line 63-69)
  and New Research Items (line 125): the brief was looking for a study of
  long-married elders whose answer was "don't sweat the small stuff ... everything
  is small", marked RESEARCH NEEDED. The Pillemer concept's attribution
  warning records that "don't sweat the small stuff" is Richard Carlson (1997),
  not Pillemer. Line 127 lists Gottman's perpetual-problems finding as a further
  open research item. Neither was ever closed with a source for sentence 2b.
- `runs/ch05/` holds plate files and plate concepts only.

So 2a has a concept. 2b never did.

## Step (b): what the literature supports

### What I actually saw, and through what

Probe results as in claim 1. Pillemer's author site, Cornell Chronicle,
ScienceDaily, Refinery29, Goodreads-type reviews: all refused by the proxy
(403). Google Books in-book search: CAPTCHA. The Internet Archive's lending
copies are access-restricted and their text was not read.

| Evidence | Kind | What it showed |
|---|---|---|
| `https://archive.org/metadata/30lessonsforlovi0000pill/metadata` | catalogue record (bibliographic) | *30 lessons for loving*, Pillemer, Karl A.; Thorndike large-print edition, 2015, "Originally published: New York : Hudson Street Press, 2015". Full **table of contents** in the record. The second part is "Communication is the key" (Talk, talk, talk; No one is a mind reader; Mind your manners; All in good time; Three danger signs; Five secrets for great communication). Later lessons include "Give up grudges", "Lighten up", "Accept your partner as is". **No lesson title about fighting less, picking battles, or letting small fights go.** |
| `https://archive.org/metadata/30lessonsforlovi0000pill_w3v0/metadata` | catalogue record | Hudson Street Press 2015, ISBN 9781594631542, xxi + 280 pp. Publisher description: "From interviews with 700 elders"; asks "What are the secrets for improving communication and reducing conflict?" No average marriage length stated. |
| WebSearch: `Karl Pillemer 30 Lessons for Loving conflict lessons long-married elders "fight" advice small issues let go` | search-synthesis | Summaries say the elders advise letting some things go, that most disagreements "aren't worth more than a day's combat", and to ask "Is this really worth it?" before an argument. **Not seen on any page. Not usable as wording, and not confirmed as Pillemer's.** One summary names a part "Communication and Conflict"; the catalogue TOC calls it "Communication is the key", which is a small sign of how loosely these summaries handle the book. |
| WebSearch: `Gottman perpetual problems 69 percent "Seven Principles for Making Marriage Work" ...` (two queries) | search-synthesis | Many secondary pages attribute to Gottman that 69% of the problems couples argue about are perpetual and never get solved; couples who do well manage them through dialogue rather than solving them. Not seen on a page. Gottman's book itself located as a catalogue record: `https://archive.org/metadata/sevenprinciplesf00gott_0` (Three Rivers Press, 1999), access-restricted. |

### What the sources support

- **2a is fine.** Long-married elders in Pillemer's project teach how to fight,
  not how to avoid it, at book level (existing concept, external check). "Fifty
  years" is the author's round figure for "very long marriages", not a
  statistic. Pillemer's sample was 30, 40, 50+ years, averaging 43 or 44
  (defect #12, still open). The sentence names a group, not a number, so it does
  not need the average.
- The **nearest real research to 2b** is Gottman's perpetual-problems finding:
  most of what couples fight about never gets solved, and the couples who last
  live with that. It points the same way, but it is a different claim: it is
  about recurring problems being *managed*, not small fights being *let go*.
  Search-level only.

### What the sources do not support

- **2b, "they learned, over thousands of small fights, that most of them didn't
  need a verdict."** Not located in Pillemer, and not something Pillemer's own
  table of contents names. It is printed as a finding about what long-married
  couples learned. It is the author's own view-from-above reading, which is a
  good reading, but nothing found here lets the book present it as what those
  couples report.

## Proposed status

| Citation | status | quote_form | evidence_source | Why |
|---|---|---|---|---|
| `pillemer-long-marriages-learn-to-fight` (existing, sub-claim 2a) | `verifiable` (no change) | `paraphrase` (no change) | **`database-abstract`** (from `search-synthesis`) | The catalogue record is now the strongest evidence actually looked at: it confirms the book, publisher, 700 elders and table of contents. It does **not** confirm the fight lesson; the note says so. Proposed revision: `concepts/pillemer-long-marriages-learn-to-fight.md` |
| `gottman-perpetual-problems` (new draft gap) | `unverified` | `none` | `search-synthesis` | Only needed if the author picks option 3 below. 69% not seen on a page. Draft: `concepts/gottman-perpetual-problems.md` |
| Sentence 2b as printed | **not supportable as a finding** | n/a | n/a | No source located |

Nothing is `verified`.

## Candidate softened wordings for the author

Original second sentence (15 words): *"They learned, over thousands of small
fights, that most of them didn't need a verdict."*

The first sentence ("The couples who stay married for fifty years didn't avoid
fighting.") stays as it is. Word counts were checked by script.

1. *"I think they learned that most small fights never needed a verdict."*
   (12 words) Makes it the author's own read, which is what it is. No source
   needed.
2. *"Most small fights don't need a verdict. Long marriages seem to learn that."*
   (13 words) Puts the claim in the author's voice as a principle, with the
   long-married couples as an observation rather than a finding.
3. *"Plenty of what they fought about never got settled. It didn't need to be."*
   (14 words) Leans on Gottman's perpetual-problems finding. **Use only after**
   `gottman-perpetual-problems` is checked against a page. Its source is about
   couples in general, not fifty-year couples specifically.

Do not name Pillemer here. Chapter 7 introduces him for the first time ("There's
a researcher named Karl Pillemer..."), so naming him in Chapter 5 would break
that introduction.

## Recommended action

Soften the second sentence at the next `/gw-edit` of Chapter 5. Option 1 is
the safest and needs no further research. Land the Pillemer concept revision.
File the perpetual-problems concept only if option 3 is chosen. Proposed defect
entry: `proposed-citation-defects.md`, #15.
