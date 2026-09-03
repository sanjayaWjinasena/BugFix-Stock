# -*- coding: utf-8 -*-
"""Sentinel declaration for x_temp_consignment_hea."""
from odoo import fields, models


class XTempConsignmentHea(models.Model):
    _name = 'x_temp_consignment_hea'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'X Temp Consignment Hea'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_select_all = fields.Boolean(string='Select All')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_temp_consignment_header_id = fields.Many2one('x_consignment_header', string='Temp Consignment Header Id')
    x_studio_temp_consignment_line_ids = fields.One2many(
        'x_temp_consignment_lin',
        'x_studio_temp_consignment_header_id',
        string='Temp Consignment Line Ids',
    )
