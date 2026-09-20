"""ttfwidth.py - text widths from a TrueType file's own tables, for plate_check.py; no font library is installable here."""
import struct
def metrics(path):
    d=open(path,'rb').read()
    n=struct.unpack('>H',d[4:6])[0]; tabs={}
    for i in range(n):
        o=12+16*i; tag=d[o:o+4].decode('latin1'); off,ln=struct.unpack('>II',d[o+8:o+16]); tabs[tag]=(off,ln)
    ho,_=tabs['head']; upem=struct.unpack('>H',d[ho+18:ho+20])[0]
    hho,_=tabs['hhea']; nhm=struct.unpack('>H',d[hho+34:hho+36])[0]
    hmo,_=tabs['hmtx']; adv=[struct.unpack('>H',d[hmo+4*i:hmo+4*i+2])[0] for i in range(nhm)]
    co,_=tabs['cmap']; ntab=struct.unpack('>H',d[co+2:co+4])[0]; sub=None
    for i in range(ntab):
        p=co+4+8*i; pid,eid,off=struct.unpack('>HHI',d[p:p+8])
        if (pid,eid) in ((3,1),(0,3),(3,10)): sub=co+off
    fmt=struct.unpack('>H',d[sub:sub+2])[0]; cmap={}
    if fmt==4:
        segX2=struct.unpack('>H',d[sub+6:sub+8])[0]; seg=segX2//2
        ends=[struct.unpack('>H',d[sub+14+2*i:sub+16+2*i])[0] for i in range(seg)]
        sso=sub+16+segX2
        starts=[struct.unpack('>H',d[sso+2*i:sso+2+2*i])[0] for i in range(seg)]
        deo=sso+segX2; deltas=[struct.unpack('>h',d[deo+2*i:deo+2+2*i])[0] for i in range(seg)]
        rngo=deo+segX2; rngs=[struct.unpack('>H',d[rngo+2*i:rngo+2+2*i])[0] for i in range(seg)]
        for i in range(seg):
            for c in range(starts[i], min(ends[i],0x2100)+1):
                if rngs[i]==0: g=(c+deltas[i])&0xFFFF
                else:
                    gi=rngo+2*i+rngs[i]+2*(c-starts[i])
                    if gi+2>len(d): continue
                    g=struct.unpack('>H',d[gi:gi+2])[0]
                    if g: g=(g+deltas[i])&0xFFFF
                if g: cmap[chr(c)]=g
    return upem, adv, cmap
def width(text,size,ls,upem,adv,cmap):
    t=0
    for ch in text:
        g=cmap.get(ch, cmap.get(' ',0)); a=adv[g] if g<len(adv) else adv[-1]
        t+=a/upem*size + ls*size
    return t
