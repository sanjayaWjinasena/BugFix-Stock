# -*- coding: utf-8 -*-
"""v17.0.0.0.128: stock.picking.x_studio_sequence_code is again a stored related field of the
operation type (related='picking_type_id.sequence_code', as on Clear-DB). The column already existed
as a plain char that nobody filled, and Odoo does not backfill an existing column for a field that
becomes computed, so recompute it for existing transfers. ORM only.
"""
from odoo import api, SUPERUSER_ID

FIELDS = ('x_studio_sequence_code',)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {'active_test': False})
    pickings = env['stock.picking'].search([])
    for name in FIELDS:
        env.add_to_compute(pickings._fields[name], pickings)
    pickings.flush_model(list(FIELDS))
