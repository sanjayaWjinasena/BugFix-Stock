# BugFix-Stock — `stock.picking`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.picking` — Transfer

*Extends a model created by `stock`.* Python: `models/stock_picking.py`.

Other repos that use this model: `access right BugFix-Analytics.access_6084_user` (BugFix-Analytics)<br>`access right BugFix-Analytics.access_6859_stock_picking` (BugFix-Analytics)<br>`account.bank.statement.line.x_studio_create_from_transfer_1` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_create_from_transfer` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_created_from_transfer` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_created_transfer` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_many2one_field_6Sjmv` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_many2one_field_TEK9K` (BugFix-Accounting)<details><summary>+34 more</summary>`account.move.x_studio_create_from_transfer_1` (BugFix-Accounting)<br>`account.move.x_studio_create_from_transfer` (BugFix-Accounting)<br>`account.move.x_studio_created_from_transfer` (BugFix-Accounting)<br>`account.payment.x_studio_create_from_transfer_1` (BugFix-Accounting)<br>`account.payment.x_studio_create_from_transfer` (BugFix-Accounting)<br>`account.payment.x_studio_created_from_transfer` (BugFix-Accounting)<br>`account.payment.x_studio_created_transfer` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_6Sjmv` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_TEK9K` (BugFix-Accounting)<br>`helpdesk.ticket._compute_x_studio_task_status()` (Fix-repair)<br>`helpdesk.ticket._compute_x_x_studio_created_from_help_ticket_stock_picking_count()` (Fix-repair)<br>`helpdesk.ticket._current_item_location()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_route()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<br>`helpdesk.ticket.action_received_at_sales_centre()` (Fix-repair)<br>`helpdesk.ticket.repair_picking_ids` (Fix-repair)<br>`helpdesk.ticket.x_studio_picking_id` (Fix-repair)<br>`project.task._compute_x_studio_incomplete_delivery_available()` (Fix-repair)<br>`project.task._compute_x_studio_material_availability()` (Fix-repair)<br>`project.task._compute_x_studio_valid_delivered_so()` (Fix-repair)<br>`record rule BugFix-Analytics.rule_188_portal_follower_transfers` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_44_stock_picking_multi_company` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_462_test` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_829_block_receipt_operations` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_904_kap` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_913_stock_data_admin` (BugFix-Analytics)<br>`record rule BugFix-Analytics.rule_919_stock_data_warehouse` (BugFix-Analytics)<br>`server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2268_sample_server_action_2` (BugFix-Studio-Misc)<br>`stock.picking._action_done()` (Fix-repair)<br>`stock.picking.button_validate()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`stock.return.picking._create_returns()` (Fix-repair)<br>`stock.return.picking.create_returns()` (Fix-Repair-Wizard-Nav)<br>`stock.return.picking.default_get()` (Fix-repair)</details>

**Summary:**

<!-- SUMMARY:model:stock.picking -->
This repo adds about 50 fields to transfers: links to the sales order, helpdesk ticket, maintenance request, material request and import consignment; repair flags (payment made, factory repair, user location validation and others, mostly computed in Fix-repair); movement journal flags with a Journal Type and G/L status; and transfer approval flags. Active automations copy the supplier invoice number from the consignment, set the source document from the linked sales order and schedule a completion activity when a Project transfer is done. Buttons cover Update Consignment, transfer approval and rejection, the movement journal offset account update and a repair re-return check, and three approval rules require approval before Cancel (Inventory Administrator), label printing (Access Rights) and Put in Pack (Internal User). The transfer form is heavily customised, other addons' extra fields are hidden, and global record rules restrict transfers by operation type and sequence code.
<!-- /SUMMARY -->

**Fields (51):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_analytic_account` | Analytic Account | many2one → `account.analytic.account` | Analytic account of the transfer, copied from the originating sales order's analytic account (related `sale_id.analytic_account_id`); shown read-only on the transfer form. | related `sale_id.analytic_account_id`; stored | `model account.analytic.account` (analytic)<br>`sale.order.analytic_account_id` (sale)<br>`stock.picking.sale_id` (sale_stock) | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_budget_created` | Budget Created | boolean | Read-only flag showing a budget has been created for this transfer; used in transfer form conditions. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_cancelled` | Cancelled | boolean | Read-only flag marking the transfer as cancelled; used in transfer form button visibility conditions. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_cash_full_payment_made` | Cash Full Payment Made | boolean | Computed flag (Fix-repair `_fix_repair_compute_cash_full_payment_made`) that is True when the ticket's cash sales order is not fully invoiced/paid, or a credit order has no invoice; False for Quick Repair tickets. Used to gate transfer form buttons. | not stored | `stock.picking._jin_compute_cash_full_payment_made()` (Fix-repair) | `stock.picking._fix_repair_compute_cash_full_payment_made()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_consignment_no` | Consignment No | many2one → `x_consignment_header` | Import consignment this transfer (GRN) belongs to; used by the Update Consignment actions and the supplier-invoice-number automation for import POs. | stored | `model x_consignment_header` | `automation BugFix-Stock.base_automation_104_supplier_invoice_no_update_in_import_pos`<br>`server action BugFix-Stock.server_action_1358_imp_update_consignment`<br>`server action BugFix-Stock.server_action_1360_imp_update_consignment_partial_grn`<br>`server action BugFix-Stock.server_action_1367_imp_update_consignment_final`<br>`server action BugFix-Stock.server_action_1697_supplier_invoice_no_update_in_import_pos`<details><summary>+1 more</summary>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`</details> |
| `x_studio_created_from_help_ticket` | Created from Help Ticket | many2one → `helpdesk.ticket` | Helpdesk ticket that created this transfer (repair flow); drives the repair computes (payment, FSM task, factory repair, user location) and checks in Validate. | stored | `model helpdesk.ticket` (helpdesk) | `stock.picking._fix_repair_compute_cash_full_payment_made()` (Fix-repair)<br>`stock.picking._fix_repair_compute_fsm_task_done()` (Fix-repair)<br>`stock.picking._fix_repair_compute_fully_paid_so()` (Fix-repair)<br>`stock.picking._fix_repair_compute_user_location_validation()` (Fix-repair)<br>`stock.picking._fix_repair_compute_valid_factory_repair()` (Fix-repair)<details><summary>+9 more</summary>`stock.picking._jin_compute_fsm_task_done()` (Fix-repair)<br>`stock.picking._jin_compute_fully_paid_so()` (Fix-repair)<br>`stock.picking._jin_compute_valid_factory_repair()` (Fix-repair)<br>`stock.picking.button_validate()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e`<br>`window action BugFix-Stock.act_window_2008_repair_trans`<br>`window action BugFix-Stock.action_2008_repair_trans`<br>`window action BugFix-Stock.aw_f4_stock_picking_repair_trans`</details> |
| `x_studio_created_from_material_request_no` | Created from Material Request No | many2one → `x_material_request` | Material Request that generated this transfer; used to count and filter transfers per material request. | stored | `model x_material_request` | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`window action BugFix-Stock.act_window_2409_transfers`<br>`window action BugFix-Stock.action_2409_transfers`<br>`window action BugFix-Stock.aw_f4_stock_picking_transfers` |
| `x_studio_custom_clearance_no` | Custom Clearance No | char | Read-only customs clearance number for the transfer, shown on the transfer form. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_factory_repair` | Factory Repair | boolean | Set by the valid-factory-repair compute to True when the linked helpdesk ticket's job location is 'Factory Repair'; used in transfer form conditions. | stored |  | `stock.picking._fix_repair_compute_valid_factory_repair()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_fsm_task_done` | FSM Task Done | boolean | Computed flag (Fix-repair) that is True when any field service task on the linked helpdesk ticket is done or its quick repair has ended; used to gate transfer buttons. | not stored | `stock.picking._jin_compute_fsm_task_done()` (Fix-repair) | `stock.picking._fix_repair_compute_fsm_task_done()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_fully_paid_so` | Fully Paid SO | boolean | Computed flag (Fix-repair) taken from the linked ticket's Fully Paid SO value for non-credit orders, False for credit orders, True for Quick Repair/no-SO tickets; used to gate transfer buttons. | not stored | `stock.picking._jin_compute_fully_paid_so()` (Fix-repair) | `stock.picking._fix_repair_compute_fully_paid_so()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_gl_account_status` | G/L Account Status | selection: Pending=Pending; Updated=Updated | Status of the movement-journal G/L offset account update: Pending or Updated. Defaults to Pending and is set by the 'Movement Journals - Update Offset Account' action. | stored |  | `default BugFix-Stock.default_392_stock_picking_x_studio_gl_account_status`<br>`server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.ported_view_5299_studio_stock_picking_tree` |
| `x_studio_helpdesk_ticket_id` | Helpdesk Ticket | many2one → `helpdesk.ticket` | Helpdesk ticket linked to this transfer; used as a fallback ticket by the repair computes and by the Validate checks. | stored | `model helpdesk.ticket` (helpdesk) | `stock.picking._fix_repair_compute_cash_full_payment_made()` (Fix-repair)<br>`stock.picking._fix_repair_compute_fsm_task_done()` (Fix-repair)<br>`stock.picking._fix_repair_compute_fully_paid_so()` (Fix-repair)<br>`stock.picking._fix_repair_compute_valid_factory_repair()` (Fix-repair)<br>`stock.picking._jin_compute_fsm_task_done()` (Fix-repair)<details><summary>+6 more</summary>`stock.picking._jin_compute_fully_paid_so()` (Fix-repair)<br>`stock.picking._jin_compute_valid_factory_repair()` (Fix-repair)<br>`stock.picking.button_validate()` (Fix-Repair-Wizard-Nav, Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e`<br>`view Fix-repair.view_stock_picking_repair_movement_fields` (Fix-repair)</details> |
| `x_studio_journal_type` | Journal Type | many2one → `x_journal_types` | Journal type (`x_journal_types`) chosen for a movement journal transfer; its offset account is used by the 'Update Offset Account' action. | stored | `model x_journal_types` (BugFix-Maintenance) | `server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_maintenance_request_` | Maintenance Request # | many2one → `maintenance.request` | Maintenance request this transfer was created for; set via a context default from the maintenance 'New' button action. | stored | `model maintenance.request` (maintenance) | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`window action BugFix-Stock.act_window_1714_new_button`<br>`window action BugFix-Stock.action_1714_new_button`<br>`window action BugFix-Stock.aw_f4_stock_picking_new_button` |
| `x_studio_mj_in` | MJ IN | boolean | Read-only flag marking the transfer as a movement journal IN; used by the 'Update Offset Account' action. | stored |  | `server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_mj_out` | MJ OUT | boolean | Read-only flag marking the transfer as a movement journal OUT; used by the 'Update Offset Account' action. | stored |  | `server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_movement_journal` | Movement Journal | boolean | Read-only flag marking the transfer as a movement journal; used by the 'Update Offset Account' action and shown in the transfers list. | stored |  | `server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.ported_view_5299_studio_stock_picking_tree` |
| `x_studio_need_approval` | Need Approval | boolean | Computed flag (Fix-repair) that is True for internal transfers without a source document and for deliveries with a source document; used to show transfer approval buttons. | not stored | `stock.picking._jin_compute_need_approval()` (Fix-repair) | `stock.picking._fix_repair_compute_need_approval()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_offset_account_updated` | Offset Account Updated | boolean | Flag set once the movement-journal offset account has been updated on the transfer's entries by the 'Update Offset Account' action. | stored |  | `server action BugFix-Stock.server_action_2448_movement_journals_update_offset_account`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_picking_count` | Picking Count | boolean | Set by the valid-factory-repair compute to True when the linked helpdesk ticket has more than one transfer; used in transfer form conditions. | stored |  | `stock.picking._fix_repair_compute_valid_factory_repair()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_pr_type` | PR Type | selection: Local=Local; Import=Import | Read-only purchase request type of the transfer: Local or Import; used in transfer form conditions. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_quotation_type` | Quotation Type | selection: Sales=Sales; Sales=Sales; Project=Project; Project=Project; Repair=Repair; Repair=Repair | Read-only quotation type of the related sales order (Sales, Project or Repair), shown on the transfer form. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_quotation_type_2` | Quotation Type (2) | selection: Sales=Sales; Sales=Sales; Project=Project; Project=Project; Repair=Repair; Repair=Repair | Second read-only copy of the quotation type (Sales, Project or Repair); used in transfer form button conditions. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_received_at_centre` | Received at Centre | boolean | Set by the valid-factory-repair compute from the linked helpdesk ticket's 'Receive at Centre' value; used in transfer form conditions. | stored |  | `stock.picking._fix_repair_compute_valid_factory_repair()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_related_field_zZDiA` | New Related Field | selection: Sales=Sales; Project=Project; Repair=Repair | Leftover Studio related selection (Sales/Project/Repair), stored read-only without its source path; not used by any view or logic. | stored |  |  |
| `x_studio_repair_payment_made` | Repair Payment Made | boolean | Computed flag (Fix-repair) that is True when the sales order is credit, RUG-approved, has a posted payment or a paid/partially paid invoice; used to gate transfer buttons. | not stored | `stock.picking._jin_compute_repair_payment_made()` (Fix-repair) | `stock.picking._fix_repair_compute_repair_payment_made()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_repair_return_location` | Repair Return Location | boolean | Read-only flag indicating a repair return location; set by the 'Update Operation Type in Help Desk Repairs' action. | stored |  | `server action BugFix-Stock.server_action_1996_rr_update_operation_type_in_help_desk_repairs`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_return_receipt_location` | Return Receipt Location | many2one → `stock.location` | Read-only location where returned repair items are received; set by the 'Update Operation Type in Help Desk Repairs' action. | stored | `model stock.location` (stock) | `server action BugFix-Stock.server_action_1996_rr_update_operation_type_in_help_desk_repairs`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_return_sequence` | Return Sequence | many2one → `ir.sequence` | Read-only sequence used for numbering return transfers; shown on the transfer form. | stored | `model ir.sequence` (base) | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_sales_order` | Sales Order (Studio) | many2one → `sale.order` | Sales order linked to the transfer; used to validate payment before shipment and to update the transfer's source document. | stored | `model sale.order` (sale) | `automation BugFix-Stock.base_automation_148_update_source_document_in_transfers`<br>`server action BugFix-Stock.sa_f5_stock_picking_sls_validate_payment_in_shipment`<br>`server action BugFix-Stock.server_action_1438_sls_validate_payment_in_shipment`<br>`server action BugFix-Stock.server_action_1774_sls_validate_payment_in_xxx`<br>`server action BugFix-Stock.server_action_1813_update_source_document_in_transfers`<details><summary>+1 more</summary>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`</details> |
| `x_studio_sequence_code` | Sequence Code | char | Read-only sequence code of the transfer's operation type; used by the operation-control record rules to restrict which transfers users see. | stored |  | `record rule BugFix-Stock.rule_452_kap_operation_control`<br>`record rule BugFix-Stock.rule_912_kap_operation_control_2`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_supplier_invoice_number` | Supplier Invoice Number | char | Supplier invoice number for the receipt, filled by the automation that copies it from the import consignment. | stored |  | `server action BugFix-Stock.server_action_1697_supplier_invoice_no_update_in_import_pos`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_supplier_invoice_number_1` | Supplier Invoice Number | char | Read-only second supplier invoice number field shown on the transfer form; no logic sets it in this repo. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_task_status` | Task Status | boolean | Read-only 'Task Status' flag used in transfer form conditions; non-stored with no compute in this repo, so it is always False. | not stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_ticket_sales_order` | Ticket Sales Order (Studio) | many2one → `sale.order` | Read-only sales order of the linked helpdesk ticket; used by the cash-full-payment compute. Non-stored with no compute in this repo. | not stored | `model sale.order` (sale) | `stock.picking._fix_repair_compute_cash_full_payment_made()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view Fix-repair.view_stock_picking_repair_movement_fields` (Fix-repair) |
| `x_studio_transfer_approval` | Transfer Approval | boolean | Flag indicating the transfer requires approval; shown on the transfer form. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_transfer_approved` | Transfer Approved | boolean | Set to True by the 'RR - Transfer Approval' action when the transfer is approved; controls approval button visibility. | stored |  | `server action BugFix-Stock.server_action_2205_rr_transfer_approval`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_transfer_rejected` | Transfer Rejected | boolean | Set to True by the 'RR - Transfer Rejection' action when the transfer is rejected; controls approval button visibility. | stored |  | `server action BugFix-Stock.server_action_2207_rr_transfer_rejection`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_transfer_request_sent` | Transfer Request Sent | boolean | Flag showing a transfer approval request has been sent; shown on the transfer form. | stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_ttt` | TTT | boolean | Test checkbox 'TTT'; not used by any view or logic. | stored |  |  |
| `x_studio_type_of_operation` | Type of Operation | selection: incoming=Receipt; incoming=Receipt; outgoing=Delivery; outgoing=Delivery; internal=Internal Transfer; internal=Internal Transfer; mrp_operation=Manufacturing; mrp_operation=Manufacturing | Read-only operation type of the transfer (Receipt, Delivery, Internal Transfer, Manufacturing); used by record rules that block transfer types and by the user location validation. | stored |  | `record rule BugFix-Stock.rule_458_transfer_type_block`<br>`record rule BugFix-Stock.rule_460_block_operations`<br>`server action BugFix-Stock.sa_f5_stock_picking_user_location_validation`<br>`server action BugFix-Stock.server_action_2474_user_location_validation`<br>`stock.picking._fix_repair_compute_user_location_validation()` (Fix-repair)<details><summary>+2 more</summary>`stock.picking._jin_compute_user_location_validation()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`</details> |
| `x_studio_update_consignment` | Update Consignment | boolean | Flag on the receipt indicating the import consignment should be/has been updated; used by the Update Consignment actions. | stored |  | `server action BugFix-Stock.server_action_1358_imp_update_consignment`<br>`server action BugFix-Stock.server_action_1360_imp_update_consignment_partial_grn`<br>`server action BugFix-Stock.server_action_1367_imp_update_consignment_final`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_user_location_validation` | User Location Validation | boolean | Computed flag (Fix-repair) that is True when the current user is NOT assigned to the relevant destination location for this operation type; used to block validation. | not stored | `stock.picking._jin_compute_user_location_validation()` (Fix-repair) | `server action BugFix-Stock.sa_f5_stock_picking_user_location_validation`<br>`server action BugFix-Stock.server_action_2474_user_location_validation`<br>`stock.picking._fix_repair_compute_user_location_validation()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_user_location_validation_2` | User Location Validation 2 | boolean | Second location check, set by the user-location compute for deliveries not from a ticket: True when the user is not assigned to the source location. | stored |  | `server action BugFix-Stock.sa_f5_stock_picking_user_location_validation`<br>`server action BugFix-Stock.server_action_2474_user_location_validation`<br>`stock.picking._fix_repair_compute_user_location_validation()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_valid_factory_repair` | Valid Factory Repair | boolean | Computed flag (Fix-repair) that is True when the linked helpdesk ticket is marked 'Receive at Factory'; the same compute also sets Factory Repair, Received at Centre and Picking Count. | not stored | `stock.picking._jin_compute_valid_factory_repair()` (Fix-repair) | `stock.picking._fix_repair_compute_valid_factory_repair()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_valid_transfer_lines` | Valid Transfer Lines | boolean | Computed flag (Fix-repair) that is True when the transfer has at least one move or move line; used to hide buttons on empty transfers. | not stored | `stock.picking._jin_compute_valid_transfer_lines()` (Fix-repair) | `stock.picking._fix_repair_compute_valid_transfer_lines()` (Fix-repair)<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form`<br>`view BugFix-Stock.view_4732_odoo_studio_stock_picking_form_button_e` |
| `x_studio_validation` | Validation | char | Text field with a default value, shown on the transfer form; no logic in this repo uses its content. | stored |  | `default BugFix-Stock.default_378_stock_picking_x_studio_validation`<br>`view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_studio_xxx` | XXX | boolean | Test checkbox 'XXX'; not used by any view or logic. | stored |  |  |
| `x_x_studio_create_from_transfer_1__account_move_count` | Create From Transfer count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the transfer form smart button. | not stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |
| `x_x_studio_created_from_transfer__account_move_count` | Created From Transfer count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the transfer form smart button. | not stored |  | `view BugFix-Stock.ported_view_2387_studio_stock_picking_form` |

**Server actions (22):**

- **IMP - Update Consignment** (`server_action_1358_imp_update_consignment`, type `code`)
  - Function: On an import GRN, checks the chosen Consignment No belongs to the PO and matches done quantities, then totals amounts/charges/duty/tax and posts reversal journal entries (Vendor Despatch, custom clearance charges) in the 'Vendor Despatch' journal; raises errors when links or ledger setup are missing.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model purchase.order.line` (purchase), `model res.company` (base), `model stock.picking` (stock)<details><summary>+8 more</summary>`model x_consignment_header`, `model x_consignment_line`, `model x_imports_ledger_setup` (BugFix-Purchase), `stock.picking.move_ids_without_package` (stock), `stock.picking.partner_id` (stock), `stock.picking.purchase_id` (purchase_stock), `stock.picking.x_studio_consignment_no`, `stock.picking.x_studio_update_consignment`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (105 lines)</summary>

```python
if record.id:
  
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  con_line = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.x_studio_consignment_no.id), ('x_studio_purchase_id', '=', record.purchase_id.id)],limit=1)
  if not con_line:
    raise UserError('The Selected Consignment No is not linked with the Current PO.')
  
  done = 0  
  select = 0
  total_amount = 0
  total_charge = 0
  total_duty = 0
  total_tax = 0
  for po_line in record.move_ids_without_package:
    if po_line.quantity_done > 0.0000:
      done += 1
      con_line_2 = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.x_studio_consignment_no.id), ('x_studio_purchase_id', '=', record.purchase_id.id), ('x_studio_product_id', '=', po_line.product_id.id), ('x_studio_invoice_qty', '=', po_line.quantity_done), ('x_studio_purchase_line_id', '=', po_line.purchase_line_id.id)],limit=1)
      if con_line_2:
        po_lines = env['purchase.order.line'].search([('id', '=', po_line.purchase_line_id.id)],limit=1)
        select += 1
        if po_lines:
          total_amount += po_line.quantity_done * (po_lines.price_subtotal / po_lines.product_qty)
          
        if con_line_2.x_studio_valid_charge == True:
          total_charge += con_line_2.x_studio_tot_charge
        if con_line_2.x_studio_valid_duty == True:
          total_duty += con_line_2.x_studio_tot_duty
        if con_line_2.x_studio_valid_tax == True:
          total_tax += con_line_2.x_studio_tot_tax
  
  if done == 0:
    raise UserError('You have not recorded done quantities yet, Atleast one done quantity should be recorded to proceed.') 
  
  if select == 0:
    raise UserError('The Selected Consignment No is not linked with the Correct Items & Item Quantities in the Current PO.')

  con_header = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_no.id)],limit=1)
  grand_total_amount = 0
  if con_header:
    journal = env['account.journal'].search([('name', '=', 'Vendor Despatch'),('company_id', '=', company.id)], limit=1) 
    if not journal:
      raise UserError('The required journal has not been setup. Process terminated.')
    
    if con_header.x_studio_vendor_dispatch == True:
      grand_total_amount = total_amount * con_header.x_studio_vendor_dispatch_exchange_rate
      if grand_total_amount > 0.0000:
        despatch_account = env['x_imports_ledger_setup'].search([('x_studio_company_id', '=', company.id)], limit=1)
        if despatch_account:
          if despatch_account.x_studio_vendor_despatch_debit_account.id == 0 or despatch_account.x_studio_vendor_despatch_credit_account.id == 0:
            raise UserError('Vendor Despatch Accounts must be Specified in Imports Ledger Setup')
            
        despatch_lines=[]
        despatch_lines.append([0,0,{
          'account_id':despatch_account.x_studio_vendor_despatch_credit_account.id,
          'partner_id':record.partner_id.id,
          'name':'Vendor Despatch Reversal',
          'debit':grand_total_amount}])
                  
        despatch_lines.append([0,0,{
          'account_id':despatch_account.x_studio_vendor_despatch_debit_account.id,
          'partner_id':record.partner_id.id,
          'name':'Vendor Despatch Reversal',
          'credit':grand_total_amount}])	
                
        vendor_despatch = env['account.move'].create({'x_studio_created_from_transfer':record.id,'journal_id':journal.id,'move_type':'entry','line_ids':despatch_lines})
              
        update_vendor_despatch = env['account.move'].search([('id', '=', vendor_despatch.id)],limit=1)
        if update_vendor_despatch:
          update_vendor_despatch.write({'state':'posted'})
        
    if con_header.x_studio_custom_clearance == True: 
      despatch_lines_2=[]
      if total_charge > 0.0000:
        despatch_lines_2.append([0,0,{
        'account_id':con_header.x_studio_account_charge.id,
        'name':'Purchase, Charge - Reversal',
        'credit':total_charge * con_header.x_studio_custom_clearance_exchange_rate}])
          
      if total_duty > 0.0000:  
        despatch_lines_2.append([0,0,{
        'account_id':con_header.x_studio_account_duty.id,
        'name':'Purchase Misc. Charges Duty - Reversal',
        'credit':total_duty * con_header.x_studio_custom_clearance_exchange_rate}])
          
      if total_tax > 0.0000:  
        despatch_lines_2.append([0,0,{
        'account_id':con_header.x_studio_account_tax.id,
        'name':'Purchase, Packing Slip Tax - Reversal',
        'credit':total_tax * con_header.x_studio_custom_clearance_exchange_rate}])
          
      if (total_charge + total_duty + total_tax) > 0.0000:    
        despatch_lines_2.append([0,0,{
        'account_id':con_header.x_studio_offset_account.id,
        'name':'Purchase Packing Slip Offset - Reversal',
        'debit':(total_charge + total_duty + total_tax) * con_header.x_studio_custom_clearance_exchange_rate}])	
            
        custom_clearance = env['account.move'].create({'x_studio_create_from_transfer_1':record.id,'journal_id':journal.id,'move_type':'entry','line_ids':despatch_lines_2})
          
        update_custom_clearance = env['account.move'].search([('id', '=', custom_clearance.id)],limit=1)
        if update_custom_clearance:
          update_custom_clearance.write({'state':'posted'})
      
  record['x_studio_update_consignment'] = True
```
  </details>
- **IMP - Update Consignment - Final** (`server_action_1367_imp_update_consignment_final`, type `code`)
  - Function: Button on the receipt form: checks the selected consignment belongs to the PO, sets each matching move's done quantity to the consignment Invoice Qty, links move and reduces delivery remainder, then sets Update Consignment. Uses `quantity_done`, which no longer exists on stock.move in Odoo 17.
  - Depends on: `model stock.picking` (stock), `model x_consignment_line`, `stock.picking.move_ids_without_package` (stock), `stock.picking.purchase_id` (purchase_stock), `stock.picking.x_studio_consignment_no`<details><summary>+1 more</summary>`stock.picking.x_studio_update_consignment`</details>
  - Used by: `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`
  <details><summary>code (26 lines)</summary>

```python
if record.id:
  con_line = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.x_studio_consignment_no.id), ('x_studio_purchase_id', '=', record.purchase_id.id)],limit=1)
  if not con_line:
    raise UserError('The Selected Consignment No is not linked with the Current PO.')
  
  done = 0  
  select = 0
  
  for po_line in record.move_ids_without_package:
    con_line_2 = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.x_studio_consignment_no.id), ('x_studio_purchase_id', '=', record.purchase_id.id), ('x_studio_product_id', '=', po_line.product_id.id), ('x_studio_invoice_qty', '<=', po_line.product_uom_qty), ('x_studio_purchase_line_id', '=', po_line.purchase_line_id.id)],limit=1)
    if con_line_2:
      select += 1
      po_line.write({'quantity_done':con_line_2.x_studio_invoice_qty})
      con_line_2.write({'x_studio_stock_move_id':po_line.id, 'x_studio_delivery_remainder':(con_line_2.x_studio_delivery_remainder - con_line_2.x_studio_invoice_qty)})
  
  for po_line_count in record.move_ids_without_package:
    if po_line_count.quantity_done > 0.0000:
      done += 1
      
  if done == 0:
    raise UserError('You have not recorded done quantities yet, Atleast one done quantity should be recorded to proceed.') 
  
  if select == 0:
    raise UserError('The Selected Consignment No is not linked with the Correct Items & Item Quantities in the Current PO.')

  record['x_studio_update_consignment'] = True
```
  </details>
- **IMP - Update Consignment - Partial GRN** (`server_action_1360_imp_update_consignment_partial_grn`, type `code`)
  - Function: Clears the Update Consignment flag and the Consignment No on the transfer (used for partial GRNs). Not referenced by any automation or view in this repo.
  - Depends on: `model stock.picking` (stock), `stock.picking.x_studio_consignment_no`, `stock.picking.x_studio_update_consignment`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
record['x_studio_update_consignment'] = False
record['x_studio_consignment_no'] = False
```
  </details>
- **Movement Journals - Update Offset Account** (`server_action_2448_movement_journals_update_offset_account`, type `code`)
  - Function: For a Movement Journal transfer, finds the Journal Type's offset account for the current company (error if missing) and rewrites the stock-output (MJ OUT) or stock-input (MJ IN) line of each move's valuation journal entry to that account, then marks the transfer Offset Account Updated / GL status 'Updated'.
  - Depends on: `model account.move.line` (account), `model account.move` (account), `model res.company` (base), `model stock.move` (stock), `model stock.picking` (stock)<details><summary>+9 more</summary>`model stock.valuation.layer` (stock_account), `model x_journal_types` (BugFix-Maintenance), `stock.picking.partner_id` (stock), `stock.picking.x_studio_gl_account_status`, `stock.picking.x_studio_journal_type`, `stock.picking.x_studio_mj_in`, `stock.picking.x_studio_mj_out`, `stock.picking.x_studio_movement_journal`, `stock.picking.x_studio_offset_account_updated`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (33 lines)</summary>

```python
if record.id:
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  if record.x_studio_movement_journal == True:
    offset_account = env['x_journal_types'].search([('id', '=', record.x_studio_journal_type.id),('x_studio_company_id', '=', company.id)], limit=1)
    #offset_account = record.x_studio_journal_type.x_studio_offset_account
    if offset_account.x_studio_offset_account == False:
      raise UserError('Offset Account for the selected Journal Type must be Specified.')
    
    stock_move = env['stock.move'].search([('picking_id', '=', record.id)])
    if stock_move:
      for stock_move_loop in stock_move:
        stock_valuation_layer = env['stock.valuation.layer'].search([('stock_move_id', '=', stock_move_loop.id)], limit=1)  
        if stock_valuation_layer:
          account_move = env['account.move'].search([('id', '=', stock_valuation_layer.account_move_id.id)], limit=1)  
          if account_move:
            if record.x_studio_mj_out == True:
              account_move_lines = env['account.move.line'].search([('move_id', '=', account_move.id),('account_id', '=', stock_move.product_id.categ_id.property_stock_account_output_categ_id.id)],limit=1)
            elif record.x_studio_mj_in == True:
              account_move_lines = env['account.move.line'].search([('move_id', '=', account_move.id),('account_id', '=', stock_move.product_id.categ_id.property_stock_account_input_categ_id.id)],limit=1)
            else:
              raise UserError('There is no journal line can be found to update the off-sett account.')
            #account_move_lines = env['account.move.line'].search([('move_id', '=', account_move.id),('debit', '>', 0)], limit=1)
            #lines = env['account.move.line'].search([('move_id', '=', account_move.id),('account_id', '=', record.journal_id.default_account_id.id)])
            #lines = env['account.move.line'].search([('move_id', '=', record.id),('account_id', '=', record.partner_id.property_account_receivable_id.id)])
            #for line in lines:
              #line.write({'account_id':rug_account.x_studio_rug_account.id}) 
            if account_move_lines:
              account_move_lines.write({'account_id':offset_account.x_studio_offset_account.id})   
    record.write({'x_studio_offset_account_updated': True, 'x_studio_gl_account_status': 'Updated'})
  
#stock_move_id
```
  </details>
- **PROJ - Notify Transfer Completion** (`server_action_2185_proj_notify_transfer_completion`, type `next_activity`)
  - Function: Schedules a To-Do activity 'Project Transfer Completed' on the transfer; run by the PROJ Notify Transfer Completion automation. Assignee type is 'specific' but no user is set in the repo.
  - Depends on: `model stock.picking` (stock)
  - Used by: `automation BugFix-Stock.base_automation_199_proj_notify_transfer_completion`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PROJ - Show Validate Block Errors** (`server_action_2181_proj_show_validate_block_errors`, type `code`)
  - Function: Always raises an error asking the user to create the budget for the selected project sales order; not referenced by any view or automation in this repo.
  - Depends on: `model stock.picking` (stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.id:
  raise UserError('Create the budget for the selected project sales order to proceed.')
```
  </details>
- **RR - Re_return Validation** (`server_action_1999_rr_re_return_validation`, type `code`)
  - Function: Button on the transfer form that always raises an error telling the user to perform 'Mark As Done' in the linked task instead.
  - Depends on: `model stock.picking` (stock)
  - Used by: `view BugFix-Stock.ported_view_2387_studio_stock_picking_form`
  <details><summary>code (2 lines)</summary>

```python
if record.id:
  raise UserError('Perform "Mark As Done" in the linked Task to proceed.')
```
  </details>
- **RR - Request Transfer Approval** (`server_action_2204_rr_request_transfer_approval`, type `multi`)
  - Function: Multi-action on transfers meant to chain the transfer-approval request steps; it defines no child actions and no code in this repo, so it currently does nothing.
  - Depends on: `model stock.picking` (stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (11 lines)</summary>

```python
# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: Odoo function to compare floats based on specific precisions
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - UserError: Warning Exception to use with raise
#  - Command: x2Many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **RR - Transfer Approval** (`server_action_2205_rr_transfer_approval`, type `object_write`)
  - Function: Update-record action that sets Transfer Approved (`x_studio_transfer_approved`) to True on the transfer.
  - Depends on: `model stock.picking` (stock), `stock.picking.x_studio_transfer_approved`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **RR - Transfer Approval Request Sent** (`server_action_2201_rr_transfer_approval_request_sent`, type `code`)
  - Function: Calls the transfer's `_repair_studio_update_rug_approval_in_pipeline` method to update the RUG approval status in the repair pipeline after an approval request is sent.
  - Depends on: `model stock.picking` (stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
# fix_repair:idempotent-v1
record._repair_studio_update_rug_approval_in_pipeline()
```
  </details>
- **RR - Transfer Rejection** (`server_action_2207_rr_transfer_rejection`, type `code`)
  - Function: Rejects a transfer: sets its state to Cancelled and Transfer Rejected to 'Yes'.
  - Depends on: `model stock.picking` (stock), `stock.picking.x_studio_transfer_rejected`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
record.write({"state": 'cancel', "x_studio_transfer_rejected": 'Yes'})
```
  </details>
- **RR - Transfer Request Approval - Notify User** (`server_action_2203_rr_transfer_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules an activity on the transfer to notify the approver of a transfer approval request (activity type and user configured on the action, not shown).
  - Depends on: `model stock.picking` (stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (11 lines)</summary>

```python
# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: Odoo function to compare floats based on specific precisions
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - UserError: Warning Exception to use with raise
#  - Command: x2Many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **RR - Update Operation Type in Help Desk Repairs** (`server_action_1996_rr_update_operation_type_in_help_desk_repairs`, type `code`)
  - Function: For repair-return transfers, sets the operation type to the incoming 'Returns' (company 1) or 'Receipts' type for the Return Receipt Location and renames the transfer using the 'purchase.request.seq' sequence (likely the wrong sequence).
  - Depends on: `model ir.sequence` (base), `model res.company` (base), `model stock.picking.type` (stock), `model stock.picking` (stock), `stock.picking.x_studio_repair_return_location`<details><summary>+1 more</summary>`stock.picking.x_studio_return_receipt_location`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (15 lines)</summary>

```python
if record.x_studio_repair_return_location == True:
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  if company.id == 1:
    opt_type = env['stock.picking.type'].search([('default_location_dest_id', '=', record.x_studio_return_receipt_location.id),('code', '=', 'incoming'),('name', '=', 'Returns')],limit=1)
  else:
    opt_type = env['stock.picking.type'].search([('default_location_dest_id', '=', record.x_studio_return_receipt_location.id),('code', '=', 'incoming'),('name', '=', 'Receipts')],limit=1)
  
  if opt_type:
    record['picking_type_id'] = opt_type.id
    
  
    seq = env['ir.sequence'].next_by_code('purchase.request.seq')
    record['name'] = seq
```
  </details>
- **SLS - Validate Payment in Shipment** (`sa_f5_stock_picking_sls_validate_payment_in_shipment`, type `code`)
  - Function: On a done transfer from a Cash sales order without temporary credit, raises an error if posted payments linked to the order total less than the order amount, showing sale, paid and due amounts.
  - Depends on: `model account.payment` (account), `model sale.order` (sale), `model stock.picking` (stock), `stock.picking.sale_id` (sale_stock), `stock.picking.state` (stock)<details><summary>+1 more</summary>`stock.picking.x_studio_sales_order`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (12 lines)</summary>

```python
if record.state == 'done':
  so = env['sale.order'].search([('id', '=', record.sale_id.id),('state', '=', 'done'),('x_studio_order_payment_method', '=', 'Cash'), ('x_studio_grant_temporary_credit', '=', False)],limit=1)
  if so:
      sum_total = 0
      payment = env['account.payment'].search([('x_studio_sales_order', '=', record.sale_id.id),('state', '=', 'posted')])
      if payment:
        for total in payment:
          sum_total += total.amount
              
      if so.amount_total > sum_total:     
        #raise UserError('The Payment Against the Cash Sales Order must be Registered First.')
        raise UserError('The Payment Against the Cash Sales Order must be Registered First.' + '\n'  + '\n' + 'This sale: ' + str(so.amount_total) + '\n' + 'Total payments: ' + str(sum_total) + '\n' + 'Payment due: ' + str(so.amount_total - sum_total))
```
  </details>
- **SLS - Validate Payment in Shipment** (`server_action_1438_sls_validate_payment_in_shipment`, type `code`)
  - Function: Run by the Validate Payment in Shipment automation: for a done delivery from a Cash sales order without temporary credit, blocks it if posted payments are less than the order total, showing amounts due.
  - Depends on: `model account.payment` (account), `model sale.order` (sale), `model stock.picking` (stock), `stock.picking.sale_id` (sale_stock), `stock.picking.state` (stock)<details><summary>+1 more</summary>`stock.picking.x_studio_sales_order`</details>
  - Used by: `automation BugFix-Stock.base_automation_81_sls_validate_payment_in_shipment`
  <details><summary>code (13 lines)</summary>

```python

if record.state == 'done':
  so = env['sale.order'].search([('id', '=', record.sale_id.id),('state', '=', 'done'),('x_studio_order_payment_method', '=', 'Cash'), ('x_studio_grant_temporary_credit', '=', False)],limit=1)
  if so:
      sum_total = 0
      payment = env['account.payment'].search([('x_studio_sales_order', '=', record.sale_id.id),('state', '=', 'posted')])
      if payment:
        for total in payment:
          sum_total += total.amount
              
      if so.amount_total > sum_total:     
        #raise UserError('The Payment Against the Cash Sales Order must be Registered First.')
        raise UserError('The Payment Against the Cash Sales Order must be Registered First.' + '\n'  + '\n' + 'This sale: ' + str(so.amount_total) + '\n' + 'Total payments: ' + str(sum_total) + '\n' + 'Payment due: ' + str(so.amount_total - sum_total))
```
  </details>
- **SLS - Validate Payment in xxx** (`server_action_1774_sls_validate_payment_in_xxx`, type `code`)
  - Function: For a done transfer of a done Cash sales order without temporary credit, sums posted payments linked to the SO and blocks with an error if they are less than the SO total. Not referenced by any automation in this repo.
  - Depends on: `model account.payment` (account), `model sale.order` (sale), `model stock.picking` (stock), `stock.picking.sale_id` (sale_stock), `stock.picking.state` (stock)<details><summary>+1 more</summary>`stock.picking.x_studio_sales_order`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (11 lines)</summary>

```python
if record.state == 'done':
  so = env['sale.order'].search([('id', '=', record.sale_id.id),('state', '=', 'done'),('x_studio_order_payment_method', '=', 'Cash'), ('x_studio_grant_temporary_credit', '=', False)],limit=1)
  if so:
      sum_total = 0
      payment = env['account.payment'].search([('x_studio_sales_order', '=', record.sale_id.id),('state', '=', 'posted')])
      if payment:
        for total in payment:
          sum_total += total.amount
              
      if so.amount_total > sum_total:     
        raise UserError('The Payment Against the Cash Sales Order must be Registered First.')
```
  </details>
- **Supplier Invoice No Update in Import POs** (`server_action_1697_supplier_invoice_no_update_in_import_pos`, type `code`)
  - Function: Copies the Supplier Invoice Number from the transfer's Consignment header onto the transfer; run by the matching automation.
  - Depends on: `model stock.picking` (stock), `model x_consignment_header`, `stock.picking.x_studio_consignment_no`, `stock.picking.x_studio_supplier_invoice_number`
  - Used by: `automation BugFix-Stock.base_automation_104_supplier_invoice_no_update_in_import_pos`
  <details><summary>code (4 lines)</summary>

```python
if record.x_studio_consignment_no:
  consignment = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_no.id)],limit=1)
  if consignment:
    record['x_studio_supplier_invoice_number'] = consignment.x_studio_supplier_invoice_number
```
  </details>
- **Update Source Document in Transfers** (`server_action_1813_update_source_document_in_transfers`, type `code`)
  - Function: Sets the transfer's Source Document (`origin`) to the linked Sales Order name, or blanks it when no Sales Order is set; run by the matching automation.
  - Depends on: `model stock.picking` (stock), `stock.picking.x_studio_sales_order`
  - Used by: `automation BugFix-Stock.base_automation_148_update_source_document_in_transfers`
  <details><summary>code (4 lines)</summary>

```python
if record.x_studio_sales_order.id:
  record['origin'] = record.x_studio_sales_order.name
else:
  record['origin'] = ""
```
  </details>
- **User Location Validation** (`sa_f5_stock_picking_user_location_validation`, type `code`)
  - Function: For non-admin users, when the transfer is flagged for user location validation, raises an error naming the source or destination location the user may not use and listing the locations they are permitted for (internal transfers vs other operation types use different permission fields).
  - Depends on: `model res.company` (base), `model stock.location` (stock), `model stock.picking` (stock), `stock.picking.location_dest_id` (stock), `stock.picking.location_id` (stock)<details><summary>+3 more</summary>`stock.picking.x_studio_type_of_operation`, `stock.picking.x_studio_user_location_validation_2`, `stock.picking.x_studio_user_location_validation`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (83 lines)</summary>

```python
if user.id != 1:

  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]

  company = env['res.company'].browse(company_id)

  

  if record.x_studio_user_location_validation == True:

    if record.x_studio_user_location_validation_2 == True:

      warehouse = record.location_id.complete_name

    else:

      warehouse = record.location_dest_id.complete_name 

    

    if record.x_studio_type_of_operation == 'internal':

      loc = env['stock.location'].search([('x_studio_users_internal_transfer', '=', user.id),('active', '=', True),('company_id', '=', company.id)])

      if loc:

        locations = ""

        for locs in loc:

          locations += (locs.complete_name + "\n")

        

        if record.x_studio_user_location_validation_2 == True:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for internal operation types.' + "\n" + "\n" + locations)

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for internal operation types.' + "\n" + "\n" + locations)

      else:

        if record.x_studio_user_location_validation_2 == True:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for internal operation types.')

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for internal operation types.') 

    else:

      loc = env['stock.location'].search([('x_studio_users_stock_location', 'ilike', user.id),('active', '=', True),('company_id', '=', company.id)])

      if loc:

        locations = ""

        for locs in loc:

          locations += (locs.complete_name + "\n")

        

        if record.x_studio_user_location_validation_2 == True:  

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for operation types not in internal.' + "\n" + "\n" + locations)

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for operation types not in internal.' + "\n" + "\n" + locations)

      else:

        if record.x_studio_user_location_validation_2 == True: 

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for operation types not in internal.')

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for operation types not in internal.')
```
  </details>
- **User Location Validation** (`server_action_2474_user_location_validation`, type `code`)
  - Function: Run by the User Location Validation automation: for non-admin users on flagged transfers, raises an error naming the disallowed source/destination location and listing the locations the user is permitted for.
  - Depends on: `model res.company` (base), `model stock.location` (stock), `model stock.picking` (stock), `stock.picking.location_dest_id` (stock), `stock.picking.location_id` (stock)<details><summary>+3 more</summary>`stock.picking.x_studio_type_of_operation`, `stock.picking.x_studio_user_location_validation_2`, `stock.picking.x_studio_user_location_validation`</details>
  - Used by: `automation BugFix-Stock.base_automation_246_user_location_validation`
  <details><summary>code (84 lines)</summary>

```python

if user.id != 1:

  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]

  company = env['res.company'].browse(company_id)

  

  if record.x_studio_user_location_validation == True:

    if record.x_studio_user_location_validation_2 == True:

      warehouse = record.location_id.complete_name

    else:

      warehouse = record.location_dest_id.complete_name 

    

    if record.x_studio_type_of_operation == 'internal':

      loc = env['stock.location'].search([('x_studio_users_internal_transfer', '=', user.id),('active', '=', True),('company_id', '=', company.id)])

      if loc:

        locations = ""

        for locs in loc:

          locations += (locs.complete_name + "\n")

        

        if record.x_studio_user_location_validation_2 == True:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for internal operation types.' + "\n" + "\n" + locations)

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for internal operation types.' + "\n" + "\n" + locations)

      else:

        if record.x_studio_user_location_validation_2 == True:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for internal operation types.')

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" + 'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for internal operation types.') 

    else:

      loc = env['stock.location'].search([('x_studio_users_stock_location', 'ilike', user.id),('active', '=', True),('company_id', '=', company.id)])

      if loc:

        locations = ""

        for locs in loc:

          locations += (locs.complete_name + "\n")

        

        if record.x_studio_user_location_validation_2 == True:  

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for operation types not in internal.' + "\n" + "\n" + locations)

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'Only the below listed warehouses are permitted for the current logged-in user for operation types not in internal.' + "\n" + "\n" + locations)

      else:

        if record.x_studio_user_location_validation_2 == True: 

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Source Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for operation types not in internal.')

        else:

          raise UserError('The current logged-in user does not have access to below listed warehouse.' + "\n" + "\n" +'Destination Location:' + "\n" + warehouse + "\n" + "\n" + 'There are no permitted warehouses set up for the current logged-in user for operation types not in internal.')
```
  </details>
- **User Location Validation-TEST** (`sa_f5_stock_picking_user_location_validation_test`, type `code`)
  - Function: Test action: creates an `x_test02` record holding the transfer's source and destination location names. Debug/test logic only.
  - Depends on: `model stock.picking` (stock), `model x_test02` (BugFix-Studio-Misc), `stock.picking.location_dest_id` (stock), `stock.picking.location_id` (stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
imp_header_charges = env['x_test02'].create({'x_name':record.location_id.complete_name,'x_studio_name_1':record.location_dest_id.complete_name})
```
  </details>
- **User Location Validation-TEST** (`server_action_2489_user_location_validation_test`, type `code`)
  - Function: Run by a test automation: creates an `x_test02` record with the transfer's source and destination location names. Debug/test only.
  - Depends on: `model stock.picking` (stock), `model x_test02` (BugFix-Studio-Misc), `stock.picking.location_dest_id` (stock), `stock.picking.location_id` (stock)
  - Used by: `automation BugFix-Stock.base_automation_247_user_location_validation_test`
  <details><summary>code (2 lines)</summary>

```python

imp_header_charges = env['x_test02'].create({'x_name':record.location_id.complete_name,'x_studio_name_1':record.location_dest_id.complete_name})
```
  </details>
**Automations (8):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Update Consignment - Partial GRN | `base_automation_63_imp_update_consignment_partial_grn` | archived | When a record is created on Transfer and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model stock.picking` (stock) |  |
| PROJ - Notify Transfer Completion | `base_automation_199_proj_notify_transfer_completion` |  | When a record is created or updated on Transfer and `[('sale_id.x_studio_quotation_type', '=', 'Project'), ('state', '=', 'done')]`, runs _PROJ - Notify Transfer Completion_. | `model stock.picking` (stock)<br>`sale.order.x_studio_quotation_type` (BugFix-Sales)<br>`server action BugFix-Stock.server_action_2185_proj_notify_transfer_completion`<br>`stock.picking.sale_id` (sale_stock)<br>`stock.picking.state` (stock) |  |
| RR - Update Operation Type in Help Desk Repairs | `base_automation_177_rr_update_operation_type_in_help_desk_repairs` | archived | When a record is created on Transfer, runs nothing (no action linked). **Archived — does not run.** | `model stock.picking` (stock) |  |
| SLS - Validate Payment in Shipment | `base_automation_81_sls_validate_payment_in_shipment` | archived | When a record is updated on Transfer, runs _SLS - Validate Payment in Shipment_. **Archived — does not run.** | `model stock.picking` (stock)<br>`server action BugFix-Stock.server_action_1438_sls_validate_payment_in_shipment` |  |
| Supplier Invoice No Update in Import POs | `base_automation_104_supplier_invoice_no_update_in_import_pos` |  | When a watched field changes in the form on Transfer, runs _Supplier Invoice No Update in Import POs_. | `model stock.picking` (stock)<br>`server action BugFix-Stock.server_action_1697_supplier_invoice_no_update_in_import_pos`<br>`stock.picking.x_studio_consignment_no` |  |
| Update Source Document in Transfers | `base_automation_148_update_source_document_in_transfers` |  | When a watched field changes in the form on Transfer, runs _Update Source Document in Transfers_. | `model stock.picking` (stock)<br>`server action BugFix-Stock.server_action_1813_update_source_document_in_transfers`<br>`stock.picking.x_studio_sales_order` |  |
| User Location Validation | `base_automation_246_user_location_validation` | archived | When a record is created or updated on Transfer and `["|","|","|",["state","=","draft"],["state","=","waiting"],["state","=","confirmed"],["state","=","assigned"]]`, runs _User Location Validation_. **Archived — does not run.** | `model stock.picking` (stock)<br>`server action BugFix-Stock.server_action_2474_user_location_validation`<br>`stock.picking.state` (stock) |  |
| User Location Validation-TEST | `base_automation_247_user_location_validation_test` | archived | When a record is updated on Transfer and `[["state","=","draft"]]`, runs _User Location Validation-TEST_. **Archived — does not run.** | `model stock.picking` (stock)<br>`server action BugFix-Stock.server_action_2489_user_location_validation_test`<br>`stock.picking.state` (stock) |  |

**Approval rules (3):**

| Name | Record name | Approver group | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Transfer/action_cancel (Inventory / Jin - Administrator) (102) | `approval_rule_102_transfer_action_cancel_inventory_jin_administrator_102` | Inventory / Administrator | Before button/method `action_cancel` on Transfer runs, an approval from **Inventory / Administrator** is required (step 1). | `group stock.group_stock_manager` (stock)<br>`model stock.picking` (stock)<br>`stock.picking.action_cancel()` (Odoo) |  |
| Transfer/action_open_label_layout (Administration / Access Rights) (56) | `approval_rule_56_transfer_action_open_label_layout_administration_access_righ` | Administration / Access Rights | Before button/method `action_open_label_layout` on Transfer runs, an approval from **Administration / Access Rights** is required (step 1). | `group base.group_erp_manager` (base)<br>`model stock.picking` (stock)<br>`stock.picking.action_open_label_layout()` (Odoo) |  |
| Transfer/action_put_in_pack (User types / Internal User) (62) | `approval_rule_62_transfer_action_put_in_pack_user_types_internal_user_62` | User types / Internal User | Before button/method `action_put_in_pack` on Transfer runs, an approval from **User types / Internal User** is required (step 1). | `group base.group_user` (base)<br>`model stock.picking` (stock)<br>`stock.picking.action_put_in_pack()` (Odoo) |  |

**Window actions (15):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| New Button | `aw_f4_stock_picking_new_button` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_maintenance_request_', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_maintenance_request_` |  |
| New Button | `action_1714_new_button` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_maintenance_request_', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_maintenance_request_` |  |
| New Button | `act_window_1714_new_button` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_maintenance_request_', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_maintenance_request_` |  |
| Picking | `act_window_2017_picking` | Opens **Transfer** records (form). | `model stock.picking` (stock) |  |
| Repair Trans. | `aw_f4_stock_picking_repair_trans` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_created_from_help_ticket', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_created_from_help_ticket` |  |
| Repair Trans. | `action_2008_repair_trans` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_created_from_help_ticket', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_created_from_help_ticket` |  |
| Repair Trans. | `act_window_2008_repair_trans` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_created_from_help_ticket', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_created_from_help_ticket` |  |
| Transfers | `aw_f4_stock_picking_transfers` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_created_from_material_request_no', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_created_from_material_request_no` |  |
| Transfers | `action_2409_transfers` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_created_from_material_request_no', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_created_from_material_request_no` | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| Transfers | `act_window_2409_transfers` | Opens **Transfer** records (tree,form), filtered to `[('x_studio_created_from_material_request_no', '=', active_id)]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_created_from_material_request_no` |  |
| stock.picking | `aw_f4_stock_picking_stock_picking` | Opens **Transfer** records (kanban,tree,form,calendar,map). | `model stock.picking` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_picking` (BugFix-Studio-Misc) |
| stock.picking | `action_2536_stock_picking` | Opens **Transfer** records (kanban,tree,form,calendar,map). | `model stock.picking` (stock) |  |
| stock.picking | `action_1978_stock_picking` | Opens **Transfer** records (kanban,tree,form,calendar,map). | `model stock.picking` (stock) |  |
| stock.picking | `act_window_2536_stock_picking` | Opens **Transfer** records (kanban,tree,form,calendar,map). | `model stock.picking` (stock) |  |
| stock.picking | `act_window_1978_stock_picking` | Opens **Transfer** records (kanban,tree,form,calendar,map). | `model stock.picking` (stock) |  |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.picking.form customization | `ported_view_2387_studio_stock_picking_form` | form | set help='Verify if the required products are available in stock. ' on `//button[@name='action_assign']`; after `//button[@name='action_assign']`: add button 'Update Consignment'; set help=The transfer order is ready to be processed, but the actual transfer has not been executed yet. on `//form[1]/header[1]/button[@name='action_confirm']`; set groups=, help=Confirm or finalize the transaction on `//form[1]/header[1]/button[@name='button_validate']`; set help=Confirm or finalize the transaction on `//form[1]/header[1]/button[@name='button_validate'][2]`; set studio_approval=True on `//button[@name='action_open_label_type']`; set groups=stock.group_stock_user on `//button[@name='852']`; after `//button[@name='852']`: add button 'Dispatch', button 'Retun Reject Reason' … | Large Studio customization of the Transfer form: help texts, Update Consignment, Dispatch, Return Reject Reason and other action buttons, approval flags, and partner, operation type and source location readonly/required/visibility rules. Uses hardcoded numeric action ids (2007, 870, 852 etc.). | `server action BugFix-Stock.server_action_1367_imp_update_consignment_final`<br>`server action BugFix-Stock.server_action_1999_rr_re_return_validation`<br>`stock.picking.partner_id` (stock)<br>`stock.picking.purchase_id` (purchase_stock)<br>`stock.picking.sale_id` (sale_stock)<details><summary>+53 more</summary>`stock.picking.state` (stock)<br>`stock.picking.x_studio_analytic_account` (BugFix-Analytics)<br>`stock.picking.x_studio_budget_created`<br>`stock.picking.x_studio_cancelled`<br>`stock.picking.x_studio_cash_full_payment_made`<br>`stock.picking.x_studio_consignment_no`<br>`stock.picking.x_studio_created_from_help_ticket`<br>`stock.picking.x_studio_created_from_material_request_no`<br>`stock.picking.x_studio_custom_clearance_no`<br>`stock.picking.x_studio_factory_repair`<br>`stock.picking.x_studio_fsm_task_done`<br>`stock.picking.x_studio_fully_paid_so`<br>`stock.picking.x_studio_gl_account_status`<br>`stock.picking.x_studio_helpdesk_ticket_id`<br>`stock.picking.x_studio_journal_type`<br>`stock.picking.x_studio_maintenance_request_`<br>`stock.picking.x_studio_mj_in`<br>`stock.picking.x_studio_mj_out`<br>`stock.picking.x_studio_movement_journal`<br>`stock.picking.x_studio_need_approval`<br>`stock.picking.x_studio_offset_account_updated`<br>`stock.picking.x_studio_picking_count`<br>`stock.picking.x_studio_pr_type`<br>`stock.picking.x_studio_quotation_type_2`<br>`stock.picking.x_studio_quotation_type`<br>`stock.picking.x_studio_received_at_centre`<br>`stock.picking.x_studio_repair_payment_made`<br>`stock.picking.x_studio_repair_return_location`<br>`stock.picking.x_studio_return_receipt_location`<br>`stock.picking.x_studio_return_sequence`<br>`stock.picking.x_studio_sales_order`<br>`stock.picking.x_studio_sequence_code`<br>`stock.picking.x_studio_supplier_invoice_number_1`<br>`stock.picking.x_studio_supplier_invoice_number`<br>`stock.picking.x_studio_task_status`<br>`stock.picking.x_studio_ticket_sales_order`<br>`stock.picking.x_studio_transfer_approval`<br>`stock.picking.x_studio_transfer_approved`<br>`stock.picking.x_studio_transfer_rejected`<br>`stock.picking.x_studio_transfer_request_sent`<br>`stock.picking.x_studio_type_of_operation`<br>`stock.picking.x_studio_update_consignment`<br>`stock.picking.x_studio_user_location_validation_2`<br>`stock.picking.x_studio_user_location_validation`<br>`stock.picking.x_studio_valid_factory_repair`<br>`stock.picking.x_studio_valid_transfer_lines`<br>`stock.picking.x_studio_validation`<br>`stock.picking.x_x_studio_create_from_transfer_1__account_move_count`<br>`stock.picking.x_x_studio_created_from_transfer__account_move_count`<br>`view stock.view_picking_form` (stock)<br>`window action BugFix-Stock.act_1362_vend_dispatch_reversal`<br>`window action BugFix-Stock.act_1363_custom_clearance_reversal`<br>`window action stock.act_stock_return_picking` (stock)</details> |  |
| Odoo Studio: stock.picking.form_button | `view_4732_odoo_studio_stock_picking_form_button_e` | form | inside `//form`: add field x_studio_budget_created, field x_studio_cancelled, field x_studio_cash_full_payment_made, field x_studio_created_from_help_ticket, field x_studio_factory_repair, field x_studio_fsm_task_done, field x_studio_fully_paid_so, field x_studio_helpdesk_ticket_id, field x_studio_need_approval, field x_studio_picking_count, field x_studio_pr_type, field x_studio_quotation_type_2 …; set invisible=((x_studio_task_status == False) and (x_studio_helpdesk_ticket_id != False)) or ((state != 'done') or (x_studio_helpdesk_ticket_id != False)) on `//header/button[@name='870']`; after `//header/button[@name='action_assign']`: add ; before `//header/button[@name='870']`: add button 'Dispatch'; before `//header/button[@name='870'][2]`: add ; set invisible=((x_studio_budget_created == False) and (x_studio_quotation_type_2 == 'Project')) or (((x_studio_update_consignment == False) and (x_studio_pr_type == 'Import')) or (((x_studio_repair_payment_made == False) and (x_studio_quotation_type_2 == 'Repair')) or ((show_validate == False) or ((state in ('waiting', 'confirmed')) or ((x_studio_transfer_rejected == True) or ((x_studio_valid_transfer_lines == False) or (x_studio_cancelled == True))))))) on `//header/button[@name='button_validate']`; set invisible=(immediate_transfer == True) or ((show_validate == False) or ((x_studio_helpdesk_ticket_id != False) or (x_studio_pr_type == 'Import'))) on `//header/button[@name='action_set_quantities_to_reservation']`; set readonly=((x_studio_update_consignment == True) and (x_studio_pr_type == 'Import')) or ((is_locked == True) and (state == 'done')) on `//sheet/notebook/page/field[@name='move_ids_without_package']` … | Inactive (archived) Studio customization of the Transfer form adding Dispatch button rules and Validate/Set Quantities/Mark as To Do visibility conditions; has no effect while inactive. | `stock.picking.state` (stock)<br>`stock.picking.x_studio_budget_created`<br>`stock.picking.x_studio_cancelled`<br>`stock.picking.x_studio_cash_full_payment_made`<br>`stock.picking.x_studio_created_from_help_ticket`<details><summary>+18 more</summary>`stock.picking.x_studio_factory_repair`<br>`stock.picking.x_studio_fsm_task_done`<br>`stock.picking.x_studio_fully_paid_so`<br>`stock.picking.x_studio_helpdesk_ticket_id`<br>`stock.picking.x_studio_need_approval`<br>`stock.picking.x_studio_picking_count`<br>`stock.picking.x_studio_pr_type`<br>`stock.picking.x_studio_quotation_type_2`<br>`stock.picking.x_studio_received_at_centre`<br>`stock.picking.x_studio_repair_payment_made`<br>`stock.picking.x_studio_task_status`<br>`stock.picking.x_studio_transfer_approved`<br>`stock.picking.x_studio_transfer_rejected`<br>`stock.picking.x_studio_update_consignment`<br>`stock.picking.x_studio_valid_factory_repair`<br>`stock.picking.x_studio_valid_transfer_lines`<br>`view stock.view_picking_form` (stock)<br>`window action stock.act_stock_return_picking` (stock)</details> |  |
| Odoo Studio: stock.picking.tree customization | `ported_view_5299_studio_stock_picking_tree` | tree | set create=true on `//tree[1]`; after `//field[@name='state']`: add field x_studio_movement_journal, field x_studio_gl_account_status | Allows creating from the Transfers list and adds a hidden Movement Journal column plus an optional GL Account Status badge shown only for movement-journal transfers. | `stock.picking.x_studio_gl_account_status`<br>`stock.picking.x_studio_movement_journal`<br>`view stock.vpicktree` (stock) |  |
| stock.picking.form.hide.dev.extras | `view_stock_picking_form_hide_dev_extras` | form | set invisible=1 on `//field[@name='is_subcontract']`; set invisible=1 on `//field[@name='show_subcontracting_details_visible']`; set invisible=1 on `//field[@name='subcontracting_source_purchase_count']`; set invisible=1 on `//button[@name='action_record_components']`; set invisible=1 on `//button[@name='action_show_subcontract_details']`; set invisible=1 on `//button[@name='action_view_subcontracting_source_purchase']`; set invisible=1 on `//button[@name='action_retry_amazon_sync']`; set invisible=1 on `//field[@name='eway_bill_number']` | Hides fields and buttons added by other installed addons on the Transfer form: subcontracting fields and buttons, the Amazon retry-sync button and the India e-way bill number. | `view stock.view_picking_form` (stock) |  |

**Record rules (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Block Operations | `rule_460_block_operations` | For everyone (global rule): read/write/create/delete on Transfer only where `[('x_studio_type_of_operation', '=', 'internal')]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_type_of_operation` |  |
| Kap-Operation Control | `rule_452_kap_operation_control` | For everyone (global rule): read/write/create/delete on Transfer only where `['&', (1, '=', 1), '|', '|', '|', '&', ('x_studio_sequence_code', '=', 'INT'), ('origin', '=', False), '&', ('x_studio_sequence_code', '=', 'MJ/OUT'), ('origin', '=', False), '&', ('x_studio_sequence_code', '=', 'MJ/IN'), ('origin', '=', False), '&', ('x_studio_sequence_code', '!=', 'INT'), ('origin', '!=', False)]`. | `model stock.picking` (stock)<br>`stock.picking.origin` (stock)<br>`stock.picking.x_studio_sequence_code` |  |
| Kap-Operation Control 2 | `rule_912_kap_operation_control_2` | For everyone (global rule): read/write/create/delete on Transfer only where `['&', (1, '=', 1), '|', '|', '|', '&', ('x_studio_sequence_code', '=', 'INT'), ('origin', '=', False), '&', ('x_studio_sequence_code', '=', 'MJ/OUT'), ('origin', '=', False), '&', ('x_studio_sequence_code', '=', 'MJ/IN'), ('origin', '=', False), '&', ('x_studio_sequence_code', '!=', 'INT'), ('origin', '!=', False)]`. | `model stock.picking` (stock)<br>`stock.picking.origin` (stock)<br>`stock.picking.x_studio_sequence_code` |  |
| Transfer Type Block | `rule_458_transfer_type_block` | For everyone (global rule): read/write/create/delete on Transfer only where `['&', '!', (0, '=', 1), ('x_studio_type_of_operation', '=', 'internal')]`. | `model stock.picking` (stock)<br>`stock.picking.x_studio_type_of_operation` |  |
