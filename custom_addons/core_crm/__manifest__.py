# -*- coding: utf-8 -*-
{
    'name': 'CORE ERP - CRM',
    'version': '17.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Gestão avançada de leads, oportunidades e funil de vendas para o CORE ERP SaaS.',
    'description': """
CORE ERP - Módulo CRM
=====================
Este módulo expande o CRM nativo do Odoo:
- Integração nativa com o módulo core_base e regras multiempresa.
- Personalização do ciclo de vida de leads e oportunidades.
- Extensão do modelo crm.lead para suporte a métricas de vendas SaaS.
    """,
    'author': 'CORE ERP Team',
    'website': 'https://github.com/wesleyroo66/core-erp',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
        'crm',
        'core_base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}