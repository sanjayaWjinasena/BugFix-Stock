# -*- coding: utf-8 -*-
from odoo import models, fields

class XConConsolidatedLinGap(models.Model):
    _inherit = 'x_con_consolidated_lin'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
