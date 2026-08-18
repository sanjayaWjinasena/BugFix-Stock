# -*- coding: utf-8 -*-
"""Sentinel declaration for x_material_request so cross-references resolve."""
from odoo import fields, models


class XMaterialRequest(models.Model):
    _name = 'x_material_request'
    _description = 'X Material Request'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Request Reference')
    x_studio_done = fields.Boolean(string='Done')
    x_studio_done_stage_updated = fields.Boolean(string='Done Stage Updated')
    x_studio_journal_type = fields.Many2one('x_journal_types', string='Journal Type')
    x_studio_many2one_field_6f0Gc = fields.Many2one('hr.department', string='Department')
    x_studio_many2one_field_THFu6 = fields.Many2one('maintenance.request', string='Maintenance Request No')
    x_studio_many2one_field_W3qKf = fields.Many2one('stock.warehouse', string='Warehouse-1')
    x_studio_new = fields.Char(string='NEW')
    x_studio_notes = fields.Char(string='Notes')
    # TODO: x_studio_one2many_field_9DTZS = fields.One2many('x_mr_config', <inverse>, string='New One2many')
    # TODO: x_studio_request_lines = fields.One2many('x_mr_config', <inverse>, string='Request Lines')
    x_studio_requested_by = fields.Many2one('res.users', string='Requested by')
    x_studio_requested_date = fields.Date(string='Requested Date')
    x_studio_selection_field_BupKG = fields.Selection([], string='Status')
    x_studio_selection_field_X1Bue = fields.Selection([], string='Pipeline status bar')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_test = fields.Char(string='Test')
    x_studio_type = fields.Selection([], string='Type')
    x_studio_warehouse = fields.Many2one('stock.location', string='Warehouse')
    x_x_studio_created_from_material_request_no_stock_picking_count = fields.Integer(string='Created from Material Request No count')
    x_x_studio_material_request_ref__x_pr_non_inventory_count = fields.Integer(string='Material Request ref count')
    x_x_studio_material_request_ref__x_purchase_request_count = fields.Integer(string='Material Request ref count')
