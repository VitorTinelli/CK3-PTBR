# Como testar uma alteração

## Verificação automática

Na pasta do repositório, execute:

```bash
python3 tools/validate.py
python3 tools/build.py
```

O validador confere o formato dos arquivos, a codificação UTF-8 com BOM, o cabeçalho de idioma, chaves duplicadas e a presença dos identificadores de referência. O pacote gerado fica em `dist/ck3-ptbr-completo.zip`.

A lista `qa/required-keys.txt` é a referência de cobertura para CK3 1.20.0.4. Ela deve ser revisada quando o projeto adotar uma nova versão do jogo. A presença de uma chave não comprova a qualidade da tradução nem seu carregamento em uma tela específica.

## Verificação no jogo

1. Siga o [guia de instalação](INSTALAR.md) e use o idioma **Español**.
2. Comece com apenas este mod ativo, para separar problemas da tradução de conflitos com outros mods.
3. Abra a tela ou evento afetado pela alteração e confira o texto em contexto.
4. Verifique acentuação, concordância, quebras de linha, nomes dinâmicos, cores, ícones e textos cortados.
5. Procure identificadores ou expressões de código aparecendo no lugar de texto.

Para alterações abrangentes, confira também menu principal, configurações, seleção de personagem, dicas ao passar o mouse, religião, cultura, decisões e eventos em uma partida de teste.

## Registrar o resultado

Na issue ou proposta de alteração, informe a versão do jogo, os DLCs e mods ativos, a tela testada e o resultado. Inclua uma captura quando ela ajudar a explicar o problema. Se não foi possível testar no jogo, indique isso claramente.

A verificação automática não substitui a revisão linguística. Textos visíveis dentro de expressões como `Concept(...)`, nomes próprios e referências dinâmicas exigem atenção ao contexto.
