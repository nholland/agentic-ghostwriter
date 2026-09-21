# Archivist review — 2026-09-21 01:10

**Window:** `6382166..84b7996` (from `.claude/state/retro-window`, verbatim), 2 commits:
`1543f17` (manual regen + republish) and `84b7996` (Stop-hook session log).
`6382166` is the prior retro's end, so this window begins where that one stopped —
contiguous, no gap, no dropped commit.

## #071 held

The earlier dispatch this session (`runs/retro/2026-09-21-plate-packet.md`,
`f4f693c..6382166`) named `1543f17` and `84b7996` as landing after it dispatched
and therefore outside its bounds. They are inside this one. The hook wrote
`6382166 84b7996` and the dispatch matched it exactly. **#071 did not recur.**
Two consecutive dispatches, handed off on a shared boundary commit, lost nothing.

The prior retro's own commit (`runs/retro/2026-09-21-plate-packet.md`, inbox
#075/#076) landed *after* `84b7996` and sits outside this window — it is next
window's business, which is #064's rule working as written, not a defect.

## Lens: what recurs — the derived table that "cannot drift" publishes three broken cells

This is the session's one substantive finding, and it is not the commit's subject;
it is what the commit stepped over.

`1543f17` did two things. It regenerated `docs/manual.html`, and it rewrote
`plate_packet.py`'s docstring first line because that line had wrapped mid-sentence
into the manual's scripts table ("...followed by a page"). The repair was made **at
the input**, one script at a time. The extractor was not touched.

`scripts/manual.py:326` is the extractor:

```python
m = re.search(r'"""\s*(.+)', body)
```

`.` does not match a newline, so the cell is the first *physical* line of the
module docstring — not the first sentence. Measured against the 32 scripts on disk
right now, three cells are still defective, and the artifact republished forty
minutes ago carries all three:

```
$ python3 -c "import sys;sys.path.insert(0,'scripts');import manual;
  print([s['name'] for s in manual.read_scripts()
         if not s['purpose'].endswith(('.','!','?'))])"
['land.py', 'toolcheck.py', 'ttfwidth.py']
```

As published (`docs/manual.html:556,573,574`):

```html
<tr><td><code>land.py</code></td><td>move a chapter from runs/chNN/ (apparatus) into books/&lt;slug&gt;/ (the book),</td></tr>
<tr><td><code>toolcheck.py</code></td><td>report which optional external tools are present, once per</td></tr>
<tr><td><code>ttfwidth.py</code></td><td>text widths from a TrueType file's own tables, for plate_check.py; no font library is installable here."""</td></tr>
```

`land.py` ends on a comma. `toolcheck.py` ends on "once per". `ttfwidth.py` — whose
docstring is a single long line — publishes the closing `"""` as prose. Python
syntax, in the artifact the author shares with readers.

**The shape.** `manual.py`'s own docstring is the cleanest statement of the standard
it is failing: it exists because "every one of those numbers was written by hand and
was right on the day it was typed," and it declares the scripts table derived and
therefore unable to drift. But *derived* was only ever a claim about the source of
the text, never about its fidelity. A lossy extractor produces a **stably** wrong
cell: the digest hashes the extracted purposes, so a truncation is hashed in and
`--check` reports clean over it forever:

```
$ python3 scripts/manual.py --check
manual: in sync (10 cold desks, 20 commands).
```

That is the shape FINDINGS keeps naming — a plausible output, no error, green
check — and the same reason #071's `--applied-by` had to move from a grep to a
fixture: a check that closes over its own defect. It is also #064/#030's family
trait, one layer up: the mechanism was fixed, the *habit* of repairing instances
by hand was not.

**Why it survives assessment.** It cost the author nothing this session — he caught
`plate_packet.py` by eye. That is precisely the problem: the catch was a human
reading a table, and it caught one of four. It is a pattern (4 instances, 3 live),
it is visible to a reader who never saw this session, and the fix has a home that
already exists.

**Placement, not a new check.** `manual.py` already refuses to publish rather than
publish a lie — the block at `:1205-1208` exits 1 with "A manual that invents a gate
is the defect this house exists to prevent." A truncated purpose belongs in that
same refusal. No new script, no new caller, no corpus word.

## Lens: what was missing — the artifact link lives only in a commit message

Both generators end their stale path with the same sentence and neither names the
thing:

```
scripts/manual.py:1226            print("  Then republish the artifact so the author's link is not stale.")
scripts/build_diagrams_page.py:165  print("  Then republish the artifact so the author's link is not stale.")
```

The Stop hook repeats it twice more in `DERIVED`. But
`https://claude.ai/artifact/Lev8Za2Uw2kNW1BUZQSZT7` appears **nowhere in the
repository** — not in `config/house.json`, not in `docs/`, not in a skill:

```
$ grep -rn "claude.ai/artifact" --include=*.py --include=*.md --include=*.sh --include=*.json .
(no match outside runs/log.md)
```

This session it was carried in the author's head and in the dispatch prompt. Forget
it once and `publish` creates a *new* artifact: the repo is in sync, `--check` says
so, and the link the author already sent to readers serves an old manual
permanently, with nothing anywhere able to notice. Two published pages, two chances.

This is Rule 14 verbatim — "a phrase he has to recall is a design defect, not a
training problem" — and Rule 4's test, a gate that cannot see. Lower severity than
the first finding (latent, not live), and the fix is a recorded string plus the
digest that was last published, so the hook can say *which* link and *how far
behind* it is.

## Lens: what was too hard

The publish call refused twice — "you haven't viewed the latest version" — until the
730-line saved artifact source was read in full via the Read tool, because the
artifact tool's own read action returned a truncated head. Real friction, ~3 extra
tool calls. **Not filed:** it is a constraint of the artifact tool, not of this
house, and no rule, script or desk here can shorten it. Naming it so silence is not
read as a pass.

## Lens: what worked

- The Stop hook's `DERIVED` drift block fired on a script landing and produced a
  same-session repair. Already credited by the earlier dispatch; it is load-bearing
  and nothing below deletes it.
- The republish reused the existing artifact URL rather than minting a new one.
  That was the right call and is exactly what the second proposal tries to make
  survive the author's memory.
- `manual.py --check` correctly reported stale, then correctly reported in sync.
  Its digest mechanism is sound; only what it hashes is incomplete.

## Assessed and not filed

- `plate_packet.py`'s new first line ("Build the plate feedback packet: ...") starts
  with a capital while most neighbouring cells start lowercase ("find the book repo
  at runtime", "prove the practice guide still quotes..."). Cosmetic, inconsistent
  both ways already, costs nobody anything.
- `84b7996` is pure Stop-hook bookkeeping. Correct, unremarkable.
- The docstring reflow in `1543f17` also moved the body text into a second
  paragraph, which is the right structure. Nothing to add.

## Corpus

18,540 words (`cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w`),
unchanged from the earlier dispatch this session. Neither proposal adds a corpus
word; the first adds none and deletes none, the second replaces two identical
hard-coded sentences.

## Proposals

Two. **Ranked:** A first — it is live, published, and closes on a fixture plus a
behavioural assertion. B second — latent, but a single forgetting is unrecoverable.
I apply nothing.

### A — the scripts table truncates at the first physical line

```
python3 scripts/inbox.py --add "docs/manual.html's derived scripts table truncates each cell at the first PHYSICAL line of the module docstring, not the first sentence, so three live rows publish mid-sentence and ttfwidth.py's row publishes a closing triple-quote as prose. Should manual.py extract the first sentence and refuse to publish a purpose that does not end in terminal punctuation, in the same block that already refuses to publish an invented gate?" \
    --raised-by gw-retro --chapter 0 \
    --context "manual.py exists because hand-written facts 'were right on the day they were typed', and it declares this table unable to drift. But derived describes where the text came from, not whether it is intact. A truncation is hashed into inputs-digest, so --check reports 'in sync' over it forever - the same close-over-your-own-defect shape that forced #071's proof from a grep to a fixture. This session repaired the fourth instance (plate_packet.py) by hand at the source; the extractor was not touched, so the next wrapped docstring reintroduces it silently." \
    --unblocks "Whether the manual's scripts table is checked for intactness or only for provenance, and whether the three live defects are repaired at the extractor or one docstring at a time forever" \
    --recommend "Parse with ast.get_docstring, take text up to the first sentence terminator, and add truncated-purpose to the existing pre-publish refusal at manual.py:1205 - no new script, no new caller, no corpus word" \
    --evidence \"python3 -c \\\"import sys;sys.path.insert(0,'scripts');import manual;print([s['purpose'] for s in manual.read_scripts() if not s['purpose'].endswith(('.','!','?'))])\\\" -> ['move a chapter from runs/chNN/ (apparatus) into books/<slug>/ (the book),', 'report which optional external tools are present, once per', 'text widths from a TrueType file own tables, for plate_check.py; no font library is installable here.\\\"\\\"\\\"'] - 3 of 32. Published now at docs/manual.html:556,573,574. The extractor is scripts/manual.py:326 m = re.search(r'\\\"\\\"\\\"\\\\s*(.+)', body) - '.' does not match a newline. python3 scripts/manual.py --check -> 'manual: in sync (10 cold desks, 20 commands).' while all three are live.\" \
    --applied-by "test -d tests/fixtures/docstrings && python3 tests/run.py && python3 -c \"import sys;sys.path.insert(0,'scripts');import manual;sys.exit(1 if [s for s in manual.read_scripts() if not s['purpose'].endswith(('.','!','?'))] else 0)\""
```

Price: code, **unmeasured** (not drafted). Corpus: **+0** — it lands inside an
existing refusal block rather than adding a rule. Deletes nothing; **repairs three
published cells** and removes the need to hand-fix a fourth.

The proof has two clauses on purpose. The fixture clause answers `tests/run.py`'s
own standard (a check whose escape is not in `tests/fixtures/` has been asserted,
not proved). The behavioural clause asserts the live state, so the item cannot close
on a fixture that passes while the artifact stays broken — the exact half-fix
`--applied-by` was tightened against. **Both clauses fail today**, the second with
`defective cells: 3 ['land.py', 'toolcheck.py', 'ttfwidth.py']`, exit 1.

### B — the published link is remembered, not recorded

```
python3 scripts/inbox.py --add "Two derived pages tell the author to 'republish the artifact so the author's link is not stale' and neither names the link: https://claude.ai/artifact/Lev8Za2Uw2kNW1BUZQSZT7 appears nowhere in the repo. Should config/house.json record each derived page's artifact URL and the inputs-digest last published to it, so the hook names the link and can say how far behind the published copy is?" \
    --raised-by gw-retro --chapter 0 \
    --context "Rule 14: a phrase he has to recall is a design defect. This session the URL was carried in the author's head and in the dispatch prompt, and the republish correctly reused it. Forget it once and publish mints a NEW artifact: the repo is in sync, --check says so, and the link already sent to readers serves an old manual permanently with nothing able to notice. --check sees the repo file only; the published copy is outside every gate in the house - Rule 4's gate that cannot see. Two published pages, so two chances." \
    --unblocks "Whether 'republish' names a specific link the next time either page goes stale, and whether a published-but-not-republished page is detectable at all" \
    --recommend "One published_artifacts block in config/house.json keyed by output path, holding url and published_digest; manual.py and build_diagrams_page.py print the URL instead of the bare noun and compare published_digest to the computed one; --published updates it" \
    --evidence \"grep -rn 'claude.ai/artifact' --include=*.py --include=*.md --include=*.sh --include=*.json . -> no match outside runs/log.md. The two identical bare sentences are scripts/manual.py:1226 and scripts/build_diagrams_page.py:165, both 'Then republish the artifact so the author's link is not stale.'; the Stop hook repeats the instruction twice more in DERIVED (.claude/hooks/session-stop.sh:67-71). python3 scripts/manual.py --check -> 'manual: in sync (10 cold desks, 20 commands).' - a statement about docs/manual.html only, never about the artifact the reader opens.\" \
    --applied-by "python3 -c \"import json,sys;h=json.load(open('config/house.json'));p=h.get('published_artifacts',{});sys.exit(0 if p.get('docs/manual.html',{}).get('url') and p.get('docs/diagrams.html',{}).get('url') else 1)\" && python3 tests/run.py"
```

Price: **replaces** two identical hard-coded sentences (34 words total, `wc -w` on
the two `print` strings) with the same sentence carrying the URL, plus one JSON
block. Corpus (`CLAUDE.md` + agents + skills): **+0** — nothing here is rule text.

Fails today: `config/house.json` has no `published_artifacts` key.

## What I looked at and found clean

- `.claude/state/retro-window` against the dispatched range — exact match, #071 did
  not recur, handoff from the prior dispatch contiguous.
- `git diff` for both commits in full. `docs/manual.html`'s diff is one table row
  and one digest line — correct and minimal for the change. `runs/log.md`'s entry is
  accurate. `plate_packet.py`'s docstring change is an improvement with no
  behavioural effect.
- `python3 tests/run.py` -> 107/107 fixtures pass.
- `python3 scripts/manual.py --check` -> in sync (true of the repo file; see B).
- Corpus 18,540, flat across the session.
- `FINDINGS.md` (7,436 w) and `.claude/LEARNINGS.md` (14,167 w) read for shape.
  Neither has a prior entry on docstring extraction or on publication state; the
  closest relatives are the citation-manifest / sweep-report "each looked current"
  family, which is why both findings above are framed as that family rather than as
  new kinds.
- Open inbox scanned (30 open, 1 ruled unapplied). Neither proposal duplicates an
  open item; #048's new-file fixture wall applies to A's fixture clause and is
  already filed, so A does not re-raise it.
