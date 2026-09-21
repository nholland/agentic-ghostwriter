---
id: 088
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 13:05
applied_by: python3 -c "
import subprocess,re,sys,glob,os
before=set(glob.glob(\"runs/manuscript/*\"))
o=subprocess.run([\"python3\",\"scripts/compile.py\",\"--from\",\"1\",\"--to\",\"4\",\"--plates\",\"--no-pdf\"],capture_output=True,text=True).stdout
for f in set(glob.glob(\"runs/manuscript/*\"))-before: os.remove(f)
lines=[l for l in o.splitlines() if \".svg\" in l]
ok=[l for l in lines if re.search(r\"\\b(ink|geometry|plate_check|checked)\\b\",l)]
print(len(ok),\"of\",len(lines),\"embedded-plate lines carry a check verdict\")
sys.exit(0 if lines and len(ok)==len(lines) else 1)"
---

# plate_check only ever runs on a source SVG a human names. Nothing runs it on the file compile.py actually selected, which is why a clipPath worry could be raised and reassured in the same paragraph without either being tested. Should compile.py --plates run plate_check on each plate it embeds and report the verdict on that plate's line?

compile.py:part_plate() prefers the landed book file, so a draft under review is unreachable by the compile path and the desk's 'chapter_pdf.py renders it correctly here' was never run against the draft at all. compile.py already builds plates.append((label, svg, landed)) and prints that list - it knows the filename and checks nothing. Same gap as open #062 at land.py, so one ruling could close both.

**Recommendation:** compile.py runs plate_check on each selected plate and prints its worst row on that plate's line; a FAIL is reported, never fatal, matching Rule 4

**Checked:**

```
python3 scripts/compile.py --from 1 --to 4 --plates --no-pdf prints the landed plate path, not the draft, and 0 of its embedded-plate lines carry a check verdict. A clip-stripped Oak gives [FAIL] ink left=9832 right=10681 exit 1, so the guard exists and has no caller.
```

**What unblocks this:** Whether a plate that fails plate_check can reach a reader PDF unnoticed, and whether #062 and this close together
