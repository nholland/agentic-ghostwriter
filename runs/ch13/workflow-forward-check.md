# Independent workflow forward check

Read only the assigned workflow sources: `.claude/skills/gw-chapter/SKILL.md`, `.claude/agents/gw-retro.md`, and `scripts/next.py`. No parent investigation or intended conclusions were consulted. Executed the real `chapter_state()` function against temporary fixtures, with bytecode writes disabled; no production artifacts were changed by the tests.

## Decisions from the instructions

1. **Refined chapter, passing standalone plate review, no audience report.** Resume scoped chapter review, dispatch the Panel for audience personas, and ensure the Slopreader's coherence review covers the final chapter and relevant context. Reuse any current chapter evidence that already covers its responsibility. Route essential findings, recheck changes independently, and record hashes and actual scope in `review.json`. A plate pass cannot replace chapter review. Continue to compilation/verdict only after those chapter reviews pass. No additional author pause is needed unless an established pause or twice-failed cold gate applies.

2. **Scoped reviews complete; author explicitly deferred older-book issues.** If essential findings affecting this chapter are resolved and evidence is current, proceed to the optional plate and verdict package. Keep the author's older-book deferrals separate and list their inbox IDs in the review record. Do not reopen a whole-book revision campaign or treat those deferrals as unfinished essential chapter work. Run the required inbox listing for the package. The instructions leave editorial judgment about whether a finding is essential to this chapter with the Publisher and reviewing desks.

3. **Author had to request an existing desk; chapter repaired; same event occurred before.** Treat the repair and prevention separately. Read the actual retro window and prior ledgers, identify the recurring missed-dispatch shape, and investigate the existing desk's caller. The chapter repair alone is insufficient evidence that recurrence is prevented. Prefer a proportionate change to the existing dispatch point or an executable missing-evidence check with an identified caller, replacing the ineffective mechanism. If a current remedy already demonstrably prevents recurrence, name its evidence instead; otherwise explain any decision to accept the remaining risk. Return the proposed finding and, if needed, a typed, priced proposal with a reproducible close condition. Do not apply it or create another desk merely because the existing desk was missed.

4. **Clean session; existing automatic checks prevented the known failure.** Name the check and observed prevention under “what worked,” and identify it as an existing remedy for the recurring shape. No change is required merely because the shape has history. A brief finding with clean coverage and no suggestions satisfies the instruction to avoid manufacturing findings. Do not add new rule text, a new check, or an inbox proposal without a remaining substantive gap.

## Temporary fixture results

All fixtures included the normal interview, research, draft, and refined artifacts. Passing review fixtures had separate persona/coherence reports and exact hashes of the refined chapter and a context file.

| Fixture | Actual next stage | Assessment |
|---|---|---|
| Passing plate, no chapter review record | `review` | Matches scenario 1. |
| Current passing scoped reviews plus author-deferred older-book ID | `verdict` | Matches scenario 2. |
| Coherence and plate present, personas absent | `review` | Correctly requires both chapter roles. |
| Persona status `fail` | `review` | Report existence alone does not pass. |
| Refined text changed after review | `review` | Correct freshness failure. |
| Reviewed context changed | `review` | Correct freshness failure. |
| Persona report changed | `review` | Correct evidence integrity failure. |
| Persona scope is JSON `null` | `verdict` | Schema weakness: `str(None)` is nonempty. |
| Standalone plate report labelled as passing personas with scope “Standalone plate only” | `verdict` | Semantic limitation: script trusts the Publisher's role/scope declaration. |
| Valid reviews, deferred older-book item also stored as chapter `inbox.md` | `parked` | Parking marker wins; separate deferrals must not be put there. |
| Recorded verdict, missing review record | `shipped` | Terminal-state precedence preserves completed chapters; it does not audit prior reviews. |

The tested error details correctly identified missing evidence, failed role status, changed input, and changed report. Scenario 3 and scenario 4 are retrospective decisions; `next.py` cannot establish that a retro diagnosed a recurrence or that a preventive change was proportionate. Its chapter evidence gate provides a concrete caller that can prevent a missing-review recurrence before verdict, as shown by the missing-personas fixture.

## Ambiguities and process cost

- The principal route is clear and proportionate: chapter reviews are explicit, evidence can be reused, coverage is scoped, older-book deferrals remain separate, and clean retros need no proposals.
- “Keep author-deferred older-book findings separate” does not explicitly say that `runs/chNN/inbox.md` is a blocking marker regardless of its contents. The fixture shows that separation needs to include storage, not merely wording in a report. `deferred` is recorded but not validated by the oracle; author approval and classification remain human/editorial responsibilities.
- The schema should ideally require scope to be a nonempty string. A null scope currently passes. The script also cannot decide whether a passing report actually discusses the chapter; it checks evidence integrity, not editorial quality. That limitation is consistent with its docstring but should not be mistaken for independent verification of report substance.
- Retro's early “three lines and stop” guidance and its later three-part return format can be reconciled by giving a concise finding, “no suggestions,” and clean coverage. There is no reason to produce a long retro for scenario 4.
- Retro's absolute rule that an addition without a deletion is an “open item” can complicate a necessary preventive check if no meaningful deletion exists. The newly added assessment section still requires a proportionate preventive response or explicit risk acceptance, so I would use an open item instead of inventing a deletion. This is process friction rather than permission to leave a recurrence unassessed.
- Hashing exact reviewed inputs is useful for catching stale evidence. It does require the Publisher to declare all relevant context; the script cannot discover omitted context or distinguish an irrelevant edit from a material one. No full-book reread or additional author approval should be inferred from this bookkeeping.

Overall, the instructions lead to the expected decisions in all four scenarios. The oracle mechanically supports the two chapter decisions and catches stale evidence, with the schema, declaration-trust, parking-marker, and terminal-state boundaries above.

Publisher follow-up: null/list/whitespace scope acceptance was fixed after this review; all three new fixtures now return review. The original observed result above is preserved. Semantic report quality, author deferral classification, and already-recorded verdicts remain deliberately editorial/trusted boundaries.
