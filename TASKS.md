# TASKS - CORE ERP

## Fase 1: Infraestrutura (Concluída)
- [x] Criar arquivos de governança do projeto (`PROJECT_MEMORY.md`, `CHANGELOG.md`, `ROADMAP.md`, `TASKS.md`).
- [x] Criar arquivo `.env` para variáveis de ambiente.
- [x] Criar diretório `custom_addons/` para desenvolvimento de novos módulos.
- [x] Criar `config/odoo.conf` com configurações de segurança e multiempresa.
- [x] Criar `docker-compose.yml` para orquestrar Odoo e PostgreSQL.
- [x] Corrigir inicialização de volume e criar a base de dados `core_erp_db` em `localhost:8069`.

---

## Fase 2: Autenticação, Multiempresa e Segurança (Concluída)
- [x] Criar a estrutura do módulo customizado `custom_addons/core_base`.
- [x] Configurar arquivos de segurança (`ir.model.access.csv` e `core_base_security.xml`).
- [x] Adicionar `README.md` interno no módulo `core_base`.
- [x] Ativar o Modo Desenvolvedor no Odoo.
- [x] Corrigir atributo na tag `<data>` do arquivo de segurança.
- [x] Instalar o módulo `CORE ERP - Módulo Base` no sistema.

---

## Fase 3: CRM - Gestão de Leads e Oportunidades (Em Andamento)

### Tarefas Atuais
- [ ] Sincronizar as atualizações da governança com o GitHub.
- [ ] Criar a estrutura do módulo customizado `custom_addons/core_crm`.
- [ ] Declarar dependência do módulo nativo `crm` e do `core_base` no manifesto.
- [ ] Customizar views do Kanban de oportunidades e regras de visualização por vendedor/empresa.