---
id: 091
status: open
raised_by: gw-retro
chapter: 0
opened: 2026-09-22 22:53
applied_by: python3 -c "
import re,sys,os,tempfile
sys.path.insert(0,'scripts')
import plate_check
LANDED='books/the-stoic-husband/parts/plate-1-steady-river.svg'
DRAFT='runs/parts/plate-1-steady-river.svg'
OAK='books/the-stoic-husband/parts/plate-2-sturdy-oak.svg'
def make_gradual_flare():
 base=open(LANDED,encoding='utf-8').read()
 P=re.findall(r'<polyline points=\"([^\"]+)\"',base)
 g=lambda s:[tuple(map(float,x.split(','))) for x in s.split()]
 def widen(pts,sign):
  return [(x+sign*max(0,i-9),y) for i,(x,y) in enumerate(pts)]
 f=lambda pts:' '.join('%.1f,%.1f'%q for q in pts)
 mut=base.replace('points=\"%s\"'%P[0],'points=\"%s\"'%f(widen(g(P[0]),-1)),1)
 mut=mut.replace('points=\"%s\"'%P[1],'points=\"%s\"'%f(widen(g(P[1]),1)),1)
 t=tempfile.NamedTemporaryFile('w',suffix='.svg',delete=False,encoding='utf-8');t.write(mut);t.close()
 return t.name
grad=make_gradual_flare()
r=lambda p,part:{n:s for s,n,d in plate_check.rows(p,part=part,book_root='books/the-stoic-husband',runs_root='runs')}
ls,ds,gs,os_=r(LANDED,1).get('canyon'),r(DRAFT,1).get('canyon'),r(grad,1).get('canyon'),r(OAK,2).get('canyon')
os.remove(grad)
print({'landed':ls,'draft':ds,'gradual':gs,'oak':os_})
sys.exit(0 if (ls=='ok' and ds not in (None,'ok') and gs not in (None,'ok') and os_!='ok') else 1)"
---

# #090's own proof only requires the canyon row to fail the sharp 400-unit flare, so a monotonicity-based implementation ('a canyon may not widen as it descends') would satisfy #090 while calling the actual defective draft ok: the draft scores zero widening steps (it narrows at every step, just too gently - the defect is taper flattening, not opening), while the landed plate it regressed from has one legitimate 2.6-unit widening step from its hand-drawn wobble. Any monotonicity bound ranks the defect cleaner than the good plate. #090 also never exercises plates 2-5, where plate-2 (the Oak) has zero polylines at all. Amend #090's proof to require failing the current draft and a gradual flare, and to not report ok on the Oak?

If #090 is built to its proof exactly as filed, it closes green while runs/parts/plate-1-steady-river.svg - the plate the whole four-retro chain is about - passes the new check, and plate-2-sturdy-oak.svg (no walls at all) gets a vacuous ok. Rule 4: a gate that cannot see is not a gate.

**Recommendation:** Before building #090, add to its own proof: the row must FAIL on the current draft, must FAIL on a gradual flare (widening 1 unit per wall per vertex below the waterline, not just the sharp 400-unit one), and must NOT report ok on plate-2-sturdy-oak.svg. Register all as plate_check_cases().

**Checked:**

```
Publisher independently verified the monotonicity blind spot: wall-vertex step widths, landed max legitimate widening step = 2.60 units (natural hand-wobble), draft = 0.0 (every step narrows, none widen - it is monotonic, just flattened). A gradual flare (+1 unit/vertex/wall from the waterline vertex, index 9 of 20) reaches bottom width 40.2 against the landed plate's 20.2 while still passing any per-step monotonicity bound tuned to admit the 2.6-unit legitimate wobble. Polyline counts confirmed: plate-1 landed 3 (2 walls + 1 wave), plate-2 landed 0, so a canyon row that runs unconditionally under --part would need explicit handling for plates with no walls. This item's own applied_by verified red today for the honest structural reason: {'landed': None, 'draft': None, 'gradual': None, 'oak': None}, exit 1 - the row does not exist yet.
```

**What unblocks this:** Whether the canyon row is specified by the defect it exists to catch, or by the single easiest mutant anyone happened to construct
