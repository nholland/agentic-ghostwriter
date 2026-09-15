# Chapter 12 — Conformance and Attribution Audit
**Checker:** `gw-specchecker`, clean-room, 2026-09-15
**Inputs:** the outline's Ch12 section + master-table row 12, and the chapter prose.
**Raw result: 4 of 17 rows PASS, 11 attribution findings.**

**Clean-room note — a deliberate deviation by the Publisher.** `gw-draft/SKILL.md`
Step 4 says hand the checker `runs/chNN/draft.md`. That file ends in `## Draft
Notes`, which contains the supersession adjudication table — it would have told
the checker the answers to the rows it was grading. The checker was given the
**prose only**. The skill's letter was not followed; its intent was. Filed as a
finding against the skill, not against the desk.

---

## Adjudication

A raw 4/17 is not a 4/17 chapter. The outline is stale by the author's own
rulings, and the checker is required not to know that. Each FAIL is adjudicated
below.

### Legitimately FAIL against a stale spec — no action

| Row | Why the FAIL stands and nothing is wrong |
|---|---|
| 1 Premise (feeling/practice half) | Superseded. Mechanism is energy allocation. |
| 2 Reader's takeaway | Superseded. "The feeling follows the practice" was replaced. |
| 4 Key point 2 | Superseded — gate rider 1. "Practice until it's who you are" is the askesis framing the author replaced. |
| 6 Central story | The anniversary dinner never existed and was ruled out. Correctly absent. |
| 8 / 15 Reader ah-ha | Superseded; the replacement is **proposed and not ruled**, so no ah-ha is authoritative. See below. |
| 11 Transition to Ch13 | Editorial, not printed. Verified: no transition prose appears between any two chapters in `manuscript.md`. |
| 13 Core argument | Superseded, same as row 2. |
| 9 / 17 Research burden | Author overrode Low → Medium. Density passes. |

### REAL DEFECTS — the supersession does not explain these

**D-1. The word "Stoic" appears zero times in a chapter of a book about Stoicism.**
Verified: `grep -c -i 'stoic'` → **0**. Rows 1, 2, 7 and 16 all touch this and the
checker caught it from four directions. The Marcus passage carries the philosophy
without ever naming it as philosophy.

**D-2. Row 16, the audience objection, is not satisfied — and the brief committed
to satisfying it.** The brief's §0 says it "survives, satisfy it in one clause in
beat 2." The draft writes the objection's exact shape and substitutes *discipline*
for *Stoicism*: "You already run the rest of your life on purpose… Discipline is
the word you'd use for all of it." Since Stoicism is never named, **a reader
holding the objection "I've applied Stoicism already — why marriage-specific?" is
never shown that the thing he has applied is the thing being extended.** The row
was not superseded. It was missed. D-1 is why.

**D-3. An attribution overclaim of exactly the kind this chapter's research pass
was run to prevent.** The finding is hedged correctly and then un-hedged one
sentence later:

> "Partners who feel appreciated **tend to** be more appreciative back… **It
> travels as a loop. Which means it turns the other way just as easily.**"

Gordon et al. 2012 is correlational and longitudinal. It supports *what travels
with what*. It does not support a bidirectional causal claim, and "just as
easily" asserts symmetry that no correlational finding can carry. The research
brief flagged this risk by name; the draft reintroduced it in the prose.

**D-4. Biography asserted as established fact.** "Marcus Aurelius… wrote notes to
himself at night, mostly about how to be a decent man in the morning." The night
composition and the morning framing are characterisation with no source, stated
flatly. Related: the prose asserts as fact both that Marcus read Democritus and
what Democritus said, when that reaches us only as Marcus's own report and the
ascription is not secure. Rule 2 territory.

**D-5. The source paragraph is unattributed.** "Researchers who followed couples
over time keep finding the same shape" — no name, no year, no discipline, and
"keep finding" asserts a converging literature. The Ghostwriter flagged this as a
deliberate call with house precedent (Ch7 names Pillemer directly). Legitimate
either way; it becomes a defect only in combination with D-3, because an unnamed
source cannot carry an un-hedged causal claim.

### AUTHOR-ONLY — a desk overrode a ruling

**D-6. Key point 1 was ruled "Keep" in the interview record and the brief
superseded it anyway.** Two artifacts in direct conflict:

- `interview.md` outline-revision table: *"Key point 1 | **Keep.** The proposed
  extension into men outside relationships is withdrawn."*
- `research.md` §0: *"Key point 1… **That is Chapter 13's premise, nearly
  verbatim.** See §8."*

The brief's reasoning (R-5) is editorially sound — the outline's Ch12 key point 1
really is close to Ch13's stated premise, and the two chapters share a framework
cell. But a cold desk resolved a conflict with a ruling artifact **silently**,
rather than raising it. That is the failure mode the two-touch design exists to
prevent, and it is the most significant desk-behaviour finding of the run.

**Raised as inbox #011.** Not blocking: the chapter is coherent without it.

---

## Attribution audit — the checker's 11 findings, triaged

| Finding | Verdict |
|---|---|
| Grandfather quoted directly, uncheckable | **Fine.** Author's own material, cleared for print. Private speech is not a citation. |
| "Sixty and expecting forty" unsourced in this chapter | **Fine.** Deliberate callback to Ch7, where it is sourced. |
| Marcus: no work, book, section or translator | **Accept for now.** No quotation marks are used, so nothing is presented as transcribed. Naming *Meditations* costs two words and should be considered. |
| Democritus asserted flatly at second hand | **D-4.** Fix. |
| Marcus's composition circumstances as fact | **D-4.** Fix. |
| Bennett: named, dated, no work | **Borderline.** Attributed and checkable enough for prose; the full citation lives in the gap marker. |
| "Platinum rule" credit blurred by "sometimes gets called" | **Fine, and deliberate** — see inbox #010, the trademark. The hedge is doing real work. |
| Longitudinal research unsourced | **D-5.** |
| Certainty inflation on the loop | **D-3.** Fix. |
| "Art as much as science" reading as empirical | **Minor.** It is the author's own line, adjacent to the research paragraph. Worth separating. |
| "Date once a week" as common knowledge | **Fine.** Self-marked as hearsay, and it is the author's own framing. |

---

## Disposition

**Revise round 1 of 2 (Rule 6):** D-1, D-2, D-3, D-4 to the Ghostwriter, cold.
D-5 folded into D-3.
**Inbox #011:** D-6, the key point 1 conflict.
**No action:** every row in the stale-spec table above.
