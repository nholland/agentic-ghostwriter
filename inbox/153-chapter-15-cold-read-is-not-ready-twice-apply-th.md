---
id: 153
status: open
raised_by: gw-slopreader
chapter: 15
opened: 2026-10-24 05:44
---

# Chapter 15 cold read is NOT READY twice. Apply the four plain text fixes and the one distillation fix it proposes?

A first-time reader found 6 sentences that need a reread after two rounds (the gate allows two). I stopped rather than loop, because the second reader's fix for 'If it is...' contradicts the first reader's. The fixes: (1) 'The habit made sense' -> 'Answering back made sense'; (2) 'came slowly, from living it' -> 'through experience'; (3) 'If you have been, fix it. If you haven't...' -> 'If it is, fix it. If it isn't, let the remark go.'; (4) 'his advice... His point' -> 'Seneca's advice... Seneca's point'; (6) drop 'When the answer is no' from practice 3 in the distillation and the practice guide. Not proposed: changing the philostorgia line (an etymology claim beyond the record). Full report: runs/ch15/coldread-refined.md.

**Recommendation:** Apply all five; they change no argument and none touches your own lines.

**Checked:**

```
grep -n 'The habit made sense\|What changed for me\|If you have been\|Seneca.s angry man' scratchpad/conf6/prose.md -> L11 'The habit made sense, the way most habits do: you use what rewards.'; L13 'What changed for me came slowly, from living it.'; L23 'If you have been, fix it. If you haven't, let the remark go.'; L35 prose cites De Ira II.34; distillation L15 'When the answer is no, take over one chore that's usually hers, and do it gladly.'
```

**What unblocks this:** Whether /gw-edit applies these five fixes, after which the cold read must run once more before the chapter is called ready
