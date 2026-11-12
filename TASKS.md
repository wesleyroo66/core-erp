# TASKS - CORE ERP

## Fase 1: Infraestrutura (Concluída)
- [x] Criar arquivos de governança do projeto (`PROJECT_MEMORY.md`, `CHANGELOG.md`, `ROADMAP.md`, `TASKS.md`).
- [x] Criar arquivo `.env` para variáveis de ambiente.
- [x] Criar diretório `custom_addons/` para desenvolvimento de novos módulos.
- [x] Criar `config/odoo.conf` com configurações de segurança e multiempresa.
- [x] Criar `docker-compose.yml` para orquestrar Odoo e PostgreSQL.
- [x] Executar o ambiente e realizar o primeiro acesso ao Odoo em `localhost:8069`.

---

## Fase 2: Autenticação, Multiempresa e Segurança (Em Andamento)

### Tarefas Atuais
- [ ] Atualizar arquivos de memória e realizar commit da Fase 1 no Git.
- [ ] Criar a estrutura do módulo customizado base `custom_addons/core_base`.
- [ ] Criar o manifesto `__manifest__.py` do módulo `core_base`.
- [ ] Configurar os arquivos de segurança (`ir.model.access.csv`).
- [ ] Configurar regras de isolamento multiempresa (*Multi-company Record Rules*).
- [ ] Adicionar README.md explicativo dentro do módulo `core_base`.