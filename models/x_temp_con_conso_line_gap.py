# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempConConsoLineGap(models.Model):
    _inherit = 'x_temp_con_conso_line'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_delivery_term = fields.Many2one(comodel_name='x_delivery_terms', string='Delivery Term')
