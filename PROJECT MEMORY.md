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
- `custom_addons/core_base`: Módulo base de segurança, grupos de acesso (`Usuário Padrão` e `Administrador`) e regras de segregação multiempresa. **Status: Instalado e Ativo.**

## 5. Decisões Técnicas Tomadas
- **Adoção do Odoo Community 17.0:** Permite total controle sobre a base de código sem custos de licenciamento por usuário da versão Enterprise.
- **Abordagem 100% Dockerizada:** Garante consistência do ambiente entre o desenvolvimento (Windows 11) e a produção (OCI Linux).
- **Mapeamento de Volume `./config/odoo.conf`:** Garante o fornecimento das diretivas corretas do Odoo (`[options]`) e alinhamento da Master Password (`admin_passwd`).
- **Remoção de atributos não padrão em XMLs:** Manutenção de tags `<data>` estritamente padrão para evitar exceções do validador `lxml`.

## 6. Pendências e Próximos Passos
- Inicializar a **Fase 3: CRM (Gestão de Leads e Oportunidades)**.
- Criar o módulo customizado `custom_addons/core_crm`.
- Configurar views de funil de vendas (Kanban), estágios de negociação e vínculo com o `core_base`.