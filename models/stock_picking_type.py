# -*- coding: utf-8 -*-
from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    x_studio_mj_in = fields.Boolean(string='MJ IN')
    x_studio_mj_out = fields.Boolean(string='MJ OUT')
    x_studio_movement_journal = fields.Boolean(string='Movement Journal')
