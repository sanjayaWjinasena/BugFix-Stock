# -*- coding: utf-8 -*-
"""BugFix-Stock: post-install hooks.

Seeds ir.model.fields.selection rows that Studio populated in CDB but
Odoo 17 doesn't recreate on install. Uses the ORM (no direct SQL) per the
project's no-direct-SQL rule; the sibling migrations/<v>/post-migrate.py
runs the same seeding on version upgrades.
"""
import logging

_logger = logging.getLogger(__name__)

# --- Field selection seed data (ORM-only, no direct SQL) ---
# All rows Studio populated in CDB but Odoo 17 doesn't recreate on install.
# `state='base'` rows: options for Python-declared Selection fields that
# Odoo would normally set at install but Studio-side sequence differs.
# `related=` rows: audit-parity stubs — Odoo resolves at runtime from the
# source field, so shipping these creates DB rows for audit match with zero
# functional effect. (See feedback-python-only-fixes: prefer ORM over SQL.)
# (model, field_name, value, display_name, sequence)
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
    """Idempotent ORM create of ir.model.fields.selection rows.
    Skip if the field is absent or the (field, value) row already exists.
    Per-row savepoint so a single failure doesn't abort the batch."""
    Fld = env['ir.model.fields'].sudo()
    Sel = env['ir.model.fields.selection'].sudo()
    for model, fname, value, label, seq in entries:
        fld = Fld.search(
            [('model', '=', model), ('name', '=', fname)], limit=1,
        )
        if not fld:
            _logger.info(
                "BugFix-Stock: seed skip %s.%s (field absent).", model, fname,
            )
            continue
        exists = Sel.search(
            [('field_id', '=', fld.id), ('value', '=', value)], limit=1,
        )
        if exists:
            continue
        try:
            with env.cr.savepoint():
                Sel.create({
                    'field_id': fld.id, 'value': value,
                    'name': label, 'sequence': seq,
                })
        except Exception as e:
            _logger.warning(
                "BugFix-Stock: seed failed %s.%s=%r (%s).",
                model, fname, value, e,
            )


def post_init_hook(env):
    _seed_field_selections(env, _FIELD_SELECTIONS)
