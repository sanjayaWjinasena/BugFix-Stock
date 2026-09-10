# -*- coding: utf-8 -*-
from odoo import models, fields

class XTariffmasterGap(models.Model):
    _inherit = 'x_tariffmaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    x_studio_tariff_master_ids = fields.One2many(comodel_name='x_tariff_date', inverse_name='x_studio_tariff_master_ids', string='Date Range')
