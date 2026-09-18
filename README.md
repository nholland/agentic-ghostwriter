# The Agentic Ghostwriter

A book production house that runs on Claude Code. Desks, gated by scripts and by
each other, so the author's time goes to the two things only he can do: **say what
the chapter is, and say whether it landed.**

This repo is the **engine**. The book lives in a separate repo and is **read-only
input**. Nothing here ever writes inside it.

### → [The house manual](docs/manual.html)

The full guide: every desk and what it owns, every command, the counted rules and
their thresholds, how a chapter moves, and what the house will never do. It is
**derived** — the roster, commands, thresholds and scripts are read from the repo
by `scripts/manual.py`, so it cannot drift the way this file used to. Open it in a
browser, or read the published version, which is the same page.

> **Status: the house ships the book.** Chapter 12 was the first chapter through it
> end to end (verdict 2026-09-18), and the same day's migration made this the book
> repo; the old pipeline is frozen in `Playground-260420`. What has actually been
> *measured* is in `FINDINGS.md`; what this house cannot do yet is in `GAPS.md`.

---

## Using it

One repository: the engine, and the book under `books/<slug>/`. So:

1. Start a session on **`agentic-ghostwriter`**.
2. Say **`/gw`**.
3. `resolve_book.py` verifies the book is intact every session start and stops
   everything if it is not.

`/gw` is the only command to remember. Alone it shows what is next and what is
waiting on you; with words after it, the Publisher reads what you mean. Never
compute "next" by reading files — `scripts/next.py` is the oracle.

---

## Loading it

| How the repo arrives | What loads | Notes |
|---|---|---|
| **Attached repo / project** (cloud sessions) | `.claude/skills/`, `.claude/agents/`, `CLAUDE.md` | The author's actual workflow. `.claude/` is canonical. |
| **Plugin** (`claude --plugin-dir .`) | root `skills/`, `agents/`, `hooks/` | Derived by `sync_plugin_layout.py`. `CLAUDE.md` does **not** auto-load here — `/gw-board` reads it explicitly. |

Edit only the `.claude/` copies. The root copies carry a DO-NOT-EDIT banner, placed
*after* the frontmatter so `description` still parses — `claude plugin validate`
caught that the first time it was placed above.

**Every agent is prefixed `gw-` for a mechanical reason:** project `.claude/agents/`
definitions **override same-named plugin agents**. A desk called `editor` or
`researcher` here would be silently replaced by the book repo's version, and a
comparison would test the old desks while reporting on the new ones.

---

## Derived files

These files are generated, and each is checked by the Stop hook rather than by
anyone remembering:

| Run | Derives | Check |
|---|---|---|
| `python3 scripts/sync_plugin_layout.py` | root `agents/`, `skills/`, `hooks/` from `.claude/` | `--check` exits 1 on drift |
| `python3 scripts/manual.py` | `docs/manual.html` from the roster, commands, scripts and thresholds | `--check` exits 1 when the house has changed |
| `python3 scripts/build_diagrams_page.py` | `docs/diagrams.html` from `docs/diagrams/*.svg` | `--check` exits 1 when a drawing changed |

Any file that calls itself derived must have a script deriving it, and any check
that calls itself enforcement must have a caller. That rule exists because
`citation-manifest.md` described itself as derived, nothing derived it, and it
drifted until its own queue read "None at this time" while seven concepts waited.

This README is **not** derived, so it states as little fact as it can get away with.
Counts, rosters and command lists belong in the manual, which is generated. Before
adding a number here, ask whether `manual.py` should be reading it instead.

---

## The map

| File | What it holds |
|---|---|
| `CLAUDE.md` | The Publisher's operating instructions and the standing rules. The house does not edit its own rules: the Archivist proposes, the author applies. |
| `ARCHITECTURE.md` | The seven-layer model, what belongs in which repo, and the "if we lost the book repo" audit. |
| `FLOW.md` | How a chapter moves, stage by stage. |
| `FINDINGS.md` | What has actually been measured, losses included. A bake-off that only records wins is decoration. |
| `GAPS.md` | What the old pipeline does that this house does not, each with the trigger that closes it. |
| `docs/manual.html` | The generated manual. Start here if you are new. |

---

## The bake-off

The house was not adopted because it was newer. Each half was proven on a real
chapter against the pipeline that shipped: the cold half first, drafting from a
brief that pipeline already produced, so the comparison cost the author no extra
time and risked nothing in the book. `/gw-bakeoff N` still builds a blind packet
for any of Ch1-11 (the control lives in the frozen archive), and the script
refuses to unseal which variant is which until the verdict is written — because the
judge is also the person who wants the new system to win. One honest row in
`FINDINGS.md` either way.
