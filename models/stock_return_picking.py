# -*- coding: utf-8 -*-
from odoo import fields, models


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    x_studio_repair_normal_with_serial_no = fields.Boolean(string='Repair Normal With Serial No', readonly=True, store=False)
    x_studio_repair_normal_without_serial_no = fields.Boolean(string='Repair Normal Without Serial No', readonly=True)
    x_studio_repair_rug = fields.Boolean(string='Repair RUG', readonly=True, store=False)
    x_studio_suggested_location_id = fields.Many2one('stock.location', string='Suggested Return Location', readonly=True)
    x_studio_suggested_location_id_1 = fields.Many2one('stock.location', string='Suggested Return Location', readonly=True)
