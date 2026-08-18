# -*- coding: utf-8 -*-
from odoo import fields, models


class StockLocation(models.Model):
    _inherit = 'stock.location'

    x_color = fields.Integer(string='Color')
    x_studio_finished_good_location = fields.Boolean(string='Finished Good Location')
    x_studio_many2many_field_7kpUe = fields.Many2many('res.users', 'stock_location_x_studio_many2many_field_7kpUe_rel', 'stock_id', 'res_users_id', string='Users (Cell Visibility)')
    x_studio_repair_factory_location = fields.Boolean(string='Repair Factory Location')
    x_studio_repair_return_location = fields.Boolean(string='Repair Return Location')
    x_studio_return_receipt_location = fields.Many2one('stock.location', string='Return Receipt Location')
    x_studio_return_sequence = fields.Many2one('ir.sequence', string='Return Sequence')
    x_studio_temp_location = fields.Boolean(string='Temp Location')
    x_studio_users_internal_transfer = fields.Many2many('res.users', 'stock_location_x_studio_users_internal_transfer_rel', 'stock_id', 'res_users_id', string='Users (Internal Transfer)')
    x_studio_users_stock_location = fields.Many2many('res.users', 'stock_location_x_studio_users_stock_location_rel', 'stock_id', 'res_users_id', string='Users (Stock Location)')