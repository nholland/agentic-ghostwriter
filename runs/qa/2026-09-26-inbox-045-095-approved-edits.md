# Approved feedback and caption batch — 2026-09-26

Authority: author replied “Approved” to the three proposed groups and declining #086. Publisher implementation in session; no desk ran cold.

- #045: replaced the 32-word feedback intake paragraph with 71 words preserving original feedback and metadata, matching the referenced version, allowing paraphrases, and pausing only uncertain affected edits. Mirrored through sync_plugin_layout.py. Net +39 words per copy; +78 across canonical and derived copies. Existing paragraph replaced; no new checker.
- #084: one caption in runs/ch04/plate.svg changed from “The hole remains.” to “It's full of holes.” Refreshed runs/ch04/pdf/plate.png and visually inspected the full rendering. All plate_check rows passed, including grounding, geometry, ink and raster freshness. Fixed the item's truncated multiline completion command; retained proposal history in Git.
- #070/#095: exactly two prose replacements and the Mechanism label approved in chat were applied to Chapter 5 source files. The 19 replaced words are documented in the proposal. No other prose, concepts or constitution changed. Existing PDF/manuscript exports were not regenerated in this source-edit batch.
- #086: declined; existing SVG clipping retained. Revisit only for a demonstrated delivery-format defect.

okf_gate passed before prose edits. Chapter 5 voice_check reported all HARD checks passed; metaphor family remained UNCHECKED. The exact output follows. Mirror synchronization and git diff --check passed. Inbox now reports 21 open and one standing ruled citation tracker.

voice_check: refined.md
  1185 words of prose, 113 sentences
  excluded from counts: {'cut_at_heading': "Editor's Notes", 'apparatus_words': 972}

  HARD (literal counts - a FAIL here is a fact)
    [ok  ] em-dash                  0 in prose (cap 0); 1 inside quoted/blockquoted text, not counted - each needs a verification_note confirming it is the translator's own (lines [63])
    [ok  ] bold-as-crutch           0 inline bolded span(s) (cap 1); 5 bolded run-in header(s), NOT counted - legalized as structure by the author 2026-09-14, per 01-voice.md's run-in header exception.
    [ok  ] long-sentence share      8/113 sentences at 25+ words = 7.1% (cap 10%)
             67w: When you zoom out and the thing is still big, that's the signal. Four places a fight ends up: you let it go; y...
             56w: Seneca's version of it, from a letter to his friend Lucilius: *"I prefer that my letters should be just what m...
             50w: Marcus put a name on the practice: the view from above. *"Look down from above on the countless herds of men a...
    [ok  ] you-density              52 direct-address words in 1185 = 43.9 per 1,000 (floor 40)
    [skip] metaphor family          no family declared - pass --metaphor-family, or have the drafter declare the chapter's anchor image in Draft Notes. UNCHECKED, not passed.

  CAND (needs a read - a clear line here is not a pass)
    [clear ] single ending            final sentence 9 words, shares 0 words with the previous one. Close: "Everything you've built here is what makes it possible."
    [clear ] rhetorical-device repetition no detectable shape over cap 2. Counts: {"you-don't pivot  'you don't X, you Y'": 1}. Regex cannot see every sentence-shape - a model read is still required.
    [clear ] Stoic term gloss on first use every listed term that appears has punctuation or a gloss verb nearby

  RESULT: all HARD checks passed
  UNCHECKED (not passed): metaphor family
