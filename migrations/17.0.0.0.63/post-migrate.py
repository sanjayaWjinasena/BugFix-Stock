"""Phase F1: seed missing ir.model.fields.selection records for state=base fields.
Odoo blocks XML/ORM writes to state=base field selections. This migration uses
direct SQL to bypass that restriction — safe because our tuples come from
CDB's ground truth and match the Python selection= tuples in fields.Selection().
"""

def migrate(cr, version):
    if not version:
        return
    # (model, field_name, value, display_name, sequence)
    data = [
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
    for model, name, value, display, seq in data:
        cr.execute("""
            INSERT INTO ir_model_fields_selection
                (field_id, value, name, sequence, create_uid, create_date, write_uid, write_date)
            SELECT f.id, %s, %s, %s, 1, NOW() AT TIME ZONE 'UTC', 1, NOW() AT TIME ZONE 'UTC'
            FROM ir_model_fields f
            WHERE f.model = %s AND f.name = %s AND NOT EXISTS (
                SELECT 1 FROM ir_model_fields_selection s
                WHERE s.field_id = f.id AND s.value = %s
            )
        """, (value, display, seq, model, name, value))