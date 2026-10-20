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

### Gerenciamento de Usuários
```bash
# 1. Criar um novo usuário
sudo adduser devops (com interatividade)

# 2. Mudar senha de usuário
sudo passwd devops (pede apenas a senha nova)

# 3. Fazer login
su - devops (faz login direto pro diretório home)

# 4. Vendo opções do usuário, Bloqueando senha & Desbloquando
sudo passwd -S devops
sudo passwd -l devops (Bloqueia a senha)
sudo passwd -u devops (Desbloquia a senha)

# 5. Bloquando & Desbloqueando a conta 
sudo usermod -L devops (Bloqueia a conta)
sudo usermod -U devops (Desbloqueia  a conta)

# 6. Modificar nome
sudo usermod -l dev_ops devops (Modifica nome de login -> nome-novo nome-antigo)
sudo usermod -c 'Vinicios' dev_ops (Altera o Nome Completo (Comentário) )

# 7. Alterar diretório home & Mover os arquivos antigos 
sudo usermod -d /novo/home -m dev_ops

# 8. Alterar shell padrão
sudo usermod -s /bin/bash dev_ops

# 9. Alterar UID único do usuário
sudo usermod -u 1500 dev_ops


# 10. Removendo usuário 
sudo deluser dev_ops (Não remove diretório home)
sudo deluser --remove-home dev_ops

### Gerenciamento de Grupos

# 1. Criar grupo
sudo groupadd nome-grupo 
sudo addgroup --gid 2330 nome-grupo (Permite colocar um GID específico)

# 2. Adicionar usuário ao grupo
sudo usermod -aG grupo usuário (Mais usado)
sudo adduser usuário grupo (Interativo)
sudo gpasswd -a usuário grupo

# 3. Alterar grupo primário do usuário
sudo usermod -g grupo usuário

# 4. Remover usuário do grupo
sudo gpasswd -d usuário grupo

# 5. Adicionar senha no grupo
sudo gpasswd grupo (Vai pedir pra colocar uma senha. Senha do grupo fica em /etc/gshadow)

# 6. Usuário entrando no grupo (Colocando a senha)
newgrp grupo

# 7. Definir usuário como administrador
sudo -A usuário grupo

# 8. Remover grupo
sudo groupdel grupo

