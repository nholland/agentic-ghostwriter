# Chapter 10 derived refresh: inbox 099

Recorded: 2026-10-02 00:23
Desk: Line Editor

## Scope and result

Read the assigned Chapter 10 authoritative prose above Editor's Notes, existing distillation, Chapter 10 practice-guide section, approved patch, and voice constitution. Wrote only the three commissioned run files. The chapter was not rewritten and no book file was changed.

Kept **The Undecided Line**, the conversation sentence, original summary, Lesson, Challenge, and all three Practice items. Added one summary paragraph making the new scope explicit: decent conduct does not require remaining in harm; an insulting conversation may end; a safe return follows the stated time; recurring mistreatment calls for naming the pattern and seeking help; fear or physical harm calls for safety first. The paragraph also names trust that can take years to rebuild.

The three practices still support naming what a boundary protects, discussing the protected concern rather than arguing over a rule, and recognizing pressure to abandon an agreed boundary. None says to tolerate mistreatment or calls damage permanent. The guide section is unchanged, including its heading, numbering, and Proactive/Reactive tags. Its three practices match the distillation through the production script's parsing and normalization functions.

## Editor's Notes

Representative change: the original summary ended with “Holding one on the night somebody he loves is upset about it is the job.” The added paragraph begins “Keeping your own conduct decent doesn't mean staying in harm's way.” This supplies the approved limit without changing the chapter's mechanism.

Judgement calls: retained the original practices rather than inventing an additional safety exercise. Retained the original Lesson and Challenge because their meaning remains supported by the corrected prose. Added the trust sentence to the summary even though the old distillation did not repeat the irreparability claim, so the updated account includes what these conduct boundaries protect. These are derived summaries of the approved text, not new rules or a guarantee of repair.

Plain-meaning review: the new paragraph names the reader's conduct, ending a conversation, returning safely, seeking help, and getting to safety. It does not portray her mood as an invading threat. No new Stoic term, citation, or factual claim was introduced. No citation status was changed. No unresolved source placeholder is present; the existing “___” is the reader's fill-in exercise.

Counted-check limitation: voice_check is a chapter-prose checker. Its raw results below are failures, not passes. It counts the required heading em-dash and guide tags, merges some list/label boundaries into sentences, and also flags genuinely long inherited sentences. The bounded commission requires keeping existing wording wherever it fits and the guide's existing heading/list format. Those existing items were therefore preserved and the failures surfaced to the Publisher; broader sentence revision was not commissioned. The single-close check is not a distillation/numbered-practice requirement. CAND review found no new repeated rhetorical device or undefined Stoic term; the ending candidates are practice instructions, not competing chapter closes. Metaphor-family counts remain UNCHECKED: no Draft Notes declaration was among this commission's inputs, and none was invented.

The OKF gate ran before writing and returned PASS. No conformance or whole-chapter voice approval is claimed. Publisher owns any reconciliation, landing, independent gate, or wider revision.

## Check output, verbatim

```text
practice_sync parser comparison: runs/ch10/practice-guide-ch10.md vs runs/ch10/distillation.md
  [PASS] Chapter 10: 3 practice(s) identical
```

```text
voice_check: distillation.md
  350 words of prose, 17 sentences

  HARD (literal counts - a FAIL here is a fact)
    [FAIL] em-dash                  1 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [FAIL] long-sentence share      6/17 sentences at 25+ words = 35.3% (cap 10%)
             47w: It will feel like being the bad guy in your own house, and that is exactly the night it counts. **Practice:** ...
             40w: Naming that does two things: it keeps the rule from folding under pressure, and it changes the argument with h...
             31w: **Mechanism:** The Undecided Line **Conversation sentence:** He had rules he'd defend without thinking and had...
    [ok  ] you-density              19 direct-address words in 350 = 54.3 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 30 words, shares 3 words with the previous one. Close: "The next time holding a line would make you the bad guy, notice the trade you're being offered: the thing you were prote"
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"you-don't pivot  'you don't X, you Y'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on em-dash, long-sentence share
  UNCHECKED (not passed): metaphor family
```

```text
voice_check: practice-guide-ch10.md
  100 words of prose, 3 sentences

  HARD (literal counts - a FAIL here is a fact)
    [FAIL] em-dash                  1 in prose (cap 0)
    [FAIL] bold-as-crutch           3 inline bolded span(s) (cap 1)
    [FAIL] long-sentence share      3/3 sentences at 25+ words = 100.0% (cap 10%)
             44w: Ask what each of you thinks it's protecting, and have that argument instead. **Reactive.** The next time holdi...
             29w: Any rule you can't finish is a preference, and it will fold under pressure. **Reactive.** When the two of you ...
             27w: **Proactive.** Write down the three or four lines you and your wife actually hold, and next to each one finish...
    [ok  ] you-density              8 direct-address words in 100 = 80.0 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 44 words, shares 6 words with the previous one. Close: "Ask what each of you thinks it's protecting, and have that argument instead. **Reactive.** The next time holding a line "
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on em-dash, bold-as-crutch, long-sentence share
  UNCHECKED (not passed): metaphor family
```

