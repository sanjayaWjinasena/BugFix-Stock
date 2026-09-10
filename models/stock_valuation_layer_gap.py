# -*- coding: utf-8 -*-
from odoo import models, fields

class StockValuationLayerGap(models.Model):
    _inherit = 'stock.valuation.layer'

    x_studio_related_field_MfcOm = fields.Char(string='New Related Field', related='stock_move_id.location_dest_id.warehouse_id.code', readonly=True)
    x_studio_related_field_dGINH = fields.Many2one(string='New Related Field', related='stock_move_id.location_dest_id.warehouse_id', readonly=True)
