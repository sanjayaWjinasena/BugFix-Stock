"""Phase F1: seed ir.model.fields.selection records for state=base fields via SQL.
Odoo 17: `name` column is JSONB (translation) - must be JSON-encoded, not plain str."""

import json


def migrate(cr, version):
    if not version:
        return
    # (model, field_name, value, display_name, sequence)
    data = [
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
        (
            "con_consolidated_hea",
            "pipeline_status_bar",
            "Draft",
            "Draft",
            10,
        ),
        ("temp_con_conso_line", "shipping_mode", "Air", "Air", 10),
        ("temp_con_conso_line", "status", "Draft", "Draft", 10),
        (
            "consignment_header",
            "cost_allocation_method",
            "equal",
            "Equal",
            10,
        ),
        ("consignment_line", "cost_allocation_method", "equal", "Equal", 10),
        ("stock.move.line", "pr_type", "Local", "Local", 10),
        ("stock.picking", "related_field_zZDiA", "Sales", "Sales", 10),
        ("stock.picking", "gl_account_status", "Pending", "Pending", 10),
        (
            "material_request_tes",
            "kanban_state",
            "normal",
            "In Progress",
            10,
        ),
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
        (
            "consignment_header",
            "status_bar",
            "Consolidated",
            "Consolidated",
            2,
        ),
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
    for model, name, value, display, seq in data:
        # Name is a JSONB translation field in Odoo 17
        name_json = json.dumps({"en_US": display})
        cr.execute(
            """
            INSERT INTO ir_model_fields_selection
                (field_id, value, name, sequence, create_uid, create_date, write_uid, write_date)
            SELECT f.id, %s, %s::jsonb, %s, 1, NOW() AT TIME ZONE 'UTC', 1, NOW() AT TIME ZONE 'UTC'
            FROM ir_model_fields f
            WHERE f.model = %s AND f.name = %s AND NOT EXISTS (
                SELECT 1 FROM ir_model_fields_selection s
                WHERE s.field_id = f.id AND s.value = %s
            )
        """,
            (value, name_json, seq, model, name, value),
        )
