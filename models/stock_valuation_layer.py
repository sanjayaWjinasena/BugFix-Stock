# -*- coding: utf-8 -*-
from odoo import fields, models


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    x_studio_related_field_MfcOm = fields.Char(string='New Related Field', readonly=True)
    x_studio_related_field_bPlxa = fields.Many2one('stock.location', string='From', readonly=True)
    x_studio_related_field_dGINH = fields.Many2one('stock.warehouse', string='New Related Field', readonly=True, store=False)
    x_studio_related_field_ygmmJ = fields.Many2one('stock.location', string='To', readonly=True)
