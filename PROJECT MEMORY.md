# PROJECT MEMORY - CORE ERP

## 1. Visão Geral
O **CORE ERP** é um sistema ERP SaaS profissional, modular, escalável e multiempresa construído sobre a plataforma **Odoo Community**. Seu objetivo principal é fornecer uma gestão empresarial robusta, flexível e preparada para implantação em nuvem (Oracle Cloud Infrastructure - OCI).

## 2. Stack Tecnológica
- **Base ERP:** Odoo Community (Python 3.10 / Odoo 17.0)
- **Banco de Dados:** PostgreSQL 15
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
- `custom_addons/`: Estrutura pronta para receber módulos customizados.

## 5. Decisões Técnicas Tomadas
- **Adoção do Odoo Community 17.0:** Permite total controle sobre a base de código sem custos de licenciamento por usuário da versão Enterprise.
- **Abordagem 100% Dockerizada:** Garante consistência do ambiente entre o desenvolvimento (Windows 11) e a produção (OCI Linux).
- **Mapeamento de Volume `./config/odoo.conf`:** Garante o fornecimento das diretivas corretas do Odoo (`[options]`) e isolamento da master password.

## 6. Pendências e Próximos Passos
- Inicializar a **Fase 2: Autenticação, Multiempresa e Segurança**.
- Criar o primeiro módulo customizado base (`custom_addons/core_base`).
- Definir regras de controle de acesso (ACLs) e isolamento rigoroso entre empresas (multi-company record rules).