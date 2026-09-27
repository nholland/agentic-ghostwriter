# Approved terminology, callback and reciprocity edits — 2026-09-26 21:40

Authority: author replied “Approved” to the exact seven proposed replacements for #096, #097 and #100. Publisher implementation in session; no desk ran cold.

Exactly seven replacements across Chapters 4, 6, 8, 9 and 12; 144 existing words replaced. All original strings were asserted unique before writing, all replacements verified, and the complete diff inspected. No broader rewrite or new temperament section. Chapter 9's calm/silence sentence and Chapter 12's chosen “trying to win favor” wording remain unchanged.

okf_gate passed before editing. All five affected chapters passed counted HARD voice checks. Metaphor family remains explicitly UNCHECKED. git diff --check passed. Existing PDF/manuscript exports were not regenerated in this source-edit batch.

## Exact replacements

### ch04

Before: The governing faculty.

After: Your capacity to choose.

### ch06

Before: It closes the gap instead of arguing about whose gap it is.

After: It lets you help each other instead of arguing about who did more.

### ch04

Before: What's already in the fence is Chapter 16's work.

After: What's already in the fence is the work of the chapter on repair.

### ch08

Before: One more kind of unfairness runs underneath all of this. It isn't about labor or money or recognition. It's about temperament, how much of the emotional room in the house one of you takes up at any given moment. The next chapter takes that one on.

After: The next chapter looks at what happens when you stay quiet and expect something back.

### ch09

Before: Chapter 8 already showed you what happens when the calmer person in a marriage never says what they think. The louder, more reactive person wins by default, every time.

After: If you keep your concerns to yourself, the decisions can end up reflecting only what she has said.

### ch12

Before: This is a thing you stopped doing, and starting again asks nobody's forgiveness.

After: This is a thing you stopped doing. You can start again, and you may also owe her an apology.

### ch12

Before: If you give her the bare minimum, the bare minimum is what comes back. That isn't her being petty. That's anyone who's been getting the leftovers long enough to stop expecting better.

After: When you stop making an effort, she may stop expecting it from you.

## Verbatim voice-check output

### ch04

```text
voice_check: refined.md
  1458 words of prose, 153 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 830}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      5/153 sentences at 25+ words = 3.3% (cap 10%)
             58w: Marcus Aurelius wrote it plainly in *Meditations*: "to be moved by passion is not manly, but that mildness and...
             46w: You're running a deeply wired social signal: "You are not treating my interests as real." The signal is real. ...
             36w: When you're depleted and another demand arrives, the scarcity is real. When you feel dismissed in front of you...
    [ok  ] you-density              73 direct-address words in 1458 = 50.1 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 8 words, shares 1 words with the previous one. Close: "That's what leadership looks like from the inside."
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family
```

### ch06

```text
voice_check: refined.md
  1294 words of prose, 101 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 697}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      5/101 sentences at 25+ words = 5.0% (cap 10%)
             47w: It's the visible difference, her hands moving, yours still, that turns an ordinary Tuesday into a verdict. **T...
             33w: Each one also turns a tired woman's comment about laundry into a trial over your character, and that's a fight...
             32w: Most of the time it just happens, one Tuesday at a time, until the dog walks belong to you and the dishes belo...
    [ok  ] you-density              72 direct-address words in 1294 = 55.6 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 5 words, shares 0 words with the previous one. Close: 'Chapter 7 examines the ledger directly.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"reframe  'That's not X. That's Y.'": 1, "you-don't pivot  'you don't X, you Y'": 2}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family
```

### ch08

```text
voice_check: refined.md
  1241 words of prose, 97 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 728}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      7/97 sentences at 25+ words = 7.2% (cap 10%)
             35w: It just keeps it from turning into a pointed comment, a flat tone, a door closed a little harder than it neede...
             34w: The small stuff underneath has been landing for a long time before it ever reaches the surface. **Different sh...
             31w: Two philosophers, one point, coming at you from two directions on purpose: the finished good deed doesn't need...
    [ok  ] you-density              51 direct-address words in 1241 = 41.1 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 19 words, shares 3 words with the previous one. Close: 'Keep gratitude standing in the doorway, and nothing quiet ever gets the chance to build a case against her.'
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family
```

### ch09

```text
voice_check: refined.md
  1259 words of prose, 116 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 1060}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 4 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      6/116 sentences at 25+ words = 5.2% (cap 10%)
             46w: If then a god or a wise teacher should present himself to a man and bid him to think of nothing and to design ...
             36w: "I have often wondered how it is that every man loves himself more than all the rest of men, but yet sets less...
             35w: A yes you gave expecting something back for it, something you never asked for directly, is a deal. Two psychol...
    [ok  ] you-density              56 direct-address words in 1259 = 44.5 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 28 words, shares 1 words with the previous one. Close: 'Next time you\'re about to say "sounds good," check whether it actually is, and if it isn\'t, say so, plainly and kindly, '
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"reframe  'That's not X. That's Y.'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family
```

### ch12

```text
voice_check: refined.md
  1287 words of prose, 105 sentences

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0)
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 4 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      6/105 sentences at 25+ words = 5.7% (cap 10%)
             42w: She's the one still across from you when they do, and the one who notices first when you drift. **The thing wi...
             39w: He put it this way nineteen hundred years ago, and he wasn't talking about marriage. *"Every habit and faculty...
             32w: It's the small thing that says I still see you rather than I planned something impressive. **What's still ther...
    [ok  ] you-density              66 direct-address words in 1287 = 51.3 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 24 words, shares 4 words with the previous one. Close: "She's been waiting to be one of the necessary things, and the muscle that puts her there is one you can start using toni"
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: none matched. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family
```

