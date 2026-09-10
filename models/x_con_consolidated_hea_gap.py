# -*- coding: utf-8 -*-
from odoo import models, fields

class XConConsolidatedHeaGap(models.Model):
    _inherit = 'x_con_consolidated_hea'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Con. Reference')
