# Archivist — 2026-09-21 01:19 — the third self-review, and the proof that closes on `mkdir`

**Window:** `0074d6e3084dafbedfee51dff710a30d403ea42b 6d8c1076661308f9845f3df0d3243761e8ab02a8`,
read verbatim from `.claude/state/retro-window` (#030). Two commits: `3c01a73`
"Archivist review of the manual republish" and `6d8c107` "auto: session log".

**No work was done in this window.** It is the prior retrospective's own output —
`runs/retro/2026-09-21-manual-republish.md`, `inbox/077`, `inbox/078` — plus Stop-hook
bookkeeping. Nothing in it is reviewable as work, and nothing new about the *loop*
needs filing: #074 and #079 already hold it. Per the desk's own damper, that would be
three lines and stop.

One thing survives assessment, and it is not about this window's commits but about
what they *contain*: the two items filed in them cannot close honestly.

---

## Lens: what recurs — a close-condition satisfied by `mkdir`

`#075` and `#077`, filed 01:10 and 01:14, both carry an existence-only proof:

```
075  applied_by: test -d tests/fixtures/plate-names
077  applied_by: test -d tests/fixtures/docstrings
```

Neither directory exists, so both are red today — which is why they were accepted.
But neither *executes* anything. `mkdir -p tests/fixtures/docstrings` closes `#077`
green, and `#077` names a **live** defect: three rows of the scripts table in the
artifact the author has already shared with readers publish mid-sentence, one of them
printing a closing `"""` as prose. Re-measured just now, unchanged:

```
$ python3 -c "import sys;sys.path.insert(0,'scripts');import manual;
  print([s['name'] for s in manual.read_scripts()
         if not s['purpose'].endswith(('.','!','?'))])"
['land.py', 'toolcheck.py', 'ttfwidth.py']
```

So the item written to stop a check from closing over its own defect has, as its
close-condition, a check that closes over its own defect. That is the shape this
ledger keeps naming, now one layer further in: not in the code, in the *proposal*.

**The mechanism, and why a grep would have been better.** `inbox.py:185` fires the
`prove.py` freshness gate only when the literal string `tests/run.py` appears in
`--applied-by`. `test -d tests/fixtures/plate-names` names a fixtures *path* — it
looks more rigorous than the seven greps before it and is strictly weaker, because a
grep at least reads content. `#075`'s own title says "proved by a two-dated-docs
fixture"; its close-condition never runs one. Nine of the last ten gw-retro proofs
execute nothing.

**Why not another guard.** FINDINGS 2026-09-19 07:11 decided to stop hardening this
lineage; `#052` (tautological `applied_by: true`) and `#053` (the reverted widening)
are open on exactly this territory, and an eighth layer was already reverted once for
refusing legitimate filings while being evaded by `cd tests && python3 run.py`. A
ninth would repeat that. The cheap fix is not a gate: **`#077`'s behavioural proof is
already pasted inside `#077`** — the command above, exiting non-zero while any purpose
lacks terminal punctuation. It needs to be moved from the Checked block to the
`applied_by` line. `#075`'s is a fixture in `retro_window_cases()`'s neighbour, which
`#079` has already established exists and is runnable.

## The two items as filed, otherwise

- **`#077`** is correct on the facts. Extractor located (`scripts/manual.py:326`,
  `re.search(r'"""\s*(.+)', body)` — `.` does not match a newline), three live rows,
  `--check` green over all three, repair placed in an existing refusal block rather
  than a new script. No corpus cost. Only its close-condition is wrong.
- **`#078`** is sound and needs nothing. Its `applied_by` reads `config/house.json`
  and exits on the value's absence — it executes, it asserts state, it cannot be
  satisfied by creating an empty thing. It is the counter-example that shows the
  problem in the other two is not "short proofs".

## Folded, not filed: new evidence for #074 / #079

The dispatch prompt called this the fourth consecutive empty-window dispatch. Measured
across all 20 completed windows in `.claude/state/`, it is not consecutive and the
real number is worse in one way and better in another:

```
6 of 20 windows were retro-only (every work commit carried a runs/retro/ file)
4 of the last 7
last 2 consecutive: 84b79969..0074d6e3, 0074d6e3..6d8c10766613
```

And this window supplies a **second independent instance** of the mixed-commit shape
`#079` turns on. `3c01a73` touches `inbox/077`, `inbox/078` *and*
`runs/retro/2026-09-21-manual-republish.md` in one commit:

```
current rule COUNT           = 1   (dispatches)
pathspec ':!runs/retro/'     = 1   (still dispatches — not a fix)
commit-level filter          = 0   (skipped — the fix)
```

`#079`'s own `applied_by` re-run just now: hook exits 2, proof exits 1. Genuinely red,
correctly discriminating. Nothing here needs a fifth item; it belongs in `#074`/`#079`
as an updated count if the author wants it there.

## What worked

- The `retro-window` handoff held for a third consecutive dispatch. `#030`/`#071` are
  not recurring; the window read verbatim was exact and contiguous with the last one.
- `#079` was filed with a genuinely behavioural proof against a real temp worktree —
  the first gw-retro item in ten to execute the thing it is about.
- `inbox.py`'s refusal to open a gw-retro item with an empty `--applied-by` is holding:
  every item since #062 carries one. The failure now is proof *quality*, not absence,
  which is the better problem.

## Measured, for the record

```
$ cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w
18540        (17,017 on 2026-09-19; 16,904 end-of-day 2026-09-18)
```

This window added **zero** corpus words. The proposal below adds zero.
