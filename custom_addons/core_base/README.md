# Módulo Base - CORE ERP (`core_base`)

## Objetivo
O módulo `core_base` é o núcleo de customização do **CORE ERP**. Ele estabelece as configurações fundamentais de segurança, grupos de acesso e regras de isolamento multiempresa para o ambiente SaaS.

## Estrutura de Arquivos
- `__manifest__.py`: Arquivo de declaração, dependências e dados do módulo.
- `__init__.py`: Inicializador Python do módulo.
- `security/core_base_security.xml`: Definição dos grupos de permissão e regras de registro multiempresa.
- `security/ir.model.access.csv`: Lista de controle de acesso (ACL) para os modelos de dados.

## Dependências
- `base`: Módulo nativo fundamental do Odoo.
- `mail`: Infraestrutura de comunicação e mensagens nativa.

## Uso e Instalação
1. Certifique-se de que o diretório `custom_addons` está mapeado no `docker-compose.yml`.
2. No Odoo (com o Modo Desenvolvedor ativo), vá em **Aplicativos** > **Atualizar Lista de Aplicativos**.
3. Busque por `CORE ERP - Módulo Base` e clique em **Instalar**.