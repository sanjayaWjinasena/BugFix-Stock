"""BugFix-Stock v17.0.0.0.111: seed ir.model.fields.selection rows via
Odoo's own _update_selection helper (framework API, not cr.execute).

Companion to _seed_field_selections in ../../hooks.py; this covers
version-upgrade path (post_init_hook covers fresh install).
"""

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)

_FIELD_SELECTIONS = [
    ("temp_structure_detai", "charge_group", "None", "None", 10),
    ("consignment_header", "shipping_mode", "Air", "Air", 10),
    ("consignment_header", "status", "Draft", "Draft", 10),
    ("consignment_header", "status_bar", "Draft", "Draft", 10),
    ("consignment_line", "status", "Draft", "Draft", 10),
    ("consignment_charge_l", "charge_group", "None", "None", 10),
    ("consignment_charge_l", "basis", "Percentage", "Percentage", 10),
    ("stock.picking", "pr_type", "Local", "Local", 10),
    ("stock.move", "pr_type", "Local", "Local", 10),
    ("con_consolidated_lin", "shipping_mode_1", "Air", "Air", 10),
    ("con_consolidated_lin", "status", "Draft", "Draft", 10),
    ("con_consolidated_hea", "status", "Draft", "Draft", 10),
    ("con_consolidated_hea", "pipeline_status_bar", "Draft", "Draft", 10),
    ("temp_con_conso_line", "shipping_mode", "Air", "Air", 10),
    ("temp_con_conso_line", "status", "Draft", "Draft", 10),
    ("consignment_header", "cost_allocation_method", "equal", "Equal", 10),
    ("consignment_line", "cost_allocation_method", "equal", "Equal", 10),
    ("stock.move.line", "pr_type", "Local", "Local", 10),
    ("stock.picking", "related_field_zZDiA", "Sales", "Sales", 10),
    ("stock.picking", "gl_account_status", "Pending", "Pending", 10),
    ("material_request_tes", "kanban_state", "normal", "In Progress", 10),
    ("material_request_mt", "kanban_state", "normal", "In Progress", 10),
    ("temp_structure_detai", "charge_group", "Charges", "Charges", 1),
    ("consignment_header", "shipping_mode", "Sea", "Sea", 1),
    ("consignment_line", "status", "In Transit", "In Transit", 1),
    ("consignment_charge_l", "charge_group", "Charges", "Charges", 1),
    (
        "consignment_charge_l",
        "basis",
        "Fixed Per Document",
        "Fixed Per Document",
        1,
    ),
    ("stock.picking", "pr_type", "Import", "Import", 1),
    ("stock.move", "pr_type", "Import", "Import", 1),
    ("consignment_header", "status_bar", "Consignment", "Confirmed", 1),
    ("con_consolidated_lin", "shipping_mode_1", "Sea", "Sea", 1),
    ("con_consolidated_lin", "status", "Consignment", "Confirmed", 1),
    ("con_consolidated_hea", "status", "Confirmed", "Confirmed", 1),
    (
        "con_consolidated_hea",
        "pipeline_status_bar",
        "Confirmed",
        "Confirmed",
        1,
    ),
    ("temp_con_conso_line", "shipping_mode", "Sea", "Sea", 1),
    ("temp_con_conso_line", "status", "Consignment", "Confirmed", 1),
    ("consignment_header", "status", "Consignment", "Confirmed", 1),
    (
        "consignment_header",
        "cost_allocation_method",
        "by_quantity",
        "By Quantity",
        1,
    ),
    (
        "consignment_line",
        "cost_allocation_method",
        "by_quantity",
        "By Quantity",
        1,
    ),
    ("stock.move.line", "pr_type", "Import", "Import", 1),
    ("stock.picking", "related_field_zZDiA", "Project", "Project", 1),
    ("stock.picking", "gl_account_status", "Updated", "Updated", 1),
    ("material_request_tes", "kanban_state", "done", "Ready", 1),
    ("material_request_mt", "kanban_state", "done", "Ready", 1),
    ("temp_structure_detai", "charge_group", "Duty", "Duty", 2),
    ("consignment_header", "shipping_mode", "Road", "Road", 2),
    (
        "consignment_line",
        "status",
        "Under Custom Clearance",
        "Under Custom Clearance",
        2,
    ),
    ("consignment_charge_l", "charge_group", "Duty", "Duty", 2),
    ("con_consolidated_lin", "shipping_mode_1", "Road", "Road", 2),
    ("con_consolidated_lin", "status", "In Transit", "In Transit", 2),
    ("temp_con_conso_line", "shipping_mode", "Road", "Road", 2),
    ("temp_con_conso_line", "status", "In Transit", "In Transit", 2),
    (
        "consignment_header",
        "cost_allocation_method",
        "by_current_cost_price",
        "By Current Cost",
        2,
    ),
    (
        "consignment_line",
        "cost_allocation_method",
        "by_current_cost_price",
        "By Current Cost",
        2,
    ),
    ("consignment_header", "status_bar", "Consolidated", "Consolidated", 2),
    ("consignment_header", "status", "Consolidated", "Consolidated", 2),
    ("stock.picking", "related_field_zZDiA", "Repair", "Repair", 2),
    ("material_request_tes", "kanban_state", "blocked", "Blocked", 2),
    ("material_request_mt", "kanban_state", "blocked", "Blocked", 2),
    ("temp_structure_detai", "charge_group", "Taxes", "Taxes", 3),
    ("consignment_header", "shipping_mode", "Courier", "Courier", 3),
    ("consignment_header", "status", "In Transit", "In Transit", 3),
    ("consignment_header", "status_bar", "In Transit", "In Transit", 3),
    ("consignment_line", "status", "Done", "Done", 3),
    ("consignment_charge_l", "charge_group", "Taxes", "Taxes", 3),
    ("con_consolidated_lin", "shipping_mode_1", "Courier", "Courier", 3),
    (
        "con_consolidated_lin",
        "status",
        "Under Custom Clearance",
        "Under Custom Clearance",
        3,
    ),
    ("temp_con_conso_line", "shipping_mode", "Courier", "Courier", 3),
    (
        "temp_con_conso_line",
        "status",
        "Under Custom Clearance",
        "Under Custom Clearance",
        3,
    ),
    (
        "consignment_header",
        "cost_allocation_method",
        "by_weight",
        "By Weight",
        3,
    ),
    (
        "consignment_line",
        "cost_allocation_method",
        "by_weight",
        "By Weight",
        3,
    ),
    (
        "temp_structure_detai",
        "charge_group",
        "Assessable Value",
        "Assessable Value",
        4,
    ),
    (
        "consignment_header",
        "status",
        "Under Custom Clearance",
        "Under Custom Clearance",
        4,
    ),
    (
        "consignment_header",
        "status_bar",
        "Under Custom Clearance",
        "Under Custom Clearance",
        4,
    ),
    ("con_consolidated_lin", "status", "Done", "Done", 4),
    ("temp_con_conso_line", "status", "Done", "Done", 4),
    (
        "consignment_header",
        "cost_allocation_method",
        "by_volume",
        "By Volume",
        4,
    ),
    (
        "consignment_line",
        "cost_allocation_method",
        "by_volume",
        "By Volume",
        4,
    ),
    ("consignment_header", "status_bar", "Done", "Done", 5),
    ("consignment_header", "status", "Done", "Done", 5),
    ("con_consolidated_lin", "status", "TP Invoice", "TP Invoice", 5),
    ("temp_con_conso_line", "status", "TP Invoice", "TP Invoice", 5),
    ("consignment_header", "status", "TP Invoice", "TP Invoice", 6),
    ("consignment_header", "status_bar", "TP Invoice", "TP Invoice", 6),
]


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Sel = env["ir.model.fields.selection"].sudo()
    Fld = env["ir.model.fields"].sudo()
    grouped = {}
    for model, fname, value, label, seq in _FIELD_SELECTIONS:
        grouped.setdefault((model, fname), []).append((value, label, seq))
    for (model, fname), values in grouped.items():
        fld = Fld.search(
            [("model", "=", model), ("name", "=", fname)],
            limit=1,
        )
        if not fld:
            continue
        existing_recs = Sel.search(
            [("field_id", "=", fld.id)],
            order="sequence",
        )
        existing_pairs = [(r.value, r.name) for r in existing_recs]
        existing_values = {v for v, _ in existing_pairs}
        added = []
        for v, line, _seq in sorted(values, key=lambda t: t[2]):
            if v in existing_values:
                continue
            existing_pairs.append((v, line))
            existing_values.add(v)
            added.append(v)
        if not added:
            continue
        try:
            with cr.savepoint():
                Sel._update_selection(model, fname, existing_pairs)
                _logger.info(
                    "BugFix-Stock v17.0.0.0.111: seeded %s.%s += %s.",
                    model,
                    fname,
                    added,
                )
        except Exception as e:
            _logger.warning(
                "BugFix-Stock v17.0.0.0.111: seed failed %s.%s (%s).",
                model,
                fname,
                e,
                exc_info=True,
            )
