# Change Log — Stoic Husband Knowledge Bundle

2026-06-14T14:00:00Z — Bundle created as an OKF proof-of-concept. Seeded with
three frameworks, one story, and two citations drawn from
`sources/evidence-library.md` and `sources/author-notes.md`. No existing book
artifacts modified.

2026-06-14T17:00:00Z — Full migration of `sources/evidence-library.md` into
this bundle, completing the OKF rollout. Every item in the former evidence
library now has a corresponding typed concept:

- **Frameworks (27 total, 24 new):** all "Confirmed Frameworks and Models"
  entries, including the three from the pilot
  ([The Virtue Question](/frameworks/the-virtue-question.md),
  [Attachment vs. Devotion](/frameworks/attachment-vs-devotion.md),
  [The Village Problem](/frameworks/the-village-problem.md)). New additions
  include the Epictetan/Marcus/Musonius/Perel/Stoic Romance/endurance
  frameworks and
  [Arête as Secular Load-Bearer](/frameworks/arete-as-secular-load-bearer.md).
- **Stories (7 total, 6 new):** all "Confirmed Stories and Anecdotes" entries,
  including the pilot's
  [Sexless and Roommates](/stories/sexless-and-roommates.md). New additions
  include
  [I Haven't Felt Desired in Years](/stories/i-havent-felt-desired-in-years.md),
  [Take Sex Off the Table](/stories/take-sex-off-the-table.md),
  [Screaming from the Rooftops](/stories/screaming-from-the-rooftops.md),
  ["Touched-Out" and the Dead Bedroom](/stories/touched-out-and-the-dead-bedroom.md),
  [Any Issues Before Kids Will Be Magnified](/stories/any-issues-before-kids-will-be-magnified.md),
  and
  [Marriage at Year 27, Clashing in the Kitchen](/stories/marriage-at-year-27-clashing-in-the-kitchen.md).
- **Citations (15 total, 13 new):** all "Confirmed Facts and Data Points"
  entries, including the pilot's
  [Gottman — The Four Horsemen](/citations/gottman-four-horsemen.md) and
  [Perel — Mating in Captivity](/citations/perel-mating-in-captivity.md).
  New citations from confirmed facts:
  [Gottman — Repair Attempts](/citations/gottman-repair-attempts.md),
  [Morally Good People and Happiness/Meaning](/citations/morally-good-people-and-happiness-meaning.md),
  [Knee et al. 2005 — Autonomy and Defensiveness](/citations/knee-2005-autonomy-and-defensiveness.md),
  [Seneca — "We May Weep, But We Must Not Wail"](/citations/seneca-weep-but-not-wail.md),
  [Marcus Aurelius — "Either Instruct Them or Bear with Them"](/citations/marcus-aurelius-instruct-or-bear-with-them.md),
  and
  [Musonius Rufus on Marriage](/citations/musonius-rufus-on-marriage.md). New
  `unverified` citations from "What Still Needs External Research" (gaps not
  already represented above):
  [Seneca — De Ira (On Anger)](/citations/seneca-de-ira-on-anger.md),
  [Epictetus — "Smoke in the Room" Passage](/citations/epictetus-smoke-in-the-room.md),
  [Marcus Aurelius — Impermanence and Gratitude](/citations/marcus-aurelius-impermanence-and-gratitude.md),
  [Prosoche (Daily Self-Attention)](/citations/prosoche-daily-self-attention.md),
  [Amor Fati](/citations/amor-fati.md),
  [Skowron 2000 — Differentiation and Marital Satisfaction](/citations/skowron-2000-differentiation-and-marital-satisfaction.md),
  and
  [Fatherly — "23 Damn Good Pieces of Marriage Advice"](/citations/fatherly-23-pieces-of-marriage-advice.md).
  The remaining gap (broader marriage/meaning research beyond the Psyche
  article) was folded into the verification note of
  [Morally Good People and Happiness/Meaning](/citations/morally-good-people-and-happiness-meaning.md)
  rather than given its own file, since it names a research direction rather
  than a specific source.

`index.md` was completely rewritten as the full rollup of all 49 concepts
(27 frameworks + 7 stories + 15 citations), grouped by type, with `Signals`,
`Findings`, and `Notes` sections present but empty pending future commands.
`sources/evidence-library.md` has been replaced with a tombstone pointing
here, per `.claude/OKF.md`. No content was invented — every concept is
faithfully derived from `sources/evidence-library.md`, cross-checked against
`sources/author-notes.md` and `sources/audience-signals.md` where needed for
context.

2026-06-14T19:00:00Z — Reconciliation migration during the merge of this
bundle into `main`. The bundle was built from the 2026-06-04 evidence library;
`main` had since added the Chapter 2–5 evidence (developed June 5–13) that the
original migration never saw. Migrated those remaining items into typed
concepts so the knowledge layer is complete and `evidence-library.md` can stay
a tombstone:

- **Frameworks (21 new, 48 total):** The Operating System (trigger/meaning/
  autopilot), Metacognition and the Internal Dialogue, Compassion vs. Empathy,
  Emotional Contagion, The Descent to Beast, Humor and Lightness, Preferred
  Externals, The Intertwined Life, Biological Mate-Seeking → Complacency, The
  4Ds, The Courage to Correct Without Needing to Win, Respect as a Resource,
  The Behavioral Loop, The Anger Spectrum, Disdain as Anger's Endpoint, The
  Nail Parable, The New Partner Is Not Better (River Comparison), The Cigarette
  Close, The Arena, The Evening Review, The Negative Rumination Loop.
- **Stories (1 new, 8 total):** The Cascade (composite).
- **Citations (6 new, 21 total):** Kruse — Stoic Compassion (Psychology Today,
  `verified`); Seneca — De Ira II.3 (`verifiable`); four Pillemer / Cornell
  Marriage Advice Project lessons (`verifiable`). The Pillemer concepts carry
  the attribution warning that "don't sweat the small stuff" is Richard Carlson
  (1997), not Pillemer.

Also fixed two pre-existing OKF conformance bugs found by `scripts/okf_validate.py`:
unquoted YAML scalars in `the-operating-system-…` (a `re:` colon) and
`touched-out-and-the-dead-bedroom` (a leading-quote title). No content was
invented — every concept is derived from `sources/evidence-library.md` (main's
version) and `sources/articles/`, with citation `status` set conservatively per
CLAUDE.md Rule 3.

2026-06-15T00:00:00Z — Gap identified during the `/book-chapter-research 6`
check-in. The author shared a large body of personal material on scorekeeping
dynamics in marriage — most of it landing on Ch7 (The End of Scorekeeping) and
partly Ch8, not Ch6. Captured as 6 new concepts so the material isn't lost
before Ch7 research begins:

- **Frameworks (3 new):**
  [Small Rocks, Big Rocks (Incompatible Scoreboards)](/frameworks/small-rocks-big-rocks.md) —
  each spouse's ledger weighs different categories, so neither ledger can
  "settle" the other;
  [Scorekeeping Is Contagious](/frameworks/scorekeeping-is-contagious.md) — one
  spouse's felt injustice triggers the other's own ledger, producing two
  parallel audits instead of resolution;
  [Scorekeeping Varies by Marriage](/frameworks/scorekeeping-varies-by-marriage.md) —
  a calibration note that scorekeeping is a dial, not universal (contrast with
  a friend's low-scorekeeping marriage), so Ch7 doesn't alienate
  low-scorekeeping readers.
- **Stories (2 new, both composite/author IP):**
  [The Bathroom Light](/stories/the-bathroom-light.md) — a trivial trigger
  absorbs a disproportionate reaction tied to an unrelated frustration and
  stays permanently loaded;
  [Two Truths: Tired Husband, Overloaded Wife](/stories/two-truths-tired-husband-overloaded-wife.md) —
  the canonical illustration of Scorekeeping Is Contagious, two genuine
  grievances on different axes colliding in one evening.
- **Citations (1 new, `unverified`):**
  [Household Labor Distribution and Caretaker Burden Research](/citations/household-labor-and-caretaker-burden.md) —
  the author asked whether research exists on the feeling that a
  home-managing spouse's work never has a stopping point. No source
  identified yet; candidate directions noted (division-of-household-labor,
  perceived-fairness-and-marital-satisfaction, Hochschild's "second shift"),
  but framing must avoid "emotional labor"/"mental load" per `02-audience.md`.
  This is the gap a future researcher needs to close before Ch7/Ch8 cite it.

No existing Ch6 artifacts were changed — Ch6 (Duty Without Resentment) research
proceeds separately. `index.md` updated to register all 6 concepts under
Frameworks, Stories, and Citations.

2026-06-15T14:00:00Z — Continued the `/book-chapter-research 6` check-in. The
author answered the Ch6 questions in detail, supplying concrete texture for
the laundry scene already on file in
`sources/interview-author-stories.md`. Two additions:

- **Citation (1 new, `unverified`):**
  [Sisyphean Labor and the Loss of Meaning (Repetitive Undone Work)](/citations/sisyphean-labor-and-meaning.md) —
  the author recalled a study where people were paid well to do repetitive
  manual work that an experimenter periodically destroyed and made them
  redo; even high pay couldn't sustain motivation once the work was visibly
  pointless. Likely candidate: Ariely's "Sisyphean condition" experiments,
  but unconfirmed. Distinct from
  [Household Labor Distribution and Caretaker Burden Research](/citations/household-labor-and-caretaker-burden.md) —
  that one is about fairness of distribution; this one is about meaning in
  work that's undone as fast as it's done.
- **Story enriched:**
  [Two Truths: Tired Husband, Overloaded Wife](/stories/two-truths-tired-husband-overloaded-wife.md)
  gained a new "A Concrete Instance" section — the specific late-night
  laundry-basket scene, including the "I knew you wouldn't raise a finger"
  line and how an accusation of laziness escalates from a chore dispute into
  an identity verdict (provider role under attack — connects to
  [The Five Hidden Judgments](/frameworks/the-five-hidden-judgments.md)'s
  "ego threat" and [The Role Frame](/frameworks/the-role-frame-ego-vs-role.md)).

The bulk of the author's answer (the "Am I lazy?" reflection, the
single-dad reframe, the list of duties he doesn't resent, and the Musonius
"carries weight without tally" illustrations) is Ch6-specific and will be
woven directly into `chapters/ch06/research.md` rather than atomized here —
it serves one chapter's argument rather than being reusable cross-chapter
material. `index.md` updated with the new citation.

2026-06-15T14:15:00Z — Author supplied sourcing for the Stoic teaching behind
Ch6's "Am I lazy?" reflection, resolving the `[PLACEHOLDER: verify source]`
flagged earlier in the check-in. New citation:

- **Citation (1 new, `verifiable`):**
  [Marcus Aurelius — Bad Breath, Tolerance, and the Virtue of Being Wrong (Meditations 5.28)](/citations/marcus-aurelius-on-correction-and-tolerance.md) —
  one passage, two readings: tolerance toward others' faults (Marcus's
  original point), and gratitude for having one's own faults pointed out (a
  modern reframe commonly associated with Donald Robertson's writing). The
  second reading is the Stoic mechanism behind the "Am I lazy?" reflection.
  Status `verifiable` — the Meditations passage is real and locatable, but
  translation wording and the Robertson attribution need author confirmation
  against physical copies per Rule 11.

`index.md` updated with the new citation. This was the last open item from
the Ch6 check-in; `chapters/ch06/research.md` is ready to be written.

2026-06-15T15:00:00Z — Mid-draft correction during `/book-chapter-draft 6`.
The first ch06 draft used the wrong mechanism (a single ambush scene over
an unfair chore) and stacked two Marcus Aurelius citations to make one
point. The author's feedback corrected the chapter's actual spine: duties
get split (consciously or by drift) and each spouse is mostly blind to the
other's labor (hero of their own story); the trigger for resentment isn't
total workload imbalance but a *visible* moment — one person resting while
the other is visibly working; criticism in that moment fires the Four D's
and births scorekeeping; the corrective is noticing and closing the gap
("I see you working, I appreciate it — help or join you?") plus a
self-check ("am I being lazy, or are we just out of rhythm?").

New citation:

- **Citation (1 new, `verifiable`):**
  [Marcus Aurelius — "You Weren't Born to Stay Under the Covers" (Meditations 5.1)](/citations/marcus-aurelius-born-to-act.md) —
  the duty-is-just-proper-work passage, used as Ch6's single anchor quote.
  Distinct from
  [Marcus Aurelius — Bad Breath, Tolerance, and the Virtue of Being Wrong (Meditations 5.28)](/citations/marcus-aurelius-on-correction-and-tolerance.md),
  which is no longer used in Ch6 (receiving-criticism mechanism, not the
  duty mechanism) but remains in the bundle for a future chapter focused
  on receiving criticism specifically.

`index.md` updated. `chapters/ch06/research.md` and `chapters/ch06/draft.md`
are being revised to match the corrected mechanism.

## 2026-06-19 — /book-signal 1
Added 5 Reader Signal concepts (0 resonance, 0 confusion, 5 objection, 0
gift, 0 extension; 0 noise skipped) to okf/signals/, covering reader craft
feedback on `marketing/substack/ch01/02-the-operating-system.md`. No GIFT
responses, no citation gaps matched.

## 2026-06-28 — Deep research pass for Ch7 (The End of Scorekeeping)
Author requested additional research beyond personal experience: Stoic
sources and external marriage research on scorekeeping. Added 4 new
`status: verifiable` citations via WebSearch:

- [Park, Johnson, Gordon & Impett (2025) — "Pay Me Back"](/citations/park-et-al-2025-pay-me-back-exchange-orientation.md) —
  13-year longitudinal study (N=7,293 German couples); exchange orientation
  predicts declining satisfaction. Stronger empirical anchor for Ch7 Claims
  1-2 than the existing Pillemer citation (complements, doesn't replace it).
- [Gillespie, Peterson & Lever (2019)](/citations/gillespie-peterson-lever-2019-fairness-housework-expenses.md) —
  N=10,236; closes the open `household-labor-and-caretaker-burden.md` gap
  (status there unchanged pending author review) without relying on
  "emotional labor"/"mental load" framing.
- [Seneca — De Beneficiis](/citations/seneca-de-beneficiis-against-keeping-accounts.md) —
  classical Stoic treatise against keeping accounts of benefits given; the
  most directly on-theme classical text found for Ch7, not previously in
  the bundle.
- [Marcus Aurelius — Meditations Book 7](/citations/marcus-aurelius-meditations-book7-no-repayment.md) —
  single-line aphorism against seeking credit/repayment for good deeds.

All four are `verifiable`, not `verified` — exact wording, page/verse
numbers, and (for the Seneca/Marcus passages) translation edition still need
confirmation before manuscript use, per CLAUDE.md Rule 11. `index.md`
updated. `chapters/ch07/research.md` updated to cross-link all four.

## 2026-07-06T15:45:00Z — /book-source-prep

Processed one new source: an author-provided screenshot of an anonymous
social-media listicle ("13 Brutally Honest Truths About Marriage"), filed at
`sources/articles/psychological-insights-13-truths-marriage.md`. Not
citation-grade (anonymous account, no credentials) — used only to check for
thematic overlap and gaps against the existing bundle.

Cross-referencing the list's 13 items against `03-outline.md` and the
existing frameworks/citations found:

- **8 items already covered**, confirming existing material tracks broader
  resonance (ego-vs-role frame, dichotomy of control, Pillemer's
  communication/scorekeeping findings, marriage-as-community-of-life).
- **2 items initially flagged as gaps turned out to already be covered**
  on closer check: continued pursuit/flirting after commitment (Ch11 + Ch12
  cover this directly) and a secular analogue to "pray for your partner
  when angry" (`the-evening-review-stoic-night-practice.md` — the author's
  own "Stoic prayer" practice — already serves this function).
- **3 genuine, narrower gaps** added as `status: unverified` citations:
  - [Sex as Recurring Ritual of Choosing Each Other](/citations/sex-as-ritual-choosing-each-other.md) (ch13, ch16)
  - [In-Law and Family-of-Origin Boundaries in Marriage](/citations/in-law-family-of-origin-boundaries.md) (ch09; flagged as a possible **outline** gap, not just a research gap — no current chapter addresses extended-family boundaries directly)
  - [Loneliness Inside a Marriage as a Signal, Not a Verdict](/citations/loneliness-as-signal-not-verdict.md) (ch17, ch03)

No new frameworks or stories added — the overlap items didn't warrant
duplicate concepts, and the 3 gaps are logged as open questions, not adopted
claims. `index.md` regenerated with the 3 new citation entries.

## 2026-07-06T16:30:00Z — Deep research pass: Loneliness as Signal, Not Verdict

Author asked to take one of the three flagged gaps and research it deeply
enough to decide whether it qualifies for a real framework. Chose
"Loneliness Inside a Marriage as a Signal, Not a Verdict." WebSearch found
solid academic backing:

- [Weiss (1973) — Emotional vs. Social Loneliness](/citations/weiss-1973-emotional-vs-social-loneliness.md) —
  the foundational typology distinguishing emotional loneliness (no
  intimate tie) from social loneliness (no peer network); emotional
  isolation isn't resolved by more social relationships.
- [Rokach, Sha'ked & Ben-Artzi (2022) — LIRS](/citations/rokach-et-al-2022-lirs-detachment-hurt-guilt.md) —
  a validated scale for loneliness inside an existing relationship,
  resolving into three factors: detachment, hurt, and guilt. The guilt
  factor (shame at feeling lonely despite having a partner) is the strongest
  find — it gives the "signal, not verdict" reframe something concrete to
  argue against.

Both are `status: verifiable` — bibliographic details confirmed across
independent sources (PubMed, MDPI, ResearchGate, SciRP), but full primary
text wasn't retrievable this session (403s), so exact quotable wording still
needs confirmation. A specific "40% of married Swedes report more loneliness"
statistic surfaced in search summaries but could not be traced to a primary
source — deliberately not included or cited anywhere, per CLAUDE.md Rule 3.

Promoted to a real framework:
[Married but Lonely (The Signal, Not the Verdict)](/frameworks/married-but-lonely-signal-not-verdict.md)
(`ip: author-synthesis`, citing both sources above). The original gap stub
`loneliness-as-signal-not-verdict.md` is marked `status: superseded` and kept
as a historical record. `index.md` regenerated: 1 new framework, 2 new
citations, 1 citation status changed to `superseded`.

## 2026-07-06T18:30:00Z — Outline revision: Chapter 10 inserted, 62-file chapter-tag renumbering

The author added a new chapter to Part II ("The Sturdy Oak") — Chapter 10,
"Not Everyone Gets a Vote" — covering external corrosive influence on the
marriage (anti-marriage friends, boundary-violating in-laws), structured
around the four Stoic cardinal virtues. This pushed old Ch10–Ch27 to
Ch11–Ch28 (27 → 28 chapters total).

Every OKF concept file tagged with a chapter number in the old 10–27 range
was renumbered to match: 62 files across `okf/frameworks/`, `okf/citations/`,
and `okf/stories/` had their `chapters:`/`tags:` frontmatter shifted (e.g.
`perel-mating-in-captivity.md` went from `[ch11, ch12, ch13, ch16, ch24,
ch26]` to `[ch12, ch13, ch14, ch17, ch25, ch27]`). A follow-up scan caught 7
files with prose-level "Chapter N" mentions in their body text (not just
frontmatter) that a frontmatter-only pass would have missed — those were
fixed by hand: `disdain-as-angers-endpoint.md`,
`the-evening-review-stoic-night-practice.md`,
`the-negative-rumination-loop.md`,
`the-new-partner-is-not-better-river-comparison.md`,
`married-but-lonely-signal-not-verdict.md`,
`sex-as-ritual-choosing-each-other.md`, and
`loneliness-as-signal-not-verdict.md`. `scripts/okf_validate.py` ran clean
before and after (pre-existing warnings about `index.md`'s framework/signal
counts and stale `evidence-library.md` references are unrelated to this
change, not introduced by it).

[In-Law and Family-of-Origin Boundaries in Marriage](/citations/in-law-family-of-origin-boundaries.md)
was retagged from `chapters: [ch09]` (with an `outline-gap` tag) to
`chapters: [ch10]` — the outline gap it flagged is now resolved by Chapter
10's existence; the citation itself stays `status: unverified` since
Pillemer's in-laws finding and the Christakis & Fowler divorce-clustering
candidate still need proper sourcing during that chapter's
`/book-chapter-research` pass. `index.md` and `sources/synthesis.md` updated
to match.

## 2026-07-06T22:28:53Z — /book-source-prep: sex/desire-discrepancy research

Author asked for a deep research pass on the "sex as ritual" gap
(`sex-as-ritual-choosing-each-other.md`), which expanded well beyond the
original ritual/covenant-renewal question into a real editorial problem:
what actually happens when one partner declines intimacy, citing
unwillingness to act "out of obligation," while the other partner still
wants it. Six real, peer-reviewed sources found and added as `status:
verifiable` citations:

- [Basson (2000)](/citations/basson-2000-responsive-vs-spontaneous-desire.md) —
  responsive vs. spontaneous desire; initiation can precede the feeling
  rather than requiring it first. Replaces the non-research-based "Great
  American Sex Diet" pop-book reference the author had originally raised.
- [Muise, Schimmack & Impett (2016)](/citations/muise-2016-sexual-frequency-well-being.md) —
  N=30,645; sexual frequency's link to well-being is curvilinear,
  plateauing around once a week.
- [Impett & Peplau (2005)](/citations/impett-peplau-2005-approach-avoidance-sexual-motives.md) —
  avoidance-motivated sexual compliance (to prevent conflict) predicts the
  lowest relationship satisfaction of any group studied; approach-motivated
  compliance (to connect) predicts the opposite.
- [Muise, Impett, Kogan & Desmarais (2013)](/citations/muise-2013-sexual-communal-strength.md) —
  "sexual communal strength": care-motivated (not avoidance-motivated)
  engagement without one's own desire present sustains desire over time
  for both partners, bounded by the caveat that "unmitigated communion"
  (total self-neglect) predicts worse outcomes.
- [Vowels & Mark (2020)](/citations/vowels-mark-2020-mitigating-desire-discrepancy.md) —
  open communication about a desire mismatch predicts better outcomes than
  forcing or avoiding it.
- [Herbenick et al. (2014)](/citations/herbenick-2014-desire-discrepancy-feature-not-bug.md) —
  desire discrepancy reframed as a normal feature of long relationships,
  not a bug — same "signal, not verdict" shape as the loneliness framework.

A seventh citation,
[Infidelity Motivation — Gendered Split](/citations/infidelity-motivation-gendered-split.md),
was explicitly logged as `status: unverified` rather than written up as
verifiable — the gendered percentages (men: sexual dissatisfaction; women:
emotional neglect) came from secondary aggregation, not a traceable
primary source, and a complicating finding (56% of men / 34% of women who
cheat rate their marriage "happy") argues against using it deterministically
even once sourced. Flagged as a future research task, not usable yet.

All six verifiable citations synthesized into a new framework,
[Bounded Generosity, Not Obligation](/frameworks/bounded-generosity-not-obligation.md)
(`ip: author-synthesis`). The original gap stub
`sex-as-ritual-choosing-each-other.md` marked `status: superseded` and kept
as a historical record. `index.md` regenerated: 1 new framework, 7 new
citations (6 verifiable, 1 unverified), 1 citation status changed to
`superseded`.

## 2026-07-08 — Session retrospective during /book-substack 2
Author flagged, across three drafted Ch2 concepts, that "her mood" had
become the default illustration of negative affect entering the household —
an unfair characterization drifting toward casting the wife as the moody
one. Added one new framework concept capturing the correction as a durable
lens, not a one-time wording fix:

- [Emotional Weather — Shared Categories, Not "Her Mood"](/frameworks/emotional-weather-shared-categories.md) —
  negative-affect examples should draw from anxiety, fear, dread, grief, and
  exhaustion (categories that hit both partners) rather than defaulting to
  "her mood." Ch03 (Sea Legs) and Ch04 (Care Without Contagion) of the Ch2
  Substack series were revised to this framing before saving.

`index.md` updated. This concept should be checked against future chapters'
Substack/social drafting whenever a concept illustrates emotional transfer
or relational dynamics.

## 2026-07-06T23:15:00Z — Schema migration: chapters → chapter_slugs, gap_type added

Following a session retrospective, the OKF spec (`.claude/OKF.md`) changed
how concepts reference chapters. All 106 concept files in this bundle
(`frameworks/`, `citations/`, `stories/`) were migrated:

- `chapters: [chNN, ...]` → `chapter_slugs: [kebab-case-title, ...]`, derived
  from the exact chapter titles in `03-outline.md` at migration time.
  `Introduction`/`Conclusion` → `introduction`/`conclusion`; the wildcard
  `all` token passed through unchanged.
- Bare `chNN`/`Introduction`/`Conclusion` tokens stripped out of `tags:`
  (topical tags only now).
- Verified after migration: zero leftover numeric chapter tokens anywhere
  in the bundle, all 106 frontmatter blocks still parse as valid YAML, and
  (via a new `scripts/okf_validate.py` check) every `chapter_slugs` entry
  resolves to a real heading in the current `03-outline.md`.

Also added: `gap_type: research | structural` on `Citation` concepts, and
formalized `status: superseded` as a fourth citation status (distinct from a
resolved *structural* gap — see `.claude/OKF.md`'s "Gap types" and
"The `superseded` status" sections for the worked distinction).
`okf/citations/in-law-family-of-origin-boundaries.md` retrofitted as the
reference example of a resolved structural gap: `gap_type: structural`,
`structural_status: resolved`, `structural_resolution` naming Chapter 10 as
what resolved it — with `status` unchanged (still `unverified`), since the
structural resolution didn't source the underlying claim.

No concept content changed beyond frontmatter — this is a schema migration,
not a research or curation pass.

2026-07-11T00:00:00Z — /book-source-prep: added 1 framework,
[The River, the Oak, and the Sun](/frameworks/the-river-the-oak-and-the-sun.md),
from a new raw source (`sources/manifesto-river-oak-sun.md`, the author's
own manifesto pasted verbatim into session). Cross-referenced against
`03-outline.md`: Parts I–III are already named "The Calming River" / "The
Sturdy Oak" / "The Warm Sun," and `05-framework.md`'s "Layer 1" already
defines the same three elements — so no gap citation was needed, only a
canonical framework concept capturing the full manifesto text (the
three-element definitions, the five-part failure-mode taxonomy, and the
closing formula) that neither existing document had in full. No stories or
citations added this run.

2026-07-19T00:00:00Z — /book-chapter-research 8 check-in: added 1 new
framework, [Four Types of Unfairness](/frameworks/four-types-of-unfairness.md)
(input/output imbalance, double standard, sideways comparison, backward
historical debt) — a taxonomy the author generated live during the Ch8
check-in, richer than the outline's original three key points. Extended
[Scorekeeping Is Contagious](/frameworks/scorekeeping-is-contagious.md) with
a new "The Missing Competition" section (grievance is contagious, gratitude
never is — nobody opens a counter-ledger of thankfulness). Also updated
`01-voice.md` with a new Never Do rule against absolutist dialogue framing
("every single time," "always") in scene dialogue, surfaced during the same
check-in.

2026-07-19T01:00:00Z — Follow-up to the same Ch8 check-in: author raised a
fifth unfairness mechanism (reactivity and industriousness spectrums
silently determining outcomes/workload) and asked for it to be added to the
knowledge layer, plus asked for a research agent to benchmark the author's
whole taxonomy against real academic literature. Added 1 new framework,
[Temperament Asymmetry (Who Cares More Wins)](/frameworks/temperament-asymmetry-who-cares-more-wins.md) —
notably, this framework explicitly names a tension with the book's own
Part I advice (be the calm one) that needs addressing wherever this
material lands, since a naive reading could make the calm partner lose
every negotiation by staying calm. Dispatched a research agent (WebSearch,
no file writes) to find real, verifiable sources on relationship fairness.
Findings: strong support for equity theory (Sprecher 2001; DeMaris 2010)
and the sociological "principle of least interest" (Sprecher, Schmeeckle &
Felmlee 2006, extending Waller 1938) as the ancestor concept to "who cares
more wins" — explicitly distinguished as relationship-wide investment, not
per-decision reactivity. Distributive justice norms in household labor
(Grote & Clark 1998) and the demand-withdraw conflict pattern (Christensen
& Heavey 1990) also verified as real, relevant, adjacent research. The
agent found **no documented study** connecting trait-level industriousness/
conscientiousness to absorbing more household labor via a personally
higher "bar for enough" — flagged explicitly in
`temperament-asymmetry-who-cares-more-wins.md` so that half of the
framework is presented in the manuscript as the author's own observed
pattern, not misattributed to research. Added 5 new citations, all
`status: verifiable`: `sprecher-2001-equity-and-social-exchange.md`,
`demaris-2010-20-year-trajectory-marital-quality.md`,
`sprecher-schmeeckle-felmlee-2006-principle-of-least-interest.md`,
`grote-clark-1998-distributive-justice-family-work.md`,
`christensen-heavey-1990-demand-withdraw.md`. Chapter placement for the
Temperament Asymmetry material (Ch8 vs. Ch9 vs. split) still open —
pending author decision.

## 2026-07-27 — Captured two frameworks flagged by /book-callouts as gaps

`/book-callouts` (run against the Prologue, Introduction, and Ch01–08)
identified two mechanisms already fully written into refined chapter prose
but never captured as their own `okf/frameworks/*.md` concepts: Ch8's
"Tipping Scale" (named as its own distillation mechanism) and Ch6's
"Bucket" (unscheduled, non-recurring labor — stated explicitly in "The
split" section but only as supporting prose). Author confirmed capturing
both. No manuscript changes — both mechanisms and their prose were already
finished and stable; this is a pure knowledge-bundle capture pass.

Added 2 new frameworks:
[The Tipping Scale](/frameworks/the-tipping-scale.md) (`chapter_slugs:
[when-your-marriage-feels-unfair]`) and [The Bucket (Unscheduled
Labor)](/frameworks/the-bucket-unscheduled-labor.md) (`chapter_slugs:
[duty-without-resentment]`). Cross-linked both into their nearest
neighbors' `# Related` sections (`four-types-of-unfairness.md` and
`small-rocks-big-rocks.md`) to keep the concept graph two-way navigable,
and noted in `the-tipping-scale.md` that this is now the third
accumulation-based metaphor in the book (nails/holes in Ch4, rocks/sand in
Ch7, now a tipping scale in Ch8) — worth a `/book-human` or `/book-sweep`
check later for whether three structurally identical metaphors is a
deliberate through-line or a repetition to vary.

Also: author confirmed The River, the Oak, and the Sun (already captured
at `the-river-the-oak-and-the-sun.md`) as the book's signature idea to
build marketing and launch positioning around, ahead of the Three-Second
Window. No file changes from this decision alone — noted here since it's
the kind of framework-priority call that shapes future `/book-marketing`
and `/book-callouts` work.

## 2026-07-27 — /book-signal 8
Added 1 Reader Signal concept (1 confusion; 0 resonance, 0 objection, 0 gift,
0 extension; 0 noise skipped) to okf/signals/. No GIFT responses in this
batch, so no citation gaps were resolved.

## 2026-07-28 — Ad hoc source intake (Instagram carousel, Laurie Santos/Yale course)
Author supplied a 16-slide Instagram carousel (@firstprinciplesconsult,
2026-07-13) summarizing Laurie Santos's Yale course on wellbeing research,
asking to add it as a new framework. Archived the raw carousel content to
`sources/articles/laurie-santos-hedonic-treadmill-instagram.md`, then ran
a full verification pass against primary/secondary academic sources before
writing anything to the bundle (per CLAUDE.md Rule 3 — pop/secondary
sources aren't citable as-is). Verification found two claims confirmed
accurate (the Yale course record; the "miswanting" term, though Santos
teaches rather than coined it), one claim confirmed with corrected
attribution (wanting vs. having as distinct neural systems — Berridge &
Robinson), and three claims that were wrong or outdated as stated: the
post's invented "satisfaction treadmill" name (the real, decades-older
term is the hedonic treadmill, Brickman & Campbell 1971); an overstated
"full baseline" claim for accident victims (the actual 1978 study found
them meaningfully less happy than controls, not equal); an outdated flat
"income plateaus at modest levels" claim (superseded by a 2021 study and
a 2023 resolution); and an inverted claim that the "specific gratitude"
practice is the *most lasting* intervention studied (Seligman et al. 2005
found it produced the largest *immediate* effect but faded within
months — a different exercise, "Three Good Things," was the one that
actually lasted at six months).

Added 1 framework (`the-hedonic-treadmill.md`, corrected version, tagged
`the-discipline-of-joy`) and 7 verified/verifiable or explicitly-flagged
citations: Brickman/Campbell + Brickman/Coates/Janoff-Bulman (hedonic
treadmill), Gilbert & Wilson (miswanting), Berridge & Robinson
(wanting/liking), Kahneman/Deaton/Killingsworth/Mellers (income and
happiness, contested — resolved 2023 version only), Seligman et al.
(gratitude visit vs. Three Good Things), Santos/Yale (course
credibility fact), and Hanson's "taking in the good" (mechanism
verifiable, specific "12-second" duration left `status: unverified`).

## 2026-07-28 — New Chapter 14 ("The Discipline of Enough") inserted into the outline
Reviewing where the Hedonic Treadmill framework belonged, the author
identified a genuine outline gap: no chapter addressed contentment/
"enough," the in-marriage comparison trap (a striking trait in someone
else measured against a wife's whole real person), or the wandering-eye
impulse distinct from the post-divorce version already covered by
`the-new-partner-is-not-better-river-comparison.md`. Author explicitly
requested the countermeasures be organized as proactive vs. reactive,
not just reactive cleanup after the fact.

Added 1 new framework, `the-discipline-of-enough.md` (ip:
author-synthesis — applies the Hedonic Treadmill's external research to
a marriage-specific argument), tagged `the-discipline-of-enough`. No new
external citations — leans on the Hedonic Treadmill's existing citation
set.

Inserted a new Chapter 14, "The Discipline of Enough," into
`03-outline.md`'s Part III, between "Pursue Her After You Have Her" and
"Sex, Rejection, and Self-Respect." Chapters formerly 14–28 renumbered
to 15–29 (mechanically verified in a script pass, not hand-edited, per
CLAUDE.md Rule 15 — chapter count and word-count target updated
accordingly). No existing OKF concept needed a chapter-number update as
a result, since `chapter_slugs` are title-based, not numeric (per
CLAUDE.md Rule 6) — only two frameworks' prose (not their
`chapter_slugs` fields) referenced the old "Chapter 26" by number and
were corrected to "Chapter 27." `book-manifest.json`'s `chapter_count`
updated 28 → 29.

---

## 2026-08-14 — Recovered nine boundary concepts from the abandoned Chapter 10 branch

The Chapter 10 research session (2026-08-08) produced ten OKF concepts
alongside a research brief and a draft. The author judged the draft
incoherent and abandoned it; the whole branch
(`claude/book-resume-vhdk8b`) sat unmerged for five weeks while `main`
moved on, and was deleted after this recovery. The chapter prose is gone
by the author's decision. The concepts are not, because most of them are
his own material captured from a live check-in rather than anything the
failed draft produced.

Imported nine: three frameworks tagged `not-everyone-gets-a-vote`
(`boundary-vs-preference`, `the-cup-two-way-friend-boundary`,
`the-oaks-boundary`), two frameworks already parked for other chapters at
the author's request (`bright-line-boundaries-before-temptation` →
`betrayal-secrets-and-the-work-of-repair`,
`defending-moms-standing-in-the-house` →
`children-exhaustion-and-the-marriage-underneath`), one story
(`the-one-time-loan`), and three external citations (`cloud-townsend-boundaries`
and `tawwab-set-boundaries-find-peace` at `status: verifiable`,
`christakis-fowler-divorce-clustering` at `status: unverified` — a real
peer-reviewed paper whose statistical method has been publicly challenged,
so the concept instructs the chapter to lean on the plain claim rather
than the contested percentages).

**Deliberately not imported:** `the-boundary-i-havent-held.md`, the
author's unresolved first-person material about his mother. Excluded at
his direction on 2026-08-14. It was the most on-topic material in the
batch and was flagged as possibly the chapter's best, so this is a
decision about disclosure, not about quality — worth re-raising if
Chapter 10 is rebuilt and the chapter needs a first-person anchor. The
text survives in git history on the deleted branch's final commit
(`aed5b54`) if the author ever wants it back.

Three imported frameworks cited `chapters/ch10/research.md` for the
brief's claim numbering. Since that brief was discarded, those references
were repointed at `03-outline.md`'s key points (Wisdom is key point 1,
Courage key point 3), which is canonical per CLAUDE.md Rule 6 and
survives a rebuild.

`the-oaks-boundary`'s provenance asserts this chapter's cell is Oak ×
Wisdom ("Discernment in Strength"). Reverified against the current
`05-framework.md` after main's 2026-08-13 renumbering pass: still
correct, unchanged.

---

## 2026-08-17 — Chapter 10 rebuilt and retitled; four citations added, one unassigned

The second research pass for this chapter (the first, 2026-08-08, produced
the draft the author discarded). The author restructured the chapter during
the check-in, which changed what it argues rather than only how much it
commissions: from "outsiders don't get a vote in your marriage" — one
domain, viewed from outside — to "boundaries are the Oak's load-bearing
strength," organized as a discernment test plus three concentric tiers (how
you treat each other → how you act → how you run your family), each closing
on the refrain *the oak holds firm*. Retitled "Boundaries Are Strength."

**Slug migration, per CLAUDE.md Rule 6's retitle playbook.** Counted first:
9 occurrences of `not-everyone-gets-a-vote` in `okf/` and 17 of the old
title text across the book directory. Seven `chapter_slugs` tags migrated to
`boundaries-are-strength` (three frameworks, one story, three citations);
the eighth was cleared rather than migrated (below). Title text updated in
`03-outline.md`, `04-archetype.md`, `05-framework.md` (Oak × Wisdom cell
description and traceability index), `okf/index.md`, `sources/synthesis.md`,
and this bundle's in-law concept. Re-grepped: zero live references to either
old form remain. Occurrences left standing are all historical records —
`provenance` and `structural_resolution` fields, this log's 2026-08-14
entry, `progress.md`, and the outline's own dated revision notes, which
should stay accurate to what happened at the time.

**Four citations created**, all `status: verifiable`, none `verified`
(Rule 11):
- `epictetus-enchiridion-33-character-in-advance` — the chapter's spine. Lay
  down your character in advance and hold it whether alone or in company. Four
  translations (Oldfather, Long, Matheson, one modern) agree on the sense.
  Notable: the disciplined-silence material Ch9 used is the **next sentence of
  the same passage**, which turns what the research pass first flagged as a
  cross-chapter reuse risk into the chapter's opening callback.
- `epictetus-enchiridion-30-relational-duties` — duties measured by relations;
  *but he is a bad father* — "Is your natural tie, then, to a good father? No,
  but to a father." Backs Tier 1's hardest beat (holding a shared line when
  she isn't) and Tier 3's in-laws.
- `epictetus-discourses-3-16-social-contagion` — the soot and the charcoal.
  Optional single use for the gossip pressure; explicitly marked as the first
  thing to cut if the draft runs long.
- `pillemer-five-major-stressors` — in-laws, finances, household labor,
  communication, intimacy. Three of the five are this chapter's three tiers,
  which is independent corroboration that the domains aren't arbitrary.
  `quote_form: none` — cite the finding, never quote it.

**One citation unassigned rather than deleted.**
`christakis-fowler-divorce-clustering` had its `chapter_slugs` cleared to
`[]` when friends were demoted from a domain to a pressure. The concept is
retained: the research is real and a later friendship chapter may want it.
Its verification note was updated with this session's findings — secondary
coverage (Pew, Yale Daily News, Globe and Mail) consistently reports **75%**
higher odds with a divorced close friend and **33%** with a
friend-of-a-friend, while the **"147%" figure recorded in the original note
could not be corroborated anywhere** and should be treated as bad secondary
reporting until a primary source says otherwise.

**Musonius Rufus was cut from this chapter**, at the author's prompting — he
raised the objection himself, that he couldn't see how the passage applied.
He was right. Musonius establishes that marriage is the most necessary human
association, which this book's reader already grants by picking it up, and
never reaches "therefore hold the line." Ch6 had also already introduced him
with "community of life," so he would have arrived as a repeat doing a job
he couldn't finish. `musonius-rufus-on-marriage` is untouched and still
serves its four other chapters.

**Sourcing caveat for everything above.** External WebFetch was blocked
throughout this session (PMC, Perseus, classics.mit.edu, sacred-texts, and
university and publisher domains all refused), so every passage here was
corroborated through search-result summaries across multiple independent
translations or outlets rather than a fetched primary text. That is enough
for `verifiable` and no further. Translator selection for the two Epictetus
anchors is deliberately left open and flagged, because `01-voice.md`'s
em-dash exception depends on knowing whose punctuation a quoted passage
carries.

## 2026-08-27 — Ch11 research pass: six new citations, one gap concept rewritten

Run during `/book-chapter-research 11`, in a fresh-research pass the author
requested after the chapter's "Rock" metaphor was cut from the spec.

**New concepts (all `chapter_slugs: [how-to-endure-without-disappearing]`):**
- `citations/randall-bodenmann-2009-stress-erodes-relationships.md` —
  `verifiable`. Bodenmann's model: chronic *minor* external stress is the
  corrosive kind because it works slowly and largely outside the couple's
  conscious awareness, via reduced shared time, weakened "we-ness," decreased
  self-disclosure, degraded dyadic coping, and withdrawal. This is Ch11's
  mechanism, arrived at independently, and it corroborates the chapter's
  "the season has no edges" observation.
- `citations/falconier-2015-dyadic-coping-meta-analysis.md` — `verifiable`.
  r = .45, 72 samples, 17,856 participants; held across gender, age,
  relationship length, education, nationality.
- `citations/gottman-turning-toward-bids.md` — `unverified`,
  `gap_type: research`. Supplies Ch11's observable test for Claim 1 (bid
  response is a behavior a reader can check tonight; a feeling is not) and
  the scale for Claim 4. The bids framework is safe in plain prose; the
  86%/33% figures are NOT, because every source carrying them is a
  practice blog or popular explainer rather than a primary — exactly the
  pattern CLAUDE.md Rule 3 warns about. The concept also records a bar on
  the "94% divorce prediction accuracy" claim, a known overclaim that must
  not appear in this book under any framing.
- `citations/marcus-aurelius-meditations-4-49-fortunate-not-shattered.md` —
  `verifiable`. Ch11's Claim 2 anchor. Carries a handling note: quote the
  reframe, leave behind the headland image that opens the same section (see
  the outline's recorded reason).
- `citations/marcus-aurelius-meditations-7-57-love-what-happens.md` —
  `verifiable`.
- `citations/epictetus-enchiridion-8-wish-things-as-they-are.md` —
  `verifiable`. The shorter and more usable of the two; states the mechanism
  rather than the sentiment.

**Rewritten:** `citations/amor-fati.md`. Its original gap, open since
2026-06-02 ("primary source material on how this concept appears in the Stoic
texts has not yet been identified"), is closed by *Meditations* 7.57 and
*Enchiridion* 8. Closing it surfaced the larger problem the original note only
gestured at: the phrase is Nietzsche's (*The Gay Science* §276, developed in
*Ecce Homo*), no Stoic wrote it, and `03-outline.md` commissions it as Ch11's
Stoic principle. Status deliberately held at `unverified` — this is not a
sourcing task, because there is no Stoic source for the phrase to find. It is
an author decision, now item 1 in `chapters/ch11/research.md`.

**Not recommended for Ch11, though tagged to it:**
`citations/marcus-aurelius-instruct-or-bear-with-them.md` (*Meditations* 8.59).
It is about bearing with other people's limitations, which in a chapter about a
depleted wife risks casting her as the burden — a direct violation of
`01-voice.md`'s rule against framing her as something to defend against. Left
tagged; flagged in the brief. It belongs to Ch17.

**Sourcing caveat, same as the 2026-08-17 pass.** No primary text was retrieved
this session. The network egress proxy blocked every host carrying one:
pubmed.ncbi.nlm.nih.gov, zora.uzh.ch, d-nb.info, tandfonline.com,
classics.mit.edu, en.wikisource.org, stoicsource.com, marriage.psych.ucla.edu.
Every finding rests on multiple independent secondary listings, which is enough
for `verifiable` and no further. Each concept states this in its own
`verification_note`. Nothing is `verified`; per CLAUDE.md Rule 11 only the
author can advance that, against a physical copy.

## 2026-08-28 — Ch11 re-scope: two concepts for the "going inward" mechanism

The author re-described the chapter's real argument (a taxonomy of suffering
vs. tolerating vs. enduring, with "going inward" as the failure mode common to
all of it) and named the mechanism precisely: the man goes inward, "either
avoiding or over rumination such that he self poisons, eventually letting that
poison out on his wife." Two concepts filed for the two halves of that.

- `citations/treynor-2003-brooding-vs-reflection.md` — `verifiable`. Rumination
  splits into brooding (no solution in view, maladaptive) and reflective
  pondering (aimed at a decision, adaptive). **This is load-bearing rather than
  decorative:** Ch11's failure mode is a man who goes inward, but this book asks
  a man to go inward on nearly every page, so "don't go inward" would
  contradict everything before it. This supplies the actual line.
- `citations/marcus-newhall-2000-displaced-aggression.md` — `verifiable`.
  Triggered displaced aggression: a trivial offense sets off a response sized
  for the load already being carried. The delivery system for the poison. Both
  the effect size and the anger framing carry handling notes — the number
  should not appear in prose, and the passage must describe what he does to
  her, never her provocation of him (`01-voice.md`).

Sourcing caveat unchanged from the 2026-08-27 pass: no primary text retrieved,
egress proxy blocks the journals. Both rest on multiple independent secondary
listings. `verifiable`, not `verified`.

## 2026-08-28 (second entry, same day) — Ch11 Stoic anchors, located at the author's request

The author asked for two phrases to be looked up by description rather than by
citation. Both found, both filed.

- `citations/marcus-aurelius-meditations-10-3-endurable-or-not.md` —
  `verifiable`. He recalled it as "if you were made to endure it, endure it
  without complaint." The actual passage does more than he expected: Marcus
  **sorts before he instructs** (endurable or not, then a different
  instruction per branch), which is structurally the same move the chapter
  makes with its three-row diagnostic. That match is why this beats the
  better-known fortitude lines. Carries a handling note: strip the armor
  reading before use, and quote only the first three sentences.
- `citations/marcus-aurelius-meditations-4-3-no-opinion.md` — `verifiable`.
  His "you don't have to have an opinion about everything." **Two things need
  verifying here, not one:** the wording AND the section number, since the
  sources carrying it are mostly quote aggregators rather than editions.
  Handling note fences it away from the courage beat, where "leave them alone"
  would be exactly wrong.

**Retagging owed.** Three concepts filed during the 2026-08-27 pass were
gathered for Ch11's earlier scope and now fit other chapters better:
`randall-bodenmann-2009-stress-erodes-relationships` and
`falconier-2015-dyadic-coping-meta-analysis` belong with **Ch21** (Children,
Exhaustion, and the Marriage Underneath), which owns the depleting-season
material Ch11 no longer centers; `gottman-turning-toward-bids` fits Ch19 or
Ch21. All three remain good findings. Left tagged to Ch11 for now and flagged
in `chapters/ch11/research.md` so a future drafter is not misdirected;
retag when Ch21 comes up.

## 2026-08-31 — Ch11: five author-IP concepts from the check-in

The author supplied the chapter's real mechanism, and it corrected the
drafter's model rather than supplementing it. Five concepts filed, four
frameworks and one story, all `ip: author` or `author-synthesis`.

- `frameworks/the-deferral-ratchet.md` — **the correction.** The brief had the
  silence starting from depletion. It starts from *good judgment applied three
  times*: no fight in you today; the evening is too good to spoil over one
  biting remark; she is too invested right now. Each is reasonable. Together
  they manufacture a fourth position that is not a reason at all — it is too
  late now — because raising it today means defending a delay rather than
  raising a thing. Then sub-dialogues run constantly, raising anything feels
  frightening because it arrives carrying everything that wasn't raised, and
  she is genuinely lost about why tonight is the night.
- `frameworks/seagull-and-torpedo.md` — the two wrong exits. Carries a firm
  attribution note: "seagull management" is Blanchard's popularization (1984
  interview, 1985 book) and he credited an unidentified British friend, so it
  must not read as the author's coinage; "torpedo" IS the author's own pairing
  and must not be attributed to anyone.
- `frameworks/say-it-dont-require-a-response.md` — the resolution, and the
  load-bearing argument underneath it: if every raise must produce an outcome,
  a man rations his raises, and rationing is how the ratchet starts. Carries
  the Ch5 boundary (Ch5 governs conduct inside a live conflict; this governs
  whether the thing is raised at all).
- `frameworks/double-standards-real-and-false.md` — three cases, so the door
  case cannot collapse into a fairness complaint. The author's yelling example
  is deliberately ambiguous, which is why it works.
- `stories/things-we-tolerate.md` — his own tolerating list. Handling note:
  use two of the four.

**Also revised:** `03-outline.md`'s Ch11 reader ah-ha, replaced by the author.
The drafter's version turned on a two-year accumulation; he rejected the
duration ("2 years is a long time. I don't think that's how it actually
works") and located the failure at an observable moment instead: entire
conversations in your head you are not willing to have with her.

## 2026-09-09 13:00 — House translation ruling applied; ten citations moved to Long (Gutenberg via GitHub)

Author ruling: quote the most modern public-domain translations. Reachable this
session: only George Long's Marcus (Gutenberg #15877) and Epictetus (#10661),
via the GITenberg mirror on raw.githubusercontent.com; archive.org and
Wikisource (Haines 1916, Oldfather 1925/28) remain blocked. Long is also the house standard
`06-sources.md` locked on 2026-09-07; remaining retrofit items are parking-lot #35.

- `citations/epictetus-discourses-2-18-test-the-impression.md` — Ch1 paraphrase-in-quotes replaced with Long verbatim; `verifiable` / `verbatim`.
- `citations/epictetus-enchiridion-1-what-is-in-our-control.md` — Ch2 MIT text miscredited to Carter replaced with Long; `verifiable`.
- `citations/seneca-letter-91-the-unexpected-load.md` — Ch3 splice separated; `unverified` → `verifiable`; XCI.4 tail still to transcribe.
- `citations/marcus-aurelius-meditations-11-18-wrongdoing-is-ignorance.md` — Ch3 Farquharson replaced with Long; em-dash clearance now moot.
- `citations/marcus-aurelius-meditations-6-20-nothing-manly-in-anger.md` — retitled to XI.18; Ch4 Hammond replaced with Long; `unverified` → `verifiable`.
- `citations/marcus-aurelius-meditations-9-28-view-from-above.md` — retitled to IX.30; Ch5 Hammond replaced with Long; em-dash gone; `unverified` → `verifiable`.
- `citations/seneca-letter-75-letters-as-conversation.md` — Ch5 punctuation corrected to Gummere's "together,—spontaneous".
- `citations/marcus-aurelius-concealing-thoughts.md` — Ch9 Hays replaced with Long XII.4.
- `citations/marcus-aurelius-meditations-4-3-no-opinion.md` — retitled to VI.52; resolved into Ch11 with Long wording; `unverified` → `verifiable`.
- `citations/marcus-aurelius-meditations-10-3-endurable-or-not.md` — resolved into Ch11 with Long wording.
- `index.md` — title lines updated to the corrected locators. Slugs unchanged so links keep resolving.

## 2026-09-11 05:20 — Chapter 11 retitled "Speak or Endure"; slug migrated

At the author's direction. The chapter was re-scoped 2026-08-28 from "the
long hard stretch" to a three-way sort (a door, no door, friction), and the
title never followed: "How to Endure Without Disappearing" was written off
the Oak × Courage cell's Ghost wording for the earlier chapter, and named
one pile of three. The new title names the decision the chapter teaches.
Considered on the way: "Three Kinds of Hard," "Quiet Is Not Patience," "Say
It Once," and the author's own "When to Speak, When to Endure," which he
then shortened.

**Slug migration, per CLAUDE.md Rule 6's retitle playbook.** Counted first:
20 live occurrences of `how-to-endure-without-disappearing` (19 concept
files here plus the research brief's slug field), 11 of the old title text
across the book's reference docs and the chapter's own files. All migrated
to `speak-or-endure` in one in-memory pass with a per-file uniqueness
assertion; the first run aborted on a wrong expected total and wrote
nothing, which is the assertion doing its job. Re-grepped: zero live
references to either old form remain. Left standing as history: this log's
2026-08-31 entry, `progress.md`, and the outline's dated revision notes.
`citation-queue.md` regenerated by script (11 lines carry the new slug).
`okf_validate.py --strict` passes.

Also fixed in the same pass, both stale since the re-scope: the outline's
Chapter Sequence Map row for Ch11 (still "active steadiness vs. passive
endurance / amor fati") and Chapter 10's transition line (still promising
"the discipline of years").


## 2026-09-23T04:28:52+00:00 — Chapter 13 authorized research intake

Authority: Author instructed: "Add those items to OKF." Research discussion and authorization, 2026-09-22. No chapter or outline revision approved.

Added two author frameworks and six source/gap concepts; linked two existing citations to Chapter 13 without changing their evidence axes. Preserved author examples as illustrative, not autobiographical. Seneca Letter 58 supplies direct Stoic reception of Heraclitus. Ritual research is a candidate qualification, not a new author ruling. No manuscript or foundation changes.

Deeper research intake 2026-09-23T04:30:26+00:00: added four candidate citations (marital disclosure, stress and support, stress and perception, preference accuracy); upgraded existing Aron 2000 access from search-synthesis to page-text after primary retrieval, preserving the former access note as history. No source set to verified.


## 2026-09-22T23:42:02-05:00 — Chapter 13 Sun-arc direction

Captured author instruction verbatim in an Author Note and indexed it. Earlier research items already exist in OKF; no duplicate sources created. Author requested moving to draft.
