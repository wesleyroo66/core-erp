# CHANGELOG - CORE ERP

Todas as alterações relevantes neste projeto serão documentadas neste arquivo.

## [0.4.0] - 2026-11-11
### Adicionado
- Instalação e ativação bem-sucedida do módulo `core_base` no banco de dados do Odoo.
- Conclusão da Fase 2 (Autenticação, Multiempresa e Segurança).

### Corrigido
- Ajuste na estrutura do arquivo `custom_addons/core_base/security/core_base_security.xml`, removendo o atributo inválido `nodry="1"` da tag `<data>` para solucionar erro de validação `lxml`.

## [0.3.0] - 2026-11-11
### Adicionado
- Criação do módulo customizado `custom_addons/core_base` com manifesto, permissões ACL e regras de segurança multiempresa.
- Documentação interna do módulo em `custom_addons/core_base/README.md`.

## [0.2.0] - 2026-11-11
### Adicionado
- Configuração completa da infraestrutura Docker para Odoo 17.0 e PostgreSQL 15.
- Criação do arquivo de ambiente `.env` para centralização de credenciais.

## [0.1.0] - 2026-11-11
### Adicionado
- Estrutura inicial de governança e documentação do projeto (`PROJECT_MEMORY.md`, `CHANGELOG.md`, `ROADMAP.md`, `TASKS.md`).