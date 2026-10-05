# Lab 02: Permissões de Arquivos no Linux (`chmod`)

**Data:** 05 de Outubro de 2026  
**Objetivo:** Compreender o sistema de permissões do Linux (Leitura, Escrita, Execução) e aplicar alterações de acesso utilizando os modos octal (numérico) e simbólico com o comando `chmod`.

---

## 1. Conceitos Fundamentais

No Linux, cada arquivo e diretório possui permissões atribuídas a 3 tipos de usuários:
* **User (u):** Dono do arquivo/diretório.
* **Group (g):** Grupo de usuários proprietário.
* **Others (o):** Todos os outros usuários do sistema.

### Tipos de Permissões
| **r** | Read | Leitura do arquivo ou listagem de diretório | **4** |
| **w** | Write | Alteração do arquivo ou criação/deleção na pasta | **2** |
| **x** | Execute | Execução de scripts/programas ou acesso à pasta | **1** |

---

## 2. Modos de Uso do `chmod`

### Modo Octal (Numérico)
Soma-se os valores das permissões para definir os acessos de `User`, `Group` e `Others`:

* **`7`** ($4+2+1$): Permissão total (`rwx`)
* **`6`** ($4+2$): Leitura e escrita (`rw-`)
* **`5`** ($4+1$): Leitura e execução (`r-x`)
* **`4`** ($4$): Apenas leitura (`r--`)
* **`0`**: Nenhum acesso (`---`)



### Modo Simbólico
Utiliza operadores para adicionar (`+`), remover (`-`) ou atribuir (`=`) permissões:

* `chmod u+x script.sh` — Adiciona permissão de execução ao dono.
* `chmod go-w arquivo.txt` — Remove permissão de escrita do grupo e de outros.
* `chmod a+r arquivo.txt` — Concede leitura para todos (*all*).

---

## 3. Comandos Executados no Laboratório

```bash
# 1. Criação do arquivo para teste
touch teste-permissoes.sh

# 2. Verificação das permissões iniciais
ls -l teste-permissoes.sh

# 3. Adicionar permissão de execução ao dono
chmod u+x teste-permissoes.sh

# 4. Alterar permissões usando notação octal (755)
chmod 755 teste-permissoes.sh

# 5. Restringir acesso apenas ao dono (600)
chmod 600 teste-permissoes.sh