import sys, os, re
# Not a missing external package: ttfwidth.py sits right here. The prior line
# hardcoded a scratchpad path from one session's container
# ('/tmp/claude-0/...'), which only worked by accident when that exact path
# happened to hold a stray copy. Import from this file's own directory instead.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ttfwidth import metrics, width
# Measure against the WIDEST plausible serif fallback, not the narrowest.
# The CSS says "Georgia,serif"; where Georgia is absent the generic serif is
# commonly DejaVu Serif, which runs ~40-50% wider than Liberation for lowercase.
# That gap is what put two glosses on top of each other on the Ch1 plate.
D='/usr/share/fonts/truetype/dejavu/DejaVuSerif%s.ttf'
FONTS={'reg':metrics(D%''),'ita':metrics(D%''),'bold':metrics(D%'-Bold')}
GEORGIA_FACTOR=1.0
CLEARANCE=10.0   # px; touching is a defect, not a pass

def boxes(path):
    s=open(path).read()
    cls={}
    for m in re.finditer(r'\.(\w+)\{([^}]*)\}', s):
        b=m.group(2)
        sz=re.search(r'(\d+(?:\.\d+)?)px',b); ls=re.search(r'letter-spacing:\.?(\d+)em',b)
        ta=re.search(r'text-anchor:(\w+)',b)
        cls[m.group(1)]=(float(sz.group(1)) if sz else 12,
                         float('.'+ls.group(1)) if ls else 0,
                         ta.group(1) if ta else 'start',
                         'italic' in b, ('600' in b or '700' in b),
                         ta is not None)
    out=[]
    for m in re.finditer(r'<text class="(\w+)"([^>]*)>([^<]*)</text>', s):
        c,attrs,t=m.group(1),m.group(2),m.group(3)
        size,ls,anch,it,bd,class_sets_anchor=cls.get(c,(12,0,'start',False,False,False))
        # SVG precedence: inline style > stylesheet class > presentation
        # attribute. The Ch12 plate set text-anchor="start" on an element whose
        # class says middle; the browser centred it off the left edge while
        # this checker, reading the attribute as final, reported clean.
        ist=re.search(r'style="[^"]*text-anchor:\s*(\w+)',attrs)
        ia=re.search(r'text-anchor="(\w+)"',attrs)
        if ist: anch=ist.group(1)
        elif ia and not class_sets_anchor: anch=ia.group(1)
        isz=re.search(r'style="[^"]*font-size:\s*([\d.]+)px',attrs)
        if isz: size=float(isz.group(1))
        x=float(re.search(r'x="([\d.]+)"',attrs).group(1))
        y=float(re.search(r'y="([\d.]+)"',attrs).group(1))
        fo=FONTS['ita'] if it else (FONTS['bold'] if bd else FONTS['reg'])
        w=width(t,size,ls,*fo)*GEORGIA_FACTOR
        l = x-w/2 if anch=='middle' else (x-w if anch=='end' else x)
        out.append(dict(cls=c,text=t,x=x,y=y,l=l,r=l+w,size=size))
    return out, s

def check(path, left=44, right=None):
    bx, s = boxes(path)
    vb=[float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    # Derive the right margin from THIS file's canvas. It was hardcoded at 596,
    # correct for the 640-wide landscape plates and meaningless for a 500-wide
    # portrait one, where the bound sat 96px off the artboard and no right-edge
    # overflow could ever be seen. Caught by the Designer reading the source
    # rather than by the checker itself.
    if right is None:
        right = vb[2] - left
    issues=[]
    for b in bx:
        if b['l']<left-0.5 or b['r']>right+0.5:
            issues.append(f"MARGIN  y={b['y']:>5} '{b['text'][:34]}' {b['l']:.0f}..{b['r']:.0f}")
    for i,a in enumerate(bx):
        for c in bx[i+1:]:
            if abs(a['y']-c['y'])<max(a['size'],c['size'])*0.9:      # same visual line
                if a['l'] < c['r']+CLEARANCE and c['l'] < a['r']+CLEARANCE:
                    ov=min(a['r'],c['r'])-max(a['l'],c['l'])  # negative = gap smaller than CLEARANCE
                    issues.append(f"COLLIDE y={a['y']:>5} '{a['text'][:26]}' [{a['l']:.0f}..{a['r']:.0f}] "
                                  f"x '{c['text'][:26]}' [{c['l']:.0f}..{c['r']:.0f}]  overlap {ov:.0f}px")
    # A plate with no classed <text> (the Part closing plates) has nothing to
    # measure; that is not a defect, so do not crash on the empty set.
    lowest=max((b['y'] for b in bx), default=0)
    if lowest > vb[3]-6: issues.append(f"VIEWBOX lowest baseline {lowest} vs height {vb[3]}")
    return issues

if __name__=='__main__':
    for p in sys.argv[1:]:
        iss=check(p)
        print(f"\n{p}")
        print("  " + ("\n  ".join(iss) if iss else "clean"))
