# 🛡️ Sentinel Firewall & IDS

![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-green)
![Security](https://img.shields.io/badge/security-IDS-red)
![Architecture](https://img.shields.io/badge/architecture-modular-purple)

---

## 🔐 Visão Geral

O **Sentinel Firewall & IDS** é um sistema modular de segurança de rede desenvolvido em Python, com foco em **monitoramento em tempo real**, **filtragem de pacotes** e **detecção de intrusão (IDS)**.

O projeto simula uma arquitetura de firewall moderna, priorizando:

- Baixo overhead de processamento
- Extensibilidade de regras
- Separação clara de responsabilidades
- Princípios de segurança como **Defesa em Profundidade**

---

## 🧠 Como Funciona

O Sentinel opera em três camadas principais:

```text
1. Captura de tráfego de rede
2. Análise e aplicação de regras de firewall
3. Registro de eventos e detecção de comportamento suspeito (IDS)

Cada pacote é analisado em tempo real e classificado com base em regras definidas no sistema.

🏗️ Arquitetura do Sistema
.
├── main.py                 # Ponto de entrada da aplicação
├── models/                 # Estruturas de dados e entidades
├── services/               # Regras de firewall e lógica IDS
├── database/
│   └── logs/               # Logs de segurança (não versionados)
├── .gitignore             # Proteção de arquivos sensíveis

A arquitetura segue o padrão modular service-based, permitindo fácil expansão para novos módulos de detecção.

🛠️ Tecnologias e Conceitos
Python 3.x
Estrutura modular (Models / Services / Core)
Simulação de Firewall de rede
Lógica de IDS (Intrusion Detection System)
Análise de logs e eventos
Otimização de filtragem (foco em eficiência e escalabilidade)
🚀 Funcionalidades
Monitoramento de tráfego de rede em tempo real
Sistema de regras para bloqueio de pacotes
Registro de eventos de segurança (logs)
Detecção básica de padrões suspeitos (IDS)
Isolamento de dados sensíveis em ambiente local
Arquitetura preparada para expansão (plugins/mods futuros)
🛡️ Princípios de Segurança

Este projeto foi desenvolvido seguindo boas práticas de Cybersecurity Engineering:

🔒 Privilégio mínimo: apenas o necessário é processado e armazenado
🧱 Defesa em profundidade: múltiplas camadas de filtragem
🧾 Auditoria segura: logs isolados e não versionados
⚡ Baixa superfície de ataque: arquitetura simples e controlada
⚙️ Como Executar
1. Clonar o repositório
git clone https://github.com/Guilherme137alves77/sentinel-firewall.git
2. Acessar o diretório
cd sentinel-firewall
3. Executar o sistema
python3 main.py
📊 Possíveis Evoluções
Machine Learning para detecção de intrusão
Integração com Suricata/Zeek
Dashboard web para visualização de logs
API REST para controle remoto do firewall
Sistema de alertas em tempo real
👨‍💻 Autor

Guilherme Alves da Silva

🔐 Cybersecurity / Backend Developer
📍 São Paulo, Brasil
💻 GitHub: https://github.com/Guilherme137alves77
💼 LinkedIn: www.linkedin.com/in/guilherme-alves-3715a3362
⚠️ Aviso

Este projeto é educacional e simula conceitos de firewall e IDS.
Não deve ser utilizado como solução de segurança em produção sem validação adicional.
