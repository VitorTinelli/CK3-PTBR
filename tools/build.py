from pathlib import Path
import zipfile
from validate import ROOT,validate
validate()
out=ROOT/'dist';out.mkdir(exist_ok=True)
with zipfile.ZipFile(out/'ck3-ptbr-completo.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted((ROOT/'mod').rglob('*')):
        if p.is_file():z.write(p,Path('ck3_ptbr_comunidade')/p.relative_to(ROOT/'mod'))
    z.writestr('ck3_ptbr_comunidade.mod',(ROOT/'mod/descriptor.mod').read_text()+'path="mod/ck3_ptbr_comunidade"\n')
    for name in ['README.md','CONTRIBUTING.md','docs/INSTALAR.md','docs/TESTAR.md']:z.write(ROOT/name,name)
print(out/'ck3-ptbr-completo.zip')
