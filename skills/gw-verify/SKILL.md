---
description: The Fact-Checker desk works the citation queue down - probes what is reachable, transcribes real pages where it can, confirms claims by search where that is enough, and packages the rest. Never marks anything verified. Runs anytime after the first refined chapter.
---

<!-- DERIVED FILE - DO NOT EDIT.
     Canonical copy: .claude/skills/gw-verify/SKILL.md
     Regenerate: python3 scripts/sync_plugin_layout.py -->
# /gw-verify — the Fact-Checker

Argument: optional chapter number, slug, or lane. `$ARGUMENTS`

## The rule this command exists to respect

**Search may LOCATE a source or FLAG a defect. It may never TRANSCRIBE a
quotation.** Asked for *Meditations* 10.3 in Long's translation, a search returned
a fluent answer that silently welded Long to an unrelated 18th-century translation
and did not hedge. Nine citation defects reached compiled prose this way, six of
them printed.

**This command never sets `verified`.** That is the author's, against his physical
copy, and no amount of reachability changes it.

## Step 0

`python3 scripts/resolve_book.py`, then read `{bookRoot}/06-sources.md` — house
editions, rights posture, evidence bar. Absent, fall back to `01-voice.md` and
**say that you did**. Never invent a house translation.

## Step 1 — probe, do not reason

Run `scripts/verification_probe.py`. **Do not decide which lanes
are available by reasoning about the environment** — reachability differs between
the cloud container and the author's laptop, and a guess here produces confident
nonsense. The probe is the oracle.

## Step 2 — dispatch

Dispatch `gw-factchecker` with the probe results and the queue. It routes each
citation by tier and reachability, sets the three axes to what it actually looked
at, and proposes fixes rather than rewriting printed prose.

Name the desk.

## Step 3 — regenerate, never hand-maintain

The reader-facing queue is rebuilt wholesale by `scripts/citation_queue.py`.
Never edit it by hand: the retired `sources/citation-manifest.md` claimed
to be derived while nothing derived it, and drifted until its own queue read "None
at this time" with seven concepts waiting.

## Step 4 — gate and report

```
python3 scripts/okf_gate.py
```

Report: what was checked, each citation's three axes and why, every defect, what
is still waiting on the author, and **what could not be reached**. The last one
matters most — an unreachable source reported as checked is the failure this whole
subsystem exists to prevent.

Anything needing his ruling goes to the inbox.
