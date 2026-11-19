# -*- coding: utf-8 -*-
from odoo import api, fields, models


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    x_studio_mj_in = fields.Boolean(string='MJ IN')
    x_studio_mj_out = fields.Boolean(string='MJ OUT')
    x_studio_movement_journal = fields.Boolean(string='Movement Journal')

    # Inventory > Overview card: show the dropdown menu only on operation types where it is wanted.
    # Pre-filled from the type itself (internal transfers and Movement Journal IN/OUT types) and
    # editable per operation type, so no names or record ids are hard-coded.
    jin_show_overview_menu = fields.Boolean(
        string='Show menu on Overview card',
        compute='_compute_jin_show_overview_menu', store=True, readonly=False,
        help="Show the dropdown menu on this operation type's card in Inventory > Overview.")

    @api.depends('code', 'x_studio_mj_in', 'x_studio_mj_out', 'x_studio_movement_journal')
    def _compute_jin_show_overview_menu(self):
        for picking_type in self:
            picking_type.jin_show_overview_menu = (
                picking_type.code == 'internal'
                or picking_type.x_studio_movement_journal
                or picking_type.x_studio_mj_in
                or picking_type.x_studio_mj_out
            )
