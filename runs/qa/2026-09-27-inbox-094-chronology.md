# Author chronology alignment — 2026-09-27 12:16

Author's exact confirmation: “Best friends in 6th grade, 1991. Dating in 10th grade, 1995. Married in 2003. Approved”

Publisher applied factual corrections in the Prologue, Chapter 1, Chapter 12, premise, and the voice constitution's biographical description. Six passages replaced 118 existing words. Fixed years avoid future anniversary drift. The Chapter 12 scene's unsupported twenty-fourth-anniversary/last-year framing was removed without inventing a replacement date. No new OKF concept was created.

The factual phrase in the voice constitution also used a rolling 23-year duration. Only that phrase changed; voice_rules_check confirms all existing thresholds remain aligned. Constitution changes are committed separately on this session's explicit approval.

okf_gate passed before editing. Chapter 12's checked HARD voice rules pass. Prologue and Chapter 1 fail direct-address density both before and after these corrections, as shown below. These pre-existing findings are outside the chronology edit scope; no broader rewrite was made. Metaphor family is unchecked for all three. git diff --check passed. Reader exports were not regenerated.

## prologue before edits

```text

voice_check: refined.md
  2002 words of prose, 175 sentences

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1)
    [ok  ] long-sentence share      11/175 sentences at 25+ words = 6.3% (cap 10%)
             40w: A lot of men skip this kind of work entirely because somewhere along the way they got the idea that a real man...
             33w: If only one of you is, it's still a problem, just a smaller one, and in my experience, one person doing this w...
             30w: Nothing prepares you for what that does to a marriage, and nothing prepares you for how differently grief land...
    [FAIL] you-density              61 direct-address words in 2002 = 30.5 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 9 words, shares 2 words with the previous one. Close: 'You can start building before it stops being fine.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"reframe  'That's not X. That's Y.'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on you-density
  UNCHECKED (not passed): metaphor family

```

## ch01 before edits

```text

voice_check: refined.md
  2032 words of prose, 207 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 795}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 9 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      7/207 sentences at 25+ words = 3.4% (cap 10%)
             41w: Does this moment actually require what you're about to do, or have you already decided and you're just executi...
             30w: The fourth virtue is on the list for exactly this reason. *Brave enough to stay engaged.* The gap is where you...
             30w: Are you governing this impulse before it fires, or have you decided that what you feel is what needs to happen...
    [FAIL] you-density              67 direct-address words in 2032 = 33.0 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 2 words, shares 1 words with the previous one. Close: 'Use it.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"you-don't pivot  'you don't X, you Y'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on you-density
  UNCHECKED (not passed): metaphor family

```

## prologue

```text

voice_check: refined.md
  1989 words of prose, 174 sentences

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1)
    [ok  ] long-sentence share      11/174 sentences at 25+ words = 6.3% (cap 10%)
             40w: A lot of men skip this kind of work entirely because somewhere along the way they got the idea that a real man...
             33w: If only one of you is, it's still a problem, just a smaller one, and in my experience, one person doing this w...
             30w: Nothing prepares you for what that does to a marriage, and nothing prepares you for how differently grief land...
    [FAIL] you-density              61 direct-address words in 1989 = 30.7 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 9 words, shares 2 words with the previous one. Close: 'You can start building before it stops being fine.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"reframe  'That's not X. That's Y.'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on you-density
  UNCHECKED (not passed): metaphor family

```

## ch01

```text

voice_check: refined.md
  2030 words of prose, 207 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 795}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 9 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      7/207 sentences at 25+ words = 3.4% (cap 10%)
             41w: Does this moment actually require what you're about to do, or have you already decided and you're just executi...
             30w: The fourth virtue is on the list for exactly this reason. *Brave enough to stay engaged.* The gap is where you...
             30w: Are you governing this impulse before it fires, or have you decided that what you feel is what needs to happen...
    [FAIL] you-density              67 direct-address words in 2030 = 33.0 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 2 words, shares 1 words with the previous one. Close: 'Use it.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"you-don't pivot  'you don't X, you Y'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: FAIL on you-density
  UNCHECKED (not passed): metaphor family

```

## ch12

```text

voice_check: refined.md
  1279 words of prose, 104 sentences

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 4 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      7/104 sentences at 25+ words = 6.7% (cap 10%)
             42w: She's the one still across from you when they do, and the one who notices first when you drift. **The thing wi...
             39w: He put it this way nineteen hundred years ago, and he wasn't talking about marriage. *"Every habit and faculty...
             32w: It's the small thing that says I still see you rather than I planned something impressive. **What's still ther...
    [ok  ] you-density              66 direct-address words in 1279 = 51.6 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 24 words, shares 4 words with the previous one. Close: "She's been waiting to be one of the necessary things, and the muscle that puts her there is one you can start using toni"
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family

```
