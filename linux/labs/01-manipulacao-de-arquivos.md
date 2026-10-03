# LAB 01 - Navegação e Manipulação de Arquivos

## Objetivo
Praticar a criação, navegação e organização de diretórios e arquivos no Linux usando o terminal WSL2.

## Cenário Prático
Estruturar o ambiente de estudos de DevOps e simular a criação de pastas organizadas para projetos.

## Passo a Passo Executado (Manipulação & Limpeza)

```bash
# 1. Estruturação
mkdir -p labs/evidencias
touch comandos.md README.md

# 2. Inspeção detalhada e recursiva
ls -la
ls -R

# 3. Remoção de arquivos e pastas
rm Arquivos/oi.txt
rmdir PastaVazia/           # Apenas para diretórios vazios
rm -rf Linux/              # Remove diretório e todo seu conteúdo recursivamente

# 4. Cópia (Aquivo e Diretório)
cp a.txt copia-a.txt
cp -r ../Arquivos ../Arquivos-backup  # -r para copiar pastas inteiras

# 5. Mover e Renomear
mv copia-a.txt renomeando.txt        # Renomeia
mv renomeando.txt ../               # Move para o diretório pai
mv *.txt ../ 			 # Move todos arquivos com final .txt 

# 6. Manipulação de conteúdo
echo -e "nome idade\nVini 19" > dados.txt
