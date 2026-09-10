# -*- coding: utf-8 -*-
from odoo import models, fields

class XTariffmasterGap(models.Model):
    _inherit = 'x_tariffmaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    # STRIPPED x_studio_tariff_master_ids: O2M inverse lives in another repo (load-order risk)