---
id: 087
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 13:04
applied_by: python3 -c "
import sys;sys.path.insert(0,\"scripts\")
from plate_check import png_rows
from chapter_pdf_local import svg_to_png
def v(p):
 t=\"/tmp/v%d.png\"%abs(hash(p));svg_to_png(p,t,scale=2)
 w,h,b,r=png_rows(t);s=w/600.0
 d=lambda x,y:sum(r[y][x*b:x*b+3])/3<128
 a=0.0
 for Y in range(190,401):
  y=int(Y*s);x=int(300*s)
  if d(x,y): continue
  l=x
  while l>0 and not d(l,y):l-=1
  q=x
  while q<w-1 and not d(q,y):q+=1
  a+=(q-l)/s
 return a
n=v(\"runs/parts/plate-1-steady-river.svg\");o=v(\"books/the-stoic-husband/parts/plate-1-steady-river.svg\")
print(\"draft %.1f landed %.1f\"%(n,o));sys.exit(0 if n<=o else 1)"
---

# The Part I redraw was meant to remove the empty wedge, but measured, the open white above the waterline is 32033 sq units against the landed plate's 29444 - 9% larger, not smaller. Reshaping the profile to fit water flattened the taper from about 11:1 to about 2:1, so below y=290 the draft canyon is wider than the landed one at every height. Redraw keeping the landed taper, or accept the wider slot?

The desk's note and the Publisher's report to the author both state the river now fills the canyon rather than leaving an empty wedge. The water is fine; the void above it is the dominant white shape on the page and it grew. A near-parallel slot between two striped blocks is closer to 'a gap opening between two sides' - the reading the redraw was commissioned to kill - than the converging cut it replaced. The Publisher re-measured independently and reproduced the numbers exactly.

**Recommendation:** Redraw: keep the landed taper above the waterline and widen only below it, so the void shrinks rather than trading height for width

**Checked:**

```
Publisher's independent run: draft void 32033.0, landed void 29444.5, +8.8%. Span at x=300 by height y=300/350/375/400 - landed 135.5/109.0/98.0/83.0 (converging), draft 148.0/138.0/132.5/129.0 (near-parallel).
```

**What unblocks this:** Whether runs/parts/plate-1-steady-river.svg lands as drawn or goes back for another profile
