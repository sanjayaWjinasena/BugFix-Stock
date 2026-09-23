# -*- coding: utf-8 -*-
"""x_mr_config declared in BugFix-Stock so x_material_request's O2M
inverse + notebook page arch validate at Stock load time.

x_mr_config is also declared in BugFix-Purchase with the same fields.
Odoo's _name-based class union merges the two declarations at
Purchase-load time. Field declarations MUST match between the two
modules (same ttype, same string, same store, same compute/related, etc.)
or Odoo logs a warning and the later declaration wins.

Load order at runtime:
  base -> stock -> BugFix-Stock (this file)
    -> purchase_stock -> purchase -> BugFix-Purchase (equivalent file)
"""
from odoo import api, fields, models


class XMrConfig(models.Model):
    _name = 'x_mr_config'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'MR config'
    _rec_name = 'x_name'
    _order = 'x_studio_sequence asc, id asc'

    x_active = fields.Boolean(string='Active', default=True, copy=True)
    x_currency_id = fields.Many2one('res.currency', string='Currency', ondelete='set null', copy=True)
    x_name = fields.Char(string='Name', copy=True)
    x_studio_available_qty_to_transfer = fields.Float(
        string='Available Qty. to Transfer', store=False,
        compute='_compute_available_qty_to_transfer', readonly=True)
    x_studio_description = fields.Html(
        string='Description', store=False,
        related='x_studio_product.description', readonly=True)
    x_studio_description_1 = fields.Char(
        string='Description', store=False,
        related='x_studio_product.name', readonly=True)
    x_studio_inventory_location = fields.Many2one(
        'stock.location', string='Inventory Location ', store=False,
        ondelete='set null',
        related='x_studio_many2one_field_02S0w.property_stock_inventory', readonly=True)
    x_studio_inventory_location_1 = fields.Many2one(
        'stock.location', string='Inventory Location ', store=False,
        ondelete='set null',
        related='x_studio_many2one_field_2LV9q.property_stock_inventory', readonly=True)
    x_studio_many2one_field_02S0w = fields.Many2one('product.product', string='Product-1', ondelete='set null', copy=True)
    x_studio_many2one_field_2LV9q = fields.Many2one('product.product', string='Product-2', ondelete='set null', copy=True)
    x_studio_many2one_field_6cvHX = fields.Many2one('maintenance.request', string='Maintenance Request', ondelete='set null', copy=True)
    x_studio_many2one_field_6yqbk = fields.Many2one(
        'x_material_request', string='Material Request',
        ondelete='set null', copy=True)
    x_studio_on_hand_qty = fields.Float(
        string='On Hand Qty', store=False,
        related='x_studio_many2one_field_02S0w.qty_available', readonly=True)
    x_studio_on_hand_qty_1 = fields.Float(
        string='On Hand Qty', store=False,
        related='x_studio_many2one_field_02S0w.qty_available', readonly=True)
    x_studio_on_hand_qty_2 = fields.Float(
        string='On Hand Qty', store=False,
        compute='_compute_on_hand_qty_2', readonly=True)
    x_studio_product = fields.Many2one('product.product', string='Product', ondelete='set null', copy=True)
    x_studio_qty = fields.Integer(string='Qty', copy=True)
    x_studio_qty_1 = fields.Integer(string='X Studio Qty 1', copy=True)
    x_studio_qty_to_transfer = fields.Float(string='Qty. to Transfer', copy=True)
    x_studio_qty_transfered = fields.Float(string='Qty. Transferred', copy=True)
    x_studio_quantity = fields.Float(string='Quantity', copy=True)
    x_studio_requested_by = fields.Many2one('res.users', string='Requested by', ondelete='set null', copy=True)
    x_studio_sequence = fields.Integer(string='Sequence', copy=True)
    x_studio_status = fields.Selection(
        [('Draft', 'Draft'), ('Confirmed', 'Confirmed'),
         ('To Be Approved', 'To Be Approved'), ('Approved', 'Approved'),
         ('Rejected', 'Rejected'), ('Done', 'Done')],
        string='Status',
        related='x_studio_many2one_field_6yqbk.x_studio_selection_field_BupKG',
        readonly=True)
    x_studio_text = fields.Char(string='Text', copy=True)
    x_studio_text_1 = fields.Char(string='Notes', copy=True)
    x_studio_transfer_remainder = fields.Float(
        string='Transfer Remainder', store=False,
        compute='_compute_transfer_remainder', readonly=True)
    x_studio_uom = fields.Many2one(
        'uom.uom', string='UoM', store=False, ondelete='set null',
        related='x_studio_many2one_field_02S0w.uom_id', readonly=True)
    x_studio_uom_1 = fields.Many2one(
        'uom.uom', string='UoM', store=False, ondelete='set null',
        related='x_studio_many2one_field_2LV9q.uom_id', readonly=True)
    x_studio_uom_1_1 = fields.Char(
        string='UOM-1', store=False,
        related='x_studio_product.uom_id.display_name', readonly=True)
    x_studio_uom_2 = fields.Char(
        string='UOM',
        related='x_studio_product.uom_id.name', readonly=True)
    x_studio_warehouse = fields.Many2one(
        'stock.location', string='Warehouse', ondelete='set null',
        related='x_studio_many2one_field_6yqbk.x_studio_warehouse', readonly=True)

    @api.depends('x_studio_quantity', 'x_studio_qty_transfered')
    def _compute_transfer_remainder(self):
        for rec in self:
            rec.x_studio_transfer_remainder = rec.x_studio_quantity - rec.x_studio_qty_transfered

    @api.depends('x_studio_quantity', 'x_studio_on_hand_qty_2', 'x_studio_qty_transfered')
    def _compute_available_qty_to_transfer(self):
        # Ported from CDB Studio compute - preserves the branch logic
        # despite unusual conditions.
        for rec in self:
            onhand_qty = 0
            if rec.x_studio_qty_transfered == 0:
                if rec.x_studio_quantity <= rec.x_studio_on_hand_qty_2:
                    onhand_qty = rec.x_studio_quantity
                else:
                    onhand_qty = rec.x_studio_on_hand_qty_2
            else:
                if (rec.x_studio_quantity - rec.x_studio_qty_transfered) <= rec.x_studio_on_hand_qty_2:
                    onhand_qty = (rec.x_studio_quantity - rec.x_studio_qty_transfered) - (rec.x_studio_quantity - rec.x_studio_on_hand_qty_2)
                else:
                    onhand_qty = rec.x_studio_on_hand_qty_2
            rec.x_studio_available_qty_to_transfer = onhand_qty

    @api.depends('x_studio_product', 'x_studio_warehouse')
    def _compute_on_hand_qty_2(self):
        # Ported from CDB Studio compute. Original code had a loop that
        # overwrote onhand_qty each iteration - preserved verbatim to
        # match CDB behavior. If x_studio_warehouse is unset, guards
        # against False comparison.
        SQ = self.env['stock.quant']
        for rec in self:
            onhand_qty = 0.0
            if rec.x_studio_product and rec.x_studio_warehouse:
                quants = SQ.search([
                    ('product_id', '=', rec.x_studio_product.id),
                    ('location_id', '=', rec.x_studio_warehouse.id),
                ])
                if quants:
                    onhand_qty = quants.available_quantity  # verbatim CDB - reads .available_quantity on the recordset
            rec.x_studio_on_hand_qty_2 = onhand_qty
