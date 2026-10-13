# Como contribuir

Você pode ajudar relatando erros, revisando português ou corrigindo textos pelo navegador.

## Relatar

Abra uma issue com a tela/evento, texto atual, sugestão, versão do jogo e outros mods ativos. Uma captura ajuda muito. Não envie saves completos nem dados pessoais quando uma captura já explicar o problema.

## Corrigir no GitHub

1. Use a busca do repositório para procurar uma frase ou identificador que aparece no jogo.
2. Abra o arquivo `.yml` dentro de `mod/localization/spanish/replace/` e clique no lápis.
3. Corrija somente o texto entre as aspas. Se necessário, aceite a criação de uma cópia do repositório (fork) para enviar sua proposta.
4. Selecione **Propose changes** e abra um **pull request** explicando a correção.
5. Aguarde a verificação automática e a revisão do mantenedor. Se a verificação acusar BOM/codificação, o mantenedor pode ajudar a normalizar o arquivo.

Exemplo:

```yaml
 MY_LABEL:0 "Texto em português"
```

Preserve `MY_LABEL`, `:0`, o cabeçalho `l_spanish:`, as referências `$NOME$`, expressões `[Character.GetName]`, ícones `@gold_icon!`, formatação `#bold ... #!` e quebras `\n`. Não remova entradas. Use português brasileiro e confira o termo usado em outras telas. Textos visíveis dentro de expressões como `Concept(...)` exigem atenção especial: peça ajuda se não tiver certeza.

Prefira uma correção ou um tema por proposta. Evite reformatação em massa, renomear arquivos ou copiar conteúdo de outras traduções sem autorização. Não precisa usar IA; se usar, revise o resultado e informe isso na proposta.

## Testar localmente (opcional)

Python 3.10 ou superior, sem bibliotecas adicionais:

```bash
python3 tools/validate.py
python3 tools/install.py
```

Consulte o [guia de instalação](docs/INSTALAR.md) para configurar o mod e o [guia de testes](docs/TESTAR.md) para verificar sua alteração. A validação automática não substitui a revisão do texto no jogo.

## Autorização da contribuição

Ao enviar uma contribuição, confirme que pode compartilhar esse conteúdo e autoriza sua incorporação, edição e distribuição neste projeto e nas publicações correspondentes do mod, com preservação dos créditos. Isso não muda os direitos dos autores da base. Para uma licença aberta uniforme de todo o projeto, o mantenedor deve acordar os termos com os titulares.
