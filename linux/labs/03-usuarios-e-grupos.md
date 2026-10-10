# Lab 03: Gerenciamento de Usuários e Grupos (`useradd`, `groupadd`, `chown`)
  
**Objetivo:** Compreender a estrutura de contas de usuários, criação de grupos de trabalho, controle de propriedades de arquivos e elevação de privilégios no Linux.

---

## 1. Estrutura de Arquivos de Sistema

No Linux, as informações de usuários e grupos ficam gravadas em arquivos de configuração no diretório `/etc`:

* `/etc/passwd`: Lista todos os usuários do sistema, UID, GID, diretório home e shell padrão.
* `/etc/group`: Lista todos os grupos e seus respectivos membros.
* `/etc/shadow`: Armazena os hashes das senhas dos usuários com acesso restrito.

---

## 2. Comandos Principais e Exercícios Práticos

### Gerenciamento de Grupos e Usuários
```bash
# 1. Criar um novo grupo para a equipe de devops
sudo groupadd devops-team

# 2. Criar um novo usuário e adicioná-lo ao grupo devops-team
sudo useradd -m -s /bin/bash -g devops-team devuser

# 3. Definir senha para o novo usuário
sudo passwd devuser

# 4. Verificar se o usuário foi criado corretamente
id devuser
grep devuser /etc/passwd