# -*- coding: utf-8 -*-
"""v17.0.0.0.114: mark stock_picking_batch (+ auto_install dependents) for uninstall.

CDB (our known-good reference) has stock_picking_batch and its 3 auto_install=True
dependents (delivery_stock_picking_batch, quality_control_picking_batch,
stock_barcode_picking_batch) uninstalled — latest_version=False on all four,
meaning they were never installed on CDB. The stock.picking.batch model does
not exist in CDB's ir.model.

On target (fresh-install env) they got installed somehow, and the override of
stock.picking.type._compute_picking_count added by stock_picking_batch fails
with "Compute method failed to assign count_picking_batch" — breaks the whole
Inventory → Operation Types list view.

This migration marks stock_picking_batch for uninstall via button_uninstall(),
which sets state='to remove' on both the module and its downstream dependents
(the 3 auto_install=True helpers). Odoo processes the removal in the current
or next registry build. 0 stock.picking.batch records on target => no data loss.

Uses ORM only, no cr.execute.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

TARGET = 'stock_picking_batch'


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Module = env['ir.module.module'].sudo()
    target = Module.search(
        [('name', '=', TARGET), ('state', '=', 'installed')],
        limit=1,
    )
    if not target:
        _logger.info(
            '[BugFix-Stock v114] %s not installed; nothing to do.', TARGET
        )
        return
    # button_uninstall sets state='to remove' on target + its downstream
    # dependents (cascades automatically). Does not trigger a registry
    # rebuild here (that would recurse inside the current upgrade cycle);
    # Odoo processes 'to remove' modules on the next registry build.
    try:
        downstream_names = target.downstream_dependencies().mapped('name')
        target.button_uninstall()
        _logger.info(
            '[BugFix-Stock v114] marked %s + %d downstream dep(s) for uninstall: %s. '
            'Odoo will complete the removal on the next registry build. '
            'If the Operation Types list still errors after this upgrade, '
            're-run the upgrade once more to flush the queued uninstall.',
            TARGET, len(downstream_names), downstream_names,
        )
    except Exception as e:
        _logger.warning(
            '[BugFix-Stock v114] button_uninstall(%s) failed: %s. '
            'Manual uninstall via Apps may be needed.',
            TARGET, e,
        )
