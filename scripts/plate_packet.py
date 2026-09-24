#!/usr/bin/env python3
"""Render the maintained plain-language plate brief into the current plates PDF.

Edit runs/design/plate-briefs.md, then run python3 scripts/plate_packet.py.
Each image precedes its intent, preserving an unprompted first reading.
The Markdown is maintained source, never overwritten by compilation.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re

import chapter_pdf_local as renderer
import compile as assembly
import resolve_book

ROOT = Path(__file__).resolve().parents[1]
BRIEF = ROOT/'runs/design/plate-briefs.md'
OUT = ROOT/'output/compiled'
FIELDS = ('Intent', 'Visual explanation', 'Validation question', 'Source')


def read_briefs(path=BRIEF):
    text = path.read_text()
    result = {}
    for match in re.finditer(r'^## (ch\d{2}|part-[IVX]+) \| ([^\n]+)\n(.*?)(?=^## |\Z)', text, re.M|re.S):
        key, title, body = match.groups()
        if key in result:
            raise ValueError(f'Duplicate plate brief: {key}')
        fields = {}
        for label in FIELDS:
            m = re.search(r'^\*\*'+re.escape(label)+r':\*\*\s*(.+?)(?=\n\s*\*\*|\Z)', body, re.M|re.S)
            if not m or not m.group(1).strip():
                raise ValueError(f'{key}: missing {label}')
            fields[label] = ' '.join(m.group(1).split())
        result[key] = (title, fields)
    if not result:
        raise ValueError('No plate briefs found')
    return result


def build_packet(book, hi=None):
    briefs = read_briefs()
    hi = hi or max(int(k[2:]) for k in briefs if k.startswith('ch'))
    entries = []
    arcs = assembly.parts((book/'03-outline.md').read_text())
    for n in range(1, hi+1):
        svg, approved = assembly.chapter_plate(str(book), n)
        entries.append((f'ch{n:02}', f'Chapter {n}', svg, approved))
        for numeral, _, first, last, _, closing in arcs:
            if first <= n and min(last, hi) == n:
                svg, approved = assembly.part_plate(str(book), numeral, closing)
                entries.append((f'part-{numeral}', f'Part {numeral}', svg, approved))
    OUT.mkdir(parents=True, exist_ok=True)
    assets = OUT/'assets';assets.mkdir(exist_ok=True)
    body, sources, metadata = [], {}, []
    for key, label, svg, approved in entries:
        if not svg or key not in briefs:
            raise ValueError(f'Missing SVG or brief for {key}')
        title, fields = briefs[key]
        png = OUT/f'plate-{key}.png'
        renderer.svg_to_png(svg, str(png))
        body.append(f'<figure class="plate"><img src="{png.name}" alt="{label}">'
                    f'<figcaption>{label}. Before turning the page: what do you think this image is saying about marriage?</figcaption></figure>')
        note = f'# {label}: {title}\n\n'
        for field in FIELDS[:-1]:
            note += f'**{field}.**\n\n{fields[field]}\n\n'
        body.append('<section>'+renderer.format_headings(renderer.md_to_html(note))+'</section>')
        sources[str(Path(svg).relative_to(ROOT))] = hashlib.sha256(Path(svg).read_bytes()).hexdigest()
        metadata.append({'id':key,'title':title,'approved_identical_copy':approved})
    pdf = OUT/'plates.pdf'
    html = renderer.render_html(''.join(body),str(pdf),'Plates: images, intended meanings, and feedback questions')
    Path(html).replace(assets/'plates.html')
    for key, *_ in entries:
        (OUT/f'plate-{key}.png').replace(assets/f'plate-{key}.png')
    sources[str(BRIEF.relative_to(ROOT))] = hashlib.sha256(BRIEF.read_bytes()).hexdigest()
    manifest = OUT/'manifest.json'
    data = json.loads(manifest.read_text()) if manifest.exists() else {}
    data['plate_packet'] = {'built':datetime.now().astimezone().isoformat(), 'source':str(BRIEF.relative_to(ROOT)), 'entries':metadata,'pages_expected':len(entries)*2,'source_sha256':sources}
    manifest.write_text(json.dumps(data,indent=2)+'\n')
    print(f'{pdf}: {len(entries)} plates, each followed by its maintained explanation')
    return data['plate_packet']


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--to', type=int)
    args=ap.parse_args()
    root, _, _=resolve_book.resolve(resolve_book.load_config())
    if not root:
        raise RuntimeError('No active book')
    info=resolve_book.inspect(root,require_okf=True)['info']
    build_packet(Path(root)/info['bookRootRelative'],args.to)

if __name__=='__main__':
    main()
