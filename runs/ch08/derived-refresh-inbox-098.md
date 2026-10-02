# Chapters 6 and 8 derived refresh, inbox 098

2026-10-02 00:35

## Scope and changed fields

Only assigned runs artifacts were written. Sources: current book chapter prose, existing book distillations and practice-guide entries, and the two approved inbox-098 patches. No new citations, biographies, or ideas were introduced. Neither book prose nor the shared guide was edited.

Chapter 6: changed Conversation sentence, synthesis, and Lesson. The former conversation claimed resentment “doesn't come from doing too much”; it now allows unseen work and unsustainable work. The synthesis's absolute denial of workload is likewise qualified. The former Lesson located resentment solely in intention and attributed that synthesis to Musonius; the new Lesson states the approved distinction directly without extending his attribution. Mechanism remains The Tally You Don't Read Aloud. Challenge and all three practices remain verbatim. The standalone guide section is unchanged from the book entry.

Chapter 8: changed synthesis, Lesson, and Practice 3. The synthesis and Lesson now cover checking her complaint, jointly examining paid work, housework and remembered responsibilities, present capacity, duration, a concrete request, review, and naming an arrangement that remains unworkable. They no longer teach the removed Seneca no-credit passage. Practice 3 replaces the deed-as-payment reminder with the pause, joint examination, capacity check, concrete request and review. The guide carries that same replacement verbatim. Mechanism remains The Tipping Scale. Conversation sentence, Challenge, and Practices 1 and 2 remain verbatim.

## Judgment calls and limits

The existing proactive duration check remains Practice 2; it complements the updated reactive workload discussion rather than duplicating it. Chapter 6's practices still serve its immediate-response subject; the practical examination of an ongoing burden sits in Chapter 8. Gratitude does not dismiss the need for help in Chapter 8's Lesson.

The unchanged Chapter 8 Practice 1 claims a named irritation “loses its power to quietly compound.” That inherited claim is stronger than the revised prose establishes; retained under the bounded instruction to preserve unaffected practices, not newly endorsed. No placeholders occur in these four outputs. No citation status was changed.

Plain-meaning read: the new material names work, capacity, request, duration, and review directly. It adds no Stoic term requiring a gloss. All CAND lines were read: single-ending judgments do not apply to independent practice lists; no new repeated rhetorical shape or undefined Stoic term was found. Existing chapter distillations are structured summaries, not chapter closes.

## Counted findings and correspondence

The following are diagnostic runs, not a claim that these artifacts pass chapter-prose gates. Title em-dashes and guide bold tags are inherited required structure. Several inherited long sentences remain, and the parser also joins labels/list boundaries to adjacent sentences. Chapter 8 guide's direct-address density is below the chapter-prose floor; imperative instructions address the reader implicitly. These were not grounds to rewrite unrelated fields. Chapter 6's metaphor family is UNCHECKED because none was declared in the commissioned inputs. Chapter 8 uses scale, weight, tip from its existing notes; tip also matches tipping, so it is supplied only once.

Standalone guide correspondence was checked with the actual practice_sync.py parsing and normalization functions, because its CLI targets the shared guide rather than the assigned standalone files:

Chapter 6: PASS, 3 practices identical using practice_sync.py parsers; guide tags Proactive, Reactive, Reactive.
Chapter 8: PASS, 3 practices identical using practice_sync.py parsers; guide tags Reactive, Proactive, Reactive.

## Final voice-check output, verbatim

```text
$ python3 scripts/voice_check.py runs/ch06/distillation.md
voice_check: distillation.md
  350 words of prose, 16 sentences

  HARD (literal counts - a FAIL here is a fact)
    [FAIL] em-dash                  1 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [FAIL] long-sentence share      7/16 sentences at 25+ words = 43.8% (cap 10%)
             40w: Giving freely doesn't mean keeping an arrangement you can't sustain. **Challenge:** It's easy to feel shortcha...
             39w: What's visible right now isn't the same as what's actually true. **Practice:** Once a week, name one thing fro...
             38w: It's backed by a self-check borrowed from Marcus Aurelius: am I actually being lazy right now, or are we just ...
    [ok  ] you-density              17 direct-address words in 350 = 48.6 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 28 words, shares 2 words with the previous one. Close: 'When criticism stings and the feeling lingers, run the self-check before you respond: am I actually being lazy right now'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"you-don't pivot  'you don't X, you Y'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on em-dash, long-sentence share
  UNCHECKED (not passed): metaphor family

$ python3 scripts/voice_check.py runs/ch06/practice-guide-ch06.md
voice_check: practice-guide-ch06.md
  104 words of prose, 4 sentences

  HARD (literal counts - a FAIL here is a fact)
    [FAIL] em-dash                  1 in prose (cap 0)
    [FAIL] bold-as-crutch           3 inline bolded span(s) (cap 1)
    [FAIL] long-sentence share      3/4 sentences at 25+ words = 75.0% (cap 10%)
             38w: Want to sit down, or should I help first?" **Reactive.** When criticism stings and the feeling lingers, run th...
             35w: Say it out loud to her, or just to yourself. **Reactive.** The next time the difference is visible, one of you...
             28w: **Proactive.** Once a week, name one thing from her "bucket," the unscheduled stuff nobody put on a calendar, ...
    [ok  ] you-density              6 direct-address words in 104 = 57.7 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 38 words, shares 1 words with the previous one. Close: 'Want to sit down, or should I help first?" **Reactive.** When criticism stings and the feeling lingers, run the self-che'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on em-dash, bold-as-crutch, long-sentence share
  UNCHECKED (not passed): metaphor family

$ python3 scripts/voice_check.py runs/ch08/distillation.md --metaphor-family scale,weight,tip
voice_check: distillation.md
  333 words of prose, 20 sentences

  HARD (literal counts - a FAIL here is a fact)
    [FAIL] em-dash                  1 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      2/20 sentences at 25+ words = 10.0% (cap 10%)
             43w: The small stuff, an uncredited weekend, a comment that stung more than she meant, a morning you swallowed some...
             29w: On a regular rhythm, monthly, or whenever a season changes, name explicitly whether the current imbalance is t...
    [ok  ] you-density              17 direct-address words in 333 = 51.1 per 1,000 (floor 40)
    [FAIL] metaphor family          4 mentions in 333 words = 12.0 per 1,000 (cap 5); {'scale': 1, 'weight': 1, 'tip': 2}

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 21 words, shares 2 words with the previous one. Close: 'Make one concrete request, hear what she can take on, and agree on when to check whether the change is working.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on em-dash, metaphor family

$ python3 scripts/voice_check.py runs/ch08/practice-guide-ch08.md --metaphor-family scale,weight,tip
voice_check: practice-guide-ch08.md
  114 words of prose, 6 sentences

  HARD (literal counts - a FAIL here is a fact)
    [FAIL] em-dash                  1 in prose (cap 0)
    [FAIL] bold-as-crutch           3 inline bolded span(s) (cap 1)
    [FAIL] long-sentence share      1/6 sentences at 25+ words = 16.7% (cap 10%)
             40w: An irritation you've named loses its power to quietly compound. **Proactive.** On a regular rhythm, monthly, o...
    [FAIL] you-density              4 direct-address words in 114 = 35.1 per 1,000 (floor 40)
    [ok  ] metaphor family          0 mentions in 114 words = 0.0 per 1,000 (cap 5); {}

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 21 words, shares 2 words with the previous one. Close: 'Make one concrete request, hear what she can take on, and agree on when to check whether the change is working.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on em-dash, bold-as-crutch, long-sentence share, you-density
```
