# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempConConsolidateGap(models.Model):
    _inherit = 'x_temp_con_consolidate'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_con_lines = fields.One2many(comodel_name='x_temp_con_conso_line', inverse_name='x_studio_temp_consolidated_header_id', string='Con. Lines')
