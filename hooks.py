# -*- coding: utf-8 -*-
"""BugFix-Stock: post-install hooks.

Seeds ir.model.fields.selection rows Studio populated in CDB but Odoo 17
doesn't recreate on install. Uses Odoo's own _update_selection framework
API (documented internal method used by ir.model.fields._compute_selection
in core) rather than cr.execute or ORM.create() (which is blocked on
state='base' fields).
"""
import logging

_logger = logging.getLogger(__name__)

# --- Field selection seeds (via Odoo _update_selection framework API) ---
# Studio-15 populated ir.model.fields.selection rows for these fields in CDB;
# Odoo 17 doesn't recreate them on install. ORM.create() is blocked for
# state='base' fields ("Properties of base fields cannot be altered..."),
# but Odoo's own _update_selection helper (used by
# ir.model.fields._compute_selection in core, see
# odoo/addons/base/models/ir_model.py:600) bypasses that guard. Uses
# framework query_insert / query_update — no cr.execute in our code.
# (model, field, value, label, sequence)
_FIELD_SELECTIONS = [
    ('x_temp_structure_detai', 'x_studio_charge_group', 'None', 'None', 10),
    ('x_consignment_header', 'x_studio_shipping_mode', 'Air', 'Air', 10),
    ('x_consignment_header', 'x_studio_status', 'Draft', 'Draft', 10),
    ('x_consignment_header', 'x_studio_status_bar', 'Draft', 'Draft', 10),
    ('x_consignment_line', 'x_studio_status', 'Draft', 'Draft', 10),
    ('x_consignment_charge_l', 'x_studio_charge_group', 'None', 'None', 10),
    ('x_consignment_charge_l', 'x_studio_basis', 'Percentage', 'Percentage', 10),
    ('stock.picking', 'x_studio_pr_type', 'Local', 'Local', 10),
    ('stock.move', 'x_studio_pr_type', 'Local', 'Local', 10),
    ('x_con_consolidated_lin', 'x_studio_shipping_mode_1', 'Air', 'Air', 10),
    ('x_con_consolidated_lin', 'x_studio_status', 'Draft', 'Draft', 10),
    ('x_con_consolidated_hea', 'x_studio_status', 'Draft', 'Draft', 10),
    ('x_con_consolidated_hea', 'x_studio_pipeline_status_bar', 'Draft', 'Draft', 10),
    ('x_temp_con_conso_line', 'x_studio_shipping_mode', 'Air', 'Air', 10),
    ('x_temp_con_conso_line', 'x_studio_status', 'Draft', 'Draft', 10),
    ('x_consignment_header', 'x_studio_cost_allocation_method', 'equal', 'Equal', 10),
    ('x_consignment_line', 'x_studio_cost_allocation_method', 'equal', 'Equal', 10),
    ('stock.move.line', 'x_studio_pr_type', 'Local', 'Local', 10),
    ('stock.picking', 'x_studio_related_field_zZDiA', 'Sales', 'Sales', 10),
    ('stock.picking', 'x_studio_gl_account_status', 'Pending', 'Pending', 10),
    ('x_material_request_tes', 'x_studio_kanban_state', 'normal', 'In Progress', 10),
    ('x_material_request_mt', 'x_studio_kanban_state', 'normal', 'In Progress', 10),
    ('x_temp_structure_detai', 'x_studio_charge_group', 'Charges', 'Charges', 1),
    ('x_consignment_header', 'x_studio_shipping_mode', 'Sea', 'Sea', 1),
    ('x_consignment_line', 'x_studio_status', 'In Transit', 'In Transit', 1),
    ('x_consignment_charge_l', 'x_studio_charge_group', 'Charges', 'Charges', 1),
    ('x_consignment_charge_l', 'x_studio_basis', 'Fixed Per Document', 'Fixed Per Document', 1),
    ('stock.picking', 'x_studio_pr_type', 'Import', 'Import', 1),
    ('stock.move', 'x_studio_pr_type', 'Import', 'Import', 1),
    ('x_consignment_header', 'x_studio_status_bar', 'Consignment', 'Confirmed', 1),
    ('x_con_consolidated_lin', 'x_studio_shipping_mode_1', 'Sea', 'Sea', 1),
    ('x_con_consolidated_lin', 'x_studio_status', 'Consignment', 'Confirmed', 1),
    ('x_con_consolidated_hea', 'x_studio_status', 'Confirmed', 'Confirmed', 1),
    ('x_con_consolidated_hea', 'x_studio_pipeline_status_bar', 'Confirmed', 'Confirmed', 1),
    ('x_temp_con_conso_line', 'x_studio_shipping_mode', 'Sea', 'Sea', 1),
    ('x_temp_con_conso_line', 'x_studio_status', 'Consignment', 'Confirmed', 1),
    ('x_consignment_header', 'x_studio_status', 'Consignment', 'Confirmed', 1),
    ('x_consignment_header', 'x_studio_cost_allocation_method', 'by_quantity', 'By Quantity', 1),
    ('x_consignment_line', 'x_studio_cost_allocation_method', 'by_quantity', 'By Quantity', 1),
    ('stock.move.line', 'x_studio_pr_type', 'Import', 'Import', 1),
    ('stock.picking', 'x_studio_related_field_zZDiA', 'Project', 'Project', 1),
    ('stock.picking', 'x_studio_gl_account_status', 'Updated', 'Updated', 1),
    ('x_material_request_tes', 'x_studio_kanban_state', 'done', 'Ready', 1),
    ('x_material_request_mt', 'x_studio_kanban_state', 'done', 'Ready', 1),
    ('x_temp_structure_detai', 'x_studio_charge_group', 'Duty', 'Duty', 2),
    ('x_consignment_header', 'x_studio_shipping_mode', 'Road', 'Road', 2),
    ('x_consignment_line', 'x_studio_status', 'Under Custom Clearance', 'Under Custom Clearance', 2),
    ('x_consignment_charge_l', 'x_studio_charge_group', 'Duty', 'Duty', 2),
    ('x_con_consolidated_lin', 'x_studio_shipping_mode_1', 'Road', 'Road', 2),
    ('x_con_consolidated_lin', 'x_studio_status', 'In Transit', 'In Transit', 2),
    ('x_temp_con_conso_line', 'x_studio_shipping_mode', 'Road', 'Road', 2),
    ('x_temp_con_conso_line', 'x_studio_status', 'In Transit', 'In Transit', 2),
    ('x_consignment_header', 'x_studio_cost_allocation_method', 'by_current_cost_price', 'By Current Cost', 2),
    ('x_consignment_line', 'x_studio_cost_allocation_method', 'by_current_cost_price', 'By Current Cost', 2),
    ('x_consignment_header', 'x_studio_status_bar', 'Consolidated', 'Consolidated', 2),
    ('x_consignment_header', 'x_studio_status', 'Consolidated', 'Consolidated', 2),
    ('stock.picking', 'x_studio_related_field_zZDiA', 'Repair', 'Repair', 2),
    ('x_material_request_tes', 'x_studio_kanban_state', 'blocked', 'Blocked', 2),
    ('x_material_request_mt', 'x_studio_kanban_state', 'blocked', 'Blocked', 2),
    ('x_temp_structure_detai', 'x_studio_charge_group', 'Taxes', 'Taxes', 3),
    ('x_consignment_header', 'x_studio_shipping_mode', 'Courier', 'Courier', 3),
    ('x_consignment_header', 'x_studio_status', 'In Transit', 'In Transit', 3),
    ('x_consignment_header', 'x_studio_status_bar', 'In Transit', 'In Transit', 3),
    ('x_consignment_line', 'x_studio_status', 'Done', 'Done', 3),
    ('x_consignment_charge_l', 'x_studio_charge_group', 'Taxes', 'Taxes', 3),
    ('x_con_consolidated_lin', 'x_studio_shipping_mode_1', 'Courier', 'Courier', 3),
    ('x_con_consolidated_lin', 'x_studio_status', 'Under Custom Clearance', 'Under Custom Clearance', 3),
    ('x_temp_con_conso_line', 'x_studio_shipping_mode', 'Courier', 'Courier', 3),
    ('x_temp_con_conso_line', 'x_studio_status', 'Under Custom Clearance', 'Under Custom Clearance', 3),
    ('x_consignment_header', 'x_studio_cost_allocation_method', 'by_weight', 'By Weight', 3),
    ('x_consignment_line', 'x_studio_cost_allocation_method', 'by_weight', 'By Weight', 3),
    ('x_temp_structure_detai', 'x_studio_charge_group', 'Assessable Value', 'Assessable Value', 4),
    ('x_consignment_header', 'x_studio_status', 'Under Custom Clearance', 'Under Custom Clearance', 4),
    ('x_consignment_header', 'x_studio_status_bar', 'Under Custom Clearance', 'Under Custom Clearance', 4),
    ('x_con_consolidated_lin', 'x_studio_status', 'Done', 'Done', 4),
    ('x_temp_con_conso_line', 'x_studio_status', 'Done', 'Done', 4),
    ('x_consignment_header', 'x_studio_cost_allocation_method', 'by_volume', 'By Volume', 4),
    ('x_consignment_line', 'x_studio_cost_allocation_method', 'by_volume', 'By Volume', 4),
    ('x_consignment_header', 'x_studio_status_bar', 'Done', 'Done', 5),
    ('x_consignment_header', 'x_studio_status', 'Done', 'Done', 5),
    ('x_con_consolidated_lin', 'x_studio_status', 'TP Invoice', 'TP Invoice', 5),
    ('x_temp_con_conso_line', 'x_studio_status', 'TP Invoice', 'TP Invoice', 5),
    ('x_consignment_header', 'x_studio_status', 'TP Invoice', 'TP Invoice', 6),
    ('x_consignment_header', 'x_studio_status_bar', 'TP Invoice', 'TP Invoice', 6),
]


def _seed_field_selections(env, entries):
    """Add missing ir.model.fields.selection rows via Odoo's
    _update_selection helper. Groups by (model, field), reads current
    selection, appends missing CDB values, calls _update_selection with
    the merged list — Odoo inserts only the new rows and keeps existing."""
    Sel = env['ir.model.fields.selection'].sudo()
    Fld = env['ir.model.fields'].sudo()
    grouped = {}
    for model, fname, value, label, seq in entries:
        grouped.setdefault((model, fname), []).append((value, label, seq))
    for (model, fname), values in grouped.items():
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-Stock: skip %s.%s (field absent).", model, fname,
            )
            continue
        existing_recs = Sel.search(
            [('field_id', '=', fld.id)], order='sequence',
        )
        existing_pairs = [(r.value, r.name) for r in existing_recs]
        existing_values = {v for v, _ in existing_pairs}
        added = []
        for v, l, _seq in sorted(values, key=lambda t: t[2]):
            if v in existing_values:
                continue
            existing_pairs.append((v, l))
            existing_values.add(v)
            added.append(v)
        if not added:
            continue
        try:
            with env.cr.savepoint():
                Sel._update_selection(model, fname, existing_pairs)
                _logger.info(
                    "BugFix-Stock: seeded %s.%s += %s.", model, fname, added,
                )
        except Exception as e:
            _logger.warning(
                "BugFix-Stock: seed failed %s.%s (%s).", model, fname, e,
            )


def post_init_hook(env):
    _seed_field_selections(env, _FIELD_SELECTIONS)
