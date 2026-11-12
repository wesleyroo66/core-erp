# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # Exemplo de campo customizado voltado para ERP SaaS
    mrr_estimate = fields.Monetary(
        string='MRR Estimado',
        currency_field='company_currency',
        help='Receita Recorrente Mensal (MRR) estimada para este lead/oportunidade.',
    )
    
    business_segment = fields.Selection(
        selection=[
            ('retail', 'Varejo / Comércio'),
            ('services', 'Prestação de Serviços'),
            ('industry', 'Indústria / Manufatura'),
            ('other', 'Outros'),
        ],
        string='Segmento de Atuação',
        default='services',
        help='Segmento de mercado da empresa prospectada.',
    )