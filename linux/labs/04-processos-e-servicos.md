# Lab 04: Processos e Monitoramento de Sistema (`ps`, `top`, `kill`, `systemctl`)

**Data:** 22 de Outubro de 2026
**Objetivo:** Compreender o ciclo de vida de processos no Linux, gerenciar o consumo de recursos do sistema e controlar serviços utilizando o `systemd`.

---

## 1. Monitoramento e Visualização de Processos

Cada programa em execução no Linux recebe um identificador único chamado **PID (Process ID)**.

### Comandos de Inspeção
- **`ps`**: Exibe um instantâneo (*snapshot*) dos processos em execução na sessão atual.
  - `ps aux`: Lista todos os processos do sistema com detalhes de CPU, memória e usuário.
  - `ps -ef`: Exibe a árvore e hierarquia de processos.
- **`top`**: Monitor de processos em tempo real (interativo).
- **`htop`**: Versão melhorada e mais amigável do `top` (com suporte a cores e navegação fácil).

---

## 2. Gerenciamento de Sinais e Finalização de Processos

Quando um processo trava ou precisa ser encerrado, enviamos **sinais (signals)** para o PID correspondente.

### Principais Sinais
| Sinal | Nome | Descrição |
| :--- | :--- | :--- |
| **`15`** | `SIGTERM` | Solicita o encerramento gracioso (padrão) |
| **`9`** | `SIGKILL` | Força a finalização imediata do processo |
| **`1`** | `SIGHUP` | Reinicia/recarrega as configurações do processo |

### Comandos Práticos
```bash
# 1. Encerrar um processo pelo PID (forma graciosa)
kill 1234

# 2. Forçar a finalização de um processo travado
kill -9 1234

# 3. Encerrar processos pelo nome da aplicação
pkill firefox
killall nginx
