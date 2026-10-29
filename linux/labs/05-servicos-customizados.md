# Lab 05: Criação de Serviços Customizados no Linux (`systemd`)

**Data:** 29 de Outubro de 2026
**Objetivo:** Criar um script de monitoramento básico e configurá-lo como um serviço nativo do sistema usando arquivos `.service` do `systemd`.

---

## 1. O que é uma Unit File no `systemd`?

No Linux moderno, serviços são definidos em arquivos de unidade (*unit files*) localizados geralmente em `/etc/systemd/system/`. 

Esses arquivos possuem três seções principais:
- **`[Unit]`**: Metadados e dependências do serviço.
- **`[Service]`**: Como o serviço deve ser executado (comando, usuário, regras de reinicialização).
- **`[Install]`**: Define em qual momento do boot o serviço deve ser ativado.

---

## 2. Passo a Passo Prático

### Passo 1: Criar o Script de Monitoramento
Criamos um script simples que grava a data e o status do sistema em um arquivo de log a cada 10 segundos:

```bash
sudo mkdir -p /opt/meus-scripts
sudo nano /opt/meus-scripts/monitor.sh

## 2. Mão na massa no terminal (Testando agora)

Bora rodar na prática aí na sua máquina!

1. Salve o arquivo `05-servicos-customizados.md` no seu repositório `devops-labs`.
2. Siga os comandos do **Passo 1** acima no terminal (criar a pasta, o script `monitor.sh` e dar permissão `chmod +x`).
3. Crie o arquivo `/etc/systemd/system/meu-monitor.service` com os comandos do **Passo 2**.
4. Rode `sudo systemctl daemon-reload` e depois `sudo systemctl start meu-monitor`.

> **Nota para WSL2:** Dependendo de como seu WSL2 foi configurado, se o `systemctl` reclamar que o `systemd` não está ativo, basta testar rodando a criação dos arquivos e me avisar que te mostro como validar a sintaxe ou ativá-lo!

Roda aí o Passo 1 e o Passo 2 e me diz o que apareceu no `sudo systemctl status meu-monitor`!
