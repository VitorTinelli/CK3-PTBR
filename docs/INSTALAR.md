# Instalação

O mod substitui os textos do idioma **Español** por português brasileiro. Evite ativar outras traduções que utilizem o mesmo idioma simultaneamente.

## Pela Steam Workshop

1. Inscreva-se no mod pela página da Workshop e aguarde o download.
2. Abra o launcher e adicione o mod ao conjunto de mods que pretende usar.
3. Ative o mod e selecione **Español** nas configurações do jogo.
4. Reinicie o jogo após alterar o idioma, se necessário.

## Pelo código-fonte

Baixe ou clone o repositório. Feche o jogo e o launcher e, em um terminal aberto na pasta do repositório, execute:

```bash
python3 tools/install.py
```

É necessário Python 3.10 ou superior, sem bibliotecas adicionais. No Windows, use `py` no lugar de `python3` se esse for o comando disponível.

O instalador utiliza o diretório de dados padrão do CK3. Para uma pasta personalizada, inclusive Documentos redirecionados para o OneDrive, informe o caminho:

```bash
python3 tools/install.py --user-dir "CAMINHO/Paradox Interactive/Crusader Kings III"
```

Informe a pasta que contém os dados de usuário do jogo, e não a pasta dos arquivos instalados pela Steam. Depois da instalação, ative o mod no launcher e selecione **Español**.

## Pelo pacote ZIP

Extraia a pasta `ck3_ptbr_comunidade` e o arquivo `ck3_ptbr_comunidade.mod` dentro da pasta `mod` do diretório de dados do CK3.

Locais padrão:

| Sistema | Diretório de dados |
| --- | --- |
| Windows | `Documentos/Paradox Interactive/Crusader Kings III` |
| Linux | `~/.local/share/Paradox Interactive/Crusader Kings III` |
| macOS | `~/Documents/Paradox Interactive/Crusader Kings III` |

No Linux, a variável `XDG_DATA_HOME` pode alterar o diretório padrão. No Windows, a localização de Documentos pode variar. Crie a pasta `mod` se ela não existir.

Reabra o launcher, ative o mod e selecione **Español**. Evite ativar ao mesmo tempo uma cópia manual e uma cópia da Workshop.

## Desativar

Desative o mod no launcher. Se desejar, escolha outro idioma nas configurações do jogo. A instalação local não altera os arquivos originais do jogo nem os saves.
