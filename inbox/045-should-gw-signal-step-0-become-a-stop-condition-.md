---
id: 045
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-19 15:00
applied_by: grep -q 'runs/signals/' .claude/skills/gw-signal/SKILL.md && grep -q 'dispatch no' .claude/skills/gw-signal/SKILL.md && grep -q 'runs/signals/' skills/gw-signal/SKILL.md && python3 scripts/sync_plugin_layout.py --check
---

# Should /gw-signal Step 0 become a stop condition - save the paste verbatim to runs/signals/, then grep its landmarks against the published chapter and refuse to dispatch a desk if they are not there?

On 2026-09-19 an 11-point editor's log arrived as Ch11 reader feedback, relayed through ChatGPT in voice mode. It described a chapter that does not exist: 'load-bearing' 0 in ch11/refined.md, 'resilien' 0 across all 14 refined chapters, 'couch' 0, 'sickness and in health' 0 in the book, the oak named 0 times in Ch11 prose; the single hit was in the Introduction's Oak section. Had it gone to the Line Editor, a desk would have rewritten a passing chapter (15/15 spec PASS) against notes for a text that does not exist. Step 0 already directs reading the published chapter 'so every response can be matched to the sentence it is about' - a purpose clause, not a gate - and nothing said to keep the paste, so the raw log is now unrecoverable and this incident cannot become a fixture. The fabricated title 'How to Endure Without Disappearing' was Ch11's OWN retired title, dropped 2026-09-11 (03-outline.md L223), so it was plausible against the book's real history. Open question the author raised: that title may indicate he uploaded a stale pre-retitle copy of Ch11, making this part stale-input and only part hallucination.

**Recommendation:** Replace Step 0 with the drafted version in both skill copies and run sync_plugin_layout.py; leave a scripts/signal_match.py unbuilt until a second instance gives it a fixture input

**Checked:**

```
wc -w on the drafted replacement -> 104; wc -w on the existing Step 0 -> 35; corpus 17017 words (cat CLAUDE.md .claude/agents/*.md .claude/skills/*/SKILL.md | wc -w). Landmark counts verified independently this session against books/the-stoic-husband/chapters/ch11/refined.md and runs/manuscript/manuscript-prologue-ch11-2026-09-15.md.
```

**What unblocks this:** Whether gw-signal/SKILL.md Step 0 is replaced with gw-retro's drafted 104-word version (net +69 corpus words, replacing the existing 35)
