"""v17.0.0.0.125: movement_journal / mj_in / mj_out on stock.picking are now
stored related fields of the operation type (as on Clear-DB). The columns already existed (plain booleans,
always False), and Odoo does not backfill an existing column for a field that becomes computed, so
recompute them for existing transfers. ORM only.
"""

from odoo import SUPERUSER_ID, api

FIELDS = ("movement_journal", "mj_in", "mj_out")


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {"active_test": False})
    pickings = env["stock.picking"].search([])
    for name in FIELDS:
        env.add_to_compute(pickings._fields[name], pickings)
    pickings.flush_model(list(FIELDS))
