---
id: 087
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-21 13:04
applied_by: python3 -c "
import re,sys
def wp(p,i):
 t=open(p,encoding='utf-8').read()
 return [tuple(map(float,x.split(','))) for x in re.findall(r'<polyline points=\"([^\"]+)\"',t)[i].split()]
def ip(pts,y):
 for j in range(len(pts)-1):
  (x1,y1),(x2,y2)=pts[j],pts[j+1]
  if y1<=y<=y2 or y2<=y<=y1:
   return x1 if y2==y1 else x1+(y-y1)/(y2-y1)*(x2-x1)
 return None
def wa(l,r,y):
 xl,xr=ip(l,y),ip(r,y)
 return None if xl is None or xr is None else xr-xl
def void(p,y0,y1):
 l,r=wp(p,0),wp(p,1)
 return sum(wa(l,r,y+0.5) or 0 for y in range(y0,y1))
d,l='runs/parts/plate-1-steady-river.svg','books/the-stoic-husband/parts/plate-1-steady-river.svg'
vd,vl=void(d,190,405),void(l,190,640)
lw,rw=wp(d,0),wp(d,1)
s300,s400=wa(lw,rw,300),wa(lw,rw,400)
ratio=s300/s400
print('void: draft=%.1f landed=%.1f not_grown=%s'%(vd,vl,vd<=vl))
print('taper: span300=%.1f span400=%.1f ratio=%.2f converges=%s'%(s300,s400,ratio,ratio>=1.5))
sys.exit(0 if (vd<=vl and ratio>=1.5) else 1)"
---

# The Part I redraw's taper collapsed from an 11:1 converging cut to a 2:1 near-parallel slot, so below y~290 the draft canyon is wider than the landed one at every height even though the total void did not grow. Redraw keeping the landed taper?

**Correction, 2026-09-22 (gw-retro, re-verified by the Publisher independently against the raw SVG wall geometry, not just the raster scan).** The original claim below said the void grew 9%. That was measured over the band y=190-400, "above the waterline" - but the draft has a waterline at y=405 and the landed plate has none at all (its wave sits at y=650, below the drawing box floor at y=640), so the band fit one plate and not the other. Measured to each plate's own extent - draft to its waterline, landed to the box floor - the draft's empty white is 32764 against the landed plate's 39852: it **shrank 17.8%**, not grew. The lower canyon also isn't white in the draft: 9.09% ink inside the walls (the water pattern) against 0.00% in the landed plate, which is empty top to bottom. So "the river now fills the canyon" is true and measurable. The taper regression is real and unchanged by this correction - it is a separate claim from the void, and it is the one that should have been the headline. The heading and applied_by above have been corrected accordingly; the original numbers are preserved in Checked below for the record.

The desk's note and the Publisher's original report to the author both said the void grew. It didn't, on a fair comparison. What's real: reshaping the profile to fit water flattened the taper from about 11:1 converging to about 2:1 near-parallel, which is closer to "a gap opening between two sides" - the reading the redraw was commissioned to kill - than the converging cut it replaced.

**Recommendation:** Redraw: keep the landed taper above the waterline and widen only below it. Built and measured, not guessed - a ten-line edit to `halfwidth()` in `runs/parts/gen-plate-1-r2.py` (the generator both walls derive from) restores the taper to within a unit at every height while keeping the void below the landed plate's: variant span 135.7/110.4/98.7/84.4 against landed 136.8/110.5/99.2/84.4, `plate_check.py --part 1` all nine rows ok.

**Checked:**

```
Original (superseded) claim: band 190-400, draft void 32033.0, landed void 29444.5, +8.8%.

Corrected, each plate to its own extent: draft void (190->405) 32764.1, landed void (190->640) 39852.0, draft is 82.2% of landed (-17.8%). Ink inside canyon walls y405-640: draft 9.09%, landed 0.00%.

Taper, span at x=300 by height y=300/350/375/400 - landed 135.5/109.0/98.0/83.0 (converging, ratio ~1.6), draft 148.0/138.0/132.5/129.0 (near-parallel, ratio ~1.15). Threshold for "converges" set at ratio>=1.5.

Re-verified by the Publisher independently via geometric integral of the wall polylines (no rasteriser): draft 32117.1, landed 29572.5 on the same band - 0.3% from the raster figures above, confirming the arithmetic; the band was the error, not the number.
```

**What unblocks this:** Whether runs/parts/plate-1-steady-river.svg lands as drawn or goes back for another profile
