# -*- coding: utf-8 -*-
from odoo import models, fields

class StockLocationGap(models.Model):
    _inherit = 'stock.location'

    x_color = fields.Integer(string='Color')
