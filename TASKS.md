# TASKS - CORE ERP

## Fase 1: Infraestrutura (Concluída)
- [x] Criar arquivos de governança do projeto (`PROJECT_MEMORY.md`, `CHANGELOG.md`, `ROADMAP.md`, `TASKS.md`).
- [x] Criar infraestrutura Docker e banco de dados PostgreSQL.

---

## Fase 2: Autenticação, Multiempresa e Segurança (Concluída)
- [x] Criar a estrutura e instalar o módulo `custom_addons/core_base`.

---

## Fase 3: CRM - Gestão de Leads e Oportunidades (Concluída)
- [x] Criar a estrutura do módulo `custom_addons/core_crm`.
- [x] Adicionar campos customizados (`mrr_estimate` e `business_segment`).
- [x] Configurar permissões ACL e views customizadas.
- [x] Resolver estrutura de pastas `security/` e instalar o módulo no Odoo.

---

## Fase 4: Vendas - Cotações e Pedidos (Em Andamento)

### Tarefas Atuais
- [ ] Salvar e enviar as alterações da Fase 3 para o GitHub.
- [ ] Criar a estrutura do módulo customizado `custom_addons/core_sale`.
- [ ] Configurar a conversão automática de oportunidades do CRM em pedidos de venda com métricas SaaS.