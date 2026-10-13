from pathlib import Path
import argparse,shutil,sys,os,re
from validate import ROOT,validate
ap=argparse.ArgumentParser(description='Instala o mod no diretório de dados do CK3.');ap.add_argument('--user-dir',type=Path,help='Diretório de dados do CK3 (não a pasta de instalação do jogo).');args=ap.parse_args()
validate()
if args.user_dir:user=args.user_dir
elif sys.platform.startswith('linux'):user=Path(os.environ.get('XDG_DATA_HOME',str(Path.home()/'.local/share')))/'Paradox Interactive/Crusader Kings III'
else:user=Path.home()/'Documents/Paradox Interactive/Crusader Kings III'
mods=user/'mod';target=mods/'ck3_ptbr_comunidade';marker=target/'.community-generated'
if target.exists() and not marker.exists():raise SystemExit('Destino já existe e não pertence ao instalador. Nenhum arquivo alterado.')
old=(target/'descriptor.mod').read_text(encoding='utf-8') if (target/'descriptor.mod').exists() else ''
workshop_id=re.search(r'^remote_file_id\s*=\s*"(\d+)"',old,re.M)
shutil.copytree(ROOT/'mod',target,dirs_exist_ok=True);marker.touch()
if workshop_id:
    with (target/'descriptor.mod').open('a',encoding='utf-8') as f:f.write(f'remote_file_id="{workshop_id[1]}"\n')
descriptor=(target/'descriptor.mod').read_text(encoding='utf-8')
(mods/'ck3_ptbr_comunidade.mod').write_text(descriptor+f'path="{target.as_posix()}"\n',encoding='utf-8')
print('Instalado:',target)
print('Abra o launcher, ative o mod e selecione Español como idioma do jogo.')
print('Evite ativar outras traduções para o mesmo idioma simultaneamente.')
