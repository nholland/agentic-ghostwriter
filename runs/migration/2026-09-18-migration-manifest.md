# Migration manifest — 2026-09-18

**Read this first in the new thread.** It is written to be understood cold, by a
session that saw none of the work. Everything below was produced between
2026-09-15 and 2026-09-18, the first end-to-end run of this house on a real
chapter.

**State in one line:** Chapter 12 is finished prose and has never left this repo.
The book repo has **zero commits and a clean tree** for the whole period.

---

## 1. What the author decided

Ruled in his own words, already applied to the artifacts here:

| | |
|---|---|
| **Mechanism** | Not cutting — **atrophy**. *"You stop working out the romance muscle and it begins to shrink."* This replaced the outline's *askesis* framing and resolved a collision with Ch11, which owns triage under load. |
| **Tone** | *"Light and loving oriented. This is the SUN!"* Part III's register. Diagnose without indicting. |
| **Opening scene** | His wife, after 24 years: *"When was the last time you took me on a date?"* Nearly five months. Replaced an invented composite. |
| **Stoic spine** | Epictetus, *Discourses* 2.18, quoted verbatim from Gutenberg #10661. |
| **Five love languages** | **Kept**, against the research desk's recommendation — *"less scientific when it comes to the specific tactics"*, useful as a way to think about effort. He was right: round 1's case against it was overstated. |
| **His language** | **Touch.** Hers: acts of service — which is his lowest. That asymmetry is the chapter's sharpest line. |
| **Platinum rule** | Kept, attributed to Milton Bennett 1979, **using Bennett's definition** (treat her as *she* wants), not the one he first recalled. Trademark: prose only, never a title. |
| **Nashville** | The flight is a short sightseeing tour. *"I don't want to sound rich."* |
| **Visual language** | `design/plates/` is the standard. The odd file out is **remade, not archived**. |
| **Rule 8** | Approved a narrow constitution exception, applied to `CLAUDE.md`. |
| **Sequencing** | Amend now, migrate after Ch13–14, delete the exception at migration. **He has since chosen to migrate now.** |

---

## 2. Owed to the book repo — nothing has moved

### 2a. Constitution — Rule 8 permits the Publisher to write these

| Source | Destination | Status |
|---|---|---|
| `runs/revisions/2026-09-16-voice-metaphor-cap.md` | `01-voice.md` + `config/house.json` | **Unapplied.** Two halves, must land together. Caps Ch12 at 3 metaphor mentions until it does. |
| `runs/revisions/2026-09-14-01-voice-run-in-headers.md` | `01-voice.md` | Unapplied. Inbox #001. |
| Inbox #018 | `sources/interview-author-stories.md` line 13 | Unapplied. The file says his primary language is words of affirmation; Ch12 prints touch. **The book contradicts itself until this lands.** |

**Blocker, verified:** `voice_rules_check.py` must be fixed **before** the metaphor
cap is applied, or engine and constitution diverge silently. See §4, #024.

### 2b. Output — Rule 8 bars the Publisher from writing these

| Source | Destination | Notes |
|---|---|---|
| `runs/ch12/okf/citations/` (**23 files**) | `okf/citations/` | Shadow tree. **5 of the 23 carry internal links written `](/okf/citations/`, where the book's 54 existing links use `](/citations/`** — those break on arrival unless repointed. Verified 2026-09-18. |
| `runs/ch12/refined.md` (prose above `## Editor's Notes`) | `chapters/ch12/refined.md` | 1,300 words, every counted check passing. |
| `runs/ch12/distillation.md` | `chapters/ch12/distillation.md` | Regenerated from the chapter; `practice_sync` passes. |
| `runs/ch12/research-round2.md` | `chapters/ch12/research.md` | Supersedes `research.md`, which is round 1 and stale. |
| `runs/ch12/interview.md` | `chapters/ch12/` or `sources/` | The author's words, two rounds, five rulings. |
| `runs/appendix/practice-guide.md` | `appendix/practice-guide.md` | **Appends, never rewrites** (Rule 15). Ch12 section only. |
| `runs/ch12/plate.svg` | `design/plates/` | Portrait 500×640. **Draws the old mechanism** — see inbox #019. |
| `runs/design/ch01-distillation.svg` | replaces `visuals/ch01-distillation.svg` | Author ruled it remade. Unresolved: Ch1 would then have three plates on one mechanism. |
| Inbox #005 | `okf/citations/gottman-four-horsemen.md` | Status must drop to `verifiable`, or he confirms against his copy. |
| Inbox #003 | `appendix/practice-guide.md` / `tactics-review.md` | Merge or retire. |

### 2c. Not for the book

`runs/ch12/draft.md`, `conformance*.md`, `brief-gaps.md`, `research.md` (round 1),
`runs/retro/*`, `runs/ch12/pdf/*`. Working apparatus. The **shipped manuscript
contains no distillation at all** — it is apparatus feeding the practice guide.

---

## 3. Chapter 12 — as it stands

```
  1300 words of prose, 106 sentences
    [ok] em-dash 0 (cap 0) · bold-as-crutch 0 inline (cap 1)
    [ok] long-sentence 6/106 = 5.7% (cap 10%) · you-density 48.5 per 1,000 (floor 40)
    [ok] metaphor family 2 mentions = 1.5 per 1,000 (cap 3)
  RESULT: all HARD checks passed
```

`practice_sync` PASS. `okf_gate` PASS. Conformance adjudicated in
`runs/ch12/conformance-refined.md` — the objection row moved FAIL→PASS on the
refined prose, confirmed by a fresh clean-room desk.

**Open against the chapter:** #019 (the plate draws the superseded mechanism) and
#018 (the love-language contradiction).

**Not verified, and it matters before outside readers:** no relationship-science
citation reached a primary source. Only the two Stoic texts did — Gutenberg is
reachable, scholarly hosts are not. Every research citation is search-level, and
**no effect size, sample size or percentage from any of them may be printed.**

---

## 4. The house — four open defects in its own machinery

Filed as inbox items, each closing on a fixture. **#024 blocks the metaphor cap.**

- **#024** — `tests/run.py` scores **14/14 against a `voice_rules_check.py` whose
  `main()` does nothing but return 1**. Nine of fourteen fixtures assert only
  "exited non-zero". No baseline; no DRIFT fixture. **Rule 8(e) rests on this check.**
- **#025** — `package_check.py` passes six packages that open on apparatus, all
  printing `opens on: chapter`. The live renderer emits a classless `<section>`,
  so that string is a default, never a finding.
- **#026** — `tests/run.py` mutates the tracked `config/house.json`; killed
  mid-run it leaves the engine unable to write prose.
- **#027** — the Stop hook's fixture guard skips in five of six tree states,
  including after a commit.

**The pattern across seven retros:** the desks worked; the scripts did not. Every
defect the author caught was in something no script read. Full record in
`runs/retro/` — read `2026-09-18-the-fixtures-cannot-fail.md` first.

---

## 5. Migration — what the new thread does

Inbox **#007**. The author has chosen to do it now rather than after Ch13–14.

**Sequence, and the order matters:**

1. **Fix #024 first.** Everything downstream closes on `tests/run.py`, and it
   currently cannot fail.
2. **Apply the metaphor-cap diff** — both halves, one commit pair.
3. **Move §2b**, repointing the 5 affected citation files' internal links from
   `](/okf/citations/` to `](/citations/`.
4. **Land Ch12** into `chapters/ch12/`, append the practice guide, resolve #019.
5. **Freeze the playground** as read-only archive.
6. **Delete Rule 8's constitution exception.** It ships with its own expiry:
   *"deleted at migration, when this repo owns the book and Rule 8 loses its
   reason."* Also retire the shadow-tree convention and `--prose-only`'s reason
   for existing.

**Do not skip 1.** Applying the cap against an unfixed checker is the
two-sources-of-truth failure the exception was written to prevent.

---

## 6. Where everything is

Branch **`claude/gateway-iqyyso`**, pushed. **Nothing on `main`** beyond the land
of 2026-09-16 (60 commits). The book repo is untouched: `git status --porcelain`
returns 0 lines, 0 commits since 2026-09-15.

Engine `/home/user/agentic-ghostwriter` · book `/home/user/playground-260420`
(cloned fresh each session; not present until attached).
