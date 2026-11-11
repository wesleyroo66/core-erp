# PROJECT MEMORY - CORE ERP

## 1. Visão Geral
O **CORE ERP** é um sistema ERP SaaS profissional, modular, escalável e multiempresa construído sobre a plataforma **Odoo Community**. Seu objetivo principal é fornecer uma gestão empresarial robusta, flexível e preparada para implantação em nuvem (Oracle Cloud Infrastructure - OCI).

## 2. Stack Tecnológica
- **Base ERP:** Odoo Community (Python)
- **Banco de Dados:** PostgreSQL
- **Containerização:** Docker & Docker Compose
- **Controle de Versão:** Git & GitHub
- **IDE Recomendada:** VS Code
- **Ambiente de Dev:** Windows 11 (WSL2 / Docker Desktop)
- **Infraestrutura Futura (Deploy):** Oracle Cloud Infrastructure (OCI)

## 3. Arquitetura do Sistema
- **Padrão:** Clean Architecture & princípios SOLID.
- **Isolamento:** Todos os serviços sob contêineres isolados via Docker.
- **Multi-tenancy / Multiempresa:** Utilização nativa do isolamento de empresas e bancos de dados do Odoo.
- **Módulos customizados:** Armazenados no diretório de addons customizados (`custom_addons/`).

## 4. Módulos Existentes
- *Nenhum módulo customizado criado até o momento (Fase 1 em inicialização).*

## 5. Decisões Técnicas Tomadas
- **Adoção do Odoo Community:** Permite total controle sobre a base de código sem custos de licenciamento por usuário da versão Enterprise.
- **Abordagem 100% Dockerizada:** Garante consistência do ambiente entre o desenvolvimento (Windows 11) e a produção (OCI Linux).

## 6. Pendências e Próximos Passos
- Criar arquivos de infraestrutura inicial (`docker-compose.yml`, `Dockerfile` e `.env`).
- Configurar o arquivo de configuração do Odoo (`odoo.conf`).
- Subir os contêineres e validar a primeira inicialização do banco PostgreSQL e Odoo.