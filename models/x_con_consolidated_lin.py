# -*- coding: utf-8 -*-
"""Sentinel declaration for x_con_consolidated_lin."""
from odoo import fields, models


# NOTE (v0.0.118): the Many2one(s) x_studio_delivery_term were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.

class XConConsolidatedLin(models.Model):
    _name = 'x_con_consolidated_lin'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Con. Consolidated Line'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_consignment_id = fields.Many2one('x_consignment_header', string='Consignment Id')
    x_studio_consolidated_header_id = fields.Many2one('x_con_consolidated_hea', string='Consolidated Header Id', ondelete='restrict')
    x_studio_container_no = fields.Char(string='Container No')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_custom_clearance_no = fields.Char(string='Custom Clearance No')
    x_studio_invoice_date = fields.Date(string='Invoice Date')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_shipment_start_date = fields.Date(string='Shipment Start Date')
    x_studio_shipping_mode_1 = fields.Selection([('Air', 'Air'), ('Sea', 'Sea'), ('Road', 'Road'), ('Courier', 'Courier')], string='Shipping Mode')
    x_studio_status = fields.Selection([('Draft', 'Draft'), ('Consignment', 'Confirmed'), ('In Transit', 'In Transit'), ('Under Custom Clearance', 'Under Custom Clearance'), ('Done', 'Done'), ('TP Invoice', 'TP Invoice')], string='Status')
    x_studio_supplier_id = fields.Many2one('res.partner', string='Vendor')
    x_studio_supplier_invoice_no = fields.Char(string='Supplier Invoice No')
