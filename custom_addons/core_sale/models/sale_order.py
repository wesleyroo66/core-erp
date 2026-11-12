# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_saas_subscription = fields.Boolean(
        string='Assinatura SaaS',
        default=True,
        help='Indica se este pedido refere-se a um contrato de assinatura recorrente.',
    )

    billing_cycle = fields.Selection(
        selection=[
            ('monthly', 'Mensal'),
            ('quarterly', 'Trimestral'),
            ('yearly', 'Anual'),
        ],
        string='Ciclo de Faturamento',
        default='monthly',
        help='Periodicidade de cobrança da assinatura.',
    )

    business_segment = fields.Selection(
        selection=[
            ('retail', 'Varejo / Comércio'),
            ('services', 'Prestação de Serviços'),
            ('industry', 'Indústria / Manufatura'),
            ('other', 'Outros'),
        ],
        string='Segmento do Cliente',
        help='Segmento de mercado herdado do CRM ou definido na venda.',
    )