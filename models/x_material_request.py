# -*- coding: utf-8 -*-
"""Sentinel declaration for x_material_request so cross-references resolve."""
from odoo import api, fields, models


class XMaterialRequest(models.Model):
    _name = 'x_material_request'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'X Material Request'

    x_active = fields.Boolean(string='Active', default=True)
    x_name = fields.Char(string='Request Reference')
    x_studio_done = fields.Boolean(
        string='Done',
        compute='_compute_done', store=True, readonly=True)
    x_studio_done_stage_updated = fields.Boolean(string='Done Stage Updated')
    x_studio_journal_type = fields.Many2one('x_journal_types', string='Journal Type')
    x_studio_many2one_field_6f0Gc = fields.Many2one('hr.department', string='Department')
    x_studio_many2one_field_THFu6 = fields.Many2one('maintenance.request', string='Maintenance Request No')
    x_studio_many2one_field_W3qKf = fields.Many2one('stock.warehouse', string='Warehouse-1')
    x_studio_new = fields.Char(string='NEW')
    x_studio_notes = fields.Char(string='Notes')
    # Both O2Ms share the same inverse x_studio_many2one_field_6yqbk on
    # x_mr_config — Studio-created redundancy preserved for CDB fidelity.
    x_studio_one2many_field_9DTZS = fields.One2many(
        'x_mr_config', 'x_studio_many2one_field_6yqbk',
        string='New One2many')
    x_studio_request_lines = fields.One2many(
        'x_mr_config', 'x_studio_many2one_field_6yqbk',
        string='Request Lines')
    x_studio_requested_by = fields.Many2one('res.users', string='Requested by')
    x_studio_requested_date = fields.Date(string='Requested Date')
    x_studio_selection_field_BupKG = fields.Selection([], string='Status')
    x_studio_selection_field_X1Bue = fields.Selection([], string='Pipeline status bar')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_test = fields.Char(string='Test')
    x_studio_type = fields.Selection([], string='Type')
    x_studio_warehouse = fields.Many2one('stock.location', string='Warehouse')
    x_x_studio_created_from_material_request_no_stock_picking_count = fields.Integer(
        string='Created from Material Request No count',
        compute='_compute_related_stock_picking_count', store=False)
    x_x_studio_material_request_ref__x_pr_non_inventory_count = fields.Integer(
        string='Material Request ref count',
        compute='_compute_related_x_pr_non_inventory_count', store=False)
    x_x_studio_material_request_ref__x_purchase_request_count = fields.Integer(
        string='Material Request ref count',
        compute='_compute_related_x_purchase_request_count', store=False)

    @api.depends('x_studio_done_stage_updated', 'x_studio_request_lines',
                 'x_studio_request_lines.x_studio_transfer_remainder')
    def _compute_done(self):
        # Ported from CDB Studio compute. Side-effects (writing status +
        # done_stage_updated) preserved verbatim — original Studio behavior
        # advances status to 'Done' when all deliveries complete and no
        # transfer remainder is left.
        SP = self.env['stock.picking']
        for rec in self:
            task_status = False
            if not rec.id:
                rec.x_studio_done = False
                continue
            delivery = SP.search(
                [('x_studio_created_from_material_request_no', '=', rec.id)], limit=1)
            if delivery:
                open_delivery = SP.search([
                    ('x_studio_created_from_material_request_no', '=', rec.id),
                    ('state', 'not in', ['done', 'cancel']),
                ], limit=1)
                task_status = not open_delivery
            for line in rec.x_studio_request_lines:
                if line.x_studio_transfer_remainder > 0:
                    task_status = False
                    break
            if task_status and not rec.x_studio_done_stage_updated:
                rec.x_studio_selection_field_BupKG = 'Done'
                rec.x_studio_done_stage_updated = True
            rec.x_studio_done = task_status

    def _compute_related_stock_picking_count(self):
        SP = self.env['stock.picking']
        has_field = 'x_studio_created_from_material_request_no' in SP._fields
        for rec in self:
            if has_field:
                rec.x_x_studio_created_from_material_request_no_stock_picking_count = \
                    SP.search_count([('x_studio_created_from_material_request_no', '=', rec.id)])
            else:
                rec.x_x_studio_created_from_material_request_no_stock_picking_count = 0

    def _compute_related_x_pr_non_inventory_count(self):
        for rec in self:
            rec.x_x_studio_material_request_ref__x_pr_non_inventory_count = self.env[
                'x_pr_non_inventory'].search_count([('x_studio_material_request_ref', '=', rec.id)])

    def _compute_related_x_purchase_request_count(self):
        for rec in self:
            rec.x_x_studio_material_request_ref__x_purchase_request_count = self.env[
                'x_purchase_request'].search_count([('x_studio_material_request_ref', '=', rec.id)])
