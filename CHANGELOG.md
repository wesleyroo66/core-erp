# CHANGELOG - CORE ERP

Todas as alterações relevantes neste projeto serão documentadas neste arquivo.

## [0.5.0] - 2026-11-11
### Adicionado
- Criação e ativação com sucesso do módulo customizado `custom_addons/core_crm`.
- Extensão do modelo `crm.lead` adicionando os campos `mrr_estimate` (MRR Estimado) e `business_segment` (Segmento de Atuação).
- Injeção dos novos campos na view de formulário do CRM via XPath.
- Conclusão da Fase 3 (CRM - Gestão de Leads e Oportunidades).

### Corrigido
- Ajuste na estrutura do diretório `security/` do módulo `core_crm`, removendo subpasta duplicada e corrigindo o erro `FileNotFoundError: core_crm/security/ir.model.access.csv`.

## [0.4.0] - 2026-11-11
### Adicionado
- Instalação e ativação bem-sucedida do módulo `core_base`.
- Conclusão da Fase 2 (Autenticação, Multiempresa e Segurança).

## [0.3.0] - 2026-11-11
### Adicionado
- Criação do módulo customizado `custom_addons/core_base`.

## [0.2.0] - 2026-11-11
### Adicionado
- Configuração completa da infraestrutura Docker para Odoo 17.0 e PostgreSQL 15.

## [0.1.0] - 2026-11-11
### Adicionado
- Estrutura inicial de governança do projeto (`PROJECT_MEMORY.md`, `CHANGELOG.md`, `ROADMAP.md`, `TASKS.md`).