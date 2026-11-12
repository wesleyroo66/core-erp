# CHANGELOG - CORE ERP

Todas as alterações relevantes neste projeto serão documentadas neste arquivo.

## [0.2.0] - 2026-11-11
### Adicionado
- Configuração completa da infraestrutura Docker para Odoo 17.0 e PostgreSQL 15.
- Criação do arquivo de ambiente `.env` para centralização de credenciais.
- Configuração do arquivo `config/odoo.conf` com parâmetros de segurança e limite de recursos.
- Criação do diretório `custom_addons/` mapeado via volume Docker.

### Corrigido
- Ajuste no caminho do arquivo de configuração de `./odoo.conf` para `./config/odoo.conf`.
- Inclusão do cabeçalho `[options]` no `odoo.conf` para evitar falha no script de bootstrap `wait-for-psql.py`.

## [0.1.0] - 2026-11-11
### Adicionado
- Estrutura inicial de governança e documentação do projeto (`PROJECT_MEMORY.md`, `CHANGELOG.md`, `ROADMAP.md`, `TASKS.md`).
- Definição da arquitetura base e diretrizes de desenvolvimento do CORE ERP.