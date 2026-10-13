"""Shared packaging and local installation for official and test editions."""
import argparse
import os
from pathlib import Path
import re
import shutil
import sys
import sqlite3
import time
import zipfile
from validate import ROOT, validate


def main(test=False):
    parser = argparse.ArgumentParser(description='Gera e instala a edição de teste.' if test else 'Gera a edição oficial para publicação manual na Steam.')
    parser.add_argument('--user-dir', type=Path, help='Diretório de dados do CK3.')
    parser.add_argument('--no-install', action='store_true', help='Somente gera os arquivos em dist.')
    args = parser.parse_args()
    validate()
    ident = 'ck3_ptbr_teste' if test else 'ck3_ptbr_comunidade'
    output = ROOT / 'dist' / ('teste' if test else 'steam')
    source = ROOT / 'mod'
    descriptor = (source / 'descriptor.mod').read_text(encoding='utf-8')
    if test:
        descriptor = re.sub(r'^name=.*$', 'name="[TESTE LOCAL] CK3 PT-BR 1.20+ (By god alone)"', descriptor, flags=re.M)
    output.mkdir(parents=True, exist_ok=True)
    package = output / ident
    if package.exists():
        shutil.rmtree(package)
    shutil.copytree(source, package)
    (package / 'descriptor.mod').write_text(descriptor, encoding='utf-8')
    (output / (ident + '.mod')).write_text(descriptor + f'path="mod/{ident}"\n', encoding='utf-8')
    archive = output / (ident + '.zip')
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for file in sorted(package.rglob('*')):
            if file.is_file():
                z.write(file, Path(ident) / file.relative_to(package))
        z.write(output / (ident + '.mod'), ident + '.mod')
    print('Pacote:', archive)
    if args.no_install:
        return
    if args.user_dir:
        user = args.user_dir
    elif sys.platform.startswith('linux'):
        user = Path(os.environ.get('XDG_DATA_HOME', str(Path.home() / '.local/share'))) / 'Paradox Interactive/Crusader Kings III'
    else:
        user = Path.home() / 'Documents/Paradox Interactive/Crusader Kings III'
    mods = user / 'mod'
    target = mods / ident
    marker = target / '.community-generated'
    if target.is_symlink() or (target.exists() and not marker.is_file()):
        raise SystemExit('Destino não pertence ao instalador. Nenhum arquivo instalado: ' + str(target))
    launcher = mods / (ident + '.mod')
    if launcher.is_symlink() or (launcher.exists() and not marker.is_file()):
        raise SystemExit('Descritor existente não pertence ao instalador: ' + str(launcher))
    # Keep the official Workshop identity only in the installed official copy.
    old = (target / 'descriptor.mod').read_text(encoding='utf-8') if (target / 'descriptor.mod').exists() else ''
    workshop = re.search(r'^remote_file_id\s*=\s*"(\d+)"', old, re.M)
    installed_descriptor = descriptor
    if not test:
        installed_descriptor += 'remote_file_id="3818924334"\n'
    mods.mkdir(parents=True, exist_ok=True)
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(package, target)
    marker.touch()
    (target / 'descriptor.mod').write_text(installed_descriptor, encoding='utf-8')
    # The launcher's external descriptor needs an unambiguous local image path.
    launcher_descriptor = re.sub(
        r'^picture="([^"\n]+)"',
        lambda m: 'picture="' + (target / m[1]).as_posix() + '"',
        installed_descriptor,
        flags=re.M,
    )
    launcher.write_text(launcher_descriptor + f'path="{target.as_posix()}"\n', encoding='utf-8')
    # Existing local entries can retain a null thumbnail even after descriptor updates.
    database = user / 'launcher-v2.sqlite'
    picture = re.search(r'^picture="([^"\n]+)"', descriptor, re.M)
    if database.exists() and picture:
        image_path = target / picture[1]
        if image_path.is_file():
            try:
                with sqlite3.connect(str(database), timeout=10) as connection:
                    rows = connection.execute(
                        "SELECT id FROM mods WHERE source='local' AND gameRegistryId=? AND dirPath=?",
                        ('mod/' + ident + '.mod', str(target)),
                    ).fetchall()
                    if rows:
                        backup = database.with_name('launcher-v2.before-local-thumbnail-' + str(time.time_ns()) + '.sqlite')
                        with sqlite3.connect(str(backup)) as destination:
                            connection.backup(destination)
                        connection.execute(
                            "UPDATE mods SET thumbnailPath=? WHERE source='local' AND gameRegistryId=? AND dirPath=?",
                            (str(image_path), 'mod/' + ident + '.mod', str(target)),
                        )
                        if not test:
                            connection.execute(
                                "UPDATE mods SET remoteSteamId=? WHERE source='local' AND gameRegistryId=? AND dirPath=?",
                                ('3818924334', 'mod/' + ident + '.mod', str(target)),
                            )
                        print('Miniatura local registrada. Backup:', backup)
            except sqlite3.Error as error:
                print('Não foi possível atualizar a miniatura no launcher:', error)
    print('Instalado:', target)
    print('Ative somente uma edição da tradução no launcher e selecione Español.')
    if not test:
        print('Edição oficial preparada. O envio à Steam deve ser feito pelo launcher.')
