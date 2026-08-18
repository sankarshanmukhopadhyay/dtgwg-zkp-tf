#!/usr/bin/env python3
"""Validate that stable semantic identifiers resolve through the master register."""
from __future__ import annotations
import re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'docs/implementation-guide/reference/identifier-register.md'
text=REG.read_text(encoding='utf-8')
registered=set(re.findall(r'<a id="[a-z0-9-]+"></a>`([^`]+)`', text))
# Semantic families centrally registered. Specialised artefact families CT-*, D-*, AB-*, DB-* remain elsewhere.
pattern=re.compile(r'\b(?:AP-\d{2}|PR-[A-Z]{3}|ADV-[A-Z]{1,2}|CL-\d|UC-\d{3}|THR-\d{3}|HRM-[A-Z]{3}|CTL-[A-Z]{3}|ZGR-\d{2}|ZAT-\d{2}|IG-\d{3}|SEC-\d{3}|TCR-\d{3}|ZKP-(?:LINK|TASK|CER)-\d{2}|ADR-\d{3})\b')
missing={}
for p in list((ROOT/'docs').rglob('*.md'))+[ROOT/'proof-of-liveness-requirements.md',ROOT/'README.md']:
    if p==REG: continue
    for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        for ident in pattern.findall(line):
            if ident not in registered:
                missing.setdefault(ident,[]).append(f'{p.relative_to(ROOT)}:{n}')
if missing:
    print('Identifiers used but absent from master register:',file=sys.stderr)
    for ident,locs in sorted(missing.items()):
        print(f'  {ident}: {", ".join(locs[:5])}',file=sys.stderr)
    raise SystemExit(1)
anchors=re.findall(r'<a id="([a-z0-9-]+)"></a>`([^`]+)`', text)
for anchor,ident in anchors:
    if anchor != ident.lower():
        print(f'Anchor mismatch: {ident} -> {anchor}',file=sys.stderr); raise SystemExit(1)
print(f'identifier register valid: {len(registered)} semantic IDs')
