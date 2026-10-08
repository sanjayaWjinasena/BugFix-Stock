# BugFix-Stock — `x_consignment_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_consignment_header` — Consignment Header

*Created by this repo.* Python: `models/x_consignment_header.py`, `models/x_consignment_header_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_consignment_header_x_consignment_header_purchase_jin_po_invoicing_payment_impor` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_x_consignment_header_x_consignment_header_purchase_jin_procurement_end_user_impor` (BugFix-Studio-Misc)<br>`account.bank.statement.line.x_studio_co` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_consignment_no` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_created_from_consignment_1` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_created_from_consignment_2` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_created_from_consignment` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_many2one_field_A197A` (BugFix-Accounting)<details><summary>+29 more</summary>`account.bank.statement.line.x_studio_many2one_field_jslCp` (BugFix-Accounting)<br>`account.bank.statement.line.x_studio_many2one_field_mucWu` (BugFix-Accounting)<br>`account.move.x_studio_co` (BugFix-Accounting)<br>`account.move.x_studio_consignment_no` (BugFix-Accounting)<br>`account.move.x_studio_created_from_consignment_1` (BugFix-Accounting)<br>`account.move.x_studio_created_from_consignment` (BugFix-Accounting)<br>`account.payment.x_studio_co` (BugFix-Accounting)<br>`account.payment.x_studio_consignment_no` (BugFix-Accounting)<br>`account.payment.x_studio_created_from_consignment_1` (BugFix-Accounting)<br>`account.payment.x_studio_created_from_consignment_2` (BugFix-Accounting)<br>`account.payment.x_studio_created_from_consignment` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_A197A` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_jslCp` (BugFix-Accounting)<br>`account.payment.x_studio_many2one_field_mucWu` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1370_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1766_supplier_invoice_no_update_in_import_vendor_bill` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1847_supplier_invoice_no_update_in_import_vendor_bill_2` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`x_temp_tp_invoice_head.x_studio_consignment_header_id` (BugFix-Accounting)<br>`x_temp_tp_invoice_line.x_studio_consignment_id` (BugFix-Accounting)<br>`x_tp_invoice_header.x_studio_con_no` (BugFix-Accounting)<br>`x_tp_invoice_line.x_studio_consignment_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:x_consignment_header -->
A Consignment Header is an import shipment from an overseas supplier, also shown as a purchase invoice, and is the centre of the imports process. It holds the vendor, currency, supplier invoice details, uploaded shipping documents, container and customs clearance details, cost allocation method and accounts, and moves through statuses from Draft through In Transit and Under Custom Clearance to Done and TP Invoice. Buttons on its form copy import PO lines in, record vendor despatch, port receipt and customs duty entries, create, allocate and reset header charges, confirm the purchase invoice, validate consolidation and copy charges to the TP invoice. Automations number the consignment, set the company and supplier currency, copy the cost allocation method from the Imports Ledger Setup and block deleting non-Draft consignments.
<!-- /SUMMARY -->

**Fields (83):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_consignment_header.activity_summary`<br>`x_consignment_header.activity_type_icon`<br>`x_consignment_header.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_consignment_header.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_consignment_header.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_consignment_header.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) |  |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) |  |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for consignments; defaults to active, inactive records show an Archived ribbon. | stored |  | `default BugFix-Stock.default_138_x_consignment_header_x_active`<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.view_2812_default_search_view_for_x_consignment_header_e` |
| `x_color` | Color | integer | Color index for the consignment; not used by any view or logic. | stored |  |  |
| `x_name` | Invoice Reference | char | Consignment (invoice) reference number, generated by the 'Consignment Details Seq. No' action on create; used in charge allocation and custom duty entries. | stored |  | `default BugFix-Stock.default_142_x_consignment_header_x_name`<br>`server action BugFix-Stock.sa_f5_x_consignment_header_imp_consignment_details_seq_no`<br>`server action BugFix-Stock.server_action_1258_imp_consignment_details_seq_no`<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<details><summary>+4 more</summary>`view BugFix-Stock.ported_view_2810_default_list_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.view_2812_default_search_view_for_x_consignment_header_e`<br>`view BugFix-Stock.view_2949_default_kanban_view_for_ir_model_905_e`</details> |
| `x_studio_account_charge` | Account Charge | many2one → `account.account` | G/L account used for posting clearance charges in the Custom Duty action. | stored | `model account.account` (account) | `server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_account_duty` | Account Duty | many2one → `account.account` | G/L account used for posting customs duty in the Custom Duty action. | stored | `model account.account` (account) | `server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_account_tax` | Account Tax | many2one → `account.account` | G/L account used for posting import taxes in the Custom Duty action. | stored | `model account.account` (account) | `server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_allocate_header_charges` | Allocate Header Charges | boolean | Flag requesting allocation of header charges to the consignment lines; used by the Allocate and Reset Header Charges actions. | stored |  | `default BugFix-Stock.default_167_x_consignment_header_x_studio_allocate_header_ch`<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.server_action_2199_imp_reset_header_charges_consignment`<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_bill_of_lading` | Bill of Lading | binary | Uploaded Bill of Lading document; required/checked by the Vendor Dispatch action. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_bill_of_lading_filename` | Filename for x_studio_binary_field_LzgTH | char | File name of the uploaded Bill of Lading. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_cargo_arrival_notice` | Cargo Arrival Notice | binary | Uploaded Cargo Arrival Notice; checked by the Port Receipt action. | stored |  | `server action BugFix-Stock.server_action_1313_imp_consignment_port_receipt`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_cargo_arrival_notice_filename` | Filename for x_studio_binary_field_M4Ehh | char | File name of the uploaded Cargo Arrival Notice; not shown in any view. | stored |  |  |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the consignment; set to the current company on create, used by the multi-company rule and by the dispatch and custom duty actions. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_512_jin_multi_company_consignment_header`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.sa_f5_x_consignment_header_jin_company_id_in_consignment_header`<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<details><summary>+3 more</summary>`server action BugFix-Stock.server_action_2607_jin_company_id_in_consignment_header`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`</details> |
| `x_studio_con_validated` | Con. Validated | boolean | Flag showing the consignment has been validated; shown on the consignment form. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_confirm_invoice` | Confirm Invoice | boolean | Flag set when the purchase invoice for the consignment is confirmed by the Confirm Purchase Invoice action. | stored |  | `server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_consignment_line_ids` | Consignment Line Ids | one2many → `x_consignment_line` | Products/PO lines included in the consignment; used when copying charges to the TP invoice. | stored | `model x_consignment_line` | `server action BugFix-Stock.server_action_1377_imp_copy_charges_to_tp_invoice`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_consolidated` | Consolidated | boolean | Flag showing the consignment has been included in a consolidation. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_consolidation_confirmed` | Consolidation Confirmed | boolean | Flag set when the consolidation containing this consignment is confirmed; used by the Validate Consolidation action. | stored |  | `server action BugFix-Stock.server_action_1456_imp_validate_consolidation_in_consignment`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_container_no` | Container No | char | Container number of the shipment; shown on the consignment form and list. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header` |
| `x_studio_cost_allocation_method` | Cost Allocation Method | selection: equal=Equal; by_quantity=By Quantity; by_current_cost_price=By Current Cost; by_weight=By Weight; by_volume=By Volume | How landed costs are split over lines (Equal, By Quantity, By Current Cost, By Weight, By Volume); used by the Confirm Purchase Invoice action. | stored |  | `server action BugFix-Stock.sa_f5_x_consignment_header_imp_update_cost_allocation_method_in_consignment`<br>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.server_action_1454_imp_update_cost_allocation_method_in_consignment`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_create_header_charges` | Create Header Charges | boolean | Flag requesting creation of header charges from the charge structure; used by the Create Header Charges action. | stored |  | `default BugFix-Stock.default_168_x_consignment_header_x_studio_create_header_char`<br>`server action BugFix-Stock.server_action_1316_imp_create_consignment_header_charges`<br>`view BugFix-Purchase.view_x_consignment_header_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Supplier currency of the consignment, defaulted and updated from the vendor; used in dispatch, charge allocation and custom duty entries. | stored | `model res.currency` (base) | `default BugFix-Stock.default_425_x_consignment_header_x_studio_currency_id`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.sa_f5_x_consignment_header_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<details><summary>+6 more</summary>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_2890_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header`</details> |
| `x_studio_custom_clearance` | Custom Clearance | boolean | Flag indicating the consignment has gone through customs clearance; used by the Custom Duty action. | stored |  | `server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_custom_clearance_exchange_rate` | Custom Clearance Exchange Rate | float | Exchange rate applied at customs clearance; used by the Custom Duty action. | stored |  | `server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_custom_clearance_no` | Custom Clearance No | char | Customs clearance number; used by the Custom Duty action and mirrored on journal entries. | stored |  | `account.move.x_studio_custom_clearance_no` (BugFix-Accounting)<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_custom_cleared_date` | Custom Cleared Date | date | Date the consignment was cleared by customs; used by header charge creation/allocation and the Custom Duty action. | stored |  | `server action BugFix-Stock.server_action_1316_imp_create_consignment_header_charges`<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_description` | Description | char | Free-text description of the consignment; set when PO lines are copied in. | stored |  | `server action BugFix-Stock.server_action_1263_imp_copy_po_lines_to_consignment`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header` |
| `x_studio_header_charges_allocated` | Header Charges Allocated | boolean | Flag set once header charges have been allocated to lines; cleared by the Reset Header Charges action. | stored |  | `server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.server_action_2199_imp_reset_header_charges_consignment`<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_invoice_date` | Supplier's Invoice Date (Bill Date) | date | Supplier's invoice (bill) date for the consignment. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header` |
| `x_studio_lines_copied` | Lines Copied | boolean | Flag showing PO lines have been copied into the consignment; reset by the Clear PO Lines action and used for button visibility. | stored |  | `server action BugFix-Stock.server_action_1303_imp_clear_po_lines_from_consignment`<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_offset_account` | Offset Account | many2one → `account.account` | Offset G/L account used by the Custom Duty journal entry. | stored | `model account.account` (account) | `server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_packing_list` | Packing List | binary | Uploaded packing list document; checked by the Confirm Purchase Invoice action. | stored |  | `server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_packing_list_filename` | Filename for x_studio_binary_field_xDIyn | char | File name of the uploaded packing list; not shown in any view. | stored |  |  |
| `x_studio_sequence` | Sequence | integer | Ordering number for consignments (list drag handle). | stored |  | `default BugFix-Stock.default_139_x_consignment_header_x_studio_sequence`<br>`view BugFix-Stock.ported_view_2810_default_list_view_for_x_consignment_header` |
| `x_studio_shipment_start_date` | Shipment Start Date | date | Date the shipment started. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header` |
| `x_studio_shipping_mode` | Shipping Mode | selection: Air=Air; Sea=Sea; Road=Road; Courier=Courier | Shipping mode: Air, Sea, Road or Courier; has a default value. | stored |  | `default BugFix-Stock.default_143_x_consignment_header_x_studio_shipping_mode`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header` |
| `x_studio_status` | Status | selection: Draft=Draft; Consignment=Confirmed; Consolidated=Consolidated; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done; TP Invoice=TP Invoice | Consignment workflow status (Draft, Confirmed, Consolidated, In Transit, Under Custom Clearance, Done, TP Invoice); advanced by the dispatch, port receipt, custom duty and invoice actions and checked before delete. | stored |  | `default BugFix-Stock.default_144_x_consignment_header_x_studio_status`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.sa_f5_x_consignment_header_imp_restrict_delete_in_consignment`<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1313_imp_consignment_port_receipt`<details><summary>+12 more</summary>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`server action BugFix-Stock.server_action_1324_imp_restrict_delete_in_consignment`<br>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.server_action_1377_imp_copy_charges_to_tp_invoice`<br>`server action BugFix-Stock.server_action_1456_imp_validate_consolidation_in_consignment`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Purchase.view_x_consignment_header_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header`<br>`view BugFix-Stock.view_2949_default_kanban_view_for_ir_model_905_e`</details> |
| `x_studio_status_bar` | Status Bar | selection: Draft=Draft; Consignment=Confirmed; Consolidated=Consolidated; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done; TP Invoice=TP Invoice | Status bar copy of the consignment status, updated by the same workflow actions and shown in the form header. | stored |  | `default BugFix-Stock.default_145_x_consignment_header_x_studio_status_bar`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1313_imp_consignment_port_receipt`<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<details><summary>+5 more</summary>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.server_action_1456_imp_validate_consolidation_in_consignment`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`</details> |
| `x_studio_supplier_document` | Purchase Invoice | binary | Uploaded supplier purchase invoice; checked by the Vendor Dispatch and Confirm Purchase Invoice actions. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<details><summary>+1 more</summary>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`</details> |
| `x_studio_supplier_document_filename` | Filename for x_studio_binary_field_KSsMR | char | File name of the uploaded purchase invoice; not shown in any view. | stored |  |  |
| `x_studio_supplier_id` | Vendor | many2one → `res.partner` | Vendor of the consignment; drives the supplier currency and is used when copying PO lines, dispatching and confirming the invoice. | stored | `model res.partner` (base) | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.sa_f5_x_consignment_header_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.server_action_1263_imp_copy_po_lines_to_consignment`<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<details><summary>+6 more</summary>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_2890_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header`<br>`view BugFix-Stock.view_2949_default_kanban_view_for_ir_model_905_e`</details> |
| `x_studio_supplier_invoice_number` | Supplier's Invoice No (Bill Reference) | char | Supplier's invoice number (bill reference) for the consignment; used in dispatch and custom duty entries. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<details><summary>+2 more</summary>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header`</details> |
| `x_studio_total_allocate_amount` | Total Allocate Amount | float | Read-only total of header charges allocated; used by the Allocate Header Charges action. | stored |  | `server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_total_amount` | Total Amount | float | Read-only total value of the consignment; used by dispatch and charge allocation and shown in the kanban card. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<details><summary>+2 more</summary>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.view_2949_default_kanban_view_for_ir_model_905_e`</details> |
| `x_studio_total_amount_cost_allocation_method` | Total Amount Cost Allocation Method | float | Read-only total used as the basis for the selected cost allocation method; shown on the form. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_vend_dispatch_status` | Vend. Dispatch Status | text | Text message describing the result of the vendor dispatch, written by the Vendor Dispatch action. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_vendor_dispatch` | Vendor Dispatch | boolean | Flag set when the vendor has dispatched the consignment (Vendor Dispatch action). | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_vendor_dispatch_exchange_rate` | Vendor Dispatch Exchange Rate | float | Exchange rate used for the vendor dispatch entry. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_voucher_date` | Vendor Dispatch Voucher Date | date | Voucher date used for the vendor dispatch accounting entry. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_2118_project_update_month_end_entries`<br>`server action BugFix-Stock.server_action_3647_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_x_studio_con_no__x_tp_invoice_header_count` | Created From Consignment No count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. | not stored |  |  |
| `x_x_studio_consignment_id__x_consignment_charge_h_count` | Consignment Id count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_x_studio_consignment_id__x_consignment_charge_l_count` | Consignment Id count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_x_studio_created_from_consignment_1__account_move_count` | Created From Consignment count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_x_studio_created_from_consignment__account_move_count` | Created From Consignment count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |

**Server actions (23):**

- **Consignment Vendor Dispatch (BugFix-Purchase)** (`server_action_3647_consignment_vendor_dispatch_bugfix_purchase`, type `code`)
  - Function: Vendor Dispatch for a consignment: checks invoice quantities, vendor and uploaded invoice/bill-of-lading documents; if the delivery term requires vendor despatch, posts a journal entry in the 'Vendor Despatch' journal at the custom exchange rate and sets status to In Transit; otherwise clears the Vendor Dispatch flag.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model x_consignment_header`, `model x_consignment_line`<details><summary>+18 more</summary>`model x_custom_currency_rate` (BugFix-Accounting), `model x_custom_currency` (BugFix-Accounting), `model x_delivery_terms` (BugFix-Sales), `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_bill_of_lading`, `x_consignment_header.x_studio_company_id`, `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_delivery_term` (BugFix-Purchase), `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`, `x_consignment_header.x_studio_supplier_document`, `x_consignment_header.x_studio_supplier_id`, `x_consignment_header.x_studio_supplier_invoice_number`, `x_consignment_header.x_studio_total_amount`, `x_consignment_header.x_studio_vend_dispatch_status`, `x_consignment_header.x_studio_vendor_dispatch_exchange_rate`, `x_consignment_header.x_studio_vendor_dispatch`, `x_consignment_header.x_studio_voucher_date`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (84 lines)</summary>

```python

if record.id:

  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)

  con_lines = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)])
  if con_lines:
    for val in con_lines:
      if val.x_studio_invoice_qty == 0.00:
        raise UserError('Invoice Qty. should be Specified in all Consignment Lines.')

if record.x_studio_supplier_id.id == 0:
  raise UserError("Vendor Account must be Specified!")

if record.x_studio_supplier_document == False:
  raise UserError("Purchase Invoice Document must be Uploaded!")

if record.x_studio_bill_of_lading == False:
    raise UserError("Bill of Lading Document must be Uploaded!")

dev_term = env['x_delivery_terms'].search([('id', '=', record.x_studio_delivery_term.id),('x_studio_vendor_despatch', '=', True)],limit=1)
if dev_term:
  despatch_account = env['x_imports_ledger_setup'].search([('x_studio_company_id', '=', company.id)], limit=1)
  if despatch_account:
    if despatch_account.x_studio_vendor_despatch_debit_account.id == 0 or despatch_account.x_studio_vendor_despatch_credit_account.id == 0:
      raise UserError('Vendor Despatch Accounts must be Specified in Imports Ledger Setup')
    else:
      custom_currency = env['x_custom_currency'].search([('x_studio_currency_id', '=', record.x_studio_currency_id.id),('x_studio_active', '=', True)],limit=1)
      if custom_currency:
        currency_rate = env['x_custom_currency_rate'].search([('x_studio_custom_currency_id', '=', custom_currency.id),('x_studio_start_date', '<=', datetime.datetime.now().date()),('x_studio_end_date', '>=', datetime.datetime.now().date())],order='x_studio_start_date desc',limit=1)
        if currency_rate:
          despatch_lines = [
            [0, 0, {
              'account_id': despatch_account.x_studio_vendor_despatch_debit_account.id,
              'partner_id': record.x_studio_supplier_id.id,
              'name': 'Vendor Despatch',
              'debit': record.x_studio_total_amount * currency_rate.x_studio_rate,
            }],
            [0, 0, {
              'account_id': despatch_account.x_studio_vendor_despatch_credit_account.id,
              'partner_id': record.x_studio_supplier_id.id,
              'name': 'Vendor Despatch',
              'credit': record.x_studio_total_amount * currency_rate.x_studio_rate,
            }],
          ]

          journal = env['account.journal'].search([('name', '=', 'Vendor Despatch'),('company_id', '=', company.id)], limit=1)
          if not journal:
             raise UserError('The required journal has not been setup. Process terminated.')

          vendor_despatch = env['account.move'].create({'x_studio_created_from_consignment':record.id,'x_studio_supplier_invoice_number':record.x_studio_supplier_invoice_number,'journal_id':journal.id,'move_type':'entry','date':record.x_studio_voucher_date,'line_ids':despatch_lines})

          update_vendor_despatch = env['account.move'].search([('id', '=', vendor_despatch.id)],limit=1)
          if update_vendor_despatch:
            update_vendor_despatch.write({'state':'posted'})

          record['x_studio_status'] = 'In Transit'
          record['x_studio_status_bar'] = 'In Transit'

          action = {
            'name': 'Journal Entries',
            'domain': [('id', '=', vendor_despatch.id)],
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
            'view_id': False,
            'context': {},
          }
          record['x_studio_vendor_dispatch'] = True
          record['x_studio_vendor_dispatch_exchange_rate'] = currency_rate.x_studio_rate
        else:
          raise UserError('There is no Valid Exchange Rate for the Consignmet Header Currency.')
      else:
        raise UserError('There is no Active Custom Currency is Setup for the Selected Consignment Header.')
  else:
      raise UserError('Imports Ledger Accounts must be Specified.')
else:
  message = "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
  record['x_studio_vendor_dispatch'] = False

  record['x_studio_status'] = 'In Transit'
  record['x_studio_status_bar'] = 'In Transit'
  record['x_studio_vend_dispatch_status'] = message
```
  </details>
- **Execute Code** (`server_action_1258_imp_consignment_details_seq_no`, type `code`)
  - Function: Run by the Consignment Details Seq No automation: when a Consignment Header is named 'New', assigns the next 'consignment.det.seq' number.
  - Depends on: `model ir.sequence` (base), `model x_consignment_header`, `x_consignment_header.x_name`
  - Used by: `automation BugFix-Stock.automation_56_jin_consignment_details_seq_no`
  <details><summary>code (6 lines)</summary>

```python

#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('consignment.det.seq')
 record.write({'x_name': seq})
```
  </details>
- **Execute Code** (`server_action_1324_imp_restrict_delete_in_consignment`, type `code`)
  - Function: Run by the Restrict Delete in Consignment automation: blocks deleting a consignment that is not in Draft status.
  - Depends on: `model x_consignment_header`, `x_consignment_header.x_studio_status`
  - Used by: `automation BugFix-Stock.automation_62_imp_restrict_delete_in_consignment`
  <details><summary>code (3 lines)</summary>

```python

if record.x_studio_status != 'Draft':
  raise UserError("You can only delete a consignment if the consignment is in draft state.")
```
  </details>
- **Execute Code** (`server_action_1454_imp_update_cost_allocation_method_in_consignment`, type `code`)
  - Function: Run by the Update Cost Allocation Method automation: copies the Cost Allocation Method from Imports Ledger Setup record id 1 onto the consignment.
  - Depends on: `model x_consignment_header`, `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_cost_allocation_method`
  - Used by: `automation BugFix-Stock.automation_86_imp_update_cost_allocation_method_in_consignment`
  <details><summary>code (4 lines)</summary>

```python

cost_allocation = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
if cost_allocation:
  record['x_studio_cost_allocation_method'] = cost_allocation.x_studio_cost_allocation_method
```
  </details>
- **Execute Code** (`server_action_2890_imp_update_supplier_currency_in_consignment`, type `code`)
  - Function: Run by the Update Supplier Currency automation: sets the consignment Currency to the supplier's purchase currency when one is set.
  - Depends on: `model x_consignment_header`, `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_supplier_id`
  - Used by: `automation BugFix-Stock.automation_339_imp_update_supplier_currency_in_consignment`
  <details><summary>code (5 lines)</summary>

```python

cost_allocation = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
if record.x_studio_supplier_id.id:
  if record.x_studio_supplier_id.property_purchase_currency_id.id:
    record['x_studio_currency_id'] = record.x_studio_supplier_id.property_purchase_currency_id.id
```
  </details>
- **Execute Code** (`server_action_2607_jin_company_id_in_consignment_header`, type `code`)
  - Function: Run by an automation: sets the Company of a Consignment Header to the user's active company.
  - Depends on: `model res.company` (base), `model x_consignment_header`, `x_consignment_header.x_studio_company_id`
  - Used by: `automation BugFix-Stock.automation_280_jin_company_id_in_consignment_header`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Allocate Consignment Header Charges** (`server_action_1318_imp_allocate_consignment_header_charges`, type `code`)
  - Function: Button action on the consignment form that allocates header charges, duties and taxes to consignment lines: determines the custom exchange rate, validates unit price/weight/volume on each line, writes the exchange rate to lines and then runs the indent costing allocation (very long script).
  - Depends on: `model res.config.settings` (base), `model x_consignment_charge_h`, `model x_consignment_charge_l`, `model x_consignment_header`, `model x_consignment_line`<details><summary>+15 more</summary>`model x_custom_currency_rate` (BugFix-Accounting), `model x_custom_currency` (BugFix-Accounting), `model x_delivery_term_charge` (BugFix-Purchase), `model x_misc_charge_codes`, `model x_tariff_date` (BugFix-Purchase), `model x_tariff_rates` (BugFix-Purchase), `x_consignment_header.x_name`, `x_consignment_header.x_studio_allocate_header_charges`, `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_custom_cleared_date`, `x_consignment_header.x_studio_delivery_term` (BugFix-Purchase), `x_consignment_header.x_studio_header_charges_allocated`, `x_consignment_header.x_studio_structure_name` (BugFix-Purchase), `x_consignment_header.x_studio_total_allocate_amount`, `x_consignment_header.x_studio_total_amount`</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (727 lines)</summary>

```python
av = 0

c_f_i = 0



##################

ex_rate = 1

company_currency = env['res.config.settings'].search([('currency_id', '=', record.x_studio_currency_id.id)],limit=1)

if company_currency:

  ex_rate = 1

else:

  custom_currency = env['x_custom_currency'].search([('x_studio_currency_id', '=', record.x_studio_currency_id.id),('x_studio_active', '=', True)],limit=1)

  if custom_currency:

    currency_rate = env['x_custom_currency_rate'].search([('x_studio_custom_currency_id', '=', custom_currency.id),('x_studio_start_date', '<=', record.x_studio_custom_cleared_date),('x_studio_end_date', '>=', record.x_studio_custom_cleared_date)],order='x_studio_start_date desc',limit=1)

    if currency_rate:

      ex_rate = currency_rate.x_studio_rate

    else:

      raise UserError('Please setup a valid currency rate in Custom Exchange Rates.')

  else:

    raise UserError('Please setup a valid currency rate in Custom Exchange Rates.')

##################



con_line = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)])

if con_line:

  for validate_unitprice in con_line:

    if validate_unitprice.x_studio_unit_price == 0.0000:

      raise UserError("Unit Price must be Specified in each Consignment Line!")

      

    if validate_unitprice.x_studio_cost_allocation_method == 'by_weight':

      if validate_unitprice.x_studio_weight == 0.0000:  

        raise UserError("Weight must be Specified in each Consignment Line!")

        

    if validate_unitprice.x_studio_cost_allocation_method == 'by_volume':

      if validate_unitprice.x_studio_volume == 0.0000:  

        raise UserError("Volume must be Specified in each Consignment Line!")

        

    validate_unitprice.write({'x_studio_exchange_rate':ex_rate}) 



#############################################################-Indent Costing - Begin-#########################################################################

delivery_term = env['x_delivery_term_charge'].search([('x_studio_delivery_terms_id', '=', record.x_studio_delivery_term.id), ('x_studio_tax_appicable', '=', True)]) 

if delivery_term:

  for valid_terms in delivery_term:

    header_charges = env['x_consignment_charge_h'].search([('x_studio_consignment_id', '=', record.id), ('x_studio_charge_group', '=', 'Charges'), ('x_studio_charge_name', '=', valid_terms.x_name)],limit=1)

    if header_charges:

      header_charges.write({'x_studio_tax_appicable': True}) 

      c_f_i += header_charges.x_studio_amount

      

##########################################################modi-20.07.2022#####################################################################################

delivery_term2 = env['x_delivery_term_charge'].search([('x_studio_delivery_terms_id', '=', record.x_studio_delivery_term.id), ('x_studio_tax_appicable2', '=', True)]) 

if delivery_term2:

  for valid_terms2 in delivery_term2:

    header_charges2 = env['x_consignment_charge_h'].search([('x_studio_consignment_id', '=', record.id), ('x_studio_charge_group', '=', 'Charges'), ('x_studio_charge_name', '=', valid_terms2.x_name)],limit=1)

    if header_charges2:

      header_charges2.write({'x_studio_tax_appicable2': True}) 

##########################################################modi-20.07.2022#####################################################################################      



#av = record.x_studio_total_allocate_amount + c_f_i #Original Code

#av = record.x_studio_total_amount + c_f_i #Version - 01 #12.09.2022

av = c_f_i #Version - 01 #12.09.2022



purchase_lines = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)]) 

if purchase_lines:

# … 607 more lines
```
  </details>
- **IMP - Clear PO Lines from Consignment** (`server_action_1303_imp_clear_po_lines_from_consignment`, type `code`)
  - Function: Button on the consignment form: deletes all consignment lines and resets the Lines Copied flag so PO lines can be copied again.
  - Depends on: `model x_consignment_header`, `model x_consignment_line`, `x_consignment_header.x_studio_lines_copied`
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (7 lines)</summary>

```python
if record.id:
  temp_rec = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)])
  if temp_rec:
    for del_temp_rec in temp_rec:
      del_temp_rec.unlink()   

record['x_studio_lines_copied'] = False
```
  </details>
- **IMP - Confirm Purchase Invoice** (`server_action_1365_imp_confirm_purchase_invoice`, type `code`)
  - Function: Confirm Purchase Invoice button on the consignment form: requires invoice qty (and volume/weight per allocation method) on all lines, copies line volume/weight to the products, requires vendor, invoice and packing list documents, then sets Confirm Invoice and status to Consignment.
  - Depends on: `model product.product` (product), `model x_consignment_header`, `model x_consignment_line`, `x_consignment_header.x_studio_confirm_invoice`, `x_consignment_header.x_studio_cost_allocation_method`<details><summary>+5 more</summary>`x_consignment_header.x_studio_packing_list`, `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`, `x_consignment_header.x_studio_supplier_document`, `x_consignment_header.x_studio_supplier_id`</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (27 lines)</summary>

```python
if record.id:
  con_lines = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)])
  if con_lines:
    for val in con_lines:
      if val.x_studio_invoice_qty == 0.00:
        raise UserError('Invoice Qty. should be Specified in all Invoice Lines.')
      if val.x_studio_volume == 0.00 and record.x_studio_cost_allocation_method == 'by_volume':
        raise UserError('Volume should be Specified in all Invoice Lines.')
      if val.x_studio_weight == 0.00 and record.x_studio_cost_allocation_method == 'by_weight':
        raise UserError('Weight should be Specified in all Invoice Lines.')
        
      update_product_product = env['product.product'].search([('id', '=', val.x_studio_product_id.id)],limit=1)
      if update_product_product:
        update_product_product.write({'volume': val.x_studio_volume,'weight': val.x_studio_weight}) 
        
  if record.x_studio_supplier_id.id == 0:
    raise UserError("Vendor Account must be Specified!")
    
  if record.x_studio_supplier_document == False:
    raise UserError("Purchase Invoice Document must be Uploaded!")
    
  if record.x_studio_packing_list == False:
    raise UserError("Packing List Document must be Uploaded!")

  record['x_studio_confirm_invoice'] = True
  record['x_studio_status'] = 'Consignment'
  record['x_studio_status_bar'] = 'Consignment'
```
  </details>
- **IMP - Consignment Custom Duty** (`server_action_1321_imp_consignment_custom_duty`, type `code`)
  - Function: Custom Duty button on the consignment form: sums ledger-posted header charges, duties and taxes per group using the accounts from Import Charges Setup, and posts a journal entry against the Packing Slip Offset Account at the current custom exchange rate. Raises errors for missing setup.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model ir.sequence` (base), `model res.company` (base), `model x_consignment_charge_h`<details><summary>+19 more</summary>`model x_consignment_header`, `model x_custom_currency_rate` (BugFix-Accounting), `model x_custom_currency` (BugFix-Accounting), `model x_import_charges` (BugFix-Purchase), `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_name`, `x_consignment_header.x_studio_account_charge`, `x_consignment_header.x_studio_account_duty`, `x_consignment_header.x_studio_account_tax`, `x_consignment_header.x_studio_company_id`, `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_custom_clearance_exchange_rate`, `x_consignment_header.x_studio_custom_clearance_no`, `x_consignment_header.x_studio_custom_clearance`, `x_consignment_header.x_studio_custom_cleared_date`, `x_consignment_header.x_studio_offset_account`, `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`, `x_consignment_header.x_studio_supplier_invoice_number`</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (141 lines)</summary>

```python
# PATCHED IN-PLACE 2026-08-04 (interim workaround until
# BugFix-Purchase v0.0.9 loads on next Odoo worker restart).
# Dropped every env['account.analytic.default'] lookup and every
# analytic_tag_ids write — both APIs removed in Odoo 17.
# account.move.line._compute_analytic_distribution now applies
# distribution via account.analytic.distribution.model automatically
# on create, matching every other journal entry in the system.
# Original code preserved at:
#   BugFix-Purchase/docs/studio-actions-backup/1321-custom-duty-BEFORE-2026-08-04.py

if record.id:
  count_charge = 0
  value_charge = 0
  account_charge = 0
  text_charge = ''
  count_duty = 0
  value_duty = 0
  account_duty = 0
  text_tax = ''
  count_tax = 0
  value_tax = 0
  account_tax = 0
  value_charge_c = 0
  value_duty_c = 0
  value_tax_c = 0
  text_tax = ''

  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)

  header_charges = env['x_consignment_charge_h'].search([('x_studio_consignment_id', '=', record.id), ('x_studio_ledger_post', '=', True)],order='x_studio_charge_group asc')
  if header_charges:
    for post_charges in header_charges:
      import_charges = env['x_import_charges'].search([('x_studio_charge_group', '=', post_charges.x_studio_charge_group), ('x_name', '=', post_charges.x_studio_charge_name), ('x_studio_post_to_ledger', '=', True), ('x_studio_company_id', '=', company.id)],limit=1)
      if import_charges:
        if import_charges.x_studio_ledger_account.id == 0:
          raise UserError('Ledger Account is not specified for the selected Charge/Duty/Tax' + ' (' + post_charges.x_studio_charge_name + ') ' + 'in Import Charges Setup.')
        else:
          if post_charges.x_studio_charge_group == 'Charges':
            count_charge += 1
            if count_charge == 1:
              account_charge = import_charges.x_studio_ledger_account.id
              text_charge = str(import_charges.x_studio_posting_type)
            value_charge += post_charges.x_studio_amount
          elif post_charges.x_studio_charge_group == 'Duty':
            count_duty += 1
            if count_duty == 1:
              account_duty = import_charges.x_studio_ledger_account.id
              text_duty = str(import_charges.x_studio_posting_type)
            value_duty += post_charges.x_studio_amount
          else:
            count_tax += 1
            if count_tax == 1:
              account_tax = import_charges.x_studio_ledger_account.id
              text_tax = str(import_charges.x_studio_posting_type)
            value_tax += post_charges.x_studio_amount
      else:
        raise UserError('Ledger Posting is Not Activated for the selected Charge/Duty/Tax' + ' (' + post_charges.x_studio_charge_name + ') ' + 'in Import Charges Setup.')

  offset_account = env['x_imports_ledger_setup'].search([('x_studio_company_id', '=', company.id)], limit=1)
  if offset_account:
    if offset_account.x_studio_purch_packing_slip_offset_account.id == 0:
      raise UserError('Packing Slip Offset Account must be Specified in Imports Ledger Setup')
    else:
      custom_currency = env['x_custom_currency'].search([('x_studio_currency_id', '=', record.x_studio_currency_id.id),('x_studio_active', '=', True)],limit=1)
      if custom_currency:
        currency_rate = env['x_custom_currency_rate'].search([('x_studio_custom_currency_id', '=', custom_currency.id),('x_studio_start_date', '<=', datetime.datetime.now().date()),('x_studio_end_date', '>=', datetime.datetime.now().date())],order='x_studio_start_date desc',limit=1)
        if currency_rate:
          despatch_lines = []

          if value_charge > 0.0000:
            value_charge_c = value_charge
            despatch_lines.append([0, 0, {
              'account_id': account_charge,
              'name': text_charge,
              'debit': round(value_charge_c, 2),
            }])

          if value_duty > 0.0000:
            value_duty_c = value_duty
            despatch_lines.append([0, 0, {
              'account_id': account_duty,
              'name': text_duty,
              'debit': round(value_duty_c, 2),
            }])

          if value_tax > 0.0000:
            value_tax_c = value_tax
            despatch_lines.append([0, 0, {
              'account_id': account_tax,
              'name': text_tax,
              'debit': round(value_tax_c, 2),
            }])

          if (value_charge + value_duty + value_tax) > 0.0000:
            despatch_lines.append([0, 0, {
              'account_id': offset_account.x_studio_purch_packing_slip_offset_account.id,
              'name': 'Purchase Packing Slip Offset',
              'credit': (round(value_charge_c, 2) + round(value_duty_c, 2) + round(value_tax_c, 2)),
            }])

          journal = env['account.journal'].search([('name', '=', 'Vendor Despatch'),('company_id', '=', company.id)], limit=1)
          if not journal:
             raise UserError('The required journal has not been setup. Process terminated.')

          custom_clearance = env['account.move'].create({'x_studio_created_from_consignment_1':record.id,'x_studio_supplier_invoice_number':record.x_studio_supplier_invoice_number,'date':record.x_studio_custom_cleared_date,'journal_id':journal.id,'move_type':'entry','line_ids':despatch_lines})

          update_custom_clearance = env['account.move'].search([('id', '=', custom_clearance.id)],limit=1)
          if update_custom_clearance:
            update_custom_clearance.write({'state':'posted'})

          record['x_studio_custom_clearance_no'] = env['ir.sequence'].next_by_code('custom.clearance.seq')
          record['x_studio_status'] = 'In Transit'
          record['x_studio_status_bar'] = 'In Transit'
          record['x_studio_custom_clearance'] = True
          record['x_studio_custom_clearance_exchange_rate'] = currency_rate.x_studio_rate
          record['x_studio_account_charge'] = account_charge
          record['x_studio_account_duty'] = account_duty
          record['x_studio_account_tax'] = account_tax
          record['x_studio_offset_account'] = offset_account.x_studio_purch_packing_slip_offset_account.id
# … 21 more lines
```
  </details>
- **IMP - Consignment Details Seq.No** (`sa_f5_x_consignment_header_imp_consignment_details_seq_no`, type `code`)
  - Function: When a Consignment Header still has the name 'New', assigns it the next number from the 'consignment.det.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_consignment_header`, `x_consignment_header.x_name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('consignment.det.seq')
 record.write({'x_name': seq})
```
  </details>
- **IMP - Consignment Port Receipt** (`server_action_1313_imp_consignment_port_receipt`, type `code`)
  - Function: Port Receipt button on the consignment form: requires the Cargo Arrival Notice document, then sets status to Under Custom Clearance.
  - Depends on: `model x_consignment_header`, `x_consignment_header.x_studio_cargo_arrival_notice`, `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (6 lines)</summary>

```python
if record.id:
  if record.x_studio_cargo_arrival_notice == False:
    raise UserError("Cargo Arrival Notice Document must be Uploaded!")
    
  record['x_studio_status'] = 'Under Custom Clearance'
  record['x_studio_status_bar'] = 'Under Custom Clearance'
```
  </details>
- **IMP - Consignment Vendor Despatch** (`server_action_1305_imp_consignment_vendor_despatch`, type `code`)
  - Function: Vendor Despatch button on the consignment form: checks invoice quantities, vendor and invoice/bill-of-lading documents; if the delivery term requires vendor despatch, posts a 'Vendor Despatch' journal entry for the total at the custom exchange rate, sets status to In Transit and flags Vendor Dispatch.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model x_consignment_header`, `model x_consignment_line`<details><summary>+18 more</summary>`model x_custom_currency_rate` (BugFix-Accounting), `model x_custom_currency` (BugFix-Accounting), `model x_delivery_terms` (BugFix-Sales), `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_bill_of_lading`, `x_consignment_header.x_studio_company_id`, `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_delivery_term` (BugFix-Purchase), `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`, `x_consignment_header.x_studio_supplier_document`, `x_consignment_header.x_studio_supplier_id`, `x_consignment_header.x_studio_supplier_invoice_number`, `x_consignment_header.x_studio_total_amount`, `x_consignment_header.x_studio_vend_dispatch_status`, `x_consignment_header.x_studio_vendor_dispatch_exchange_rate`, `x_consignment_header.x_studio_vendor_dispatch`, `x_consignment_header.x_studio_voucher_date`</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (94 lines)</summary>

```python
# PATCHED IN-PLACE 2026-08-04 (interim workaround until
# BugFix-Purchase v0.0.9 loads on next Odoo worker restart).
# Dropped every env['account.analytic.default'] lookup and every
# analytic_tag_ids write — both APIs removed in Odoo 17.
# account.move.line._compute_analytic_distribution now applies
# distribution via account.analytic.distribution.model automatically
# on create, matching every other journal entry in the system.
# Original code preserved at:
#   BugFix-Purchase/docs/studio-actions-backup/1305-vendor-despatch-BEFORE-2026-08-04.py

if record.id:

  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)

  con_lines = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)])
  if con_lines:
    for val in con_lines:
      if val.x_studio_invoice_qty == 0.00:
        raise UserError('Invoice Qty. should be Specified in all Consignment Lines.')

if record.x_studio_supplier_id.id == 0:
  raise UserError("Vendor Account must be Specified!")

if record.x_studio_supplier_document == False:
  raise UserError("Purchase Invoice Document must be Uploaded!")

if record.x_studio_bill_of_lading == False:
    raise UserError("Bill of Lading Document must be Uploaded!")

dev_term = env['x_delivery_terms'].search([('id', '=', record.x_studio_delivery_term.id),('x_studio_vendor_despatch', '=', True)],limit=1)
if dev_term:
  despatch_account = env['x_imports_ledger_setup'].search([('x_studio_company_id', '=', company.id)], limit=1)
  if despatch_account:
    if despatch_account.x_studio_vendor_despatch_debit_account.id == 0 or despatch_account.x_studio_vendor_despatch_credit_account.id == 0:
      raise UserError('Vendor Despatch Accounts must be Specified in Imports Ledger Setup')
    else:
      custom_currency = env['x_custom_currency'].search([('x_studio_currency_id', '=', record.x_studio_currency_id.id),('x_studio_active', '=', True)],limit=1)
      if custom_currency:
        currency_rate = env['x_custom_currency_rate'].search([('x_studio_custom_currency_id', '=', custom_currency.id),('x_studio_start_date', '<=', datetime.datetime.now().date()),('x_studio_end_date', '>=', datetime.datetime.now().date())],order='x_studio_start_date desc',limit=1)
        if currency_rate:
          despatch_lines = [
            [0, 0, {
              'account_id': despatch_account.x_studio_vendor_despatch_debit_account.id,
              'partner_id': record.x_studio_supplier_id.id,
              'name': 'Vendor Despatch',
              'debit': record.x_studio_total_amount * currency_rate.x_studio_rate,
            }],
            [0, 0, {
              'account_id': despatch_account.x_studio_vendor_despatch_credit_account.id,
              'partner_id': record.x_studio_supplier_id.id,
              'name': 'Vendor Despatch',
              'credit': record.x_studio_total_amount * currency_rate.x_studio_rate,
            }],
          ]

          journal = env['account.journal'].search([('name', '=', 'Vendor Despatch'),('company_id', '=', company.id)], limit=1)
          if not journal:
             raise UserError('The required journal has not been setup. Process terminated.')

          vendor_despatch = env['account.move'].create({'x_studio_created_from_consignment':record.id,'x_studio_supplier_invoice_number':record.x_studio_supplier_invoice_number,'journal_id':journal.id,'move_type':'entry','date':record.x_studio_voucher_date,'line_ids':despatch_lines})

          update_vendor_despatch = env['account.move'].search([('id', '=', vendor_despatch.id)],limit=1)
          if update_vendor_despatch:
            update_vendor_despatch.write({'state':'posted'})

          record['x_studio_status'] = 'In Transit'
          record['x_studio_status_bar'] = 'In Transit'

          action = {
                    'name': 'Journal Entries',
                    'domain': [('id', '=', vendor_despatch.id)],
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.move',
                    'view_mode': 'tree,form',
                    'view_type': 'form',
                    'view_id': False,
                    'context': False,
                    }
          record['x_studio_vendor_dispatch'] = True
          record['x_studio_vendor_dispatch_exchange_rate'] = currency_rate.x_studio_rate
        else:
          raise UserError('There is no Valid Exchange Rate for the Consignmet Header Currency.')
      else:
        raise UserError('There is no Active Custom Currency is Setup for the Selected Consignment Header.')
  else:
      raise UserError('Imports Ledger Accounts must be Specified.')
else:
  message = "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
  record['x_studio_vendor_dispatch'] = False

  record['x_studio_status'] = 'In Transit'
  record['x_studio_status_bar'] = 'In Transit'
  record['x_studio_vend_dispatch_status'] = message
```
  </details>
- **IMP - Copy Charges to TP Invoice** (`server_action_1377_imp_copy_charges_to_tp_invoice`, type `code`)
  - Function: Button on the consignment form: requires every consignment line to have a posted bill line, then opens the Copy Charge Lines wizard (`x_temp_tp_invoice_head`) pre-filled with unprocessed, non-tax header charges for creating the third-party invoice.
  - Depends on: `model account.move.line` (account), `model x_consignment_charge_h`, `model x_consignment_header`, `x_consignment_header.x_studio_consignment_line_ids`, `x_consignment_header.x_studio_status`
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (35 lines)</summary>

```python
if record.id:
  count = 0
  ##########################################################################################################################################################
  for posted_lines in record.x_studio_consignment_line_ids:
    bill_lines = env['account.move.line'].search([('purchase_order_id', '=', posted_lines.x_studio_purchase_id.id),('purchase_line_id', '=', posted_lines.x_studio_purchase_line_id.id),('product_id', '=', posted_lines.	x_studio_product_id.id),('quantity', '=', posted_lines.	x_studio_invoice_qty),('x_studio_status', '=', 'posted')])
    if not bill_lines:
      count += 1
      
  if count > 0:
    raise UserError('There are Linked PO Lines yet to be Inviced. Please Invoice the Remaining Lines to Proceed.')
  ##########################################################################################################################################################
  charge_lines=[]
  
  charge_line = env['x_consignment_charge_h'].search([('x_studio_consignment_id', '=', record.id),('x_studio_tp_processed', '=', False),('x_studio_tax_appicable2', '=', False)])
  if charge_line:
    for validate_lines in charge_line:
      charge_lines.append([0,0,{
        'x_studio_consignment_charge_header_id':validate_lines.id,
        'x_studio_consignment_id':record.id,
        'x_studio_charge_group':validate_lines.x_studio_charge_group,
        'x_studio_charge_name':validate_lines.x_studio_charge_name,
        'x_studio_basis':validate_lines.x_studio_basis,
        'x_studio_amount':validate_lines.x_studio_amount}])

  ctx = env.context
  ctx.update({'default_x_studio_consignment_header_id':record.id,'default_x_studio_charge_line':charge_lines})
  action = {
            'name': 'Copy Charge Lines',
            'type': 'ir.actions.act_window',
            'res_model': 'x_temp_tp_invoice_head',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': ctx,
            }
```
  </details>
- **IMP - Copy PO Lines to Consignment** (`server_action_1263_imp_copy_po_lines_to_consignment`, type `code`)
  - Function: Copy PO Lines button on the consignment form: finds confirmed Import PO lines of the same supplier and delivery term with remaining quantity not fully invoiced, and opens the Copy PO Lines wizard pre-filled with them and their remaining quantities.
  - Depends on: `model purchase.order.line` (purchase), `model x_consignment_header`, `model x_consignment_line`, `x_consignment_header.x_studio_delivery_term` (BugFix-Purchase), `x_consignment_header.x_studio_description`<details><summary>+1 more</summary>`x_consignment_header.x_studio_supplier_id`</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (45 lines)</summary>

```python
if record.id: 
  po_lines=[]
  
  purch_line = env['purchase.order.line'].search([('partner_id', '=', record.x_studio_supplier_id.id),('x_studio_pr_type', '=', 'Import'),('x_studio_delivery_term', '=', record.x_studio_delivery_term.id),('state', '=', 'purchase'),('x_Studio_Deliver_Remainder', '>', 0.00),('x_studio_billing_status', '!=', 'invoiced')])
  if purch_line:
    for validate_lines in purch_line:
      con_remainder = 0
      if validate_lines.product_qty != validate_lines.qty_received:
        con_lines = env['x_consignment_line'].search([('x_studio_purchase_line_id', '=', validate_lines.id)])
        if con_lines:
          for sum_lines in con_lines:
            con_remainder += sum_lines.x_studio_invoice_qty
             
        if con_remainder < validate_lines.product_qty:       
          po_lines.append([0,0,{
          'x_studio_purchase_line_id':validate_lines.id,
          'x_studio_purchase_id':validate_lines.order_id.id,
          'x_studio_supplier_id':validate_lines.partner_id.id,
          'x_studio_indent_no':validate_lines.order_id.x_studio_indent,
          'x_studio_product_id':validate_lines.product_id.id,
          'x_studio_description':validate_lines.name or validate_lines.product_id.name,
          'x_studio_quantity':validate_lines.product_qty,
          'x_studio_weight':validate_lines.x_studio_weight,
          'x_studio_volume':validate_lines.x_studio_volume,
          'x_studio_delivery_remainder':validate_lines.product_qty - validate_lines.qty_received,
          'x_studio_consignment_remainder':validate_lines.product_qty - con_remainder,
          'x_studio_unit_price':validate_lines.price_unit,
          'x_studio_concessional_rate':validate_lines.x_studio_concessional_rate,
          'x_currency_id':validate_lines.currency_id.id,
          'x_studio_subtotal':validate_lines.price_subtotal,
          'x_studio_payment_method':validate_lines.x_studio_payment_method.id,
          'x_studio_delivery_date':validate_lines.date_planned,
          'x_studio_uom_id':validate_lines.product_id.uom_id.id}])

  ctx = env.context
  ctx.update({'default_x_studio_temp_consignment_header_id':record.id,'default_x_studio_temp_consignment_line_ids':po_lines})
  action = {
            'name': 'Copy PO Lines',
            'type': 'ir.actions.act_window',
            'res_model': 'x_temp_consignment_hea',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': ctx,
            }
```
  </details>
- **IMP - Create Consignment Header Charges** (`server_action_1316_imp_create_consignment_header_charges`, type `code`)
  - Function: Button on the consignment form: requires Custom Cleared Date, Delivery Term and Structure, creates one header charge line per structure detail of the selected structure, clears the Create Header Charges flag and opens the header charges grouped by charge group.
  - Depends on: `model x_consignment_charge_h`, `model x_consignment_header`, `model x_structure_details` (BugFix-Purchase), `x_consignment_header.x_studio_create_header_charges`, `x_consignment_header.x_studio_custom_cleared_date`<details><summary>+2 more</summary>`x_consignment_header.x_studio_delivery_term` (BugFix-Purchase), `x_consignment_header.x_studio_structure_name` (BugFix-Purchase)</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (27 lines)</summary>

```python
if record.x_studio_custom_cleared_date == False:
  raise UserError("Custom Cleared Date must be Specified!")
  
if record.x_studio_delivery_term.id == 0: 
  raise UserError("Delivery Term must be Specified!")
  
if record.x_studio_structure_name.id == 0:
  raise UserError("Structure Name must be Specified!")  

header_charges = env['x_structure_details'].search([('x_studio_structure_master_id', '=', record.x_studio_structure_name.id)],order='x_studio_structure_no asc')
if header_charges:
  for update_header_charges in header_charges:
    imp_header_charges = env['x_consignment_charge_h'].create({'x_studio_consignment_id':record.id,'x_studio_structure_master_id':update_header_charges.x_studio_structure_master_id.id,'x_studio_structure_details_line_ids':update_header_charges.id,'x_studio_structure_no':update_header_charges.x_studio_structure_no,'x_studio_basis':update_header_charges.x_studio_basis,'x_studio_charge_group':update_header_charges.x_studio_charge_group,'x_studio_charge_name':update_header_charges.x_studio_charge_name,'x_studio_formula':update_header_charges.x_studio_formula})  

record.write({'x_studio_create_header_charges': False}) 

action = {
          'name': 'Header Charges',
          'domain': [('x_studio_consignment_id', '=', record.id)],
          'type': 'ir.actions.act_window',
          'res_model': 'x_consignment_charge_h',
          'view_mode': 'tree,form',
          'view_type': 'form',
          'view_id': False,
          'context': False,
          'context': {'group_by': 'x_studio_charge_group'},
          }
```
  </details>
- **IMP - Reset Header Charges - Consignment** (`server_action_2199_imp_reset_header_charges_consignment`, type `code`)
  - Function: Reset Header Charges button on the consignment form: when charges were allocated, deletes the allocated charge lines, zeros non-'Charges' header amounts, clears their allocation/tax flags and re-enables Allocate Header Charges.
  - Depends on: `model x_consignment_charge_h`, `model x_consignment_charge_l`, `model x_consignment_header`, `x_consignment_header.x_studio_allocate_header_charges`, `x_consignment_header.x_studio_header_charges_allocated`<details><summary>+1 more</summary>`x_consignment_header.x_studio_structure_name` (BugFix-Purchase)</details>
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (29 lines)</summary>

```python
if record.x_studio_header_charges_allocated == True:

  header_lines_del = env['x_consignment_charge_h'].search([('x_studio_consignment_id', '=', record.id), ('x_studio_structure_master_id', '=', record.x_studio_structure_name.id)],order='x_studio_structure_no asc') 

  if header_lines_del:

      for del_lines in header_lines_del:

        temp_rec_del = env['x_consignment_charge_l'].search([('x_studio_consignment_charge_header_id', '=', del_lines.id),('x_studio_consignment_id', '=', del_lines.x_studio_consignment_id.id)])

        if temp_rec_del:

          for temp_rec_del_loop in temp_rec_del:

            temp_rec_del_loop.unlink()

        

        if del_lines.x_studio_charge_group != 'Charges':

          del_lines.write({'x_studio_amount': 0.00})

        

        del_lines.write({'x_studio_allocate_header_charges': False,'x_studio_tax_appicable': False})

        

      record.write({'x_studio_allocate_header_charges': True, 'x_studio_header_charges_allocated': False})
```
  </details>
- **IMP - Restrict Delete in Consignment** (`sa_f5_x_consignment_header_imp_restrict_delete_in_consignment`, type `code`)
  - Function: Blocks deletion of a Consignment Header unless its status is Draft, raising an error otherwise.
  - Depends on: `model x_consignment_header`, `x_consignment_header.x_studio_status`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_status != 'Draft':
  raise UserError("You can only delete a consignment if the consignment is in draft state.")
```
  </details>
- **IMP - Update Cost Allocation Method in Consignment** (`sa_f5_x_consignment_header_imp_update_cost_allocation_method_in_consignment`, type `code`)
  - Function: Copies the Cost Allocation Method from the Imports Ledger Setup record with id 1 onto the Consignment Header.
  - Depends on: `model x_consignment_header`, `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_cost_allocation_method`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
cost_allocation = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
if cost_allocation:
  record['x_studio_cost_allocation_method'] = cost_allocation.x_studio_cost_allocation_method
```
  </details>
- **IMP - Update Supplier Currency in Consignment** (`sa_f5_x_consignment_header_imp_update_supplier_currency_in_consignment`, type `code`)
  - Function: Sets the Consignment Header's Currency to the selected supplier's purchase currency, if the supplier has one.
  - Depends on: `model x_consignment_header`, `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_supplier_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
cost_allocation = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
if record.x_studio_supplier_id.id:
  if record.x_studio_supplier_id.property_purchase_currency_id.id:
    record['x_studio_currency_id'] = record.x_studio_supplier_id.property_purchase_currency_id.id
```
  </details>
- **IMP - Validate Consolidation in Consignment** (`server_action_1456_imp_validate_consolidation_in_consignment`, type `code`)
  - Function: Button on the consignment form: if the consignment's consolidation is confirmed, sets its status to Consolidated; otherwise raises an error asking to consolidate it first.
  - Depends on: `model x_consignment_header`, `x_consignment_header.x_studio_consolidation_confirmed`, `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`
  - Used by: `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`
  <details><summary>code (5 lines)</summary>

```python
if record.x_studio_consolidation_confirmed == True:
  record['x_studio_status'] = 'Consolidated'
  record['x_studio_status_bar'] = 'Consolidated'
else:
  raise UserError('The Selected Consignment Should be Consolidated First to Proceed.')
```
  </details>
- **JIN - Company Id in Consignment Header** (`sa_f5_x_consignment_header_jin_company_id_in_consignment_header`, type `code`)
  - Function: Sets the Company of a Consignment Header to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_consignment_header`, `x_consignment_header.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **Project - Update Month End Entries** (`server_action_2118_project_update_month_end_entries`, type `code`)
  - Function: Despite its name, an older copy of the consignment Vendor Despatch logic: validates lines and documents, posts a vendor despatch journal entry into journal id 15 (hard-coded) using Imports Ledger Setup id 1, and sets status In Transit. Not referenced by any view or automation in this repo.
  - Depends on: `model account.move` (account), `model x_consignment_header`, `model x_consignment_line`, `model x_custom_currency_rate` (BugFix-Accounting), `model x_custom_currency` (BugFix-Accounting)<details><summary>+15 more</summary>`model x_delivery_terms` (BugFix-Sales), `model x_imports_ledger_setup` (BugFix-Purchase), `x_consignment_header.x_studio_bill_of_lading`, `x_consignment_header.x_studio_currency_id`, `x_consignment_header.x_studio_delivery_term` (BugFix-Purchase), `x_consignment_header.x_studio_status_bar`, `x_consignment_header.x_studio_status`, `x_consignment_header.x_studio_supplier_document`, `x_consignment_header.x_studio_supplier_id`, `x_consignment_header.x_studio_supplier_invoice_number`, `x_consignment_header.x_studio_total_amount`, `x_consignment_header.x_studio_vend_dispatch_status`, `x_consignment_header.x_studio_vendor_dispatch_exchange_rate`, `x_consignment_header.x_studio_vendor_dispatch`, `x_consignment_header.x_studio_voucher_date`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (83 lines)</summary>

```python
if record.id:
  con_lines = env['x_consignment_line'].search([('x_studio_consignment_header_id', '=', record.id)])
  if con_lines:
    for val in con_lines:
      if val.x_studio_invoice_qty == 0.00:
        raise UserError('Invoice Qty. should be Specified in all Consignment Lines.')
        
if record.x_studio_supplier_id.id == 0:
  raise UserError("Vendor Account must be Specified!")
  
if record.x_studio_supplier_document == False:
  raise UserError("Purchase Invoice Document must be Uploaded!")
  
if record.x_studio_bill_of_lading == False:
    raise UserError("Bill of Lading Document must be Uploaded!")
  
dev_term = env['x_delivery_terms'].search([('id', '=', record.x_studio_delivery_term.id),('x_studio_vendor_despatch', '=', True)],limit=1)  
if dev_term:
  despatch_account = env['x_imports_ledger_setup'].search([('id', '=', 1)], limit=1)
  if despatch_account:
    if despatch_account.x_studio_vendor_despatch_debit_account.id == 0 or despatch_account.x_studio_vendor_despatch_credit_account.id == 0:
      raise UserError('Vendor Despatch Accounts must be Specified in Imports Ledger Setup')
    else:
      custom_currency = env['x_custom_currency'].search([('x_studio_currency_id', '=', record.x_studio_currency_id.id),('x_studio_active', '=', True)],limit=1)
      if custom_currency:
        currency_rate = env['x_custom_currency_rate'].search([('x_studio_custom_currency_id', '=', custom_currency.id),('x_studio_start_date', '<=', datetime.datetime.now().date()),('x_studio_end_date', '>=', datetime.datetime.now().date())],order='x_studio_start_date desc',limit=1)
        if currency_rate:
          despatch_lines=[]
          despatch_lines.append([0,0,{
            'account_id':despatch_account.x_studio_vendor_despatch_debit_account.id,
            'partner_id':record.x_studio_supplier_id.id,
            'name':'Vendor Despatch',
            'debit':record.x_studio_total_amount * currency_rate.x_studio_rate}])
              
          despatch_lines.append([0,0,{
            'account_id':despatch_account.x_studio_vendor_despatch_credit_account.id,
            'partner_id':record.x_studio_supplier_id.id,
            'name':'Vendor Despatch',
            'credit':record.x_studio_total_amount * currency_rate.x_studio_rate}])	
            
          vendor_despatch = env['account.move'].create({'x_studio_created_from_consignment':record.id,'x_studio_supplier_invoice_number':record.x_studio_supplier_invoice_number,'journal_id':15,'move_type':'entry','date':record.x_studio_voucher_date,'line_ids':despatch_lines})
          
          update_vendor_despatch = env['account.move'].search([('id', '=', vendor_despatch.id)],limit=1)
          if update_vendor_despatch:
            update_vendor_despatch.write({'state':'posted'})
            
          record['x_studio_status'] = 'In Transit'
          record['x_studio_status_bar'] = 'In Transit'
            
          action = {
                    'name': 'Journal Entries',
                    'domain': [('id', '=', vendor_despatch.id)],
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.move',
                    'view_mode': 'tree,form',
                    'view_type': 'form',
                    'view_id': False,
                    'context': False,
                    }
          record['x_studio_vendor_dispatch'] = True
          record['x_studio_vendor_dispatch_exchange_rate'] = currency_rate.x_studio_rate
        else:
          raise UserError('There is no Valid Exchange Rate for the Consignmet Header Currency.')
      else:
        raise UserError('There is no Active Custom Currency is Setup for the Selected Consignment Header.')
  else:
      raise UserError('Imports Ledger Accounts must be Specified.')
else:
  message = "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
  record['x_studio_vendor_dispatch'] = False
  
  record['x_studio_status'] = 'In Transit'
  record['x_studio_status_bar'] = 'In Transit'
  record['x_studio_vend_dispatch_status'] = message
  
#  title = "Vendor Dispatch"
#  message = "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
  
#  action = {
#            'type': 'ir.actions.client',
#            'tag': 'display_notification',
#            'params': {'title': title,'message': message,'sticky': False,}
#            }
```
  </details>
**Automations (5):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Restrict Delete in Consignment | `automation_62_imp_restrict_delete_in_consignment` |  | When a record is deleted on Consignment Header, runs _Execute Code_. | `model x_consignment_header`<br>`server action BugFix-Stock.server_action_1324_imp_restrict_delete_in_consignment` |  |
| IMP - Update Cost Allocation Method in Consignment | `automation_86_imp_update_cost_allocation_method_in_consignment` |  | When a watched field changes in the form on Consignment Header, runs _Execute Code_. | `model x_consignment_header`<br>`server action BugFix-Stock.server_action_1454_imp_update_cost_allocation_method_in_consignment` |  |
| IMP - Update Supplier Currency in Consignment | `automation_339_imp_update_supplier_currency_in_consignment` |  | When a watched field changes in the form on Consignment Header, runs _Execute Code_. | `model x_consignment_header`<br>`server action BugFix-Stock.server_action_2890_imp_update_supplier_currency_in_consignment` |  |
| JIN - Company Id in Consignment Header | `automation_280_jin_company_id_in_consignment_header` |  | When a record is created or updated on Consignment Header, runs _Execute Code_. | `model x_consignment_header`<br>`server action BugFix-Stock.server_action_2607_jin_company_id_in_consignment_header` |  |
| JIN-Consignment Details Seq.No | `automation_56_jin_consignment_details_seq_no` |  | When a record is created or updated on Consignment Header, runs _Execute Code_. | `model x_consignment_header`<br>`server action BugFix-Stock.server_action_1258_imp_consignment_details_seq_no` |  |

**Window actions (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Header (x_consignment_header) | `action_2852_consignment_header_x_consignment_header` | Opens **Consignment Header** records (kanban,tree,form). | `model x_consignment_header` |  |
| Consignment Header (x_consignment_header) | `action_2862_consignment_header_x_consignment_header` | Opens **Consignment Header** records (kanban,tree,form). | `model x_consignment_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_consignment_header_x_consignment_header` (BugFix-Studio-Misc) |
| Consignment Header Analysis | `action_x_consignment_header_analysis` | Opens **Consignment Header** records (graph,pivot). | `model x_consignment_header` | `menu BugFix-Stock.menu_x_consignment_header_analysis` |
| Imports - 01 | `action_1323_imports_01` | Opens **Consignment Header** records (tree,form). | `model x_consignment_header` | `menu BugFix-Stock.menu_f6_imports_01` |
| Purchase Invoice Header | `action_1256_purchase_invoice_header` | Opens **Consignment Header** records (tree,form,kanban). | `model x_consignment_header` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_purchase_invoices` (BugFix-Studio-Misc) |
| Purchase Invoices | `action_2052_purchase_invoices` | Opens **Consignment Header** records (tree,kanban,form). | `model x_consignment_header` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_purchase_invoices` (BugFix-Studio-Misc) |
| Purchase Invoices | `action_2887_purchase_invoices` | Opens **Consignment Header** records (kanban,tree,form). | `model x_consignment_header` |  |
| x_consignment_header | `action_2800_x_consignment_header` | Opens **Consignment Header** records (kanban,tree,form). | `model x_consignment_header` |  |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_consignment_header | `ported_view_2811_default_form_view_for_x_consignment_header` | form | full form layout with 7 fields | Consignment Header form with status-driven workflow buttons (Copy/Clear PO Lines, Confirm Invoice, Validate Consolidation, Vendor Dispatch, Port Receipt, header charges, Custom Duty, TP Invoice). Buttons use hardcoded numeric action ids (1962-1987). | `server action BugFix-Stock.server_action_1263_imp_copy_po_lines_to_consignment`<br>`server action BugFix-Stock.server_action_1303_imp_clear_po_lines_from_consignment`<br>`server action BugFix-Stock.server_action_1305_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.server_action_1313_imp_consignment_port_receipt`<br>`server action BugFix-Stock.server_action_1316_imp_create_consignment_header_charges`<details><summary>+13 more</summary>`server action BugFix-Stock.server_action_1318_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.server_action_1321_imp_consignment_custom_duty`<br>`server action BugFix-Stock.server_action_1365_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.server_action_1377_imp_copy_charges_to_tp_invoice`<br>`server action BugFix-Stock.server_action_1456_imp_validate_consolidation_in_consignment`<br>`server action BugFix-Stock.server_action_2199_imp_reset_header_charges_consignment`<br>`x_consignment_header.x_active`<br>`x_consignment_header.x_name`<br>`x_consignment_header.x_studio_allocate_header_charges`<br>`x_consignment_header.x_studio_create_header_charges`<br>`x_consignment_header.x_studio_header_charges_allocated`<br>`x_consignment_header.x_studio_lines_copied`<br>`x_consignment_header.x_studio_status`</details> | `view BugFix-Purchase.view_x_consignment_header_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.view_9609_bugfix_purchase_x_consignment_header_form_rewire_vendor_disp_e` |
| Default kanban view for ir.model(905,) | `view_2949_default_kanban_view_for_ir_model_905_e` | kanban | full kanban layout with 4 fields | Kanban cards for Consignment Headers showing vendor, total amount, reference and status. | `x_consignment_header.x_name`<br>`x_consignment_header.x_studio_status`<br>`x_consignment_header.x_studio_supplier_id`<br>`x_consignment_header.x_studio_total_amount` |  |
| Default list view for x_consignment_header | `ported_view_2810_default_list_view_for_x_consignment_header` | tree | full tree layout with 2 fields | Base list view of Consignment Headers showing a drag handle (sequence) and the name. | `x_consignment_header.x_name`<br>`x_consignment_header.x_studio_sequence` | `view BugFix-Stock.ported_view_2819_studio_tree_x_consignment_header` |
| Default search view for x_consignment_header | `view_2812_default_search_view_for_x_consignment_header_e` | search | full search layout with 1 fields | Search view for Consignment Headers: search by name and an Archived filter. | `x_consignment_header.x_active`<br>`x_consignment_header.x_name` |  |
| Odoo Studio: Default form view for x_consignment_header customization | `ported_view_2816_studio_form_x_consignment_header` | form | after `//button[@name='1967']`: add field x_studio_status_bar; before `//form[1]/sheet[1]/widget[@name='web_ribbon']`: add div; set force_save=True, placeholder=New, string=Consignment Reference, readonly=1, required= on `//field[@name='x_name']`; inside `//group[@name='studio_group_01a9e3_left']`: add field x_studio_description, field x_studio_supplier_id, field x_studio_currency_id, field x_studio_supplier_invoice_number, field x_studio_invoice_date, field x_studio_shipment_start_date, field x_studio_voucher_date; inside `//group[@name='studio_group_01a9e3_right']`: add field x_studio_container_no, field x_studio_shipping_mode, field x_studio_custom_clearance_no, field create_uid, field create_date, field x_studio_status, field x_studio_cost_allocation_method, field x_studio_consolidated, field x_studio_consolidation_confirmed, field x_studio_con_validated, field x_studio_offset_account, field x_studio_account_tax …; after `//group[@name='studio_group_01a9e3']`: add notebook | Customizes the Consignment Header form: adds a status bar, smart buttons (Header Charges, Line Charges, Custom Clearance entries), read-only 'Consignment Reference' title, vendor/currency/invoice/shipment/clearance and accounting fields mostly locked after Draft, plus a notebook of lines. | `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header`<br>`window action BugFix-Stock.act_1306_vendor_despatch`<br>`window action BugFix-Stock.act_1322_custom_clearance`<br>`window action BugFix-Stock.action_1317_header_charges`<br>`window action BugFix-Stock.action_1319_line_charges`<details><summary>+84 more</summary>`x_consignment_header.x_active`<br>`x_consignment_header.x_studio_account_charge`<br>`x_consignment_header.x_studio_account_duty`<br>`x_consignment_header.x_studio_account_tax`<br>`x_consignment_header.x_studio_allocate_header_charges`<br>`x_consignment_header.x_studio_bill_of_lading_filename`<br>`x_consignment_header.x_studio_bill_of_lading`<br>`x_consignment_header.x_studio_cargo_arrival_notice`<br>`x_consignment_header.x_studio_company_id`<br>`x_consignment_header.x_studio_con_validated`<br>`x_consignment_header.x_studio_confirm_invoice`<br>`x_consignment_header.x_studio_consignment_line_ids`<br>`x_consignment_header.x_studio_consolidated`<br>`x_consignment_header.x_studio_consolidation_confirmed`<br>`x_consignment_header.x_studio_container_no`<br>`x_consignment_header.x_studio_cost_allocation_method`<br>`x_consignment_header.x_studio_create_header_charges`<br>`x_consignment_header.x_studio_currency_id`<br>`x_consignment_header.x_studio_custom_clearance_exchange_rate`<br>`x_consignment_header.x_studio_custom_clearance_no`<br>`x_consignment_header.x_studio_custom_clearance`<br>`x_consignment_header.x_studio_custom_cleared_date`<br>`x_consignment_header.x_studio_description`<br>`x_consignment_header.x_studio_header_charges_allocated`<br>`x_consignment_header.x_studio_invoice_date`<br>`x_consignment_header.x_studio_lines_copied`<br>`x_consignment_header.x_studio_offset_account`<br>`x_consignment_header.x_studio_packing_list`<br>`x_consignment_header.x_studio_shipment_start_date`<br>`x_consignment_header.x_studio_shipping_mode`<br>`x_consignment_header.x_studio_status_bar`<br>`x_consignment_header.x_studio_status`<br>`x_consignment_header.x_studio_supplier_document`<br>`x_consignment_header.x_studio_supplier_id`<br>`x_consignment_header.x_studio_supplier_invoice_number`<br>`x_consignment_header.x_studio_total_allocate_amount`<br>`x_consignment_header.x_studio_total_amount_cost_allocation_method`<br>`x_consignment_header.x_studio_total_amount`<br>`x_consignment_header.x_studio_vend_dispatch_status`<br>`x_consignment_header.x_studio_vendor_dispatch_exchange_rate`<br>`x_consignment_header.x_studio_vendor_dispatch`<br>`x_consignment_header.x_studio_voucher_date`<br>`x_consignment_header.x_x_studio_consignment_id__x_consignment_charge_h_count`<br>`x_consignment_header.x_x_studio_consignment_id__x_consignment_charge_l_count`<br>`x_consignment_header.x_x_studio_created_from_consignment_1__account_move_count`<br>`x_consignment_header.x_x_studio_created_from_consignment__account_move_count`<br>`x_consignment_line.x_active`<br>`x_consignment_line.x_currency_id`<br>`x_consignment_line.x_name`<br>`x_consignment_line.x_studio_allocate_amount`<br>`x_consignment_line.x_studio_amount`<br>`x_consignment_line.x_studio_concessional_rate`<br>`x_consignment_line.x_studio_consignment_header_id`<br>`x_consignment_line.x_studio_cost_allocation_method`<br>`x_consignment_line.x_studio_delivery_remainder`<br>`x_consignment_line.x_studio_description`<br>`x_consignment_line.x_studio_exchange_rate`<br>`x_consignment_line.x_studio_header_charges_allocated`<br>`x_consignment_line.x_studio_invoice_qty`<br>`x_consignment_line.x_studio_order_remainder`<br>`x_consignment_line.x_studio_original_delivery_remainder`<br>`x_consignment_line.x_studio_product_id`<br>`x_consignment_line.x_studio_purchase_id`<br>`x_consignment_line.x_studio_purchase_line_id`<br>`x_consignment_line.x_studio_received_qty`<br>`x_consignment_line.x_studio_sequence`<br>`x_consignment_line.x_studio_status`<br>`x_consignment_line.x_studio_stock_move_id`<br>`x_consignment_line.x_studio_tariff_code`<br>`x_consignment_line.x_studio_tot_charge_cd_ids`<br>`x_consignment_line.x_studio_tot_charge_ex_cd_ids`<br>`x_consignment_line.x_studio_tot_charge_ex_ids`<br>`x_consignment_line.x_studio_tot_charge`<br>`x_consignment_line.x_studio_tot_duty_ex_cd_ids`<br>`x_consignment_line.x_studio_tot_duty`<br>`x_consignment_line.x_studio_tot_tax_ex_cd_ids`<br>`x_consignment_line.x_studio_tot_tax`<br>`x_consignment_line.x_studio_unit_price`<br>`x_consignment_line.x_studio_valid_charge`<br>`x_consignment_line.x_studio_valid_duty`<br>`x_consignment_line.x_studio_valid_tax`<br>`x_consignment_line.x_studio_volume`<br>`x_consignment_line.x_studio_warehouse`<br>`x_consignment_line.x_studio_weight`</details> |  |
| Odoo Studio: Default list view for x_consignment_header customization | `ported_view_2819_studio_tree_x_consignment_header` | tree | set default_order=x_name desc on `//tree[1]`; before `//field[@name='x_studio_sequence']`: add xpath, field x_studio_description, field x_studio_supplier_id, field x_studio_currency_id, field x_studio_shipment_start_date, field x_studio_shipping_mode, field create_uid, field create_date, field x_studio_invoice_date, field x_studio_container_no, field x_studio_supplier_invoice_number, field x_studio_status; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set string=Invoice Reference on `//field[@name='x_name']` | Customizes the Consignment Header list: sorted by name descending, name shown as 'Invoice Reference' first, plus description, supplier, currency, shipment and invoice dates, shipping mode, container, supplier invoice no and status. | `view BugFix-Stock.ported_view_2810_default_list_view_for_x_consignment_header`<br>`x_consignment_header.x_studio_container_no`<br>`x_consignment_header.x_studio_currency_id`<br>`x_consignment_header.x_studio_description`<br>`x_consignment_header.x_studio_invoice_date`<details><summary>+5 more</summary>`x_consignment_header.x_studio_shipment_start_date`<br>`x_consignment_header.x_studio_shipping_mode`<br>`x_consignment_header.x_studio_status`<br>`x_consignment_header.x_studio_supplier_id`<br>`x_consignment_header.x_studio_supplier_invoice_number`</details> |  |
| bugfix_purchase.x_consignment_header.form.rewire.vendor.dispatch | `view_9609_bugfix_purchase_x_consignment_header_form_rewire_vendor_disp_e` | form |  | Inherits the Consignment Header form but contains only comments (its xpaths were stripped), so it changes nothing. | `view BugFix-Stock.ported_view_2811_default_form_view_for_x_consignment_header` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Header group_system | `access_1291_consignment_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Consignment Header records. | `group base.group_system` (base)<br>`model x_consignment_header` |  |
| Consignment Header group_user | `access_1292_consignment_header_group_user` | Gives **User types / Internal User** read access to Consignment Header records. | `group base.group_user` (base)<br>`model x_consignment_header` |  |
| x_consignment_header user access | `access_x_consignment_header_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Header records. | `group base.group_user` (base)<br>`model x_consignment_header` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consignment Header | `rule_512_jin_multi_company_consignment_header` | For everyone (global rule): read/write/create/delete on Consignment Header only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_consignment_header`<br>`x_consignment_header.x_studio_company_id` |  |
