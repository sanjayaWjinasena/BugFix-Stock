# -*- coding: utf-8 -*-
from odoo import models, fields

class StockLotGap(models.Model):
    _inherit = 'stock.lot'

    x_currency_id = fields.Many2one(string='Currency', related='product_id.stock_valuation_layer_ids.currency_id')
