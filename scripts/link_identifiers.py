#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REGISTER=ROOT/'docs/implementation-guide/reference/identifier-register.md'
SCAN_ROOTS=[ROOT/'docs',ROOT/'proof-of-liveness-requirements.md',ROOT/'README.md']
ANCHOR_RE=re.compile(r'<a id="([a-z0-9-]+)"></a>`([^`]+)`')

def known_ids():
    return {ident for _,ident in ANCHOR_RE.findall(REGISTER.read_text(encoding='utf-8'))}

def markdown_files():
    for item in SCAN_ROOTS:
        if item.is_file(): yield item
        elif item.exists(): yield from sorted(item.rglob('*.md'))

def rel_target(path,ident):
    return os.path.relpath(REGISTER,path.parent).replace(os.sep,'/')+'#'+ident.lower()

def transform(path,ids):
    text=path.read_text(encoding='utf-8')
    if path.resolve()==REGISTER.resolve(): return text
    token_alt='|'.join(sorted(map(re.escape,ids),key=len,reverse=True))
    inline_re=re.compile(rf'(?<!\[)`({token_alt})`')
    bare_re=re.compile(rf'(?<![A-Z0-9_`\[/#-])({token_alt})(?![A-Z0-9_`\]-])')
    out=[]; fenced=False; front=False
    for i,line in enumerate(text.splitlines(keepends=True)):
        stripped=line.strip()
        if i==0 and stripped=='---': front=True; out.append(line); continue
        if front:
            out.append(line)
            if stripped=='---': front=False
            continue
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fenced=not fenced; out.append(line); continue
        if fenced or line.lstrip().startswith('#'):
            out.append(line); continue
        line=inline_re.sub(lambda m:f'[`{m.group(1)}`]({rel_target(path,m.group(1))})',line)
        line=bare_re.sub(lambda m:f'[`{m.group(1)}`]({rel_target(path,m.group(1))})',line)
        out.append(line)
    return ''.join(out)

def main():
    ap=argparse.ArgumentParser(); g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',action='store_true'); g.add_argument('--check',action='store_true'); args=ap.parse_args()
    ids=known_ids(); changed=[]
    for path in markdown_files():
        old=path.read_text(encoding='utf-8'); new=transform(path,ids)
        if new!=old:
            changed.append(path.relative_to(ROOT))
            if args.write: path.write_text(new,encoding='utf-8')
    if args.check and changed:
        print('Unlinked stable identifiers found in:',file=sys.stderr)
        for p in changed: print('  -',p,file=sys.stderr)
        return 1
    print(f"identifier links {'updated' if args.write else 'verified'}; files changed={len(changed)}; registered IDs={len(ids)}")
    return 0
if __name__=='__main__': raise SystemExit(main())
