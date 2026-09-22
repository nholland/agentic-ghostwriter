---
id: 090
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-22 22:44
applied_by: python3 -c "
import re,sys,os,tempfile;sys.path.insert(0,'scripts')
import plate_check
L='books/the-stoic-husband/parts/plate-1-steady-river.svg'
base=open(L,encoding='utf-8').read()
P=re.findall(r'<polyline points=\"([^\"]+)\"',base)
g=lambda s:[tuple(map(float,x.split(','))) for x in s.split()]
def flare(pts,sign):
 return [(x,y) if y<=405 else (x+sign*(y-405)/235.0*((510-x) if sign>0 else (x-90))*.95,y) for x,y in pts]
f=lambda p:' '.join('%.1f,%.1f'%q for q in p)
mut=base.replace('points=\"%s\"'%P[0],'points=\"%s\"'%f(flare(g(P[0]),-1)),1)
mut=mut.replace('points=\"%s\"'%P[1],'points=\"%s\"'%f(flare(g(P[1]),1)),1)
t=tempfile.NamedTemporaryFile('w',suffix='.svg',delete=False,encoding='utf-8');t.write(mut);t.close()
r=lambda p:{n:s for s,n,d in plate_check.rows(p,part=1,book_root='books/the-stoic-husband',runs_root='runs')}
a,b=r(L),r(t.name);os.remove(t.name)
print('landed:',a.get('canyon'),' flared-to-400-units:',b.get('canyon'))
sys.exit(0 if (a.get('canyon')=='ok' and b.get('canyon') not in (None,'ok')) else 1)"
---

# #087's corrected proof samples void and taper only above the waterline (y=190-405), so a redraw that follows its own recommendation and widens below the waterline closes it green even if the canyon flares wide open there. Verified: a plate whose canyon flares to 400 units at y=640 (landed: 20.2) passes #087's proof at exit 0. Move the measurement into plate_check as a canyon row under --part, with the over-widened plate as its fixture, and retire the one-shot applied_by?

Sixth instance of the FINDINGS.md shape (a check passing the defect it exists to catch), introduced in the same commit that removed the fifth (#089's grep). Three bespoke measurement scripts have now been written for this one plate - a raster scan, a geometric integral, a wall-polyline integral - and none landed anywhere runnable; plate_check reports nine rows on this file and none can see a canyon. Separately worth recording in the row's design: the 'void shrank 17.8%' conclusion itself rests on an unstated judgment - treating the draft's watered lower canyon as filled rather than as mostly-white pixels. That judgment is defensible (the water strokes measure 9.33% ink density against the rock stripes' 4.65% - denser than the rock it runs between, not emptier) but #087 never states it, and weighting the region by raw white-pixel fraction instead flips the sign to +41.2%. A canyon row should make this explicit (ink-density threshold, not white-pixel area) rather than leave the sign resting on an unstated choice.

**Recommendation:** Add a canyon row to plate_check under --part: derive the waterline from the topmost non-wall polyline rather than hardcoding 405, assert the two widest polylines are the walls rather than taking them by index, measure void by ink density (not raw white-pixel area) so the filled-vs-textured judgment is explicit, and sample taper across the full wall range including below the waterline. Register the over-widened plate in plate_check_cases().

**Checked:**

```
Publisher reproduced independently: current #087 proof against a half-fix that follows its own recommendation (landed taper kept above y=405, widened below) - void: draft=29988.8 landed=39852.0 not_grown=True; taper: span300=136.8 span400=84.4 ratio=1.62 converges=True; exit 0, closes green. Span at y=640 in that half-fix is 400.0 against the landed plate's 20.2, walls running to the drawing-box margins - the 'gap opening between two sides' the redraw was commissioned to kill. plate_check --part 1 on the landed plate prints nine rows (charset, geometry, anchor-attr, em-dash, digits, canvas, captions, alignment, ink) and no canyon row exists. Water ink density 9.33% vs rock field 4.65%, measured across the draft's lower canyon.
```

**What unblocks this:** Whether the Part I redraw can be verified by anything except a hand measurement rewritten from scratch each time, and whether the sign of 'did the void grow or shrink' is a stated rule or an implicit choice
