# -*- coding: utf-8 -*-
"""v17.0.0.0.134: stock.picking.x_studio_custom_clearance_no is again a stored related field of the
consignment (related='x_studio_consignment_no.x_studio_custom_clearance_no', as on Clear-DB/KG; bug
sheet Imports row 28). The column already existed as a plain char that nobody filled, and Odoo does not
backfill an existing column for a field that becomes computed, so recompute it for existing transfers.
ORM only. (PR Type on receipts is restored by BugFix-Purchase 17.0.1.0.209, models/stock_pr_type.py.)
"""
from odoo import api, SUPERUSER_ID

FIELDS = ('x_studio_custom_clearance_no',)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {'active_test': False})
    pickings = env['stock.picking'].search([('x_studio_consignment_no', '!=', False)])
    for name in FIELDS:
        env.add_to_compute(pickings._fields[name], pickings)
    pickings.flush_model(list(FIELDS))
