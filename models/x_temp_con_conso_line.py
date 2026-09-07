# -*- coding: utf-8 -*-
"""Studio-ported custom model x_temp_con_conso_line."""
from odoo import fields, models


class XTempConConsoLine(models.Model):
    _name = 'x_temp_con_conso_line'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Temp Con. Conso. Line'

    x_name = fields.Char(string='Name')
    x_studio_consignment_id = fields.Many2one('x_consignment_header', string='Consignment Id')
    x_studio_container_no = fields.Char(string='Container No')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_custom_clearance_no = fields.Char(string='Custom Clearance No')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_select = fields.Boolean(string='Select')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_shipment_start_date = fields.Date(string='Shipment Start Date')
    x_studio_shipping_mode = fields.Selection([], string='Shipping Mode')
    x_studio_status = fields.Selection([], string='Status')
    x_studio_supplier_id = fields.Many2one('res.partner', string='Vendor')
    x_studio_supplier_invoice_no = fields.Char(string='Supplier Invoice No')
    x_studio_temp_consolidated_header_id = fields.Many2one('x_temp_con_consolidate', string='Temp Consolidated Header Id')

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   x_studio_delivery_term (many2one rel='x_delivery_terms' not safe)
