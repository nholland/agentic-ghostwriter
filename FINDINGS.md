# Findings

One honest row per experiment. A bake-off that only records wins is decoration.

---

## 2026-09-12 — Stage 0: `voice_check.py` validated against the existing corpus

Before any desk ran, the counted-rules script was calibrated against chapters
whose numbers were already reported, then run across the refined corpus.

**Calibration against Ch11** (reported: 2,828 words, em-dashes 0, long sentences
5.6%, you-density 47.7, door family 2.1/1,000):

| Measure | Reported | Script | Note |
|---|---|---|---|
| Prose words | 2,828 | 2,833 | within 5; hyphenate/possessive tokenisation |
| Em-dashes | 0 | 0 | match |
| Long-sentence share | 5.6% | 5.8% | sentence-split variance |
| You-density | 47.7 | 43.1 | consistent direction; denominator likely differs |
| Door family / 1,000 | 2.1 | 2.8 | prefix matching catches more conjugations |

Ch09 and Ch11 pass every HARD check, which is what their "clean by count" reports
claimed. The script agrees with the record where the record was right.

**Two findings where it does not agree.**

1. **`you-density` is below its floor on three artifacts.** Floor is 40 per 1,000
   (added 2026-07-23 after Ch8 ran at 28). Measured: **ch01 33.0, prologue 30.5,
   introduction 30.8**. All three are below a counted floor and none was flagged.
   The likely cause is the same class as the wife's-mood rule that sat on an
   unpushed branch for five weeks: the floor arrived after ch01 was written, and
   nothing back-scanned the artifacts that predated it. Worth a pass.

2. **The bold cap fails every numbered chapter, and the chapters are not wrong.**
   `01-voice.md` caps bold at one genuine pull-quote per piece. Every numbered
   chapter uses bolded run-in section headers (`**No door.**` alone on its line
   after a divider): ch01 has 5, ch05/ch10/ch11 have 5, ch09 has 4. Prologue and
   Introduction have none. This is a convention the spec never contemplated, not
   eleven defects. The script now counts only *inline* bold against the cap and
   reports run-in headers separately as needing an author ruling — it does not
   exempt them silently, because loosening a counted rule is the author's call.
   Under that split, **ch01 still has 4 genuine inline bolds against a cap of 1.**

**Two defects found in the script itself, both by checking its output against a
known number rather than trusting it.** It first reported Ch11 at 4,325 words and
a "164-word sentence": the apparatus splitter cut each `Editor's Notes` section
individually and resumed counting at the next heading, letting ~1,500 words of
conformance tables back in, and markdown table rows were being counted as
sentences. Prose now ends at the *first* apparatus heading, one boundary, and
table rows are dropped. The general lesson is the compile word-count lesson again:
a counting bug does not error, it just returns a plausible number.

**Status:** no desk has drafted anything yet. Ch12 shadow run is next.

---

## 2026-09-12 — V1 roster wired; three defects found in this repo's own tooling

All ten desks now exist, the two author-facing ones as session modes rather than
sub-agents (a sub-agent cannot ask the author anything, which is the constraint the
architecture is built around). Shared context resolved **by reference**: a copy of
the book was ruled out as the `citation-manifest.md` failure at repo scale.

**The citation-gate regression, found and closed.** The first version of this
repo's `gw-refine` ran no citation check at all, while the book pipeline's
`/book-chapter-refine` and `/book-compile` both run `okf_validate.py --strict` as
a *blocking* gate before writing prose. For a day this replacement pipeline was
**less safe on citations than the pipeline it replaces**, in the exact area where
nine defects reached compiled prose, six of them printed. `scripts/okf_gate.py`
now wraps the book repo's own validator — wraps, not reimplements, because two
validators would drift — and fails closed when it cannot find it. Wired as
blocking into `gw-draft`, `gw-refine`, `gw-research`, `gw-verify` and `gw-market`.

**The hardcoded book path.** `config/house.json` originally held
`../Playground-260420/books/the-stoic-husband`, which resolved only because two
repos happened to be cloned as siblings with those exact names in one session.
Replaced by `scripts/resolve_book.py`: discovery, then validation of every required
artifact, then a non-zero exit that stops every desk. Both the discovery fallback
and the total-failure path were tested, not assumed. The reason this mattered more
than it looks: a skill reading a missing voice spec does not crash, it writes
generic prose.

**`claude plugin validate` caught a bug in the mirror script.**
`sync_plugin_layout.py` prepended a DO-NOT-EDIT banner to each derived file, which
put it *above* the YAML frontmatter — so the frontmatter was no longer at the top
of the file and `description` stopped parsing. Every mirrored skill would have
loaded without the metadata that makes it findable, and nothing would have
errored. The banner now goes after the frontmatter block, and `--check` detects
drift (verified by tampering with a file and confirming exit 1).

Three defects, all three the same shape as the two in the previous entry: **a
plausible wrong answer that raises no error.** None was found by reading the code.
Each was found by running something that could disagree — a known number, a probe,
a validator.

**Two items seeded into `inbox/` from the previous entry's findings**, as the real
first test of whether the inbox holds what the author would want to rule on:
#001 whether bolded run-in section headers are legal, #002 the three artifacts
below the you-density floor.

**Still unproven:** every desk. Nothing here has drafted a chapter.
