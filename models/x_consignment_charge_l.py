# -*- coding: utf-8 -*-
"""Sentinel declaration for x_consignment_charge_l."""
from odoo import fields, models


class XConsignmentChargeL(models.Model):
    _name = 'x_consignment_charge_l'
    _description = 'X Consignment Charge L'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_amount = fields.Float(string='Amount')
    x_studio_basis = fields.Selection([], string='Basis')
    x_studio_charge_group = fields.Selection([], string='Charge Group')
    x_studio_charge_name = fields.Char(string='Charge Name')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_consignment_charge_header_id = fields.Many2one('x_consignment_charge_h', string='Consignment Charge Header Id')
    x_studio_consignment_id = fields.Many2one('x_consignment_header', string='Consignment Id')
    x_studio_formula = fields.Char(string='Formula')
    x_studio_indent_id = fields.Char(string='Indent_ID')
    x_studio_percent = fields.Float(string='Percent')
    x_studio_product = fields.Many2one('product.product', string='Product')
    x_studio_quantity = fields.Float(string='Quantity')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_structure_details_line_ids = fields.Many2one('x_structure_details', string='Structure Details Line Ids')
    x_studio_structure_master_id = fields.Many2one('x_structure_master', string='Structure Master Id')
    x_studio_structure_no = fields.Integer(string='Structure No')
    x_studio_unit_price = fields.Float(string='Unit Price')
