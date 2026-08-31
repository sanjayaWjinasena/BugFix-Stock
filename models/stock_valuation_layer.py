# -*- coding: utf-8 -*-
"""Related-field navigation on stock.valuation.layer.

Ports 2 x_studio_related_field_* M2Os that view 2585 (Studio inherit
on stock.valuation.layer tree) references. Both are simple related-
computed fields traversing stock_move_id -> stock.move.location_*
and pinned to stock_account on Clear-DB.

Previously deleted in v0.0.12 CRITICAL revert because stock_account
was not installed on dev at that time. As of 2026-08-31 stock_account
IS installed on repair-test-101 (module id 1008) and is transitively
pulled by our existing stock_landed_costs dep. Re-adding with the
correct Clear-DB spec (v0.0.12 had them without the `related=`
attribute, which would have left them as empty columns).

Only 2 of the 4 fields from the deleted file are re-added here -
x_studio_related_field_MfcOm (Char) and x_studio_related_field_dGINH
(M2O stock.warehouse, store=False) are not referenced by any view
currently being ported.
"""
from odoo import fields, models


class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'

    x_studio_related_field_bPlxa = fields.Many2one(
        'stock.location',
        related='stock_move_id.location_id',
        string='From',
        readonly=True,
        store=True,
    )
    x_studio_related_field_ygmmJ = fields.Many2one(
        'stock.location',
        related='stock_move_id.location_dest_id',
        string='To',
        readonly=True,
        store=True,
    )
