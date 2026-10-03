## Comandos Linux

Guia de referência rápida para os comandos praticados durante o treinamento de DevOps.

## 1. Navegação e Manipulação
- `pwd`: Exibe o caminho do diretório atual.
- `ls -la`: Lista todos os arquivos (inclusive ocultos) com detalhes de permissão.
- `ls -R`: Listagem recursiva de pastas e subpastas.
- `mkdir -p <caminho>`: Cria diretórios e subdiretórios de forma encadeada.
- `touch <arquivo>`: Cria arquivo vazio ou atualiza a data de modificação.
- `rm -rf <diretório>`: Remove diretórios e seus conteúdos recursivamente e forçadamente.
- `cp -r <origem> <destino>`: Copia arquivos ou pastas recursivamente.
- `mv <origem> <destino>`: Move ou renomeia arquivos e diretórios.

## 2. Manipulação de Texto
- `cat <arquivo>`: Exibe o conteúdo completo do arquivo no terminal.
- `echo -e "texto\nlinha"`: Exibe texto com suporte a caracteres de escape (`\n` para quebra de linha).
- `>` e `>>`: Redireciona a saída para um arquivo (substitui com `>` e anexa com `>>`).

## 3. Permissões e Segurança (Em progresso)
- `chmod`: Altera permissões de leitura (`r=4`), escrita (`w=2`) e execução (`x=1`).
- `chown`: Altera o proprietário e grupo do arquivo/diretório.
