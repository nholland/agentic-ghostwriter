---
id: 084
status: open
raised_by: gw-retro
chapter: 4
opened: 2026-09-21 12:52
applied_by: python3 -c "
import sys; sys.path.insert(0,'scripts'); import plate_check as pc
s=open('runs/ch04/plate.svg',encoding='utf-8').read()
assert 's full of holes.' in s, 'row three caption unchanged'
r={n:l for l,n,m in pc.rows('runs/ch04/plate.svg',chapter=4,runs_root='runs')}
assert r['grounded']=='ok' and r['captions']=='ok', r
"
---

# Ch4 row three's caption 'The hole remains.' is singular and about persistence under a picture of ten holes claiming accumulation. The chapter's own sentence 'It's full of holes.' (refined.md:73) fixes it, passes grounded, and stays at the caption cap - unlike the Panel's 'The holes remain. And they keep coming.', which fails grounded. Change row three's caption to the chapter's sentence?

The plate argues two different points in one row, and the only option put to you needed an ungrounded Author addition when your own words already solved it. Publisher verified: 'The hole remains.' grounded=True, "It's full of holes." grounded=True, the Panel phrase grounded=False.

**Recommendation:** Change it to "It's full of holes." - it is your sentence, it needs no addition, and it is the beat the picture is already making

**Checked:**

```
CURRENT 'The hole remains.' -> ALL OK / PROPOSED "It's full of holes." -> ALL OK / PANEL 'The holes remain. And they keep coming.' -> NOT OK: ['grounded']. Source at books/the-stoic-husband/chapters/ch04/refined.md line 73.
```

**What unblocks this:** Whether row three's caption matches what row three draws
