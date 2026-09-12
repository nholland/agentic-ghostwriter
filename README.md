# The Agentic Ghostwriter

A Level 3 book production house. Ten desks, gated by scripts and by each other,
so the author's time goes to the two things only he can do: **say what the chapter
is, and say whether it landed.**

This repo is the **engine**. The book lives in a separate repo and is **read-only
input**. Nothing here ever writes inside it.

> **Status: V1 of the roster is defined and wired. No desk has produced a chapter
> yet.** The pipeline in `Playground-260420` is still the one that ships. What has
> actually been *measured* is in `FINDINGS.md`.
>
> **This repo is an add-on to the book repo, not yet a standalone system.** Every
> desk serves the per-chapter phase; nothing here serves Foundation, so a book can
> be continued but not started. Four of the book repo's production scripts are
> engine code this repo calls by name. `ARCHITECTURE.md` has the seven-layer model,
> the full "if we lost the book repo" audit, and what to move where.

---

## The roster

Two desks need the author in the room, so they run **in session** — a sub-agent
cannot ask him anything, which is the constraint the whole architecture is built
around.

| Desk | Runs as | Invoke |
|---|---|---|
| **The Publisher** | Session persona | `CLAUDE.md` + `/gw-board`, `/gw-inbox` |
| **The Developmental Editor** | Session mode | `/gw-interview` |

Eight run cold as sub-agents:

| Desk | Agent | Driven by |
|---|---|---|
| The Researcher | `gw-researcher` | `/gw-research` |
| The Ghostwriter | `gw-ghostwriter` | `/gw-draft` (also the brief's plan-only reviewer) |
| The Line Editor | `gw-lineeditor` | `/gw-refine` |
| The Conformance Checker | `gw-specchecker` | `/gw-draft`, `/gw-refine`, `/gw-bakeoff` |
| The Anti-Slop Reader | `gw-slopreader` | `/gw-refine`, `/gw-qa` |
| The Fact-Checker | `gw-factchecker` | `/gw-verify` |
| The Reader Panel | `gw-panel` | `/gw-qa` |
| The Publicist | `gw-publicist` | `/gw-market` |

Production is scripts and hooks, not a desk:

| Script | Does |
|---|---|
| `resolve_book.py` | Finds and validates the book repo at runtime. Fails loudly. |
| `okf_gate.py` | The blocking citation gate. Delegates to the book repo's own validator. |
| `voice_check.py` | The counted voice rules, by literal count. |
| `inbox.py` | Everything waiting on the author, in one place. |
| `bakeoff.py` | The blind A/B comparison packet. |
| `sync_plugin_layout.py` | Derives the plugin-root layout from `.claude/`. |

---

## How the book is shared

**By reference, resolved at runtime.** One source of truth, no copies, no drift,
and writes stay one-directional.

```
python3 scripts/resolve_book.py
```

It finds a directory containing `book-manifest.json` — via `$GW_BOOK_REPO`, then
the ordered hints in `config/house.json`, then by scanning siblings — reads the
manifest for the **active** `bookRoot` rather than assuming a slug, and checks that
`01-voice.md`, `00-premise.md`, `03-outline.md`, `okf/` and the book repo's
`okf_validate.py` are actually there. Non-zero exit means no desk may run.

That last part is the point. The first version of this repo hardcoded
`../Playground-260420/books/the-stoic-husband`, which resolved only because two
repos happened to be siblings with those exact names in one session. **A skill
reading a missing voice spec does not crash — it writes generic prose.** A wrong
answer that looks fine is the failure mode this whole repo exists to prevent, so
the path is discovered and validated, never assumed.

**A copy of the book was ruled out.** Two divergent copies of 185 OKF concepts is
the `citation-manifest.md` failure at repo scale: a thing that calls itself derived
with nothing deriving it. Extracting the book into its own repo is the right
long-term shape and is a later migration, not a now one.

---

## Loading it

| How the repo arrives | What loads | Notes |
|---|---|---|
| **Attached repo / project** (cloud sessions) | `.claude/skills/`, `.claude/agents/`, `CLAUDE.md` | The author's actual workflow. `.claude/` is canonical. |
| **Plugin** (`claude --plugin-dir .`) | root `skills/`, `agents/`, `hooks/` | Derived by `sync_plugin_layout.py`. `CLAUDE.md` does **not** auto-load here — `/gw-board` reads it explicitly. |

Edit only the `.claude/` copies. Run `python3 scripts/sync_plugin_layout.py` after
any change and `--check` before committing; it exits 1 on drift. The root copies
carry a DO-NOT-EDIT banner, placed *after* the frontmatter so `description` still
parses — `claude plugin validate` caught that the first time it was placed above.

**Every agent is prefixed `gw-` for a mechanical reason:** project
`.claude/agents/` definitions **override same-named plugin agents**. A desk called
`editor` or `researcher` here would be silently replaced by the book repo's
version, and a comparison would test the old desks while reporting on the new
ones.

---

## The flow

```
/gw-interview 12    Developmental Editor, author in the room. Writes interview.md.
/gw-research 12     Researcher builds the brief. Gated by the Ghostwriter's
                    plan-only review: "could someone who never read the
                    interview write this chapter from this file alone?"
/gw-draft 12        Ghostwriter, cold. Gated by voice_check + the clean-room checker.
/gw-refine 12       Line Editor, cold. Gated by voice_check (run independently of
                    what the desk reported), the Anti-Slop Reader, and the checker.
/gw-verify          Fact-Checker works the citation queue.
/gw-qa              Reader Panel + Anti-Slop Reader, whole book.
/gw-market 12       Publicist drafts. Nothing is ever posted.
/gw-board           Where everything stands.  /gw-inbox  What needs a ruling.
```

Two gate rounds, then the inbox. No desk grades its own counted work — the skill
re-runs the script independently, and **a discrepancy between what the desk
reported and what the script says is itself a finding.** That is precisely the
failure that hit Ch9, Ch10 and the Prologue.

---

## The bake-off

The design proposed proving each desk on a real chapter. That holds — but it
cannot mean running the interview twice: a second interview already knows the
first one's answers, and it is the author's most expensive time. So the two halves
are tested separately.

**Ch12 shadow run — the cold half.** Ch12 ships on the old pipeline as normal;
this one re-runs it from the same brief into `runs/ch12/`. Zero extra author time,
zero risk. `/gw-bakeoff 12` builds a blind packet: two neutrally-named variants, a
counted comparison labelled by variant rather than by system, and a sealed
mapping. The script **refuses to unseal until `verdict.md` has an answer** — the
author is the judge and also the person who wants the new system to win, so the
blind protects the measurement from the judge's preference.

**Ch13 lead run — the warm half.** The Developmental Editor leads the interview.
The baseline already exists: Ch11's brief took **five rounds** of author
correction, and four of the ideas that chapter rests on exist only because he was
in the room.

Record every result in `FINDINGS.md`, losses included. A bake-off that only
records wins is decoration.

---

## What is deliberately not here

**The corpus collapse.** The design targets ~23,000 words against the book repo's
~83,000. It is the most satisfying item on the list and the most dangerous to do
on a clean repo, because that corpus is scar tissue: Rule 9 exists because of two
dating incidents, Rule 11 because nine citation defects reached printed prose,
Rule 15 because of a bulk-edit near-miss. A fresh start makes it frictionless to
write an elegant system that silently drops the rules that only exist because
something broke. The collapse happens last, in the book repo, with the migration
ledger mapping every deleted rule to the desk or script that now enforces it —
after desks have shipped chapters the author approved.

**Any change to the book pipeline.** None has been made.

---

## Migration, when the bake-off earns it

Three switches, each independently reversible:

1. **Reading** — the book repo stays the source of truth for content. Never changes.
2. **Producing** — `/gw-*` writes into `{bookRoot}/chapters/` instead of `runs/`.
   One path change per skill.
3. **Defaulting** — the old `/book-chapter-*` commands retire, with the ledger.

Nothing retires before its replacement has shipped a real chapter he approved.
Until switch 2, the worst case for a failed experiment is a directory of prose
nobody uses.

---

*Design of record: `docs/AGENTIC-PUBLISHING-HOUSE.md` in `Playground-260420`
(2026-09-09), parked there as item #34.*
