# -*- coding: utf-8 -*-
from odoo import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def _prepare_opportunity_quotation_context(self):
        """
        Sobrescreve o método nativo do Odoo que prepara os dados ao clicar em
        'Nova Cotação' dentro de uma oportunidade do CRM, repassando o segmento.
        """
        quotation_context = super()._prepare_opportunity_quotation_context()
        if self.business_segment:
            quotation_context['default_business_segment'] = self.business_segment
        return quotation_context