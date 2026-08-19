# -*- coding: utf-8 -*-
"""Sentinel declaration for x_temp_consignment_lin."""
from odoo import fields, models


class XTempConsignmentLin(models.Model):
    _name = 'x_temp_consignment_lin'
    _description = 'X Temp Consignment Lin'

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one('res.currency', string='Currency')
    x_name = fields.Char(string='Name')
    x_studio_concessional_rate = fields.Boolean(string='Concessional Rate')
    x_studio_consignment_remainder = fields.Float(string='Consignment Remainder')
    x_studio_delivery_date = fields.Datetime(string='Delivery Date')
    x_studio_delivery_remainder = fields.Float(string='Delivery Remainder')
    x_studio_description = fields.Text(string='Description')
    x_studio_indent_no = fields.Char(string='Indent No')
    x_studio_payment_method = fields.Many2one('x_payment_methods', string='Payment Method')
    x_studio_product_id = fields.Many2one('product.product', string='Product')
    x_studio_purchase_id = fields.Many2one('purchase.order', string='Order Reference')
    x_studio_purchase_line_id = fields.Many2one('purchase.order.line', string='Purchase Line Id')
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_select = fields.Boolean(string='Select')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_structure_name = fields.Many2one('x_structure_master', string='Structure Name')
    x_studio_subtotal = fields.Float(string='Subtotal')  # was Monetary
    x_studio_supplier_id = fields.Many2one('res.partner', string='Vendor')
    x_studio_temp_consignment_header_id = fields.Many2one('x_temp_consignment_hea', string='Temp Consignment Header Id')
    x_studio_unit_price = fields.Float(string='Unit Price')
    x_studio_uom_id = fields.Many2one('uom.uom', string='UOM')
    x_studio_volume = fields.Float(string='Volume')
    x_studio_weight = fields.Float(string='Weight')
