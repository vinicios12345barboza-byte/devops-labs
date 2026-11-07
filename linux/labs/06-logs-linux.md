# Lab 06: Gestão de Logs (`journalctl`, `tail` e `grep`)

**Data:** Novembro de 2026
**Objetivo:** Rastrear, filtrar e analisar logs do sistema e de serviços customizados usando o `journalctl`, combinando com ferramentas tradicionais de arquivos de texto (`tail` e `grep`).

---

## 1. Onde os Logs Vivem no Linux?

No Linux moderno, a gestão de logs é dividida entre o ecossistema centralizado do sistema operacional e arquivos de texto plano tradicionais:

- **`systemd-journald` (`journalctl`):** Coleta e armazena logs do kernel, serviços e do sistema de forma binária e indexada, garantindo buscas rápidas.
- **Arquivos de Texto Plano (`/var/log/`):** Utilizados por aplicações legadas, servidores web (como Nginx) ou scripts customizados para gravação direta.

---

## 2. Auditoria de Serviços com `journalctl`

Como criamos um serviço customizado (`meu-monitor.service`) nos labs anteriores, podemos auditar o seu comportamento diretamente pelo `journalctl`.

### Comandos de Inspeção e Rastreio
- **`journalctl -u <servico>`**: Exibe todos os logs referentes a um serviço específico.
- **`journalctl -u <servico> -f`**: Acompanha os logs em tempo real (*follow*), ideal para monitoramento ativo.
- **`journalctl -u <servico> -n <linhas>`**: Mostra apenas as últimas $N$ entradas do log.
- **`journalctl --since "1 hour ago"`**: Filtra logs gerados dentro de um intervalo de tempo específico.

### Exemplos Práticos
```bash
# 1. Visualizar todo o histórico de logs do nosso monitor
sudo journalctl -u meu-monitor.service

# 2. Acompanhar os logs do monitor em tempo real
sudo journalctl -u meu-monitor.service -f
Manipulação de Logs em Texto Plano (tail, grep e pipe)
# 3. Exibir apenas as últimas 10 linhas do serviço
sudo journalctl -u meu-monitor.service -n 10

## 3. Manipulação de Logs em Texto Plano (tail, grep e pipe)
Se o seu script ou aplicação grava logs diretamente em arquivos de texto plano (como o tradicional `/var/log/syslog` ou arquivos de log customizados), utilizamos utilitários clássicos do Linux para filtragem e monitoramento ágil.

### Ferramentas Fundamentais
- **`tail`**: Exibe o final de um arquivo de texto. Com a flag `-f`, mantém a leitura ativa em tempo real conforme novos dados são gravados. Com `-n`, define quantas linhas exibir.
- **`grep`**: Pesquisa por padrões de texto ou palavras-chave específicas dentro de arquivos ou fluxos de dados.
- **`Pipe (\|)`**: O operador de tubulação (`|`) redireciona a saída padrão (*stdout*) de um comando para a entrada padrão (*stdin*) de outro.

### Exemplos Práticos

```bash
# 1. Acompanhar em tempo real as novas entradas de um log de sistema
sudo tail -f /var/log/syslog

# 2. Filtrar apenas as linhas que contêm a palavra "error" em um log
sudo grep -i "error" /var/log/syslog
# (Nota: a flag -i faz com que o grep ignore diferenças entre maiúsculas Oe minúsculas)

# 3. O Poder do Pipe: Pegar as últimas 100 linhas de um log e filtrar apenas o que diz "failed"
sudo tail -n 100 /var/log/syslog | grep "failed"

# 4. Monitorar um log customizado em tempo real já filtrando por uma palavra-chave
sudo tail -f /var/log/meu-monitor.log | grep "normal"
