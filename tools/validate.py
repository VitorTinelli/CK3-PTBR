"""Validate localization syntax, uniqueness and reference key coverage."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
ENTRY=re.compile(r'^\s*([^\s:#]+):\d*\s*"((?:[^"\\]|\\.)*)"\s*$')
def validate():
    keys=set();errors=[];files=list((ROOT/'mod/localization').rglob('*.yml'))
    for p in files:
        raw=p.read_bytes()
        if not raw.startswith(b'\xef\xbb\xbf'):errors.append(f'{p.relative_to(ROOT)}: falta BOM UTF-8')
        try:lines=raw.decode('utf-8-sig').splitlines()
        except UnicodeDecodeError:errors.append(f'{p}: UTF-8 inválido');continue
        if not lines or lines[0].strip()!='l_spanish:':errors.append(f'{p}: cabeçalho incorreto')
        for n,line in enumerate(lines[1:],2):
            if not line.strip() or line.lstrip().startswith('#'):continue
            m=ENTRY.fullmatch(line)
            if not m:errors.append(f'{p.relative_to(ROOT)}:{n}: sintaxe inválida');continue
            if m[1] in keys:errors.append(f'{p.relative_to(ROOT)}:{n}: chave duplicada {m[1]}')
            keys.add(m[1])
    required=set((ROOT/'qa/required-keys.txt').read_text().splitlines())
    for k in sorted(required-keys):errors.append('Chave obrigatória ausente: '+k)
    descriptor=(ROOT/'mod/descriptor.mod').read_text()
    if 'remote_file_id' in descriptor:errors.append('Não versionar remote_file_id: a publicação deve usar o item próprio.')
    print(f'{len(files)} arquivos; {len(keys)} chaves; {len(required-keys)} ausentes; {len(errors)} erros.')
    for e in errors[:40]:print(e)
    if errors:raise SystemExit(1)
    return keys
if __name__=='__main__':validate()
