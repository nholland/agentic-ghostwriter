# Ch15 staged OKF: proposed updates to existing concepts

Researcher desk (gw-researcher), cold run. Written 2026-10-23 15:10 (clock read 14:58 at start).
Sources: `runs/ch15/research-kindness.md` section 8 ("Updates to existing concepts") and
`runs/ch15/research-premise.md` section 10, plus reconciliation links found while staging.

**Nothing below has been applied.** No file in `books/` was edited. Each entry names the exact
file, the exact change, and the authority. Status stays as it is in every case. No entry sets
`verified` or `verifiable`.

Items 1-4 come from the research files' own update lists. Items 5-12 are optional
cross-links and one defect note found while staging; the Publisher decides whether to apply them.

---

## 1. `books/the-stoic-husband/okf/citations/seneca-letter-81-wages-of-a-good-deed.md` (Fact-Checker)

**Why:** the "suspected splice" in its Backfill Note (2026-09-08) is resolved at page-text.
The research pass read Gummere on Wikisource (research-kindness B4 and section 8).

**Frontmatter changes proposed:**
- `evidence_source: search-synthesis` -> `evidence_source: page-text` (the page was read; the
  strongest evidence obtained is now page-text).
- `status`: **unchanged, stays `unverified`** (research-kindness section 8: "Status stays
  `unverified` until reconciled").
- `resource`: append the sentence: `Read on Wikisource in Gummere's translation, Letter 81,
  section 19 (section number is the researcher's reading of Wikisource's markers).`

**Body: append this section, verbatim:**

```
# Splice Check, 2026-10-23 (research, page-text)

Resolved at page-text by the Ch15 research pass (runs/ch15/research-kindness.md, B4):
Gummere on Wikisource, Letter 81.19, reads: "There is not a man who, when he has
benefited his neighbour, has not benefited himself … but that the reward for all the
virtues lies in the virtues themselves. For they are not practised with a view to
recompense; the wages of a good deed is to have done it."

The two printed fragments appear in this order, in one section, with only the sentence
"For they are not practised with a view to recompense;" between them. The section marker
"20." follows. The section number is the researcher's reading of Wikisource's markers.
The printed quotation capitalizes "The reward", which is lowercase mid-sentence in
Gummere; confirm the house treatment. Status stays unverified: only the author can
verify, against his copy.
```

(The ellipsis inside the Gummere passage is the research file's omission.)

---

## 2. `books/the-stoic-husband/okf/citations/impett-peplau-2005-approach-avoidance-sexual-motives.md` (Fact-Checker)

**Why:** possible missing third author (research-kindness A2 and section 8). Search-located,
not resolved.

**Frontmatter change proposed:** append to `verification_note`, verbatim:

```
POSSIBLE AUTHOR-LIST DEFECT (flagged 2026-10-23, runs/ch15/research-kindness.md A2;
search only): the UCLA lab PDF surfaced in search is named Impett_Peplau_Gable_2005.pdf,
and a summary calls the paper "Impett, Peplau & Gable." The author list in `resource`
may be missing Gable. Do not change `resource` until the paper's byline is read.
```

`resource`, `status`, `title`: **unchanged** until the Fact-Checker confirms the byline.

Related staged concept: `runs/ch15/okf/citations/impett-gable-peplau-2005-daily-sacrifice-motives.md`
(a different 2005 paper, *JPSP*).

---

## 3. `books/the-stoic-husband/okf/citations/musonius-rufus-on-marriage.md`

**Why:** research-kindness B2 and section 8: add the "outdo the other in devotion" locus as
search-located. Note that the concept's `description` already says "each striving to outdo
the other in devotion", so this adds the locus and its evidence level, not new content.

**Frontmatter change proposed:** append to `verification_note`, verbatim:

```
"Each striving to outdo the other in devotion" is located by search (2026-10-23,
runs/ch15/research-kindness.md B2) in Lutz Lecture XIIIA, reprinted by Plough. A Thomas
R. Martin rendering in a textbook gives "each works to outdo the other." Search only;
paraphrase only.
```

`status`, `quote_form`, `evidence_source`: **unchanged**.

Optional `chapter_slugs` addition: `be-patient-be-kind` (research-kindness E: "Ch15
callback"; Ch6 already prints Musonius, so a Ch15 use is a callback, not a fresh anchor).

Related staged gap: `runs/ch15/okf/citations/musonius-lecture-14-wording.md`.

---

## 4. `books/the-stoic-husband/okf/citations/epictetus-discourses-2-18-test-the-impression.md`

**Why:** research-premise section 10: "Extend `epictetus-discourses-2-18-test-the-impression.md`
with the habit passage (second excerpt)." Also a slug finding from the reuse check.

**Body: append this section, verbatim:**

```
# Second Excerpt: the habit and sensitization passage (staged 2026-10-23, unverified)

Read at page-text in Long (Gutenberg #10661) by the Ch15 research pass
(runs/ch15/research-premise.md, sections 2 and 3). Same discourse as the Ch1 excerpt;
a second excerpt, not a new source. This section is unverified; the concept-level
`status: verifiable` describes the Ch1 excerpt only.

- "being again excited by the corresponding appearance, it is inflamed to desire
  quicker than before: and when this takes place continually, it is henceforth hardened."
- "when he is again lashed on the same places, the lash will produce not blisters
  (weals) but sores."
- "you have also increased the habit, and in a manner thrown fuel upon fire"
- "If then you wish not to be of an angry temper, do not feed the habit … count the
  days on which you have not been angry"

Context: Epictetus is writing about desire and anger together. The first quotation's
example is the love of money; the remedy he gives is for anger. The ellipsis is the
research file's omission. Proposed for Ch15 (be-patient-be-kind) on "fed up = faster
and hotter" and "you use what rewards". Reuse: Ch1 and Ch12 already print this
discourse; a Ch15 use is a third outing (research-kindness B5: callback only).
```

**Frontmatter changes proposed:**
- `chapter_slugs: [the-three-second-window]` -> add `romance-is-a-discipline`. **Finding:** Ch12
  prints a different II.18 excerpt ("Every habit and faculty is maintained and increased by the
  corresponding actions…", `chapters/ch12/refined.md` line 31, "*Discourses* 2.18, Long trans.").
  The concept does not list Ch12.
- Add `be-patient-be-kind` only if the author keeps the excerpt for Ch15.
- `status`, `quote_form`, `evidence_source`: **unchanged** (they describe the Ch1 excerpt).

**Alternative, if the Publisher prefers one excerpt per concept:** stage the habit passage as
its own concept, `epictetus-discourses-2-18-habit-and-sores.md`, with `status: unverified`,
`quote_form: verbatim`, `evidence_source: page-text`, and the same wording. This desk did not
stage it as a separate file because the research file asked for an extension.

---

## 5. `books/the-stoic-husband/okf/citations/household-labor-and-caretaker-burden.md` (optional)

**Why:** research-kindness A3: "Gordon 2022 and Saxbe 2011 are candidates to fill it, after
Ch7/Ch8 confirm they do not want them."

**Body: append under `# Status`, verbatim:**

```
Candidates located 2026-10-23 (Ch15 research, search only, not read):
/citations/gordon-et-al-2022-appreciation-buffers-housework.md and
/citations/saxbe-repetti-graesch-2011-housework-leisure-recovery.md. Neither fills this
gap until read. Ch7/Ch8 own fairness; Ch15 would use them only for what appreciation
does to a heavy load and for the evening after work.
```

`status`: **unchanged** (`unverified`). Supersession is not proposed: both candidates are
search-only.

---

## 6. `books/the-stoic-husband/okf/citations/seneca-de-ira-on-anger.md` (optional cross-link)

**Why:** this is the generic De Ira gap (Ch4). The Ch15 premise pass located four specific
passages in Stewart. Not a duplicate: those are separate passages with their own locators.

**Body: append, verbatim:**

```
# Related (added 2026-10-23)

Specific De Ira passages read at page-text in Stewart (1889) for Ch15, each unverified:
- [De Ira II.34: a quarrel taken up on one side](/citations/seneca-de-ira-2-34-quarrel-on-one-side.md)
- [De Ira II.29 and III.12: delay](/citations/seneca-de-ira-2-29-and-3-12-delay.md)
- [De Ira II.31: domestic trifles](/citations/seneca-de-ira-2-31-domestic-trifles.md)
- [De Ira III.43: practise humanity](/citations/seneca-de-ira-3-43-practise-humanity.md)
Ch4 printed De Ira as Basore; the house edition for Seneca's dialogues is unruled.
```

`status`: **unchanged**.

---

## 7. `books/the-stoic-husband/okf/citations/seneca-de-beneficiis-against-keeping-accounts.md` (optional cross-link)

**Body: append, verbatim:**

```
# Related (added 2026-10-23)

Other De Beneficiis passages read at page-text in Stewart (1887, Gutenberg #3794) for
Ch15, each unverified: I.1 (given out of weariness), I.6 (the spirit, not the thing),
II.1-3 (give quickly; anticipate), II.6 (no reproach while helping). See the
seneca-de-beneficiis-* concepts. The Ch15 pass did not locate this concept's
"out at interest" passage.
```

`status`: **unchanged**.

---

## 8. `books/the-stoic-husband/okf/citations/seneca-calm-not-root-out-emotions.md` (optional cross-link)

**Body: append, verbatim:**

```
# Related (added 2026-10-23)

For what Seneca actually said about pity and help, read at page-text in Stewart:
[On Clemency II.4-6](/citations/seneca-de-clementia-2-5-6-help-not-pity.md) (unverified).
```

---

## 9. `books/the-stoic-husband/okf/citations/wilcox-dew-2012-date-night-opportunity.md` (optional cross-link)

**Body: append, verbatim:**

```
# Related (added 2026-10-23)

Same survey: [Dew & Wilcox (2013), generosity](/citations/dew-wilcox-2013-generosity.md)
(search only, unverified).
```

---

## 10. Author frameworks written this session (optional links; the Publisher decides)

These are author IP. A link adds no claim to them. Apply only if the Publisher wants the
research reachable from the framework.

- `books/the-stoic-husband/okf/frameworks/would-you-rather-be-right-or-married.md`, end of
  `# Origin`, append: `Ledger entry: [right-or-married-unattributed](/citations/right-or-married-unattributed.md).`
- `books/the-stoic-husband/okf/frameworks/the-home-is-the-haven.md`, append under a `# Related`
  heading: `Research gap, not located: [Saxbe & Repetti (2010)](/citations/saxbe-repetti-2010-home-as-haven.md). The haven idea is the author's family's and needs no source.`
- `books/the-stoic-husband/okf/frameworks/kindness-takes-the-load-off-her-plate.md`, append
  under a `# Related` heading: `Research, search only: [Gordon et al. 2022](/citations/gordon-et-al-2022-appreciation-buffers-housework.md), [dyadic coping](/citations/bodenmann-dyadic-coping-model.md), [Dew & Wilcox 2013](/citations/dew-wilcox-2013-generosity.md).`

---

## 11. Defect noted, not proposed as an edit here (inbox)

`books/the-stoic-husband/okf/citations/marcus-aurelius-meditations-6-20-nothing-manly-in-anger.md`
holds Meditations XI.18 under a 6-20 slug. The real VI.20 (the gymnasium sparring partner) is
not in the bundle (research-premise sections 9 and 10, inbox candidate 3). A rename touches
links and chapter references, so this desk files it as an inbox question, not an edit.
No concept was staged for VI.20 (voice risk) or for XI.18 (barred in Ch15, inbox 111).

---

## 12. Duplicates

No candidate duplicated an existing `okf/citations/` file (checked by filename and by content
grep for each author, title and locator). Two overlaps, both written anyway and recorded here:

- `dew-wilcox-2013-generosity` is listed in both research files; staged once.
- `right-or-married-unattributed` partly overlaps the `# Origin` section of
  `frameworks/would-you-rather-be-right-or-married.md` (a Framework, not a Citation). The
  citation is the ledger entry for the attribution question; see item 10.

## Staging targets for the Publisher

On landing, all 73 files in `runs/ch15/okf/citations/` would go to
`books/the-stoic-husband/okf/citations/`, with `index.md` rows added (not regenerated: Rule 17)
and a `log.md` line. Links in the staged files are bundle-absolute (`/citations/...`,
`/frameworks/...`) and resolve only after landing.
