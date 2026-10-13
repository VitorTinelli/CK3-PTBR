# CK3 PT-BR 1.20+ (By god alone)

Tradução de **Crusader Kings III para português brasileiro**, com textos de interface, menus, eventos e outros conteúdos do jogo.

O mod utiliza o idioma **Español** como base. Para exibir a tradução, selecione esse idioma nas configurações do jogo.

## Compatibilidade

Preparado para **Crusader Kings III 1.20.x**. Atualizações do jogo podem adicionar textos ou exigir ajustes na tradução.

A tradução está em revisão contínua. Parte do conteúdo foi traduzida com assistência de IA e pode conter erros de contexto, concordância ou termos ainda em outro idioma. Sugestões e correções são bem-vindas.

## Como usar

1. Instale o mod pela Steam Workshop ou faça a instalação manual conforme o [guia de instalação](docs/INSTALAR.md).
2. Ative o mod no launcher do jogo.
3. Selecione **Español** como idioma e reinicie o jogo, se necessário.

Evite usar outras traduções que substituam o mesmo idioma ao mesmo tempo, pois elas podem causar conflitos.

## Como contribuir

Você pode ajudar sem saber programar:

- **Relate um problema:** abra uma [issue](https://github.com/VitorTinelli/CK3-PTBR/issues) informando a tela ou evento, o texto encontrado e a versão do jogo. Se possível, anexe uma captura.
- **Sugira uma correção:** encontre o texto em [`mod/localization/spanish/replace`](mod/localization/spanish/replace), abra o arquivo no GitHub e clique no lápis para propor uma alteração.
- **Revise os textos:** ajude a melhorar a clareza, a concordância e a consistência dos termos.

Consulte o [guia de contribuição](CONTRIBUTING.md) antes de editar. Não é necessário instalar ferramentas para relatar problemas ou propor pequenas correções pelo navegador.

## Desenvolvimento

Para validar os arquivos e gerar um pacote local, use Python 3.10 ou superior na pasta do repositório:

```bash
python3 tools/validate.py
python3 tools/build.py
```

Para gerar e instalar uma edição separada para testes:

```bash
python3 tools/build_test.py
```

Ela aparece no launcher como `[TESTE LOCAL] CK3 PT-BR 1.20+ (By god alone)` e usa a pasta `ck3_ptbr_teste`.

Para gerar e instalar a edição com o nome oficial, pronta para envio manual pelo launcher à Steam:

```bash
python3 tools/build_steam.py
```

Os pacotes e pastas de publicação ficam em `dist/teste/` e `dist/steam/`. Ambos aceitam `--no-install` para somente gerar os arquivos ou `--user-dir "CAMINHO/Paradox Interactive/Crusader Kings III"` para escolher a pasta de dados. A edição oficial preserva o `remote_file_id` de uma instalação oficial anterior gerenciada pelo instalador; a edição de teste não herda esse identificador. Ative apenas uma edição da tradução por vez.

O comando antigo `tools/build.py` continua gerando `dist/ck3-ptbr-completo.zip`. As verificações também são executadas pelo GitHub Actions nas propostas de alteração.

A validação automática confere o formato dos arquivos e a presença das chaves esperadas. Ela não substitui a revisão linguística nem os [testes no jogo](docs/TESTAR.md).

## Estrutura do repositório

- `mod/`: arquivos de tradução e imagens do mod.
- `docs/`: instruções de instalação e testes.
- `tools/`: ferramentas de instalação, validação e geração do pacote.
- `qa/required-keys.txt`: identificadores usados como referência de cobertura.
- `.github/`: formulários de contribuição e verificações automáticas.
