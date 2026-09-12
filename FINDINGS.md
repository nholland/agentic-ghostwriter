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
