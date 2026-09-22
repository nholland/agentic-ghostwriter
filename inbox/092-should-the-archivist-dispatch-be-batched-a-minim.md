---
id: 092
status: open
raised_by: Publisher
chapter: 0
opened: 2026-09-22 22:58
---

# Should the Archivist dispatch be batched (a minimum number of watched-path commits accumulated) instead of firing on every Stop-hook checkpoint that finds even one unreviewed commit?

Tonight's session dispatched gw-retro five times in under 40 minutes chasing one plate's canyon measurement, each round several minutes long. Every round found something real - a wrong comparison band, a tautological proof, a proof with a blind spot, a second blind spot in the fix for the first - so the reviews were not noise. But the author said directly, mid-session, 'it takes forever,' and asked whether to reduce the Archivist's mandate. .claude/hooks/retro-check.sh already deliberately rejected a commit-count threshold: its own header says 'per session, not every N commits' and explains why - the old pipeline's threshold existed to stop a different loop (retrospectives editing rule files, which is now structurally impossible since the Archivist never applies and rule paths are unwatched), so 'frequency is no longer the danger, and the author asked to learn from each session.' That was a real prior decision, not an oversight. What changed tonight is not the hook's logic but the session's shape: many Stop-hook checkpoints in one continuous working session, each with at least one new watched-path commit, fired the full five-lens review every time rather than once.

**Recommendation:** Keep 'per session' as the concept but redefine what counts as one: require a minimum number of accumulated watched-path commits (for example 3-5) since the last dispatch before firing, rather than firing on the first Stop-hook checkpoint with even one. A long single-topic working session like tonight's would then get one or two dispatches instead of five, while a short session with real but sparse changes still gets reviewed before it ends. Leave the desk's own damper (nothing substantive, three lines, stop) and the never-applies rule untouched - narrow the trigger, not the mandate.

**Checked:**

```
Session transcript: five gw-retro dispatches between roughly 22:22 and 22:56 (Part-plate drafts review, the canyon-void re-verification, the correction-of-the-correction, the chain-close review, plus one the Publisher chose to skip rather than dispatch). All five had at least one real, non-duplicate finding. .claude/hooks/retro-check.sh header, read in full, documents the 'per session not every N commits' decision and its reasoning.
```

**What unblocks this:** Whether the Archivist's mandate itself needs narrowing, or whether the fix is entirely in when it fires - the Publisher's read is the latter: the five-lens review is doing real work each time it runs, and batching would keep that value while cutting how often the author waits for it
