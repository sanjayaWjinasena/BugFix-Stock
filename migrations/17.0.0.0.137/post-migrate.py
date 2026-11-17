"""Uninstall stock_picking_batch on databases installed before 17.0.0.0.137.

The 17.0.0.0.114 migration removed Batch / Wave Transfers (not on Clear-DB, and with
bi_warehouse_restrictions installed it breaks the Inventory overview: "Compute method failed
to assign ... count_picking_batch"), but only on databases upgraded past 114. A fresh install
at a later version kept it. post_init_hook now removes it on install; this does the same for
databases installed before, e.g. the new-install env. Same code as hooks.remove_batch_transfers.
"""

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    module = env["ir.module.module"].sudo().search(
        [("name", "=", "stock_picking_batch"), ("state", "=", "installed")], limit=1
    )
    if not module:
        return
    dependents = module.downstream_dependencies().mapped("name")
    module.button_uninstall()
    _logger.info(
        "[BugFix-Stock 137] stock_picking_batch marked for removal (with %s), as on Clear-DB",
        ", ".join(dependents) or "no add-ons",
    )
