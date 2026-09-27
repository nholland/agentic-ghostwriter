---
id: 084
status: resolved
raised_by: gw-retro
chapter: 4
opened: 2026-09-21 12:52
applied_by: python3 -c 'import sys;sys.path.insert(0,'"'"'scripts'"'"');import plate_check as p;from pathlib import Path;s=Path('"'"'runs/ch04/plate.svg'"'"').read_text();assert chr(73)+chr(116)+chr(39)+'"'"'s full of holes.'"'"' in s;r={n:v for v,n,d in p.rows('"'"'runs/ch04/plate.svg'"'"',chapter=4,runs_root='"'"'runs'"'"',check_preview=False)};assert r['"'"'grounded'"'"']=='"'"'ok'"'"' and r['"'"'captions'"'"']=='"'"'ok'"'"' and r['"'"'geometry'"'"']=='"'"'ok'"'"',r'
resolved: 2026-09-26 18:50
---

# Ch4 row three's caption 'The hole remains.' is singular and about persistence under a picture of ten holes claiming accumulation. The chapter's own sentence 'It's full of holes.' (refined.md:73) fixes it, passes grounded, and stays at the caption cap - unlike the Panel's 'The holes remain. And they keep coming.', which fails grounded. Change row three's caption to the chapter's sentence?

The plate argues two different points in one row, and the only option put to you needed an ungrounded Author addition when your own words already solved it. Publisher verified: 'The hole remains.' grounded=True, "It's full of holes." grounded=True, the Panel phrase grounded=False.

**Recommendation:** Change it to "It's full of holes." - it is your sentence, it needs no addition, and it is the beat the picture is already making

**Checked:**

```
CURRENT 'The hole remains.' -> ALL OK / PROPOSED "It's full of holes." -> ALL OK / PANEL 'The holes remain. And they keep coming.' -> NOT OK: ['grounded']. Source at books/the-stoic-husband/chapters/ch04/refined.md line 73.
```

**What unblocks this:** Whether row three's caption matches what row three draws

**Resolution (2026-09-26 18:50):** Author approved the exact caption: It is now “It’s full of holes.” in runs/ch04/plate.svg. Refreshed the PNG preview, visually inspected it, and passed every plate_check row including ink and raster-current. No other plate wording changed.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 -c "` exits 0.

**Resolution (2026-09-26 18:51):** Replaced the truncated historical multiline proof with a runnable caption, grounding, captions and geometry check. Full rendered checks and visual inspection also passed for this revision.

**Not applied yet.** This ruling lands outside this repo. It closes when `python3 -c 'import sys;sys.path.insert(0,'"'"'scripts'"'"');import plate_check as p;from pathlib import Path;s=Path('"'"'runs/ch04/plate.svg'"'"').read_text();assert chr(73)+chr(116)+chr(39)+'"'"'s full of holes.'"'"' in s;r={n:v for v,n,d in p.rows('"'"'runs/ch04/plate.svg'"'"',chapter=4,runs_root='"'"'runs'"'"',check_preview=False)};assert r['"'"'grounded'"'"']=='"'"'ok'"'"' and r['"'"'captions'"'"']=='"'"'ok'"'"' and r['"'"'geometry'"'"']=='"'"'ok'"'"',r'` exits 0.

**Applied, confirmed 2026-09-26 18:51:** `python3 -c 'import sys;sys.path.insert(0,'"'"'scripts'"'"');import plate_check as p;from pathlib import Path;s=Path('"'"'runs/ch04/plate.svg'"'"').read_text();assert chr(73)+chr(116)+chr(39)+'"'"'s full of holes.'"'"' in s;r={n:v for v,n,d in p.rows('"'"'runs/ch04/plate.svg'"'"',chapter=4,runs_root='"'"'runs'"'"',check_preview=False)};assert r['"'"'grounded'"'"']=='"'"'ok'"'"' and r['"'"'captions'"'"']=='"'"'ok'"'"' and r['"'"'geometry'"'"']=='"'"'ok'"'"',r'` now exits 0.
