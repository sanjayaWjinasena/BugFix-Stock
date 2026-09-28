# -*- coding: utf-8 -*-
"""Studio-owned field x_studio_available_qty on product.product.

Related=stock_quant_ids.available_quantity, store=False (per CDB).
Convenient computed display for available inventory quantity.
"""
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    x_studio_available_qty = fields.Float(
        related='stock_quant_ids.available_quantity',
        store=False,
        string='Available Qty',
    )
