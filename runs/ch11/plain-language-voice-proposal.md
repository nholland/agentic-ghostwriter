# Plain-language voice proposal

Status: proposed, not applied. The author requested a new Chapter 11 draft and asked how to make its plain-speaking standard permanent.

The existing constitution already bans indirect gestures and targets sixth-grade prose. The failure is that the qualitative review currently accepts a general impression. Strengthen that existing rule and require evidence of the clarity pass; do not add another numeric readability threshold.

## Exact scope

| File | Words in replaced passages not retained verbatim | Net word change |
|---|---:|---:|
| `books/the-stoic-husband/01-voice.md` | 33 | +318 |
| `books/the-stoic-husband/02-audience.md` | 15 | +58 |
| `.claude/agents/gw-lineeditor.md` | 0 | +70 |

The patch preserves all existing numeric thresholds and the full existing plain-meaning rule, including its tests for cleverness, invented objections, and negative social proof. It replaces the generic qualitative-review paragraph, clarifies one audience description, and extends the Line Editor's existing clarity pass. No author history is deleted. No change to config/house.json is needed.

## Proposed permanent expectation

Name the action, fear, choice, or consequence. State the actual difference when comparing ideas. Complete familiar expressions. Use headings that say what the section is about. A reader should not have to remember a set of metaphor labels to understand the next paragraph. Review this separately from sentence length and vocabulary.

The Ghostwriter already reads 01-voice.md before drafting, and the Anti-Slop Reader already reads its Never Do and Verification sections. This gives both desks the same standard. The Line Editor must show representative repairs and flag meaning it cannot establish without inventing facts.

If approved, apply the attached patch, regenerate the derived plugin layout with scripts/sync_plugin_layout.py, and run voice_rules_check.py, sync_plugin_layout.py --check, and okf_gate.py. Keep the constitution change in its own commit with the author's authorization. The draft itself remains a separate review decision.

## Related limitation

The Chapter 11 outline also names the categories as door/no door/friction and specifies several additional distinctions. The new draft expresses those ideas plainly. If the author chooses to remove a distinction entirely, the outline will need a separate targeted amendment; stronger voice wording alone cannot reduce a chapter's required scope.
