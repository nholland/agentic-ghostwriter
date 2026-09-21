---
id: 078
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 01:14
applied_by: test -f config/house.json && python3 -c "import json;h=json.load(open('config/house.json'));p=h.get('published_artifacts',{});exit(0 if p.get('docs/manual.html',{}).get('url') else 1)"
---

# Two derived pages tell the author to 'republish the artifact so the author's link is not stale' and neither names the link: https://claude.ai/artifact/Lev8Za2Uw2kNW1BUZQSZT7 appears nowhere in the repo. Should config/house.json record each derived page's artifact URL and the inputs-digest last published to it, so the hook names the link and can say how far behind the published copy is?

Rule 14: a phrase he has to recall is a design defect. This session the URL was carried in the author's head and in the dispatch prompt, and the republish correctly reused it. Forget it once and publish mints a NEW artifact: the repo is in sync, --check says so, and the link already sent to readers serves an old manual permanently with nothing able to notice. --check sees the repo file only; the published copy is outside every gate in the house - Rule 4's gate that cannot see. Two published pages, so two chances.

**Recommendation:** One published_artifacts block in config/house.json keyed by output path, holding url and published_digest; manual.py and build_diagrams_page.py print the URL instead of the bare noun and compare published_digest to the computed one; --published updates it

**Checked:**

```
grep -rn 'claude.ai/artifact' --include=*.py --include=*.md --include=*.sh --include=*.json . -> no match outside runs/log.md. The two identical bare sentences are scripts/manual.py:1226 and scripts/build_diagrams_page.py:165. Stop hook repeats it twice more (.claude/hooks/session-stop.sh:67-71). python3 scripts/manual.py --check -> 'in sync' - a statement about docs/manual.html only, never about the artifact the reader opens.
```

**What unblocks this:** Whether 'republish' names a specific link the next time either page goes stale, and whether a published-but-not-republished page is detectable at all
