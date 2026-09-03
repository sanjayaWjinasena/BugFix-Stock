# -*- coding: utf-8 -*-
"""Sentinel declaration for x_con_consolidated_lin."""
from odoo import fields, models


class XConConsolidatedLin(models.Model):
    _name = 'x_con_consolidated_lin'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'X Con Consolidated Lin'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_consignment_id = fields.Many2one('x_consignment_header', string='Consignment Id')
    x_studio_consolidated_header_id = fields.Many2one('x_con_consolidated_hea', string='Consolidated Header Id')
    x_studio_container_no = fields.Char(string='Container No')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_custom_clearance_no = fields.Char(string='Custom Clearance No')
    x_studio_delivery_term = fields.Many2one('x_delivery_terms', string='Delivery Term')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_shipment_start_date = fields.Date(string='Shipment Start Date')
    x_studio_shipping_mode_1 = fields.Selection([], string='Shipping Mode')
    x_studio_status = fields.Selection([], string='Status')
    x_studio_supplier_id = fields.Many2one('res.partner', string='Vendor')
    x_studio_supplier_invoice_no = fields.Char(string='Supplier Invoice No')
