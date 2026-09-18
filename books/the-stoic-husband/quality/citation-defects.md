# Citation defects found by external verification

**Generated from the packet loop, not by hand.** Regenerate the underlying
evidence with `scripts/verification_packet.py`; each defect's full evidence
lives in its `okf/citations/{slug}.md` under `# External Verification`.

**Status as of 2026-09-06: 24 checked (16 Tier 1 quotes, 8 Tier 2 claims). 9 defective, 7 of them printed.** Six of
those are quotations already printed in `manuscript.md`. Nothing has been
rewritten — changing a quotation inside a sentence can break the sentence
around it, so each of these is an author decision.

---

## A. Wrong section number — the text is real, the citation is not

The most common defect and the one nobody would catch by reading. Three of
eight entries in the second packet.

### 1. Ch4 — `Meditations` 6.20 → **XI.18**
Printed: *"there is nothing manly in being angry, but a gentle calm is both
more human and therefore more virile."* (*Meditations*, 6.20.)
The words are Martin Hammond's (Penguin, 2006), excerpted mid-sentence. The
correct locus is **XI.18**. Long's VI.20 is about being scratched during
gymnastic exercise — a different passage entirely.
**Also:** no translator is named in the prose, which makes the line look
edition-neutral. It isn't; Long's XI.18 reads *"to be moved by passion is not
manly, but that mildness and gentleness."*

### 2. Ch5 — `Meditations` 9.28 → **IX.30**
Printed: *"Take a view from above — look at the thousands of flocks and herds,
the thousands of human ceremonies, every sort of voyage…"* (*Meditations*, 9.28.)
Hammond 2006 again, and Hammond's own commentary identifies the passage as
**9.30**. Hays 9.28 is an unrelated reflection on the world's cycles, which
rules out an edition-numbering explanation.
**Also:** the em dash in this quotation is **not** cleared. The verifier could
only see a facsimile extraction rendering it as a hyphen-minus, which does not
prove the printed glyph. `01-voice.md`'s em-dash exception requires confirmed
punctuation, so this one still needs a look at a printed Penguin page.

### 3. Ch11 draft placeholder — `Meditations` 4.3 → **VI.52**, and the
translator is probably wrong too
Not printed; caught before it reached prose. The wording recorded is not Hays
4.3 (which is the withdraw-into-your-own-mind passage) and not Hays 6.52
either. It is most likely Hicks & Hicks, *The Emperor's Handbook* (Scribner,
2002). **Do not print it as Hays 4.3.** Long VI.52 is the public-domain option:
*"It is in our power to have no opinion about a thing."*

---

## B. Misrepresented quotation

### 4. Ch3 — `Letter` 91 is a silent splice
Printed as one continuous two-sentence quotation. In Gummere the two fragments
are in **different sections** with material between them: §3's fragment begins
lowercase after a semicolon and is followed by two further sentences about
strangeness and surprise; §4 then opens with a transitional line before the
second fragment. As printed, the book invents a continuity the source does not
have. Fix by quoting the parts separately or marking the omission.

### 5. Ch2 — `Enchiridion` 1 is attributed to a translator who did not write it
From packet 1. The printed wording is the modernized MIT Classics text, not
Elizabeth Carter's 1759 translation, which reads *"In our Power are Opinion,
Pursuit, Desire, Aversion…"* Recommended fix is Long 1877, the house standard,
whose full wording still needs to be pulled.

---

## C. Wording and punctuation

### 6. Ch3 — `Meditations` 11.18
From packet 1. Printed *"if they do what is wrong"*; Farquharson 1944 reads
*"but if what is wrong."* The quotation is also cut mid-construction — the
sentence is a two-part conditional and starting at "but if" needs the first
half or an ellipsis. **The em dash here IS cleared** as Farquharson's own.

### 7. Ch5 — `Letter` 75
Gummere 1920 prints `together,—spontaneous` — comma immediately followed by
the dash, no space. The book prints `together — spontaneous`.

### 8. Ch11 brief — `Meditations` 4.49
Not printed. Not verbatim Hays: he writes *"It's"* where we have *"It is"* and
joins the clauses with an em dash rather than a comma. Long is materially
different and is the house-standard replacement.

---

### 9. Ch1 — `Discourses` II.18 is a paraphrase printed as a quotation
Found 2026-09-06, in the first claims packet, **after overriding the
verifier's own verdict.** It returned CONFIRMED while its note said "the
manuscript wording is not verbatim George Long, but a close and faithful
paraphrase." Given how Ch1 presents the line, that note is the finding and the
verdict was wrong.

Printed: *"Hold on a moment,"* he told himself, when an impression hit hard.
*"Let me see who you are and what you represent."* (*Discourses*, II.18)

Quotation marks plus a citation means the reader is being told these are
Epictetus's words. Long actually wrote: *"Appearances, wait for me a little:
let me see who you are, and what you are about: let me put you to the test."*

Not "Hold on a moment." Not "what you represent." **A paraphrase set in
quotation marks and cited is a misquotation**, and this one is in Chapter 1,
where it anchors the three-second window.

Two fixes, both clean: quote Long exactly, or drop the quotation marks and let
it read as a paraphrase.

---

## Clean

- Ch2 — `Meditations` 6.8, confirmed against the Haines 1916 scan, wording,
  capitalization and punctuation all matching.
- Ch11 — `Meditations` 7.57, confirmed exactly in Long 1889.
- Ch10 — `Enchiridion` 33, confirmed exactly in Long 1877.
- Ch10 — `Enchiridion` 30; Ch9 — `Discourses` III.16; Ch2 — Brené Brown.
- Ch11 — `Enchiridion` 8, confirmed in Long 1877.

## Corrections to our own records, already applied

- `Enchiridion` 8: edition is Bell & Sons **1877**, not the 1888 recorded.
- `Meditations` 7.57: Long edition is **1889**, not 1888.
- `Enchiridion` 33: our note wrongly attributed the "Immediately prescribe"
  wording to Matheson, who begins *"Lay down for yourself from the first."*


---

## Tier 2, first packet (2026-09-06) — mostly good

Seven of eight held up. Two results are worth recording beyond their verdicts.

**The Gottman 86%/33% figures survived, and my prediction that they would not
was wrong.** They had been filed `unverified` on the reasoning that every
source carrying them was a practice blog. That reasoning was incomplete: the
figures, the six-year follow-up, the 130-couple apartment-lab sample and the
17 divorces are all confirmed in Gottman's own reporting, including an APA
interview in which he states them himself. The remaining limit is narrower and
should be respected in prose: the exact *peer-reviewed* provenance of the
percentage pair is unresolved, so attribute them to Gottman's own account of
the apartment-lab study, never to Driver & Gottman (2004) specifically.

**`gottman-repair-attempts` gained a real paper.** It previously carried
`status: unverified` and a Gottman Institute blog post as its only resource.
The underlying study exists: Gottman, Driver & Tabares (2015), *Journal of
Family Psychotherapy* 26(2), 85-108, DOI 10.1080/08975353.2015.1038962.

**Two evidence caveats, neither a defect.** Cloud & Townsend rests on Google
Books *descriptive text* rather than a page image, and Glover rests on a
publisher catalog page. Both books are paraphrased rather than quoted in the
prose, so there is no wording exposure — but neither should be described as
page-verified, and Glover's edition year should not be stated as 2003 without
the copyright page.

**A standing bar, reaffirmed twice:** no universal divorce-prediction
percentage may be attached to the Four Horsemen or to repair attempts. The
"94% accuracy" claim remains barred from this book under any framing.

---

## Found by the `quote_form` backfill, 2026-09-08

The backfill enumerated every quoted span in `manuscript.md` — 38 of them — and
attributed each. That is a complete pass, not a sample: any citation not matching
one of those spans is provably not quoted verbatim.

### 10. Ch1 — a modern condensation printed as Marcus Aurelius's own words

**Printed** (Ch1, "You Own This"):

> Marcus Aurelius was a Roman emperor… The whole time, he wrote himself notes.
> Not for anyone else to read, not for history. Just reminders, written in the
> middle of everything else. *"You have power over your mind, not outside events.
> Realize this, and you will find strength."*

**The concept's own `resource` field says:** *"Commonly attributed to Marcus
Aurelius, Meditations, loosely associated with Book 2 / Book 12. **Not a verbatim
line in any standard translation** (Hays / Farquharson / Long)."* `status:
unverified`.

Italics and quotation marks, placed immediately after describing him writing his
notes. The reader is told these are his words. They are a modern condensation —
one of the best-known misattributions in popular Stoicism — and unlike defect #9
there is no locator, so a reader who tries to check it finds nothing at all. It
anchors Chapter 1's central move.

**Two clean fixes, both author decisions:**
1. Drop the quotation marks and render it as summary. The sentence still works;
   it just stops claiming to be a quotation.
2. Replace it with a real line carrying the same idea. *Meditations* 12.22 and
   8.47 both do, and Long is public domain under the house standard.

**Why nothing caught this earlier:** it was filed `quote_form: paraphrase`, so the
transcription rule never fired on it. The axis had been set from what the wording
was *intended* to be rather than from how the prose presents it. `.claude/OKF.md`
now states the rule explicitly — quotation marks are a claim about wording, and
the reader cannot see intent.

### 11. Ch8 — *Letter* 81 is a spliced quotation (suspected)

Printed as one continuous quotation with an ellipsis: *"The reward for all the
virtues lies in the virtues themselves… the wages of a good deed is to have done
it."* Same class as defect #4 (the *Letter* 91 splice) and better in one respect —
the omission is at least marked. Not yet confirmed that the two halves appear in
this order or how much sits between them. Lane C; do not close from a search.

### Also flagged, not a defect — Ch8, Pillemer

*"The phrase that kept coming up instead was some version of 'give more than you
get.'"* Quotation marks, but "some version of" says this is a composite of what
many interviewees said rather than one person's words. If that is right, the fix
is to drop the quotation marks rather than to source the phrase — there may be no
single utterance to verify. Recorded as `verbatim` because that is the stricter
reading and the safer error.

### Seven printed quotations moved from "source found" to "needs checking"

Applying the transcription rule to the backfilled ledger dropped seven citations
from `verifiable` to `unverified`: `epictetus-enchiridion-1-what-is-in-our-control`,
`marcus-aurelius-concealing-thoughts`, `marcus-aurelius-meditations-4-49-fortunate-not-shattered`,
`marcus-aurelius-on-correction-and-tolerance`, `pillemer-dont-keep-score`,
`seneca-calm-not-root-out-emotions`, `seneca-letter-81-wages-of-a-good-deed`.

No prose changed. What changed is the ledger's honesty: each is a word-for-word
quotation whose evidence is a search result rather than the page, so the printed
wording was never established. Two of them (`enchiridion-1`, `4-49`) already
carried `DIFFERENT_WORDING` verdicts saying outright that the printed wording is
wrong, while still sitting at `verifiable`.

---

## Found by the Lane B claims pass, 2026-09-08

Nineteen claim-level citations checked against bibliographic records. **No source
turned out not to exist, and no claim turned out to be unsupported.** The yield is
different in kind: scope limits that "confirmed" would otherwise paper over.

### The fix for defect #10 is available

Long, *Meditations* **8.47**: *"If thou art pained by any external thing, it is not
this thing that disturbs thee, but thy own judgement about it. And it is in thy
power to wipe out this judgement now."*

Same idea as the condensation currently printed in Ch1, in a real line, in the
house translation, public domain. A drop-in if you would rather keep a quotation
than convert the passage to summary. (5.16, *"the soul is dyed by the thoughts,"*
is also Long but a different thought.)

### 12. Pillemer — 43 or 44 years?

Our concepts state the 700 elders were married an average of **44 years**, and the
manuscript prints that figure. Author-site and publisher descriptions found in this
pass say **43**. One digit, and it is in the book. Settle it against the
introduction of *30 Lessons for Loving* itself — a number like this drifts through
secondary summaries, which is exactly why it should not be closed from one.

**Also:** `pillemer-five-major-stressors` claims five. Publisher copy names four —
child-rearing, work, money, in-laws. If the book asserts a fifth, locate it in the
text.

### 13. Wiesel — popularized, not coined

The 1986 *US News & World Report* interview (Sanoff, 27 October) is real and
correctly dated, so citing Wiesel for the line is defensible. But Quote
Investigator traces the formulation to Wilhelm Stekel's *The Beloved Ego* (English
translation, 1921), before Wiesel was born. **Do not write "as Wiesel first said"
or otherwise imply coinage.** The manuscript currently renders the idea in its own
words rather than quoting, so there is no wording exposure today — this is a
framing constraint, not a defect in the prose as it stands.

### Scope limits now recorded on the concepts themselves

These are not errors. They are the difference between "the study exists" and "the
study supports what this chapter says," and they now live in each citation's
`verification_note` so they surface in `citation-queue.md`:

| Citation | Limit |
|---|---|
| Jack & Dill 1992 | All three validation samples are **women**, two of them high-distress populations. Applying self-silencing to a husband is an extrapolation past the instrument. |
| Christensen & Heavey 1990 | **n = 31 couples**, and the gendered pattern held reliably *only* when the topic was a change the wife wanted. |
| Sprecher 2001 | **Dating couples, not married.** And the result is asymmetric: *underbenefiting* predicts dissatisfaction, overbenefiting does not. |
| Sprecher, Schmeeckle & Felmlee 2006 | Dating couples again. The principle is **Waller's (1938)**; this paper tests it rather than originating it. |
| Park et al. 2025 | **German** national sample (7,293 couples, 13 years) — strong, but say so rather than implying US data. |
| Rokach et al. 2022 | **Israeli** samples; a scale-development paper, so cite it for the three-factor structure, not for prevalence. |
| Gillespie et al. 2019 | n = 10,236 but a **self-selected online news-site** sample — large, not representative. |
| Sell, Tooby & Cosmides 2009 | Sound, but use the *mechanism* (anger as a bid to renegotiate welfare weighting) rather than the strength-and-attractiveness correlations, which invite a reading this book should not want. |

### Two rights notes for `06-sources.md`

- **Musonius Rufus** — Cora Lutz's 1947 translation is almost certainly still in
  copyright, so it does not fit the public-domain house standard the way Long and
  Gummere do. Fine while the chapter paraphrases; needs a decision before any
  verbatim quotation.
- **Seneca, *De Beneficiis*** — Basore's Loeb (1935) is likewise in copyright. The
  public-domain option is **Aubrey Stewart (1887)**. Also: the specific
  against-keeping-accounts passage was *not* located at a section number and should
  not be cited to one until it is.

---

## Resolved 2026-09-09

**#10 — Ch1, the Marcus condensation. FIXED in `chapters/ch01/refined.md`.**
The author's ruling: drop the quotation marks rather than swap in a real line.
A bare strip would have left *"You have power over your mind…"* floating as the
narrator's own imperative — trading a misquotation for a different problem — so
the passage was recast as reported speech, which is what "summary, not quotation"
actually means:

> Just reminders, written in the middle of everything else. That he had power over
> his own mind, whatever was happening outside it. That this was where whatever
> strength he had left would have to come from. A man in a hard season, reminding
> himself of the one thing he still owned.

Long's *Meditations* 8.47 stays on the shelf if a real quotation is ever wanted in
that slot. It was not used here because thee/thou in Chapter 1's opening beat
fights `01-voice.md`'s reading-level target, and the passage does not need a quote
to land.

**#12 — Pillemer's 43-vs-44 years. SIDESTEPPED in `chapters/ch07/refined.md`.**
Now reads *"married more than four decades,"* which is true under either figure and
needs no page check. The precise number is no longer load-bearing, so the
discrepancy stops being a defect. `pillemer-five-major-stressors` still asserts
five where publisher copy names four — unresolved, and worth naming the stressors
the chapter actually discusses rather than asserting a count.

**#13 — Wiesel. No prose change needed.** The manuscript renders the idea in its
own words rather than quoting, so nothing is wrong today. The constraint is
forward-looking: never write "as Wiesel first said" or otherwise imply coinage.

**`manuscript.md` is now stale** with respect to Ch1 and Ch7. Run `/book-compile`
to regenerate; the compile gate (`okf_validate.py --strict`, Step 4.4) passes.

---

## Resolved 2026-09-09 (second pass) — the house-translation retrofit applied

Long's Marcus and Epictetus were transcribed from Project Gutenberg through its
GitHub mirror (raw.githubusercontent.com/GITenberg/...), the one route to a
primary text this container can reach, and printed per `06-sources.md`. Every
row below has `evidence_source: page-text`; none is `verified` (Rule 11).

| # | Chapter | Defect | Resolution |
|---|---|---|---|
| 1 | Ch4 | 6.20 → XI.18, Hammond | Long XI.18 verbatim, credited |
| 2 | Ch5 | 9.28 → IX.30, Hammond, uncleared dash | Long IX.30 verbatim, credited; dash gone |
| 3 | Ch11 | 4.3 → VI.52 | Long VI.52 verbatim in the refined chapter |
| 4 | Ch3 | Letter 91 splice | Two quotations with prose between; lowercase "it" kept; §4 tail still to transcribe (#35) |
| 5 | Ch2 | Enchiridion 1 miscredited | Long verbatim, credited to Long |
| 6 | Ch3 | 11.18 Farquharson wording | Long verbatim |
| 7 | Ch5 | Letter 75 punctuation | "together,—spontaneous" as Gummere prints it |
| 8 | Ch11 | 4.49 not verbatim Hays | Not quoted in the chapter; nothing to swap |
| 9 | Ch1 | Discourses II.18 paraphrase in quotes | Long verbatim, credited |
| + | Ch9 | Meditations 12.4 was Hays (in copyright) | Long XII.4 verbatim, credited |

Still open from this ledger: #11 (Letter 81 splice, Lane C), #12's stressor
count, and the Ch10 Enchiridion 30 translator question recorded in parking-lot #35.
