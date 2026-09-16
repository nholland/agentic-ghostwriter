# Revision proposal — the metaphor cap
**Artifact:** `books/the-stoic-husband/01-voice.md` (BOOK REPO — the author applies this; this engine never writes there)
**Raised:** 2026-09-16 · **Trigger:** the author's Ch12 atrophy reframe
**Status:** PROPOSED. Not applied.

## Why

Ch12's mechanism is now the muscle — *"you stop working out the romance muscle and
it begins to shrink"* — so the anchor image is the argument, not decoration. At
1,202 words the current cap permits **3 mentions**; a 4th scores 3.33 per 1,000
and FAILs a HARD check.

The spec already says **"~3 mentions, scaled by length"** and **"roughly 3 times
per 1,000 words."** `config/house.json` hardened *roughly* into exactly 3.00. So
this is less a loosening than a statement of the number the spec meant.

## The edit

`01-voice.md` line 107, counted-rules list:

```diff
- the metaphor word-family cap (~3 mentions, scaled by length)
+ the metaphor word-family cap (~3 mentions per 1,000 words, scaled by length;
+   up to 5 where the anchor image carries the chapter's mechanism rather than
+   decorating it, declared in Draft Notes)
```

## The matching engine change, which must land in the same breath

`config/house.json`:

```diff
-      "value": 3,
-      "spec_probe": "3 total mentions|~3 mentions"
+      "value": 5,
+      "spec_probe": "up to 5 where the anchor image carries"
```

**Do not apply one without the other.** `okf_gate.py` calls a threshold that no
longer matches the spec a structural failure, which is the one class that blocks.

## A defect this surfaced — reported, not fixed

`voice_rules_check.py` checks that each threshold's **source phrase is still
present** in `01-voice.md`. It does **not** check that the phrase's number matches
the value the engine enforces. So today, changing `value` from 3 to 5 while the
spec still reads "~3 mentions" prints `[ok] metaphor_family_max_per_1000 = 3`
and exits 0 — the engine would enforce 5 against a constitution saying 3, and
every gate would stay green.

That is the two-sources-of-truth failure the house is built against, inside the
check built to prevent it. Fix: have the probe extract the number and compare it
to `value`. **Archivist's to propose, the author's to apply.**

## Effect on Ch12

At ~1,222 words after the rewrite, a cap of 5 permits **6 mentions** (6/1222 =
4.91). Enough for the mechanism to run through the chapter instead of appearing
twice.
