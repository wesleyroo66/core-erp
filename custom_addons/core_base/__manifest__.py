# -*- coding: utf-8 -*-
{
    'name': 'CORE ERP - Módulo Base',
    'version': '17.0.1.0.0',
    'category': 'Core/Enterprise',
    'summary': 'Módulo base de arquitetura, segurança e multiempresa para o CORE ERP SaaS.',
    'description': """
CORE ERP - Módulo Base
======================
Este módulo estabelece a fundação do CORE ERP:
- Estrutura base de dados e preferências.
- Regras de segurança centralizadas e controle de acesso (ACLs).
- Isolamento rigoroso de dados multiempresa (Multi-tenancy).
    """,
    'author': 'CORE ERP Team',
    'website': 'https://github.com/wesleyroo66/core-erp',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/core_base_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}