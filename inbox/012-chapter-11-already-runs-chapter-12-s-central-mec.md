---
id: 012
status: resolved
raised_by: gw-slopreader
chapter: 12
opened: 2026-09-15 17:56
resolved: 2026-09-16 11:29
applied_by: ! python3 /home/user/agentic-ghostwriter/scripts/voice_check.py /home/user/agentic-ghostwriter/runs/ch12/refined.md --prose-only | grep -q 'The first thing cut'
---

# Chapter 11 already runs Chapter 12's central mechanism, one chapter earlier. How should 12 handle it?

Verified against shipped prose. Ch11 line 37: 'What goes wrong is the order of the cuts... The first thing to go is almost always something that costs only you, because cutting it doesn't require a conversation with anyone. That's what makes it feel like the responsible cut. It's also why nobody notices it's gone, including you.' Ch12 beat 2, titled 'The first thing cut': 'So when a week gets heavy, something gets cut. And the thing that goes first is never the mortgage... You never catch it happening, because it never felt like a decision.' Same mechanism (triage under load), same selection rule (the thing with no external witness goes first), same twist (the cutter never registers the cut), in back-to-back chapters, and neither acknowledges the other. Three fixes, cheapest first: (a) Ch12 claims it as a callback the way it already claims the grandfather - one clause, about eight words: 'Chapter 11 called this the order of the cuts. Here is what gets cut first when the week is only ordinary.' (b) Ch12 differentiates: Ch11's cut happens under a named emergency, Ch12's happens in a week that isn't one. That distinction is real and the chapter does not currently make it. (c) One of the two chapters gives the mechanism up.

**Recommendation:** Do (b), and it costs almost nothing. Ch11's cutting happens inside a crisis; Ch12's happens in an ordinary heavy week, which is the more damaging case precisely because nothing justifies it. Saying that turns a repeat into the sharper version of the idea. (a) is the safe fallback if you want it done in one clause.

**Checked:**

```
gw-slopreader whole-book pass, 2026-09-15: 'Same mechanism, same selection rule, same twist, one chapter apart, in adjacent chapters a reader will read back to back. Neither acknowledges the other. This is the relabelled-mechanism failure in its clearest form, and it is invisible to any single-chapter read.' Publisher verified Ch11 line 37 directly.
```

**What unblocks this:** Whether Ch12 keeps the mechanism as-is, turns it into a callback, or differentiates it from Ch11's emergency framing.

**Resolution (2026-09-16 11:29):** Not a cut - atrophy. The author's reframe: 'I see it less as a cutting and more like atrophy of the muscle. You stop working out the romance muscle and it begins to shrink. You need to keep at it!' This resolves the Ch11 collision by differentiation rather than by callback: Ch11 owns triage under load, the order of the cuts; Ch12 owns disuse and atrophy. Beat 2's label 'The first thing cut' is replaced. It also promotes the muscle from a simile used twice to the chapter's actual mechanism, which fixes the Line Editor's separate flag that the anchor image had thinned to two mentions.

**Not applied yet.** This ruling lands outside this repo. It closes when `! python3 /home/user/agentic-ghostwriter/scripts/voice_check.py /home/user/agentic-ghostwriter/runs/ch12/refined.md --prose-only | grep -q 'The first thing cut'` exits 0.

**Applied, confirmed 2026-09-18 04:52:** `! python3 /home/user/agentic-ghostwriter/scripts/voice_check.py /home/user/agentic-ghostwriter/runs/ch12/refined.md --prose-only | grep -q 'The first thing cut'` now exits 0.
