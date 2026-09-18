# Chapter 12 — Research Brief, Round 2

**Chapter:** Romance Is a Discipline
**Book:** *River, Oak, Sun: The Stoic Husband*
**Cell:** Sun × Wisdom — Love as Ongoing Practice. Failure mode: The Trophy Mistake.
**Target:** 1,000–1,300 words. **Current state: 1,202 words of prose, refined and finished.**
**Desk:** The Researcher (cold sub-agent)
**Built:** 2026-09-16 11:25
**Supersedes:** nothing. `runs/ch12/research.md` still stands except where this file
names a correction. Read that file for the chapter's ruled material (the
grandfather, the bare-minimum line, the Walgreens exclusion, the Ch12/Ch13
boundary, the metaphor-family declaration). Read **this** file for what changed.

> **This is a brief for a revision, not a rewrite.** The chapter works. Everything
> below is ranked by whether it earns a place in a chapter that is already full,
> and §7 does the arithmetic on what comes out to pay for what goes in.

**Inputs read this round:** `runs/ch12/research.md`, `runs/ch12/refined.md`,
`runs/ch12/interview.md`, `00-premise.md`, `01-voice.md`, `02-audience.md`,
`03-outline.md` (Ch12), `04-archetype.md`, `05-framework.md`, `06-sources.md`,
`okf/index.md` and the Ch12/Ch13-tagged concepts, `sources/interview-author-stories.md`,
`sources/audience-signals.md`, the refined chapters Ch10 and Ch11, plus the
author's round-3 rulings as relayed in the dispatch.

---

## 0. What this round changed, in one table

| | Round 1 said | Round 2 says |
|---|---|---|
| Reachability | "Every publisher and repository host is blocked. No primary text was read." | **Wrong as a generalisation.** Project Gutenberg and archive.org are reachable. Two classical primary texts were retrieved and read in full. See §1. |
| *Meditations* IV.24 | Wording unreachable; print no quotation. | **Wording retrieved and read.** The chapter may now quote Long if it wants to. §2. |
| Democritus | Assumed, unexamined. | **LIVE DEFECT IN THE PRINTED CHAPTER.** Long does not name Democritus. §2. |
| Five love languages | "DO NOT BUILD ON IT." Do not name it. | **Author ruling reverses this.** It stays, calibrated. And round 1's summary of the evidence was itself too strong. §3. |
| Perceived partner responsiveness | Primary not pinned; carry the idea unattributed. | **Both primaries pinned** (Reis & Shaver 1988; Reis, Clark & Holmes 2004). §4.2. |
| Why effort declines | No evidence; supported by analogy only. | **Two real sources**, one meta-analytic and one longitudinal. §4.1. This is the biggest gain of the round. |
| "A date a week" | Not investigated. | **Traced.** It is a National Marriage Project survey report, not a peer-reviewed dose. The chapter's existing sentence is safe as written. §4.4. |
| Gordon et al. 2012 DOI | Unconfirmed. | Corroborated at search level: `10.1037/a0028723`. §4.3. |
| Inbox #008 (may the chapter build a scene?) | Open; a composite was written as a placeholder. | **Closed by the author's round-3 material.** He supplied a real scene. §5. |
| Inbox #009 (a concrete instance for the platinum paragraph) | Open; the faucet composite was written as a placeholder. | **Closed by the author's round-3 material.** And the placeholder is now factually backwards. §6.2. |

---

## 1. What was reachable, and how — read this before believing any "blocked"

Round 1 concluded that everything was blocked and reached no primary source. That
conclusion was over-general and it cost the chapter a printed defect. Here is the
actual map, tested this session rather than assumed.

**Reachable, content retrieved and read:**

| Host | What was taken from it |
|---|---|
| `www.gutenberg.org` | George Long's *Meditations* in full (ebook #15877) and Aubrey Stewart's Seneca *Minor Dialogues* in full (ebook #64576). Both read directly. |
| `archive.org` | Responds. Not needed this round. |
| WebSearch (the tool) | Every research citation in §4. Returns abstract-level summaries with converging bibliographic detail. |

**Refused — `403` on CONNECT from the egress proxy, confirmed at
`$HTTPS_PROXY/__agentproxy/status`:**

`doi.org`, `api.crossref.org`, `openalex.org`, `semanticscholar.org`,
`pmc.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`, `eutils.ncbi.nlm.nih.gov`,
`arxiv.org`, `psyarxiv.com`, `osf.io`, `europepmc.org`, `openlibrary.org`,
`jstor.org`, `scholar.google.com`, `researchgate.net`, `journals.sagepub.com`,
`onlinelibrary.wiley.com`, `tandfonline.com`, `apa.org`, `en.wikipedia.org`,
`gottman.com`, and every university-hosted author PDF tried
(`sas.rochester.edu`, `people.uncw.edu`, `files.blogs.baruch.cuny.edu`,
`affective-science.org`, `scottbarrykaufman.com`, `columbia.edu`).

**Reachable but unusable:** `pubmed.ncbi.nlm.nih.gov` returns HTTP 200 and then
serves a cookie/proof-of-work challenge page instead of the record, to `curl` and
to WebFetch alike. **The caller's "PubMed is reachable (203)" test measured the
status line, not the body.** PubMed is a status code, not a source, in this
environment.

**The rule that follows, for anyone reading this after me:** public-domain text
hosts work and scholarly hosts do not. So the open lane is genuinely open for
**Marcus, Epictetus, Seneca and anything else pre-1929** — which is most of what
this book quotes verbatim — and genuinely closed for **relationship science**,
which this book only ever paraphrases. That is a workable split, and it means the
evidence bar in `06-sources.md` can be met for the quotations that matter.

---

## 2. Marcus and Democritus — the corrected position, and a live defect

### 2.1 What Long actually says

Retrieved and read 2026-09-16 from Project Gutenberg #15877, *Thoughts of Marcus
Aurelius Antoninus*, trans. George Long:

> 24. Occupy thyself with few things, says the philosopher, if thou wouldst be
> tranquil.--But consider if it would not be better to say, Do what is necessary,
> and whatever the reason of the animal which is naturally social requires, and
> as it requires. For this brings not only the tranquillity which comes from
> doing well, but also that which comes from doing few things.

**"Says the philosopher." Long names nobody.** A search of the whole Long file for
"Democritus" returns three hits, all elsewhere in the book, none at IV.24, and
Long attaches no editorial note to IV.24 naming him.

### 2.2 The defect

The refined chapter prints:

> In 4.24 he picks up an old line **he credits to the philosopher Democritus**:
> if you want to be untroubled, do few things.

That is a claim about an act Marcus performed. In the house edition he did not
perform it. The Democritus name is **editorial apparatus** — it comes from
commentators, principally A. S. L. Farquharson, who identifies the maxim as
Democritus's via Stobaeus, and from modern translations (Hays among them) that
print the name in the text. `06-sources.md` already lists Farquharson as
rights-ambiguous and not house standard.

Concept: `runs/ch12/okf/citations/meditations-4-24-democritus-ascription-defect.md`

### 2.3 The repair — do this one

**Cut the name.** Two words, no restructuring:

> In 4.24 he picks up an old line about doing few things: if you want to be
> untroubled, do few things.

Or, keeping the rhythm the sentence already has: *"he picks up an old line from
some philosopher he doesn't bother to name."* That is true, faithful to Long, and
better in this book's voice than the original — it makes Marcus sound like a man
writing to himself, which is the whole point of the *Meditations* framing the
chapter already uses.

**Two alternatives, if the author wants Democritus kept.**

- *Attribute the identification rather than the text:* "a line later scholars
  trace to Democritus." True. Costs four words.
- *Attribute it through Seneca.* Now available, public domain, retrieved and read
  from Gutenberg #64576 — Seneca, "Of Anger" III.6, trans. Aubrey Stewart: *"that
  sound maxim of Democritus which defines peace of mind to consist in not
  labouring much, or too much for our strength, either in public or private
  matters."* This is real evidence and it is inside the book's own tradition. It
  is also a **second classical citation in a chapter with no room**, and
  `04-archetype.md` sets citation density low. Recommended only on request.
  Concept: `runs/ch12/okf/citations/seneca-de-ira-3-6-democritus-tranquillity.md`

### 2.4 The quotation question, now reopened

Round 1 ruled *this chapter prints no quotation from Marcus*, because the wording
could not be reached. **That ruling was forced by an evidence limit that no longer
exists.** The text is in hand, in the house translator, in the public domain.

**My read: leave the chapter as it is, carrying the idea in plain English.** Three
reasons. `06-sources.md` pre-authorises exactly this ("where a Long passage would
fight the register badly, prefer rendering the idea in the author's own words"),
and Long's *thee/thou* is the case that caveat was written for. The chapter's
plain-English rendering already reads well and costs fewer words. And the chapter
has no words spare.

**If the author wants old language before the plain translation**, one sentence is
now legitimately quotable and contains no dash and no splice:

> "Occupy thyself with few things, says the philosopher, if thou wouldst be
> tranquil."

**Do not quote across the dash.** Gutenberg renders it `--`. `01-voice.md` bans
em dashes, and `06-sources.md` permits a translator's dash inside a quotation only
where a `verification_note` records it as the translator's own **confirmed against
a printed page**. Nobody has done that. Concept:
`runs/ch12/okf/citations/marcus-aurelius-meditations-4-24-do-few-things.md`
(now `evidence_source: page-text`, `status: verifiable`; only the author sets
`verified`).

---

## 3. The five love languages — can the ruling be printed honestly?

### 3.1 The answer: yes, and the distinction the author drew is the right one

His ruling: *"I do want to keep the 5 love languages even if it's pseudoscience...
Let's say it's less scientific when it comes to the specific tactics. It is highly
relevant to the fact that you need to think about all 5 of those and you have
higher tendencies to do one versus the other."*

That is printable. It is printable because **he is not claiming it as science, and
the chapter does not need it to be.** The framework enters as a popular idea a man
found useful for thinking with, in his own voice, and the chapter's actual
authority rests where it already rests — on his grandfather, his marriage, and
Marcus. Nothing is borrowed from Chapman except a set of labels.

### 3.2 Round 1 overstated the evidence against, and that has to be corrected

Round 1 wrote: *"Matching your partner's language improves the relationship. Not
supported."* Flat. That is stronger than the record supports, and I am correcting
it rather than letting it stand because it was about to be used to overrule the
author.

The field is **mixed and entirely correlational:**

| Source | What it found |
|---|---|
| Impett, Park & Muise (2024), review, *Current Directions in Psych. Science* | Weak support for all three of Chapman's central assumptions. People endorse all five highly rather than having one. Factor structures come out inconsistent. |
| Bunt & Hazelwood (2017), 67 couples, *Personal Relationships* | Alignment made little difference; each partner's self-regulation predicted satisfaction better. |
| **Mostova, Stolarski & Matthews (2022), 100 couples, *PLOS ONE*** | **The other way.** Love-language mismatch correlated negatively with relationship and sexual satisfaction. Cross-sectional. |

Concept for the new one:
`runs/ch12/okf/citations/mostova-stolarski-matthews-2022-love-language-matching.md`
The Chapman concept has been updated in place with this correction.

**The sentence that is true, that nobody can falsify, and that the chapter can
print if it wants a calibration line at all:**

> Nobody has ever shown that changing what you do to match her stated language
> changes anything. The categories were never derived from data in the first
> place. It is still the most useful list a tired man has been handed.

All three clauses hold. The first is the honest state of the matching literature
(no experiment exists). The second is a fact about Chapman's method. The third is
the author's own position, stated as his own.

### 3.3 The load-bearing claim — "people differ in what registers as care"

This is the part the dispatch asked me to look hardest at, so here is the honest
answer: **there is good independent support for the weaker, sturdier version of
the claim, and no independent support for the specific five-channel version.**

**Supported, independent of Chapman:**

- **Giving and registering are different events.** Bolger, Zuckerman & Kessler
  (2000) ran a daily diary on couples under a major stressor and found that a
  large share of the support transactions the *giver* recorded did not appear in
  the *receiver's* record of the day at all. Not ingratitude. Not imagination. A
  measured gap.
  *Use the giver/receiver gap only.* The paper's own thesis — that support works
  better when unnoticed — points away from where this chapter wants to go, and a
  careless use of it would undercut the chapter's own argument. Concept:
  `runs/ch12/okf/citations/bolger-zuckerman-kessler-2000-invisible-support.md`
- **What predicts outcomes is the receiver's perception, not the giver's act.**
  Perceived partner responsiveness: whether she comes away believing you
  understand her, value what matters to her, and acted on it. §4.2.
- **Population-level differences in preference do exist**, but the best evidence
  for them is polling, not research. §3.5.

**Not supported, and the chapter must not imply it:** that there are five
channels; that they are distinct; that each person has one primary; that a
mismatch is a diagnosable fault.

**So the honest form of the author's own idea is his own second sentence, not his
first.** *"You need to think about all 5 of those"* is the defensible half —
breadth, a checklist against your own narrowness. *"You have higher tendencies to
do one versus the other"* is the half that leans on the taxonomy, and it survives
as a description of himself, which is unfalsifiable and better writing anyway.

### 3.4 How it should enter the prose — one paragraph, his own instance, no citation

The chapter already contains the platinum rule, which is the same idea with better
provenance. The love languages should arrive **after** it, as the practical
version — the crude list that tells a man what to go look at. Then his instance,
which is where the paragraph earns its place:

- He leads with **touch**. *"I specifically love it when... I lay my head in her
  lap while we watch TV and she rubs my head."* That detail is cleared, specific,
  and exactly what `01-voice.md` means by named detail.
- She leads with **acts of service**. *"Grilling together, I'm helping cook, both
  having a little wine, both laughing and talking while we also get work done."*
- **His lowest is acts of service — which is hers.** *"I do not naturally think of
  kind things to do... that takes real work."*

**That last line is the whole chapter in one fact.** The thing she reads as love
is the thing he is worst at, and he did not choose that, and it is not a
character defect, and it still has to be done. A man reading at 11pm recognises
that in one beat. No study is needed and none should be cited.

**Do not name the Impett review in prose. Do not stage a debunking.** `02-audience.md`
gives Eric a well-calibrated detector; he half-knows the framework is soft. One
clause of calibration (§3.2) buys all the credibility a debunking would, at a
twentieth of the words.

**Do not import the "balanced diet" metaphor** from the Impett paper. `01-voice.md`
allows one image per chapter and this chapter's is the muscle.

### 3.5 FLAG, NOT FIXED — "every man loves touch as a love language"

The author also said this. `01-voice.md`'s Never Do list: *"Never assert a
universal claim about all men ('every man is built this way,' 'all men do this',
'no man wants that')... A flat universal is one counterexample away from a reader
dismissing the whole claim."* This is that rule, exactly.

It is also the sentence most likely to lose the chapter's best reader. A man whose
wife initiates touch and who himself would rather be asked about his day stops
reading there.

**What the evidence supports:** men are **more likely than women** to name
physical touch as their preferred way of receiving love. The source for that is a
YouGov survey (2022, nationally representative, n reported as 1,000 U.S. adults,
fielded 27–31 January 2022). **That is polling, not research, and the percentage
figures disagree across the secondary summaries I could reach — none of them may
be printed.** The one peer-reviewed study of physical-affection preference I
located (Gulledge, Gulledge & Stahmann, 2003) sampled BYU students and cannot
speak about married men in their forties.
Concept: `runs/ch12/okf/citations/touch-preference-gender-evidence.md`

**The repair, ranked:**

1. **Cut the general claim and keep his instance.** "I lay my head in her lap while
   we watch TV and she rubs my head" does the entire job, and it is his, so no
   reader can be the counterexample.
2. Scope it: *"most men," "a lot of men."* `01-voice.md` names these as the
   approved forms.
3. If he wants the population claim stated, the honest form is *"surveys find men
   more likely than women to put touch first"* — attributed as a survey, with no
   number.

Recommendation 1. The chapter is not short of general claims; it is short of
specific ones.

---

## 4. The research, ranked by what earns a place

Ranked strictly by what a finished 1,202-word chapter should buy with the words
it has. Ranks 1–2 change the chapter. Ranks 3–5 are available on request. Ranks
6–8 are for other chapters and are recorded so nobody researches them twice.

### RANK 1 — Why the effort declines. This is the round's real gain.

The chapter's central claim is that romance is the first thing cut. Round 1 had
**no evidence for it** and said so; it was told not to borrow Ch11's stress study.
There are now two real sources, and between them they cover both halves.

**Ogolsky & Bowers (2013)** — meta-analysis, 35 studies, reported 12,273
participants, *JSPR* 30(3), 343–367. The five maintenance behaviours correlate
positively with satisfaction, commitment, love and liking — **with one exception:
relationship duration, which is negatively associated with positivity and
assurances.** The two behaviours most about warmth and reassurance run the
opposite way from how long you have been together.
*Language constraint: this is a cross-sectional association between duration and
reported behaviour. It supports "couples further in report less of this." It does
not support "your effort fell off," because nobody was followed.*
Concept: `runs/ch12/okf/citations/ogolsky-bowers-2013-maintenance-meta-analysis.md`

**Huston, Caughlin, Houts, Smith & George (2001)**, *JPSP* 80(2), 237–252 — the
"connubial crucible." Newlyweds followed thirteen years. The finding: it was
**disillusionment** — the abatement of love and the decline in overt affection —
**rather than the emergence of distress** (rising negativity, more conflict) that
predicted which marriages failed and how fast.
*Language constraint: the sample is newlyweds and the predictor window is the
first two years. Do not write "the research shows that when the romance goes out
of a twenty-year marriage, it ends." Write what forecasts trouble, not what causes
divorce.*
Concept: `runs/ch12/okf/citations/huston-et-al-2001-connubial-crucible.md`

**Why this earns its place and almost nothing else does.** The chapter's reader
does not think he has a problem, because he isn't fighting. Huston is the finding
that says the quiet version is the dangerous one. In a book whose first two Parts
are largely about conflict, this is the sentence that makes Part III necessary.

**Cost: one sentence.** Not a paragraph, not a named study, not a number. The
chapter's existing research paragraph (¶21, Gordon) already spends 106 words; this
should compress into that same slot rather than opening a second one. Something of
the shape: *couples who are followed over time don't come apart because the
fighting starts, they come apart because the warmth stops, and the warmth stops
first in the couples who have been at it longest.* Two clauses, both honest.

### RANK 2 — Perceived partner responsiveness, now attributable

Round 1's gap RG-1 is closed.

- Reis, H. T., & Shaver, P. (1988). Intimacy as an interpersonal process. In
  S. Duck (Ed.), *Handbook of Personal Relationships* (pp. 367–389). Wiley.
- Reis, H. T., Clark, M. S., & Holmes, J. G. (2004). Perceived partner
  responsiveness as an organizing construct in the study of intimacy and
  closeness. In Mashek & Aron (Eds.), *Handbook of Closeness and Intimacy*
  (pp. 201–225). Erlbaum.

The construct: the extent to which a person believes their partner **understands**
them, **values** what matters to them, and **acts** on it. Note what is absent from
the definition — the format of the act.

**This does not go in the prose.** It goes in the brief so the chapter's existing
sentence — *"it arrived in a form she doesn't read as love"* — is now known to be
standing on something rather than floating. `04-archetype.md` sets citation
density low; the idea carries in plain English and already does.
**And the three-component wording may not be quoted**, however tempting: it is
reported consistently across sources, which is exactly why it is probably close to
verbatim, and a verbatim citation cannot reach `verifiable` on search evidence.
Concept: `runs/ch12/okf/citations/perceived-partner-responsiveness-reis.md`

### RANK 3 — Novelty and self-expansion (available; the answer to "so what do I do")

**Aron, Norman, Aron, McKenna & Heyman (2000)**, *JPSP* 78(2), 273–284. Survey
and questionnaire studies found shared "exciting" activities correlated with
satisfaction, mediated by boredom. Then **three laboratory experiments** found
that couples who did a short novel and arousing task together showed greater
increases in experienced relationship quality than couples given a mundane one.
**This is the one place in the Ch12 material where "causes" is defensible** — and
what it caused was a rise in how the relationship felt immediately afterward, not
a saved marriage.

**Tsapelas, Aron & Orbuch (2009)**, *Psychological Science* 20(5), 543–545.
Boredom at year seven predicted lower satisfaction at year sixteen, controlling
for satisfaction at year seven.

Concepts: `aron-et-al-2000-novel-arousing-activities.md`,
`tsapelas-aron-orbuch-2009-marital-boredom.md`

**Why it is rank 3 and not rank 1:** it is the direct answer to *"I rented planes
and wrote letters twenty years ago and haven't in a long time,"* and it is a
genuinely better prescription than "go on a date." But the chapter's argument is
about **priority and form**, and novelty is a third thing. Adding it means either
a fifth beat or a thinner version of beats 2 and 3. **Recommendation: hold it for
Ch13,** whose premise is the pursuit that should have continued — where the rented
planes belong anyway, and where the Ch12/Ch13 boundary (R-5 in round 1) says the
courtship material lives.

*If the author insists the planes go in Ch12*, the finding is one clause and no
citation: *what you do with the evening is not neutral; something new does
something the usual thing does not.*

### RANK 4 — Does a date a week do anything? (Answer the chapter can use in one clause)

**The prescription traces to a real document that is weaker than the advice.**
Wilcox & Dew (2012), *The Date Night Opportunity*, National Marriage Project,
University of Virginia. Survey of Marital Generosity data; the headline is that
spouses who devote time specifically to one another at least once a week are
markedly more likely to report high-quality relationships. **Cross-sectional
survey work published by a marriage-promotion research centre, not a peer-reviewed
experiment, and the weekly threshold is not an experimentally derived dose.**
DO NOT PRINT A NUMBER FROM IT. Concept:
`runs/ch12/okf/citations/wilcox-dew-2012-date-night-opportunity.md`

**The peer-reviewed literature prescribes no frequency at all.** What it supports
is different and better:

- **Girme, Overall & Faingataa (2014)**, *Personal Relationships* 21(1), 125–149 —
  shared activities did their work **only when both partners were engaged,
  responsive, and wanted to be there.** The man who books the restaurant and
  spends the evening elsewhere in his head has done the activity and not the
  thing.
- **Harasymchuk, Walker, Muise & Impett (2021)**, *JSPR* 38(5), 1692–1709 —
  people who got closeness out of a date were the ones who planned it around what
  the *partner* would enjoy.

**What this does to the chapter: nothing is broken.** The existing sentence —
*"We've heard the same advice you've heard, that you should get out on a date
once a week"* — reports the advice **as advice** and then immediately admits to
failing it. That is exactly right and needs no repair.

What is newly available is one clause that makes the chapter smarter than the
advice it quotes: *the frequency is the part nobody ever actually established;
what has been tested is whether you were there.* It pairs naturally with the new
scene (§5), because his wife's question is about frequency and the chapter's
answer is about presence. **Recommendation: take this clause.** It is cheap and it
turns a received platitude into the chapter's own point.

### RANK 5 — Relationship maintenance as a named literature

**Stafford & Canary (1991)**, *JSPR* 8(2), 217–242 — positivity, openness,
assurances, social networks, sharing tasks. The peer-reviewed taxonomy that
occupies the ground Chapman occupies in popular culture.
Concept: `runs/ch12/okf/citations/stafford-canary-1991-relational-maintenance.md`

**Recommendation: do not print the list.** It is the honest cousin of the love
languages and the author would probably enjoy it, but this chapter is about to
carry one five-item taxonomy already, and two is a listicle. Its value here is
that it makes Ogolsky & Bowers (rank 1) legible, and rank 1 is where the words
should go.

### RANK 6–8 — Real, relevant, and for other chapters

| Source | Finding | Where it belongs |
|---|---|---|
| **Algoe, Gable & Maisel (2010)**, *Personal Relationships* 17(2), 217–233 | Gratitude from an interaction predicted more connection and satisfaction **the following day**, for giver and receiver. | Ch12 already carries Gordon 2012 making the same point. Hold in reserve; use only if the author wants the Gordon paragraph replaced with something that acts on a one-day timescale. |
| **Gable, Reis, Impett & Asher (2004)**, *JPSP* 87(2), 228–245 | Capitalization: how you answer her good news. Benefits larger when the response is active and constructive. | Ch16 (Warmth Is Strength) or Ch27 (The Discipline of Joy). Ch12 already has the mirror image in the "asking again on Thursday" line. |
| **Gottman "turning toward bids"** | — | **Already in the book's own bundle at `okf/citations/gottman-turning-toward-bids.md`, tagged to Ch11, with its 86%/33% figures marked DO NOT PRINT until a primary is pinned.** Ch12 must not use it. See §8. |

---

## 5. The new central scene — and it closes inbox #008

**AUTHOR MATERIAL, round 3. Real, and it replaces the invented composite.**

After 24 years, his wife asked: **"When was the last time you took me on a date?"**

> *"It hit me like a ton of bricks because she's right. It had been months... we
> hadn't gone on a date in nearly 5 months."*

Supporting, same round: both of them have forgotten their anniversary in busy
years; he used to rent planes and write letters twenty years ago and has not in a
long time.

### 5.1 Why this matters more than any of the research

Round 1's inbox #008 said, honestly, *"This chapter has no scene."* The anniversary
dinner never existed, the Walgreens scene was excluded, third-person vignettes are
banned book-wide, and what was left was secondhand advice plus one flat admission
sentence. **The author has now supplied the missing scene, and it is better than
anything a desk could have built**, because it is a real question, asked by a real
person, in the exact register `01-voice.md` asks for: accumulated friction, not a
discrete fight. Nobody raised their voice. She asked a question with an answer in
it.

### 5.2 Where it goes — recommendation: it opens the chapter

The chapter currently opens *"You used to plan things for her."* That is opening
type 1, direct address. **So does Ch10** (*"There are rules in your marriage nobody
ever wrote down"*) **and so does Ch11** (*"There's something in your marriage
you've decided to live with"*). `04-archetype.md` forbids repeating an opening
approach in consecutive chapters and its Red Flag list names this exact drift:
*"scene-first twice in a row becomes a formula the reader feels before he notices
it."* Ch12 would be the **third consecutive type-1 opening**, and rewriting the
sentence does not fix that, because the approach is the thing being repeated.

The new scene is the way out, and it is the only one available that does not cost
the chapter something it was ruled to keep. Shape:

1. **Orientation, 1–3 sentences** (`01-voice.md` and `04-archetype.md` both require
   it): a compass line telling the reader what he is about to realise. Not a
   description of circumstances.
2. **The question, in the author's first person.** She asked it. He did the
   arithmetic in his head. Nearly five months. `04-archetype.md`'s tertiary
   evidence type — *"brief first-person moments from the author... used sparingly
   and only when the author's own experience is the most honest proof available"*
   — is precisely this case.
3. **Do not soften it and do not add a recovery clause.** No "but we're good now."
   Round 1's Ruling 5 constraint applies with more force here, not less.
4. **Then hand the chapter back to "you"** and go to the grandfather. The author
   is never the protagonist (`04-archetype.md`); he is the man who went first.

**The safe fallback, if the Line Editor or the author would rather not move the
opening:** put the scene in beat 2, in the slot the current date-admission
paragraph occupies (¶11). It works there. It just leaves the three-consecutive-
type-1 problem unsolved, and that will come back from `gw-specchecker` or the
Panel as a cross-chapter finding.

### 5.3 What it replaces

**¶11 comes out.** Currently: *"In my own marriage, romance ebbs and flows. We've
heard the same advice you've heard, that you should get out on a date once a week.
We have gone weeks and sometimes months without going on a date."* (38 words.)

The new material is **harder, not softer**, so Ruling 5 is honoured rather than
overridden: "nearly five months" beats "weeks and sometimes months," and a question
from his wife beats a self-report. The "date once a week" clause survives — move it
into the scene, where it is what makes her question land.

The *"romance ebbs and flows"* phrase can go with it without loss. The Line Editor
already flagged it as a water figure in a chapter whose declared image is the
muscle, and it is a dead idiom doing no work the scene will not do better.

### 5.4 The anniversary and the planes — hold both

- **"We've both forgotten our anniversary in busy years."** Strong, and free
  (zero uses of "anniversar*" anywhere in the manuscript). But the chapter now has
  one real scene and does not need two, and this one risks re-opening the
  anniversary-dinner slot that round 1 correctly ruled out as never having
  existed. **Hold it.** If the author wants a second beat of texture, it is one
  sentence and it fits in the same paragraph as the question.
- **The rented planes.** See rank 3. This is Ch13 material by the Ch12/Ch13
  boundary rule. Using it here pulls courtship into Ch12, which round 1 spent a
  whole finding preventing.

---

## 6. What comes out — the two placeholders are now obsolete

### 6.1 Inbox #008 and #009 are both closed by the author's round-3 material

Round 1 wrote two placeholder passages explicitly designed to be lifted out when
the author supplied real material. He has. Both should now come out.

### 6.2 The kitchen faucet paragraph is not just a placeholder — it is now backwards

¶15 (59 words): *"Say the kitchen faucet has been dripping since spring, and you
give it a Saturday. Six hours, a trip out for the part, skinned knuckles... She
says thank you, and she means it, and it's flat."*

Round 1 invented this because it had no real instance, and the Line Editor flagged
the named faucet as an addition pending the author's word.

**Here is the finding that makes this more than a swap.** The faucet is an **act of
service**. In the passage, *he* performs it and *she* fails to read it. The
author's real configuration is the exact inverse: **acts of service is his lowest
and her highest.** So the invented instance stages the author's own dynamic
backwards, and if it stayed next to his real instance the chapter would contradict
itself inside two paragraphs.

**¶15 comes out. His instance replaces it.** ¶16 — *"She isn't ungrateful. The
effort was real... it arrived in a form she doesn't read as love. To her, love is
you asking about the meeting at work she's been dreading. Then asking again on
Thursday"* — is the load-bearing turn and **survives**, re-pointed to whatever
setup replaces the faucet. The Thursday line is the best sentence in the chapter
and the Anti-Slop Reader already asked for it to be protected.

### 6.3 The Democritus clause

Two words. §2.3.

---

## 7. The displacement plan — the arithmetic

Measured directly off `runs/ch12/refined.md`. The chapter is **1,202 words of
prose** (`voice_check.py`, verbatim in the Editor's Notes). The target is
1,000–1,300 and refine applies a 15% tolerance, so the effective hard ceiling is
about 1,495. **Aim for 1,250–1,300. Do not use the tolerance.**

| Out | Words | Why |
|---|---|---|
| ¶1, the opening paragraph | 48 | Replaced by orientation + the scene (§5.2). Third consecutive type-1 opening. |
| ¶11, "romance ebbs and flows" / the date admission | 38 | Superseded by the scene, which says the same thing harder (§5.3). |
| ¶15, the kitchen faucet | 59 | Placeholder, and now factually inverted (§6.2). |
| ¶9, "You already run the rest of your life on purpose" | 89 → ~45 | Compress. It discharges the outline's objection row ("why marriage-specific?"), which costs a sentence, not a paragraph. |
| ¶21, the Gordon research paragraph | 106 → ~65 | Compress, and fold the Huston/Ogolsky clause into the same slot (§4 rank 1) rather than opening a second research paragraph. |
| The Democritus clause | 2 | §2.3. |
| **Reclaimed** | **~280** | |

| In | Words | Rank |
|---|---|---|
| Orientation + the date question scene | ~130 | Must. §5. |
| The love-languages paragraph with his instance | ~120 | Must. §3.4. Author ruling. |
| The "warmth stops before the fighting starts" clause | ~30 | Rank 1. Inside the compressed ¶21. |
| The date-frequency clause ("nobody established the number") | ~20 | Rank 4. Inside the scene. |
| **Added** | **~300** | |

**Net: about +20 words. Lands near 1,222.** There is room for one of the held
items (§5.4's anniversary sentence, or the rank-3 novelty clause) if the author
wants it, and still ~60 words of headroom to 1,300.

**Beat structure after the revision** — still four beats, still within
`04-archetype.md`'s 3–5:

1. *(opening)* Orientation, then the question, then the arithmetic. Hand back to "you."
2. **The second piece of advice.** The grandfather. Unchanged. Ruled: never cut.
3. **The first thing cut.** The mechanism, the compressed objection clause, Marcus
   with the Democritus fix.
4. **Her currency, not yours.** Platinum over golden with Bennett's attribution,
   then the five languages calibrated, then his instance, then the turn (¶16
   surviving), then year-ten, then the receiving side.
5. **What it costs.** Compressed research, bare minimum, the muscle.
6. *(close)* One sentence. Unchanged.

**Beat 4 is now the heaviest beat in the chapter.** Watch it. If it runs past about
420 words, the thing to cut is ¶17 (year-ten, 66 words), which discharges an
outline row that the love-languages paragraph now discharges better — attention is
how you find out what her currency is, and his instance demonstrates it instead of
asserting it.

---

## 8. Cross-chapter reuse — findings

Checked by grepping the whole book repo (`manuscript.md`, every `chapters/*/refined.md`,
the OKF bundle, and `sources/`).

### R2-1 (significant): the book's own audience research already ruled the way the author just ruled

`sources/audience-signals.md`, previously uncited in any Ch12 brief:

> **Love languages** — the most commonly cited framework; helpful but limited;
> it's a diagnostic tool, not a philosophy of character

> **Date nights** — named as a fix but often feel like a band-aid over
> disconnection; the book needs to affirm the impulse while arguing for the deeper
> discipline

> **"I've already tried everything"** — the exhausted spouse who has tried
> therapy, date nights, love languages; the book's answer is that those are
> tactics, not a philosophy of self-governance

**This is the author's round-3 calibration, already written down in the book's
constitution-adjacent source material, months ago.** Round 1 recommended not
naming the framework at all, which was in tension with the book's own audience
position and nobody caught it. The ruling is not a reversal; it is the book
returning to a line it already held.

It also supplies the chapter's framing for free: *tactic, not philosophy.* That is
the sentence that lets the five languages in without granting them authority.

### R2-2 (significant): the author's recorded love languages do not match his round-3 statement

`sources/interview-author-stories.md`, line 13, recorded by the author:

> Love languages: **Words of affirmation (primary)** — needs to hear he's a good
> husband, a good dad. **Touch (secondary)** — likes to hug and kiss on her.

Round 3 says he **leads with touch**. The old record says touch is his *secondary*
and words of affirmation his *primary*. Words of affirmation does not appear in
the round-3 material at all.

These are not flatly contradictory — a man can revise this about himself, and the
older note may have been written loosely. **But the chapter is about to print his
primary, in his voice, as a load-bearing specific.** If the book says "touch" in
Ch12 and a later chapter uses "words of affirmation" from the older record, a
careful reader has caught the author inventing himself.

**This is an author question and I have not resolved it.** See §9, gap RG2-1.

### R2-3: Gottman's bids belong to Ch11 and must not migrate here

`okf/citations/gottman-turning-toward-bids.md` is in the book's own bundle, tagged
`speak-or-endure` (Ch11), and carries an explicit instruction: **do not print the
86%/33% figures until a primary is pinned**, plus a related caution that the
"94% divorce prediction" claim attached to Gottman is a known overclaim and is
banned book-wide. The dispatch asked for the turning-toward literature. It is
already spent, and it is spent in the chapter immediately before this one.
Ch12 must not use it. (Driver & Gottman 2004, *Family Process* 43(3), 301–314,
is the nearest peer-reviewed anchor for the bids concept and was located this
session; it is recorded here only so nobody researches it a third time.)

### R2-4: what is free, recounted

| Item | Status |
|---|---|
| "anniversar*" | **0 uses** anywhere in `manuscript.md` or any refined chapter. Free. |
| "plane," "flew," "flight" | **0 uses.** Free. |
| "courtship," "win her," "won her" | **0 uses.** Free — and reserved for Ch13. |
| "Democritus" | **0 uses** outside Ch12's own run directory. |
| "platinum" | **0 uses.** Bennett is new to the book. |
| "Stafford," "Canary," "Reis," "Algoe," "Bolger," "Huston," "Wilcox," "self-expansion," "invisible support" | **0 uses.** All new. |
| "Aron" | 6 files, all `sell-tooby-cosmides` (Aaron Sell, Ch4). **Different person.** No collision, but do not name Arthur Aron in prose in a book that already names an Aaron in a research context. |
| "boredom" | 3 files, none in refined prose. Free. |
| "touch" | 36 files. Heavily used, but as ordinary English and in Ch2's emotional-contagion material, not as a love-language claim. Not a collision; worth a Panel read on the whole-book pass. |
| "gratitude" / "appreciat*" | 37 / 17 files. The register is well used. Ch8 owns the Seneca *De Beneficiis* "the wages of a good deed is to have done it" argument. **Ch12's appreciation paragraph must not re-argue Ch8's point** that you are not owed her gratitude — Ch12's claim is the opposite direction (you owe her effort a real reading), and the two need to stay distinguishable. |
| Randall & Bodenmann 2009 | Still tagged to Ch11 and still off-limits here (round 1, R-4). Unchanged. |

### R2-5: Impett is now attached to three Ch12 sources

Impett is an author on the love-languages review (2024), on Gordon et al. (2012),
and on Harasymchuk et al. (2021), and `park-et-al-2025-pay-me-back` is already used
in Ch7. Round 1 warned against naming her in prose twice. **The simplest rule, and
the one the archetype's low citation density wants anyway: name no relationship
researcher in this chapter's prose at all.** The only name the chapter needs is
Bennett's, which is an attribution obligation rather than a citation.

---

## 9. Gaps — what this brief still cannot answer

**RG2-1 (material, author only). Which is his primary love language?**
The book's own source file says words of affirmation, with touch second. Round 3
says he leads with touch. The chapter is about to print one of these as a
first-person specific.
*Recommended inbox item:* "Chapter 12 will print your own instance: you lead with
touch, she leads with acts of service, and your lowest is the one she reads best.
Your earlier interview notes recorded words of affirmation as your primary and
touch as secondary. Which is right for print, and does words of affirmation belong
in the chapter at all?"

**RG2-2 (material, author only). The 'every man loves touch' claim.**
Flagged, scoped, not fixed — §3.5. He should choose between cutting the general
claim, scoping it to "most men," or attributing it as a survey finding with no
number. The voice spec forbids only the flat universal, not the idea.

**RG2-3 (structural, author or Line Editor). Does the scene open the chapter?**
§5.2 recommends yes and names the fallback. This is an editorial call about the
shape of a finished chapter, not a research finding, and I have not ruled it.
Whoever rules it should know the cost of not moving it: three consecutive
type-1 openings across Ch10, Ch11 and Ch12.

**RG2-4 (rights, carried forward, still open). The Platinum Rule trademark.**
Round 1's RG-4 is unchanged and unanswered. "The Platinum Rule" is Tony
Alessandra's registered trademark. Using and attributing the idea in prose is
fine; putting the phrase in a chapter title, subtitle, Substack headline or social
asset needs the author's decision.

**RG2-5 (carried forward). Round 1's RG-3, the consequence chain.**
Whether infidelity is cut from the chain or kept as one of several outcomes. Still
the author's. The chapter as refined cuts it, per round 1's instruction. Nothing in
this round changes that.

**RG2-6 (structural, not blocking). No relationship-science primary was read.**
Every research citation in §4 rests on **converging search summaries**, not on a
retrieved page. Bibliographic details are corroborated across independent listings
and are marked in each concept with exactly which elements are inferred (issue
numbers and page ranges, mostly). **No effect size, sample size, percentage or
verbatim quotation from any of them may be printed.** That restriction is not a
formality: `06-sources.md` exists because six defects came from search answering
confidently.

**RG2-7 (not blocking). `03-outline.md` is still stale.**
Round 1's §0 supersession table still governs and the outline still says the old
thing, because this engine does not write in the book repo. Round 2 adds nothing
to that table except that the outline's "Research burden: Low" is now doubly
wrong — the author was right, there is a lot.

---

## 10. Content concepts — PROPOSED, not written (Rule 9)

Four concepts capture the author's own material or a claim about what he thinks.
None was written to disk. Their full proposed frontmatter and body are in this
desk's return to the Publisher, for him to confirm.

1. **`stories/the-last-time-you-took-me-on-a-date.md`** — the round-3 scene. His
   wife's question after 24 years, nearly five months.
2. **`frameworks/her-currency-not-yours.md`** — the platinum rule as this book
   states it, with the five languages entering as a tactic rather than a model,
   and his own touch / acts-of-service instance as the demonstration.
3. **`frameworks/the-language-you-are-worst-at-is-usually-hers.md`** — the sharper
   claim underneath: his lowest is her highest, it is not a character defect, and
   it still has to be done. This may be the chapter's real idea and it is not in
   the outline anywhere.
4. **`stories/we-have-both-forgotten-the-anniversary.md`** — held, per §5.4.

Every gap marker referenced in this brief **was** written, immediately, to
`runs/ch12/okf/citations/` — thirteen new files and three updated. They are shadow
copies awaiting migration into the book bundle **by the author**, never by a desk
(CLAUDE.md Rule 8).

---

## Provenance

| Round | What happened | What it changed |
|---|---|---|
| Interview rounds 1–2 | Recorded in `runs/ch12/interview.md`. | Five rulings; the mechanism, the grandfather anchor, platinum over golden. |
| Research round 1 | Three sources found, no primary read, "everything is blocked." | Produced a usable brief and one printed defect. The love-languages ruling in it overruled the author on evidence that was real but overstated. |
| Draft → refine → conformance → distillation | Chapter reached 1,202 words, all HARD checks passing. | Two placeholder passages written pending author input (inbox #008, #009), both flagged as liftable. |
| **Author pushback, round 3** | He said the research was too thin and that the love languages stays in. | **He was right on both counts and the record should say so.** The "too thin" finding traced to a false constraint (§1), not to the literature. The love-languages ruling reversed round 1's ban, and on re-examination round 1's evidence summary was itself too strong (§3.2) — the correction went the author's way. He also supplied the scene that closed inbox #008 and the instance that closed inbox #009, which no desk could have produced. Two rounds of his pushback have now changed this chapter's central story twice: from a story that never existed, to the grandfather, to the grandfather plus a real scene. |
| **Research round 2 (this file)** | Open lane found and used. Fourteen sources located; two classical primaries retrieved and read in full. | A live attribution defect found and repaired (§2). Round 1's Marcus no-quotation ruling released. Round 1's love-languages position corrected. The chapter's central mechanism given real evidence for the first time (§4 rank 1). A placeholder found to be factually inverted against the author's real material (§6.2). Two cross-chapter findings: the book's own audience research already held the author's position (R2-1), and his recorded primary love language conflicts with what he just said (R2-2). |

*No content concept was written to disk by this desk. Four are proposed in the
return. Gap markers were written immediately, to the shadow path, per Rule 8.
No citation was marked `verified`; that is the author's, against his own copy.*
