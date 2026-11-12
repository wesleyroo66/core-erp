# -*- coding: utf-8 -*-
{
    'name': 'CORE ERP - Vendas',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Gestão de cotações, pedidos de venda e contratos SaaS no CORE ERP.',
    'description': """
CORE ERP - Módulo de Vendas
===========================
Este módulo expande o fluxo de vendas do Odoo:
- Integração com core_base (multiempresa) e core_crm (leads/oportunidades).
- Suporte a faturamento recorrente e ciclo de assinatura (Mensal/Anual).
- Transferência automática de dados do CRM para a Cotação.
    """,
    'author': 'CORE ERP Team',
    'website': 'https://github.com/wesleyroo66/core-erp',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'sale_management',
        'core_base',
        'core_crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}