# -*- coding: utf-8 -*-
from odoo import fields, models


class StockLot(models.Model):
    _inherit = 'stock.lot'

    x_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_cost = fields.Float(string='Cost', readonly=True)
    x_studio_no_of_days = fields.Char(string='No of Days', readonly=True, store=False)
    x_studio_no_of_days_2 = fields.Integer(string='No of Days 2', readonly=True)
    x_studio_price_1 = fields.Char(string='Price 1', readonly=True, store=False)
    x_studio_price_2 = fields.Char(string='Price 2', readonly=True, store=False)
    x_studio_production_id = fields.Many2one('mrp.production', string='Production Order')
    x_studio_production_order = fields.Char(string='Production Order')
    x_studio_related_field_IlrRW = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_KzAMe = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_Vz7B8 = fields.Char(string='New Related Field', readonly=True)
    x_studio_related_field_bz0VM = fields.Boolean(string='New Related Field', readonly=True)
    x_studio_related_field_e2LSH = fields.Integer(string='New Related Field', readonly=True)
    x_studio_related_field_fTaKf = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_related_field_jS93T = fields.Integer(string='New Related Field', readonly=True)
    x_studio_related_field_vTORT = fields.Char(string='New Related Field', readonly=True, store=False)
    x_studio_sequence_size = fields.Integer(string='Sequence Size')
    x_studio_serial_no_prefix = fields.Char(string='Serial No Prefix')
    x_studio_starting_serial_no = fields.Integer(string='Starting Serial No')
    x_studio_warehouse = fields.Char(string='Warehouse', readonly=True)
