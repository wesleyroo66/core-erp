# Módulo CRM - CORE ERP (`core_crm`)

## Objetivo
O módulo `core_crm` amplia os recursos de gestão de leads e oportunidades comerciais do **CORE ERP**, adicionando campos específicos de receita recorrente (MRR) e segmentação de mercado, respeitando as permissões e regras multiempresa do `core_base`.

## Dependências
- `base`: Núcleo do Odoo.
- `mail`: Mensageria e chatter.
- `crm`: Módulo nativo de CRM do Odoo Community.
- `core_base`: Módulo base do CORE ERP.

## Funcionalidades Adicionadas
- **Campo `mrr_estimate`**: Estimativa de Receita Recorrente Mensal para modelo SaaS.
- **Campo `business_segment`**: Classificação por segmento de negócio.
- **Permissões Integradas**: Atribuição automática de regras com base nos grupos do `core_base`.