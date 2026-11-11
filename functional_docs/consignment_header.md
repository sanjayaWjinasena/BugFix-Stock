# BugFix-Stock — `consignment_header`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `consignment_header` — Consignment Header

*Created by this repo.* Python: `models/consignment_header.py`, `models/x_consignment_header_gap.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_consignment_header_consignment_header_purchase_jin_po_invoicing_payment_impor` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_consignment_header_consignment_header_purchase_jin_procurement_end_user_impor` (BugFix-Studio-Misc)<br>`account.bank.statement.line.co` (BugFix-Accounting)<br>`account.bank.statement.line.consignment_no` (BugFix-Accounting)<br>`account.bank.statement.line.created_from_consignment_1` (BugFix-Accounting)<br>`account.bank.statement.line.created_from_consignment_2` (BugFix-Accounting)<br>`account.bank.statement.line.created_from_consignment` (BugFix-Accounting)<br>`account.bank.statement.line.many2one_field_A197A` (BugFix-Accounting)<details><summary>+29 more</summary>`account.bank.statement.line.many2one_field_jslCp` (BugFix-Accounting)<br>`account.bank.statement.line.many2one_field_mucWu` (BugFix-Accounting)<br>`account.move.co` (BugFix-Accounting)<br>`account.move.consignment_no` (BugFix-Accounting)<br>`account.move.created_from_consignment_1` (BugFix-Accounting)<br>`account.move.created_from_consignment` (BugFix-Accounting)<br>`account.payment.co` (BugFix-Accounting)<br>`account.payment.consignment_no` (BugFix-Accounting)<br>`account.payment.created_from_consignment_1` (BugFix-Accounting)<br>`account.payment.created_from_consignment_2` (BugFix-Accounting)<br>`account.payment.created_from_consignment` (BugFix-Accounting)<br>`account.payment.many2one_field_A197A` (BugFix-Accounting)<br>`account.payment.many2one_field_jslCp` (BugFix-Accounting)<br>`account.payment.many2one_field_mucWu` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_supplier_invoice_no_update_in_import_vendor_bill_2` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`temp_tp_invoice_head.consignment_header_id` (BugFix-Accounting)<br>`temp_tp_invoice_line.consignment_id` (BugFix-Accounting)<br>`tp_invoice_header.con_no` (BugFix-Accounting)<br>`tp_invoice_line.consignment_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:consignment_header -->
A Consignment Header is an import shipment from an overseas supplier, also shown as a purchase invoice, and is the centre of the imports process. It holds the vendor, currency, supplier invoice details, uploaded shipping documents, container and customs clearance details, cost allocation method and accounts, and moves through statuses from Draft through In Transit and Under Custom Clearance to Done and TP Invoice. Buttons on its form copy import PO lines in, record vendor despatch, port receipt and customs duty entries, create, allocate and reset header charges, confirm the purchase invoice, validate consolidation and copy charges to the TP invoice. Automations number the consignment, set the company and supplier currency, copy the cost allocation method from the Imports Ledger Setup and block deleting non-Draft consignments.
<!-- /SUMMARY -->

**Fields (83):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `consignment_header.activity_summary`<br>`consignment_header.activity_type_icon`<br>`consignment_header.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`consignment_header.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`consignment_header.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`consignment_header.activity_ids` |  |
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
| `active` | Active | boolean | Archive flag for consignments; defaults to active, inactive records show an Archived ribbon. | stored |  | `default BugFix-Stock.default_consignment_header_active`<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_consignment_header_search` |
| `color` | Color | integer | Color index for the consignment; not used by any view or logic. | stored |  |  |
| `name` | Invoice Reference | char | Consignment (invoice) reference number, generated by the 'Consignment Details Seq. No' action on create; used in charge allocation and custom duty entries. | stored |  | `default BugFix-Stock.default_consignment_header_name`<br>`server action BugFix-Stock.action_consignment_header_imp_consignment_details_seq_no`<br>`server action BugFix-Stock.action_imp_consignment_details_seq_no`<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<details><summary>+4 more</summary>`view BugFix-Stock.view_consignment_header_list`<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_consignment_header_search`<br>`view BugFix-Stock.view_consignment_header_kanban`</details> |
| `account_charge` | Account Charge | many2one → `account.account` | G/L account used for posting clearance charges in the Custom Duty action. | stored | `model account.account` (account) | `server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `account_duty` | Account Duty | many2one → `account.account` | G/L account used for posting customs duty in the Custom Duty action. | stored | `model account.account` (account) | `server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `account_tax` | Account Tax | many2one → `account.account` | G/L account used for posting import taxes in the Custom Duty action. | stored | `model account.account` (account) | `server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `allocate_header_charges` | Allocate Header Charges | boolean | Flag requesting allocation of header charges to the consignment lines; used by the Allocate and Reset Header Charges actions. | stored |  | `default BugFix-Stock.default_consignment_header_allocate_header_ch`<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.action_imp_reset_header_charges_consignment`<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `bill_of_lading` | Bill of Lading | binary | Uploaded Bill of Lading document; required/checked by the Vendor Dispatch action. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `bill_of_lading_filename` | Filename for x_studio_binary_field_LzgTH | char | File name of the uploaded Bill of Lading. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `cargo_arrival_notice` | Cargo Arrival Notice | binary | Uploaded Cargo Arrival Notice; checked by the Port Receipt action. | stored |  | `server action BugFix-Stock.action_imp_consignment_port_receipt`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `cargo_arrival_notice_filename` | Filename for x_studio_binary_field_M4Ehh | char | File name of the uploaded Cargo Arrival Notice; not shown in any view. | stored |  |  |
| `accounting_company_id` | Company | many2one → `res.company` | Company of the consignment; set to the current company on create, used by the multi-company rule and by the dispatch and custom duty actions. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_jin_multi_company_consignment_header`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_consignment_header_jin_company_id_in_consignment_header`<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<details><summary>+3 more</summary>`server action BugFix-Stock.action_jin_company_id_in_consignment_header`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`</details> |
| `con_validated` | Con. Validated | boolean | Flag showing the consignment has been validated; shown on the consignment form. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `confirm_invoice` | Confirm Invoice | boolean | Flag set when the purchase invoice for the consignment is confirmed by the Confirm Purchase Invoice action. | stored |  | `server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `consignment_line_ids` | Consignment Line Ids | one2many → `consignment_line` | Products/PO lines included in the consignment; used when copying charges to the TP invoice. | stored | `model consignment_line` | `server action BugFix-Stock.action_imp_copy_charges_to_tp_invoice`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `consolidated` | Consolidated | boolean | Flag showing the consignment has been included in a consolidation. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `consolidation_confirmed` | Consolidation Confirmed | boolean | Flag set when the consolidation containing this consignment is confirmed; used by the Validate Consolidation action. | stored |  | `server action BugFix-Stock.action_imp_validate_consolidation_in_consignment`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `container_no` | Container No | char | Container number of the shipment; shown on the consignment form and list. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit` |
| `cost_allocation_method` | Cost Allocation Method | selection: equal=Equal; by_quantity=By Quantity; by_current_cost_price=By Current Cost; by_weight=By Weight; by_volume=By Volume | How landed costs are split over lines (Equal, By Quantity, By Current Cost, By Weight, By Volume); used by the Confirm Purchase Invoice action. | stored |  | `server action BugFix-Stock.action_consignment_header_imp_update_cost_allocation_method_in_consignment`<br>`server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.action_imp_update_cost_allocation_method_in_consignment`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `create_header_charges` | Create Header Charges | boolean | Flag requesting creation of header charges from the charge structure; used by the Create Header Charges action. | stored |  | `default BugFix-Stock.default_consignment_header_create_header_char`<br>`server action BugFix-Stock.action_imp_create_consignment_header_charges`<br>`view BugFix-Purchase.view_consignment_header_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `accounting_currency_id` | Currency | many2one → `res.currency` | Supplier currency of the consignment, defaulted and updated from the vendor; used in dispatch, charge allocation and custom duty entries. | stored | `model res.currency` (base) | `default BugFix-Stock.default_consignment_header_accounting_currency_id`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_consignment_header_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<details><summary>+6 more</summary>`server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit`</details> |
| `custom_clearance` | Custom Clearance | boolean | Flag indicating the consignment has gone through customs clearance; used by the Custom Duty action. | stored |  | `server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `custom_clearance_exchange_rate` | Custom Clearance Exchange Rate | float | Exchange rate applied at customs clearance; used by the Custom Duty action. | stored |  | `server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `custom_clearance_no` | Custom Clearance No | char | Customs clearance number; used by the Custom Duty action and mirrored on journal entries. | stored |  | `account.move.custom_clearance_no` (BugFix-Accounting)<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `custom_cleared_date` | Custom Cleared Date | date | Date the consignment was cleared by customs; used by header charge creation/allocation and the Custom Duty action. | stored |  | `server action BugFix-Stock.action_imp_create_consignment_header_charges`<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `description` | Description | char | Free-text description of the consignment; set when PO lines are copied in. | stored |  | `server action BugFix-Stock.action_imp_copy_po_lines_to_consignment`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit` |
| `header_charges_allocated` | Header Charges Allocated | boolean | Flag set once header charges have been allocated to lines; cleared by the Reset Header Charges action. | stored |  | `server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.action_imp_reset_header_charges_consignment`<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `accounting_invoice_date` | Supplier's Invoice Date (Bill Date) | date | Supplier's invoice (bill) date for the consignment. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit` |
| `lines_copied` | Lines Copied | boolean | Flag showing PO lines have been copied into the consignment; reset by the Clear PO Lines action and used for button visibility. | stored |  | `server action BugFix-Stock.action_imp_clear_po_lines_from_consignment`<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `offset_account` | Offset Account | many2one → `account.account` | Offset G/L account used by the Custom Duty journal entry. | stored | `model account.account` (account) | `server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `packing_list` | Packing List | binary | Uploaded packing list document; checked by the Confirm Purchase Invoice action. | stored |  | `server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `packing_list_filename` | Filename for x_studio_binary_field_xDIyn | char | File name of the uploaded packing list; not shown in any view. | stored |  |  |
| `sequence` | Sequence | integer | Ordering number for consignments (list drag handle). | stored |  | `default BugFix-Stock.default_consignment_header_sequence`<br>`view BugFix-Stock.view_consignment_header_list` |
| `shipment_start_date` | Shipment Start Date | date | Date the shipment started. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit` |
| `shipping_mode` | Shipping Mode | selection: Air=Air; Sea=Sea; Road=Road; Courier=Courier | Shipping mode: Air, Sea, Road or Courier; has a default value. | stored |  | `default BugFix-Stock.default_consignment_header_shipping_mode`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit` |
| `status` | Status | selection: Draft=Draft; Consignment=Confirmed; Consolidated=Consolidated; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done; TP Invoice=TP Invoice | Consignment workflow status (Draft, Confirmed, Consolidated, In Transit, Under Custom Clearance, Done, TP Invoice); advanced by the dispatch, port receipt, custom duty and invoice actions and checked before delete. | stored |  | `default BugFix-Stock.default_consignment_header_status`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_consignment_header_imp_restrict_delete_in_consignment`<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_consignment_port_receipt`<details><summary>+12 more</summary>`server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`server action BugFix-Stock.action_imp_restrict_delete_in_consignment`<br>`server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.action_imp_copy_charges_to_tp_invoice`<br>`server action BugFix-Stock.action_imp_validate_consolidation_in_consignment`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Purchase.view_consignment_header_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.view_consignment_header_form`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_consignment_header_kanban`</details> |
| `status_bar` | Status Bar | selection: Draft=Draft; Consignment=Confirmed; Consolidated=Consolidated; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done; TP Invoice=TP Invoice | Status bar copy of the consignment status, updated by the same workflow actions and shown in the form header. | stored |  | `default BugFix-Stock.default_consignment_header_status_bar`<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_consignment_port_receipt`<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<details><summary>+5 more</summary>`server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.action_imp_validate_consolidation_in_consignment`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`</details> |
| `supplier_document` | Purchase Invoice | binary | Uploaded supplier purchase invoice; checked by the Vendor Dispatch and Confirm Purchase Invoice actions. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<details><summary>+1 more</summary>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`</details> |
| `supplier_document_filename` | Filename for x_studio_binary_field_KSsMR | char | File name of the uploaded purchase invoice; not shown in any view. | stored |  |  |
| `supplier_id` | Vendor | many2one → `res.partner` | Vendor of the consignment; drives the supplier currency and is used when copying PO lines, dispatching and confirming the invoice. | stored | `model res.partner` (base) | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_consignment_header_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.action_imp_copy_po_lines_to_consignment`<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_confirm_purchase_invoice`<details><summary>+6 more</summary>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_imp_update_supplier_currency_in_consignment`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_consignment_header_kanban`</details> |
| `supplier_invoice_number` | Supplier's Invoice No (Bill Reference) | char | Supplier's invoice number (bill reference) for the consignment; used in dispatch and custom duty entries. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<details><summary>+2 more</summary>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_default_list_view_for_consignment_header_inherit`</details> |
| `total_allocate_amount` | Total Allocate Amount | float | Read-only total of header charges allocated; used by the Allocate Header Charges action. | stored |  | `server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `total_amount` | Total Amount | float | Read-only total value of the consignment; used by dispatch and charge allocation and shown in the kanban card. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<details><summary>+2 more</summary>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_consignment_header_kanban`</details> |
| `total_amount_cost_allocation_method` | Total Amount Cost Allocation Method | float | Read-only total used as the basis for the selected cost allocation method; shown on the form. | stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `vend_dispatch_status` | Vend. Dispatch Status | text | Text message describing the result of the vendor dispatch, written by the Vendor Dispatch action. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `vendor_dispatch` | Vendor Dispatch | boolean | Flag set when the vendor has dispatched the consignment (Vendor Dispatch action). | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `vendor_dispatch_exchange_rate` | Vendor Dispatch Exchange Rate | float | Exchange rate used for the vendor dispatch entry. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `voucher_date` | Vendor Dispatch Voucher Date | date | Voucher date used for the vendor dispatch accounting entry. | stored |  | `server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_project_update_month_end_entries`<br>`server action BugFix-Stock.action_consignment_vendor_dispatch_bugfix_purchase`<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `con_no__x_tp_invoice_header_count` | Created From Consignment No count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. | not stored |  |  |
| `consignment_id__x_consignment_charge_h_count` | Consignment Id count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `consignment_id__x_consignment_charge_l_count` | Consignment Id count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `created_from_consignment_1__account_move_count` | Created From Consignment count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| `created_from_consignment__account_move_count` | Created From Consignment count | integer | Smart-button counter left over from Studio; declared non-stored with no compute anywhere in the repos, so it always shows 0. Shown on the consignment form smart button. | not stored |  | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |

**Server actions (23):**

- **Consignment Vendor Dispatch (BugFix-Purchase)** (`action_consignment_vendor_dispatch_bugfix_purchase`, type `code`)
  - Function: Vendor Dispatch for a consignment: checks invoice quantities, vendor and uploaded invoice/bill-of-lading documents; if the delivery term requires vendor despatch, posts a journal entry in the 'Vendor Despatch' journal at the custom exchange rate and sets status to In Transit; otherwise clears the Vendor Dispatch flag.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model consignment_header`, `model consignment_line`<details><summary>+18 more</summary>`model custom_currency_rate` (BugFix-Accounting), `model custom_currency` (BugFix-Accounting), `model delivery_terms` (BugFix-Sales), `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.bill_of_lading`, `consignment_header.accounting_company_id`, `consignment_header.accounting_currency_id`, `consignment_header.delivery_term` (BugFix-Purchase), `consignment_header.status_bar`, `consignment_header.status`, `consignment_header.supplier_document`, `consignment_header.supplier_id`, `consignment_header.supplier_invoice_number`, `consignment_header.total_amount`, `consignment_header.vend_dispatch_status`, `consignment_header.vendor_dispatch_exchange_rate`, `consignment_header.vendor_dispatch`, `consignment_header.voucher_date`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (84 lines)</summary>

```python
if record.id:
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    con_lines = env["consignment_line"].search(
        [("consignment_header_id", "=", record.id)]
    )
    if con_lines:
        for val in con_lines:
            if val.invoice_qty == 0.00:
                raise UserError(
                    "Invoice Qty. should be Specified in all Consignment Lines."
                )

if record.supplier_id.id == 0:
    raise UserError("Vendor Account must be Specified!")

if record.supplier_document == False:
    raise UserError("Purchase Invoice Document must be Uploaded!")

if record.bill_of_lading == False:
    raise UserError("Bill of Lading Document must be Uploaded!")

dev_term = env["delivery_terms"].search(
    [
        ("id", "=", record.delivery_term.id),
        ("vendor_despatch", "=", True),
    ],
    limit=1,
)
if dev_term:
    despatch_account = env["imports_ledger_setup"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )
    if despatch_account:
        if (
            despatch_account.vendor_despatch_debit_account.id == 0
            or despatch_account.vendor_despatch_credit_account.id == 0
        ):
            raise UserError(
                "Vendor Despatch Accounts must be Specified in Imports Ledger Setup"
            )
        else:
            custom_currency = env["custom_currency"].search(
                [
                    ("accounting_currency_id", "=", record.accounting_currency_id.id),
                    ("accounting_active", "=", True),
                ],
                limit=1,
            )
            if custom_currency:
                currency_rate = env["custom_currency_rate"].search(
                    [
                        ("custom_currency_id", "=", custom_currency.id),
                        ("start_date", "<=", datetime.datetime.now().date()),
                        ("end_date", ">=", datetime.datetime.now().date()),
                    ],
                    order="start_date desc",
                    limit=1,
                )
                if currency_rate:
                    despatch_lines = [
                        [
                            0,
                            0,
                            {
                                "account_id": despatch_account.vendor_despatch_debit_account.id,
                                "partner_id": record.supplier_id.id,
                                "name": "Vendor Despatch",
                                "debit": record.total_amount
                                * currency_rate.rate,
                            },
                        ],
                        [
                            0,
                            0,
                            {
                                "account_id": despatch_account.vendor_despatch_credit_account.id,
                                "partner_id": record.supplier_id.id,
                                "name": "Vendor Despatch",
                                "credit": record.total_amount
                                * currency_rate.rate,
                            },
                        ],
                    ]

                    journal = env["account.journal"].search(
                        [
                            ("name", "=", "Vendor Despatch"),
                            ("company_id", "=", company.id),
                        ],
                        limit=1,
                    )
                    if not journal:
                        raise UserError(
                            "The required journal has not been setup. Process terminated."
                        )

                    vendor_despatch = env["account.move"].create(
                        {
                            "created_from_consignment": record.id,
                            "supplier_invoice_number": record.supplier_invoice_number,
                            "journal_id": journal.id,
                            "move_type": "entry",
                            "date": record.voucher_date,
                            "line_ids": despatch_lines,
                        }
                    )

                    update_vendor_despatch = env["account.move"].search(
                        [("id", "=", vendor_despatch.id)], limit=1
                    )
                    if update_vendor_despatch:
                        update_vendor_despatch.write({"state": "posted"})

                    record["status"] = "In Transit"
                    record["status_bar"] = "In Transit"

                    action = {
                        "name": "Journal Entries",
                        "domain": [("id", "=", vendor_despatch.id)],
                        "type": "ir.actions.act_window",
                        "res_model": "account.move",
                        "view_mode": "tree,form",
                        "view_id": False,
                        "context": {},
                    }
                    record["vendor_dispatch"] = True
                    record["vendor_dispatch_exchange_rate"] = (
                        currency_rate.rate
                    )
                else:
                    raise UserError(
                        "There is no Valid Exchange Rate for the Consignmet Header Currency."
                    )
            else:
                raise UserError(
                    "There is no Active Custom Currency is Setup for the Selected Consignment Header."
                )
    else:
        raise UserError("Imports Ledger Accounts must be Specified.")
else:
    message = (
        "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
    )
    record["vendor_dispatch"] = False

    record["status"] = "In Transit"
    record["status_bar"] = "In Transit"
    record["vend_dispatch_status"] = message
```
  </details>
- **Execute Code** (`action_imp_consignment_details_seq_no`, type `code`)
  - Function: Run by the Consignment Details Seq No automation: when a Consignment Header is named 'New', assigns the next 'consignment.det.seq' number.
  - Depends on: `model ir.sequence` (base), `model consignment_header`, `consignment_header.name`
  - Used by: `automation BugFix-Stock.automation_56_jin_consignment_details_seq_no`
  <details><summary>code (6 lines)</summary>

```python
# record['name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.name == "New":
    seq = env["ir.sequence"].next_by_code("consignment.det.seq")
    record.write({"name": seq})
```
  </details>
- **Execute Code** (`action_imp_restrict_delete_in_consignment`, type `code`)
  - Function: Run by the Restrict Delete in Consignment automation: blocks deleting a consignment that is not in Draft status.
  - Depends on: `model consignment_header`, `consignment_header.status`
  - Used by: `automation BugFix-Stock.automation_62_imp_restrict_delete_in_consignment`
  <details><summary>code (3 lines)</summary>

```python
if record.status != "Draft":
    raise UserError(
        "You can only delete a consignment if the consignment is in draft state."
    )
```
  </details>
- **Execute Code** (`action_imp_update_cost_allocation_method_in_consignment`, type `code`)
  - Function: Run by the Update Cost Allocation Method automation: copies the Cost Allocation Method from Imports Ledger Setup record id 1 onto the consignment.
  - Depends on: `model consignment_header`, `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.cost_allocation_method`
  - Used by: `automation BugFix-Stock.automation_86_imp_update_cost_allocation_method_in_consignment`
  <details><summary>code (4 lines)</summary>

```python
cost_allocation = env["imports_ledger_setup"].search([("id", "=", 1)], limit=1)
if cost_allocation:
    record["cost_allocation_method"] = (
        cost_allocation.cost_allocation_method
    )
```
  </details>
- **Execute Code** (`action_imp_update_supplier_currency_in_consignment`, type `code`)
  - Function: Run by the Update Supplier Currency automation: sets the consignment Currency to the supplier's purchase currency when one is set.
  - Depends on: `model consignment_header`, `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.accounting_currency_id`, `consignment_header.supplier_id`
  - Used by: `automation BugFix-Stock.automation_imp_update_supplier_currency_in_consignment`
  <details><summary>code (5 lines)</summary>

```python
cost_allocation = env["imports_ledger_setup"].search([("id", "=", 1)], limit=1)
if record.supplier_id.id:
    if record.supplier_id.property_purchase_currency_id.id:
        record["accounting_currency_id"] = (
            record.supplier_id.property_purchase_currency_id.id
        )
```
  </details>
- **Execute Code** (`action_jin_company_id_in_consignment_header`, type `code`)
  - Function: Run by an automation: sets the Company of a Consignment Header to the user's active company.
  - Depends on: `model res.company` (base), `model consignment_header`, `consignment_header.accounting_company_id`
  - Used by: `automation BugFix-Stock.automation_jin_company_id_in_consignment_header`
  <details><summary>code (5 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["accounting_company_id"] = company.id
```
  </details>
- **IMP - Allocate Consignment Header Charges** (`action_imp_allocate_consignment_header_charges`, type `code`)
  - Function: Button action on the consignment form that allocates header charges, duties and taxes to consignment lines: determines the custom exchange rate, validates unit price/weight/volume on each line, writes the exchange rate to lines and then runs the indent costing allocation (very long script).
  - Depends on: `model res.config.settings` (base), `model consignment_charge_h`, `model consignment_charge_l`, `model consignment_header`, `model consignment_line`<details><summary>+15 more</summary>`model custom_currency_rate` (BugFix-Accounting), `model custom_currency` (BugFix-Accounting), `model delivery_term_charge` (BugFix-Purchase), `model misc_charge_codes`, `model tariff_date` (BugFix-Purchase), `model tariff_rates` (BugFix-Purchase), `consignment_header.name`, `consignment_header.allocate_header_charges`, `consignment_header.accounting_currency_id`, `consignment_header.custom_cleared_date`, `consignment_header.delivery_term` (BugFix-Purchase), `consignment_header.header_charges_allocated`, `consignment_header.structure_name` (BugFix-Purchase), `consignment_header.total_allocate_amount`, `consignment_header.total_amount`</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (727 lines)</summary>

```python
av = 0

c_f_i = 0



##################

ex_rate = 1

company_currency = env['res.config.settings'].search([('currency_id', '=', record.accounting_currency_id.id)],limit=1)

if company_currency:

  ex_rate = 1

else:

  custom_currency = env['custom_currency'].search([('accounting_currency_id', '=', record.accounting_currency_id.id),('accounting_active', '=', True)],limit=1)

  if custom_currency:

    currency_rate = env['custom_currency_rate'].search([('custom_currency_id', '=', custom_currency.id),('start_date', '<=', record.custom_cleared_date),('end_date', '>=', record.custom_cleared_date)],order='start_date desc',limit=1)

    if currency_rate:

      ex_rate = currency_rate.rate

    else:

      raise UserError('Please setup a valid currency rate in Custom Exchange Rates.')

  else:

    raise UserError('Please setup a valid currency rate in Custom Exchange Rates.')

##################



con_line = env['consignment_line'].search([('consignment_header_id', '=', record.id)])

if con_line:

  for validate_unitprice in con_line:

    if validate_unitprice.unit_price == 0.0000:

      raise UserError("Unit Price must be Specified in each Consignment Line!")

      

    if validate_unitprice.cost_allocation_method == 'by_weight':

      if validate_unitprice.weight == 0.0000:  

        raise UserError("Weight must be Specified in each Consignment Line!")

        

    if validate_unitprice.cost_allocation_method == 'by_volume':

      if validate_unitprice.volume == 0.0000:  

        raise UserError("Volume must be Specified in each Consignment Line!")

        

    validate_unitprice.write({'exchange_rate':ex_rate}) 



#############################################################-Indent Costing - Begin-#########################################################################

delivery_term = env['delivery_term_charge'].search([('delivery_terms_id', '=', record.delivery_term.id), ('tax_appicable', '=', True)]) 

if delivery_term:

  for valid_terms in delivery_term:

    header_charges = env['consignment_charge_h'].search([('consignment_id', '=', record.id), ('charge_group', '=', 'Charges'), ('charge_name', '=', valid_terms.name)],limit=1)

    if header_charges:

      header_charges.write({'tax_appicable': True}) 

      c_f_i += header_charges.amount

      

##########################################################modi-20.07.2022#####################################################################################

delivery_term2 = env['delivery_term_charge'].search([('delivery_terms_id', '=', record.delivery_term.id), ('tax_appicable2', '=', True)]) 

if delivery_term2:

  for valid_terms2 in delivery_term2:

    header_charges2 = env['consignment_charge_h'].search([('consignment_id', '=', record.id), ('charge_group', '=', 'Charges'), ('charge_name', '=', valid_terms2.name)],limit=1)

    if header_charges2:

      header_charges2.write({'tax_appicable2': True}) 

##########################################################modi-20.07.2022#####################################################################################      



#av = record.total_allocate_amount + c_f_i #Original Code

#av = record.total_amount + c_f_i #Version - 01 #12.09.2022

av = c_f_i #Version - 01 #12.09.2022



purchase_lines = env['consignment_line'].search([('consignment_header_id', '=', record.id)]) 

if purchase_lines:

# … 607 more lines
```
  </details>
- **IMP - Clear PO Lines from Consignment** (`action_imp_clear_po_lines_from_consignment`, type `code`)
  - Function: Button on the consignment form: deletes all consignment lines and resets the Lines Copied flag so PO lines can be copied again.
  - Depends on: `model consignment_header`, `model consignment_line`, `consignment_header.lines_copied`
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (7 lines)</summary>

```python
if record.id:
    temp_rec = env["consignment_line"].search(
        [("consignment_header_id", "=", record.id)]
    )
    if temp_rec:
        for del_temp_rec in temp_rec:
            del_temp_rec.unlink()

record["lines_copied"] = False
```
  </details>
- **IMP - Confirm Purchase Invoice** (`action_imp_confirm_purchase_invoice`, type `code`)
  - Function: Confirm Purchase Invoice button on the consignment form: requires invoice qty (and volume/weight per allocation method) on all lines, copies line volume/weight to the products, requires vendor, invoice and packing list documents, then sets Confirm Invoice and status to Consignment.
  - Depends on: `model product.product` (product), `model consignment_header`, `model consignment_line`, `consignment_header.confirm_invoice`, `consignment_header.cost_allocation_method`<details><summary>+5 more</summary>`consignment_header.packing_list`, `consignment_header.status_bar`, `consignment_header.status`, `consignment_header.supplier_document`, `consignment_header.supplier_id`</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (27 lines)</summary>

```python
if record.id:
    con_lines = env["consignment_line"].search(
        [("consignment_header_id", "=", record.id)]
    )
    if con_lines:
        for val in con_lines:
            if val.invoice_qty == 0.00:
                raise UserError(
                    "Invoice Qty. should be Specified in all Invoice Lines."
                )
            if (
                val.volume == 0.00
                and record.cost_allocation_method == "by_volume"
            ):
                raise UserError("Volume should be Specified in all Invoice Lines.")
            if (
                val.weight == 0.00
                and record.cost_allocation_method == "by_weight"
            ):
                raise UserError("Weight should be Specified in all Invoice Lines.")

            update_product_product = env["product.product"].search(
                [("id", "=", val.product_id.id)], limit=1
            )
            if update_product_product:
                update_product_product.write(
                    {"volume": val.volume, "weight": val.weight}
                )

    if record.supplier_id.id == 0:
        raise UserError("Vendor Account must be Specified!")

    if record.supplier_document == False:
        raise UserError("Purchase Invoice Document must be Uploaded!")

    if record.packing_list == False:
        raise UserError("Packing List Document must be Uploaded!")

    record["confirm_invoice"] = True
    record["status"] = "Consignment"
    record["status_bar"] = "Consignment"
```
  </details>
- **IMP - Consignment Custom Duty** (`action_imp_consignment_custom_duty`, type `code`)
  - Function: Custom Duty button on the consignment form: sums ledger-posted header charges, duties and taxes per group using the accounts from Import Charges Setup, and posts a journal entry against the Packing Slip Offset Account at the current custom exchange rate. Raises errors for missing setup.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model ir.sequence` (base), `model res.company` (base), `model consignment_charge_h`<details><summary>+19 more</summary>`model consignment_header`, `model custom_currency_rate` (BugFix-Accounting), `model custom_currency` (BugFix-Accounting), `model import_charges` (BugFix-Purchase), `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.name`, `consignment_header.account_charge`, `consignment_header.account_duty`, `consignment_header.account_tax`, `consignment_header.accounting_company_id`, `consignment_header.accounting_currency_id`, `consignment_header.custom_clearance_exchange_rate`, `consignment_header.custom_clearance_no`, `consignment_header.custom_clearance`, `consignment_header.custom_cleared_date`, `consignment_header.offset_account`, `consignment_header.status_bar`, `consignment_header.status`, `consignment_header.supplier_invoice_number`</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
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
    text_charge = ""
    count_duty = 0
    value_duty = 0
    account_duty = 0
    text_tax = ""
    count_tax = 0
    value_tax = 0
    account_tax = 0
    value_charge_c = 0
    value_duty_c = 0
    value_tax_c = 0
    text_tax = ""

    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    header_charges = env["consignment_charge_h"].search(
        [
            ("consignment_id", "=", record.id),
            ("ledger_post", "=", True),
        ],
        order="charge_group asc",
    )
    if header_charges:
        for post_charges in header_charges:
            import_charges = env["import_charges"].search(
                [
                    ("charge_group", "=", post_charges.charge_group),
                    ("name", "=", post_charges.charge_name),
                    ("post_to_ledger", "=", True),
                    ("accounting_company_id", "=", company.id),
                ],
                limit=1,
            )
            if import_charges:
                if import_charges.ledger_account.id == 0:
                    raise UserError(
                        "Ledger Account is not specified for the selected Charge/Duty/Tax"
                        + " ("
                        + post_charges.charge_name
                        + ") "
                        + "in Import Charges Setup."
                    )
                else:
                    if post_charges.charge_group == "Charges":
                        count_charge += 1
                        if count_charge == 1:
                            account_charge = import_charges.ledger_account.id
                            text_charge = str(import_charges.posting_type)
                        value_charge += post_charges.amount
                    elif post_charges.charge_group == "Duty":
                        count_duty += 1
                        if count_duty == 1:
                            account_duty = import_charges.ledger_account.id
                            text_duty = str(import_charges.posting_type)
                        value_duty += post_charges.amount
                    else:
                        count_tax += 1
                        if count_tax == 1:
                            account_tax = import_charges.ledger_account.id
                            text_tax = str(import_charges.posting_type)
                        value_tax += post_charges.amount
            else:
                raise UserError(
                    "Ledger Posting is Not Activated for the selected Charge/Duty/Tax"
                    + " ("
                    + post_charges.charge_name
                    + ") "
                    + "in Import Charges Setup."
                )

    offset_account = env["imports_ledger_setup"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )
    if offset_account:
        if offset_account.purch_packing_slip_offset_account.id == 0:
            raise UserError(
                "Packing Slip Offset Account must be Specified in Imports Ledger Setup"
            )
        else:
            custom_currency = env["custom_currency"].search(
                [
                    ("accounting_currency_id", "=", record.accounting_currency_id.id),
                    ("accounting_active", "=", True),
                ],
                limit=1,
            )
            if custom_currency:
                currency_rate = env["custom_currency_rate"].search(
                    [
                        ("custom_currency_id", "=", custom_currency.id),
                        ("start_date", "<=", datetime.datetime.now().date()),
                        ("end_date", ">=", datetime.datetime.now().date()),
                    ],
                    order="start_date desc",
                    limit=1,
                )
                if currency_rate:
                    despatch_lines = []

                    if value_charge > 0.0000:
                        value_charge_c = value_charge
                        despatch_lines.append(
                            [
                                0,
                                0,
                                {
                                    "account_id": account_charge,
                                    "name": text_charge,
                                    "debit": round(value_charge_c, 2),
                                },
                            ]
                        )

                    if value_duty > 0.0000:
                        value_duty_c = value_duty
                        despatch_lines.append(
                            [
                                0,
                                0,
                                {
                                    "account_id": account_duty,
                                    "name": text_duty,
                                    "debit": round(value_duty_c, 2),
                                },
                            ]
                        )

                    if value_tax > 0.0000:
                        value_tax_c = value_tax
                        despatch_lines.append(
                            [
                                0,
                                0,
                                {
                                    "account_id": account_tax,
                                    "name": text_tax,
                                    "debit": round(value_tax_c, 2),
                                },
                            ]
                        )

                    if (value_charge + value_duty + value_tax) > 0.0000:
                        despatch_lines.append(
                            [
                                0,
                                0,
                                {
                                    "account_id": offset_account.purch_packing_slip_offset_account.id,
                                    "name": "Purchase Packing Slip Offset",
                                    "credit": (
                                        round(value_charge_c, 2)
                                        + round(value_duty_c, 2)
                                        + round(value_tax_c, 2)
                                    ),
                                },
                            ]
                        )

                    journal = env["account.journal"].search(
                        [
                            ("name", "=", "Vendor Despatch"),
                            ("company_id", "=", company.id),
                        ],
                        limit=1,
                    )
                    if not journal:
                        raise UserError(
                            "The required journal has not been setup. Process terminated."
                        )

                    custom_clearance = env["account.move"].create(
                        {
                            "created_from_consignment_1": record.id,
                            "supplier_invoice_number": record.supplier_invoice_number,
                            "date": record.custom_cleared_date,
                            "journal_id": journal.id,
                            "move_type": "entry",
                            "line_ids": despatch_lines,
                        }
                    )

                    update_custom_clearance = env["account.move"].search(
                        [("id", "=", custom_clearance.id)], limit=1
                    )
                    if update_custom_clearance:
                        update_custom_clearance.write({"state": "posted"})

                    record["custom_clearance_no"] = env[
                        "ir.sequence"
                    ].next_by_code("custom.clearance.seq")
                    record["status"] = "In Transit"
                    record["status_bar"] = "In Transit"
                    record["custom_clearance"] = True
                    record["custom_clearance_exchange_rate"] = (
                        currency_rate.rate
                    )
                    record["account_charge"] = account_charge
                    record["account_duty"] = account_duty
                    record["account_tax"] = account_tax
                    record["offset_account"] = (
                        offset_account.purch_packing_slip_offset_account.id
                    )
# … 21 more lines
```
  </details>
- **IMP - Consignment Details Seq.No** (`action_consignment_header_imp_consignment_details_seq_no`, type `code`)
  - Function: When a Consignment Header still has the name 'New', assigns it the next number from the 'consignment.det.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model consignment_header`, `consignment_header.name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
# record['name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.name == "New":
    seq = env["ir.sequence"].next_by_code("consignment.det.seq")
    record.write({"name": seq})
```
  </details>
- **IMP - Consignment Port Receipt** (`action_imp_consignment_port_receipt`, type `code`)
  - Function: Port Receipt button on the consignment form: requires the Cargo Arrival Notice document, then sets status to Under Custom Clearance.
  - Depends on: `model consignment_header`, `consignment_header.cargo_arrival_notice`, `consignment_header.status_bar`, `consignment_header.status`
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (6 lines)</summary>

```python
if record.id:
    if record.cargo_arrival_notice == False:
        raise UserError("Cargo Arrival Notice Document must be Uploaded!")

    record["status"] = "Under Custom Clearance"
    record["status_bar"] = "Under Custom Clearance"
```
  </details>
- **IMP - Consignment Vendor Despatch** (`action_imp_consignment_vendor_despatch`, type `code`)
  - Function: Vendor Despatch button on the consignment form: checks invoice quantities, vendor and invoice/bill-of-lading documents; if the delivery term requires vendor despatch, posts a 'Vendor Despatch' journal entry for the total at the custom exchange rate, sets status to In Transit and flags Vendor Dispatch.
  - Depends on: `model account.journal` (account), `model account.move` (account), `model res.company` (base), `model consignment_header`, `model consignment_line`<details><summary>+18 more</summary>`model custom_currency_rate` (BugFix-Accounting), `model custom_currency` (BugFix-Accounting), `model delivery_terms` (BugFix-Sales), `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.bill_of_lading`, `consignment_header.accounting_company_id`, `consignment_header.accounting_currency_id`, `consignment_header.delivery_term` (BugFix-Purchase), `consignment_header.status_bar`, `consignment_header.status`, `consignment_header.supplier_document`, `consignment_header.supplier_id`, `consignment_header.supplier_invoice_number`, `consignment_header.total_amount`, `consignment_header.vend_dispatch_status`, `consignment_header.vendor_dispatch_exchange_rate`, `consignment_header.vendor_dispatch`, `consignment_header.voucher_date`</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
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
    company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
    company = env["res.company"].browse(company_id)

    con_lines = env["consignment_line"].search(
        [("consignment_header_id", "=", record.id)]
    )
    if con_lines:
        for val in con_lines:
            if val.invoice_qty == 0.00:
                raise UserError(
                    "Invoice Qty. should be Specified in all Consignment Lines."
                )

if record.supplier_id.id == 0:
    raise UserError("Vendor Account must be Specified!")

if record.supplier_document == False:
    raise UserError("Purchase Invoice Document must be Uploaded!")

if record.bill_of_lading == False:
    raise UserError("Bill of Lading Document must be Uploaded!")

dev_term = env["delivery_terms"].search(
    [
        ("id", "=", record.delivery_term.id),
        ("vendor_despatch", "=", True),
    ],
    limit=1,
)
if dev_term:
    despatch_account = env["imports_ledger_setup"].search(
        [("accounting_company_id", "=", company.id)], limit=1
    )
    if despatch_account:
        if (
            despatch_account.vendor_despatch_debit_account.id == 0
            or despatch_account.vendor_despatch_credit_account.id == 0
        ):
            raise UserError(
                "Vendor Despatch Accounts must be Specified in Imports Ledger Setup"
            )
        else:
            custom_currency = env["custom_currency"].search(
                [
                    ("accounting_currency_id", "=", record.accounting_currency_id.id),
                    ("accounting_active", "=", True),
                ],
                limit=1,
            )
            if custom_currency:
                currency_rate = env["custom_currency_rate"].search(
                    [
                        ("custom_currency_id", "=", custom_currency.id),
                        ("start_date", "<=", datetime.datetime.now().date()),
                        ("end_date", ">=", datetime.datetime.now().date()),
                    ],
                    order="start_date desc",
                    limit=1,
                )
                if currency_rate:
                    despatch_lines = [
                        [
                            0,
                            0,
                            {
                                "account_id": despatch_account.vendor_despatch_debit_account.id,
                                "partner_id": record.supplier_id.id,
                                "name": "Vendor Despatch",
                                "debit": record.total_amount
                                * currency_rate.rate,
                            },
                        ],
                        [
                            0,
                            0,
                            {
                                "account_id": despatch_account.vendor_despatch_credit_account.id,
                                "partner_id": record.supplier_id.id,
                                "name": "Vendor Despatch",
                                "credit": record.total_amount
                                * currency_rate.rate,
                            },
                        ],
                    ]

                    journal = env["account.journal"].search(
                        [
                            ("name", "=", "Vendor Despatch"),
                            ("company_id", "=", company.id),
                        ],
                        limit=1,
                    )
                    if not journal:
                        raise UserError(
                            "The required journal has not been setup. Process terminated."
                        )

                    vendor_despatch = env["account.move"].create(
                        {
                            "created_from_consignment": record.id,
                            "supplier_invoice_number": record.supplier_invoice_number,
                            "journal_id": journal.id,
                            "move_type": "entry",
                            "date": record.voucher_date,
                            "line_ids": despatch_lines,
                        }
                    )

                    update_vendor_despatch = env["account.move"].search(
                        [("id", "=", vendor_despatch.id)], limit=1
                    )
                    if update_vendor_despatch:
                        update_vendor_despatch.write({"state": "posted"})

                    record["status"] = "In Transit"
                    record["status_bar"] = "In Transit"

                    action = {
                        "name": "Journal Entries",
                        "domain": [("id", "=", vendor_despatch.id)],
                        "type": "ir.actions.act_window",
                        "res_model": "account.move",
                        "view_mode": "tree,form",
                        "view_type": "form",
                        "view_id": False,
                        "context": False,
                    }
                    record["vendor_dispatch"] = True
                    record["vendor_dispatch_exchange_rate"] = (
                        currency_rate.rate
                    )
                else:
                    raise UserError(
                        "There is no Valid Exchange Rate for the Consignmet Header Currency."
                    )
            else:
                raise UserError(
                    "There is no Active Custom Currency is Setup for the Selected Consignment Header."
                )
    else:
        raise UserError("Imports Ledger Accounts must be Specified.")
else:
    message = (
        "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
    )
    record["vendor_dispatch"] = False

    record["status"] = "In Transit"
    record["status_bar"] = "In Transit"
    record["vend_dispatch_status"] = message
```
  </details>
- **IMP - Copy Charges to TP Invoice** (`action_imp_copy_charges_to_tp_invoice`, type `code`)
  - Function: Button on the consignment form: requires every consignment line to have a posted bill line, then opens the Copy Charge Lines wizard (`temp_tp_invoice_head`) pre-filled with unprocessed, non-tax header charges for creating the third-party invoice.
  - Depends on: `model account.move.line` (account), `model consignment_charge_h`, `model consignment_header`, `consignment_header.consignment_line_ids`, `consignment_header.status`
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (35 lines)</summary>

```python
if record.id:
    count = 0
    ##########################################################################################################################################################
    for posted_lines in record.consignment_line_ids:
        bill_lines = env["account.move.line"].search(
            [
                ("purchase_order_id", "=", posted_lines.accounting_purchase_id.id),
                ("purchase_line_id", "=", posted_lines.purchase_line_id.id),
                ("product_id", "=", posted_lines.product_id.id),
                ("quantity", "=", posted_lines.invoice_qty),
                ("status", "=", "posted"),
            ]
        )
        if not bill_lines:
            count += 1

    if count > 0:
        raise UserError(
            "There are Linked PO Lines yet to be Inviced. Please Invoice the Remaining Lines to Proceed."
        )
    ##########################################################################################################################################################
    charge_lines = []

    charge_line = env["consignment_charge_h"].search(
        [
            ("consignment_id", "=", record.id),
            ("tp_processed", "=", False),
            ("tax_appicable2", "=", False),
        ]
    )
    if charge_line:
        for validate_lines in charge_line:
            charge_lines.append(
                [
                    0,
                    0,
                    {
                        "consignment_charge_header_id": validate_lines.id,
                        "consignment_id": record.id,
                        "charge_group": validate_lines.charge_group,
                        "charge_name": validate_lines.charge_name,
                        "basis": validate_lines.basis,
                        "amount": validate_lines.amount,
                    },
                ]
            )

    ctx = env.context
    ctx.update(
        {
            "default_consignment_header_id": record.id,
            "default_charge_line": charge_lines,
        }
    )
    action = {
        "name": "Copy Charge Lines",
        "type": "ir.actions.act_window",
        "res_model": "temp_tp_invoice_head",
        "view_mode": "form",
        "view_type": "form",
        "target": "new",
        "context": ctx,
    }
```
  </details>
- **IMP - Copy PO Lines to Consignment** (`action_imp_copy_po_lines_to_consignment`, type `code`)
  - Function: Copy PO Lines button on the consignment form: finds confirmed Import PO lines of the same supplier and delivery term with remaining quantity not fully invoiced, and opens the Copy PO Lines wizard pre-filled with them and their remaining quantities.
  - Depends on: `model purchase.order.line` (purchase), `model consignment_header`, `model consignment_line`, `consignment_header.delivery_term` (BugFix-Purchase), `consignment_header.description`<details><summary>+1 more</summary>`consignment_header.supplier_id`</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (45 lines)</summary>

```python
if record.id:
    po_lines = []

    purch_line = env["purchase.order.line"].search(
        [
            ("partner_id", "=", record.supplier_id.id),
            ("pr_type", "=", "Import"),
            ("delivery_term", "=", record.delivery_term.id),
            ("state", "=", "purchase"),
            ("Studio_Deliver_Remainder", ">", 0.00),
            ("billing_status", "!=", "invoiced"),
        ]
    )
    if purch_line:
        for validate_lines in purch_line:
            con_remainder = 0
            if validate_lines.product_qty != validate_lines.qty_received:
                con_lines = env["consignment_line"].search(
                    [("purchase_line_id", "=", validate_lines.id)]
                )
                if con_lines:
                    for sum_lines in con_lines:
                        con_remainder += sum_lines.invoice_qty

                if con_remainder < validate_lines.product_qty:
                    po_lines.append(
                        [
                            0,
                            0,
                            {
                                "purchase_line_id": validate_lines.id,
                                "accounting_purchase_id": validate_lines.order_id.id,
                                "supplier_id": validate_lines.partner_id.id,
                                "indent_no": validate_lines.order_id.indent,
                                "product_id": validate_lines.product_id.id,
                                "description": validate_lines.name
                                or validate_lines.product_id.name,
                                "quantity": validate_lines.product_qty,
                                "weight": validate_lines.weight,
                                "volume": validate_lines.volume,
                                "delivery_remainder": validate_lines.product_qty
                                - validate_lines.qty_received,
                                "consignment_remainder": validate_lines.product_qty
                                - con_remainder,
                                "unit_price": validate_lines.price_unit,
                                "concessional_rate": validate_lines.concessional_rate,
                                "currency_id": validate_lines.currency_id.id,
                                "subtotal": validate_lines.price_subtotal,
                                "payment_method": validate_lines.payment_method.id,
                                "delivery_date": validate_lines.date_planned,
                                "uom_id": validate_lines.product_id.uom_id.id,
                            },
                        ]
                    )

    ctx = env.context
    ctx.update(
        {
            "default_temp_consignment_header_id": record.id,
            "default_temp_consignment_line_ids": po_lines,
        }
    )
    action = {
        "name": "Copy PO Lines",
        "type": "ir.actions.act_window",
        "res_model": "temp_consignment_hea",
        "view_mode": "form",
        "view_type": "form",
        "target": "new",
        "context": ctx,
    }
```
  </details>
- **IMP - Create Consignment Header Charges** (`action_imp_create_consignment_header_charges`, type `code`)
  - Function: Button on the consignment form: requires Custom Cleared Date, Delivery Term and Structure, creates one header charge line per structure detail of the selected structure, clears the Create Header Charges flag and opens the header charges grouped by charge group.
  - Depends on: `model consignment_charge_h`, `model consignment_header`, `model structure_details` (BugFix-Purchase), `consignment_header.create_header_charges`, `consignment_header.custom_cleared_date`<details><summary>+2 more</summary>`consignment_header.delivery_term` (BugFix-Purchase), `consignment_header.structure_name` (BugFix-Purchase)</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (27 lines)</summary>

```python
if record.custom_cleared_date == False:
    raise UserError("Custom Cleared Date must be Specified!")

if record.delivery_term.id == 0:
    raise UserError("Delivery Term must be Specified!")

if record.structure_name.id == 0:
    raise UserError("Structure Name must be Specified!")

header_charges = env["structure_details"].search(
    [("structure_master_id", "=", record.structure_name.id)],
    order="structure_no asc",
)
if header_charges:
    for update_header_charges in header_charges:
        imp_header_charges = env["consignment_charge_h"].create(
            {
                "consignment_id": record.id,
                "structure_master_id": update_header_charges.structure_master_id.id,
                "structure_details_line_ids": update_header_charges.id,
                "structure_no": update_header_charges.structure_no,
                "basis": update_header_charges.basis,
                "charge_group": update_header_charges.charge_group,
                "charge_name": update_header_charges.charge_name,
                "formula": update_header_charges.formula,
            }
        )

record.write({"create_header_charges": False})

action = {
    "name": "Header Charges",
    "domain": [("consignment_id", "=", record.id)],
    "type": "ir.actions.act_window",
    "res_model": "consignment_charge_h",
    "view_mode": "tree,form",
    "view_type": "form",
    "view_id": False,
    "context": False,
    "context": {"group_by": "charge_group"},
}
```
  </details>
- **IMP - Reset Header Charges - Consignment** (`action_imp_reset_header_charges_consignment`, type `code`)
  - Function: Reset Header Charges button on the consignment form: when charges were allocated, deletes the allocated charge lines, zeros non-'Charges' header amounts, clears their allocation/tax flags and re-enables Allocate Header Charges.
  - Depends on: `model consignment_charge_h`, `model consignment_charge_l`, `model consignment_header`, `consignment_header.allocate_header_charges`, `consignment_header.header_charges_allocated`<details><summary>+1 more</summary>`consignment_header.structure_name` (BugFix-Purchase)</details>
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (29 lines)</summary>

```python
if record.header_charges_allocated == True:
    header_lines_del = env["consignment_charge_h"].search(
        [
            ("consignment_id", "=", record.id),
            ("structure_master_id", "=", record.structure_name.id),
        ],
        order="structure_no asc",
    )

    if header_lines_del:
        for del_lines in header_lines_del:
            temp_rec_del = env["consignment_charge_l"].search(
                [
                    ("consignment_charge_header_id", "=", del_lines.id),
                    (
                        "consignment_id",
                        "=",
                        del_lines.consignment_id.id,
                    ),
                ]
            )

            if temp_rec_del:
                for temp_rec_del_loop in temp_rec_del:
                    temp_rec_del_loop.unlink()

            if del_lines.charge_group != "Charges":
                del_lines.write({"amount": 0.00})

            del_lines.write(
                {
                    "allocate_header_charges": False,
                    "tax_appicable": False,
                }
            )

        record.write(
            {
                "allocate_header_charges": True,
                "header_charges_allocated": False,
            }
        )
```
  </details>
- **IMP - Restrict Delete in Consignment** (`action_consignment_header_imp_restrict_delete_in_consignment`, type `code`)
  - Function: Blocks deletion of a Consignment Header unless its status is Draft, raising an error otherwise.
  - Depends on: `model consignment_header`, `consignment_header.status`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.status != "Draft":
    raise UserError(
        "You can only delete a consignment if the consignment is in draft state."
    )
```
  </details>
- **IMP - Update Cost Allocation Method in Consignment** (`action_consignment_header_imp_update_cost_allocation_method_in_consignment`, type `code`)
  - Function: Copies the Cost Allocation Method from the Imports Ledger Setup record with id 1 onto the Consignment Header.
  - Depends on: `model consignment_header`, `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.cost_allocation_method`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (3 lines)</summary>

```python
cost_allocation = env["imports_ledger_setup"].search([("id", "=", 1)], limit=1)
if cost_allocation:
    record["cost_allocation_method"] = (
        cost_allocation.cost_allocation_method
    )
```
  </details>
- **IMP - Update Supplier Currency in Consignment** (`action_consignment_header_imp_update_supplier_currency_in_consignment`, type `code`)
  - Function: Sets the Consignment Header's Currency to the selected supplier's purchase currency, if the supplier has one.
  - Depends on: `model consignment_header`, `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.accounting_currency_id`, `consignment_header.supplier_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
cost_allocation = env["imports_ledger_setup"].search([("id", "=", 1)], limit=1)
if record.supplier_id.id:
    if record.supplier_id.property_purchase_currency_id.id:
        record["accounting_currency_id"] = (
            record.supplier_id.property_purchase_currency_id.id
        )
```
  </details>
- **IMP - Validate Consolidation in Consignment** (`action_imp_validate_consolidation_in_consignment`, type `code`)
  - Function: Button on the consignment form: if the consignment's consolidation is confirmed, sets its status to Consolidated; otherwise raises an error asking to consolidate it first.
  - Depends on: `model consignment_header`, `consignment_header.consolidation_confirmed`, `consignment_header.status_bar`, `consignment_header.status`
  - Used by: `view BugFix-Stock.view_consignment_header_form`
  <details><summary>code (5 lines)</summary>

```python
if record.consolidation_confirmed == True:
    record["status"] = "Consolidated"
    record["status_bar"] = "Consolidated"
else:
    raise UserError("The Selected Consignment Should be Consolidated First to Proceed.")
```
  </details>
- **JIN - Company Id in Consignment Header** (`action_consignment_header_jin_company_id_in_consignment_header`, type `code`)
  - Function: Sets the Company of a Consignment Header to the user's currently active company.
  - Depends on: `model res.company` (base), `model consignment_header`, `consignment_header.accounting_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["accounting_company_id"] = company.id
```
  </details>
- **Project - Update Month End Entries** (`action_project_update_month_end_entries`, type `code`)
  - Function: Despite its name, an older copy of the consignment Vendor Despatch logic: validates lines and documents, posts a vendor despatch journal entry into journal id 15 (hard-coded) using Imports Ledger Setup id 1, and sets status In Transit. Not referenced by any view or automation in this repo.
  - Depends on: `model account.move` (account), `model consignment_header`, `model consignment_line`, `model custom_currency_rate` (BugFix-Accounting), `model custom_currency` (BugFix-Accounting)<details><summary>+15 more</summary>`model delivery_terms` (BugFix-Sales), `model imports_ledger_setup` (BugFix-Purchase), `consignment_header.bill_of_lading`, `consignment_header.accounting_currency_id`, `consignment_header.delivery_term` (BugFix-Purchase), `consignment_header.status_bar`, `consignment_header.status`, `consignment_header.supplier_document`, `consignment_header.supplier_id`, `consignment_header.supplier_invoice_number`, `consignment_header.total_amount`, `consignment_header.vend_dispatch_status`, `consignment_header.vendor_dispatch_exchange_rate`, `consignment_header.vendor_dispatch`, `consignment_header.voucher_date`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (83 lines)</summary>

```python
if record.id:
    con_lines = env["consignment_line"].search(
        [("consignment_header_id", "=", record.id)]
    )
    if con_lines:
        for val in con_lines:
            if val.invoice_qty == 0.00:
                raise UserError(
                    "Invoice Qty. should be Specified in all Consignment Lines."
                )

if record.supplier_id.id == 0:
    raise UserError("Vendor Account must be Specified!")

if record.supplier_document == False:
    raise UserError("Purchase Invoice Document must be Uploaded!")

if record.bill_of_lading == False:
    raise UserError("Bill of Lading Document must be Uploaded!")

dev_term = env["delivery_terms"].search(
    [
        ("id", "=", record.delivery_term.id),
        ("vendor_despatch", "=", True),
    ],
    limit=1,
)
if dev_term:
    despatch_account = env["imports_ledger_setup"].search([("id", "=", 1)], limit=1)
    if despatch_account:
        if (
            despatch_account.vendor_despatch_debit_account.id == 0
            or despatch_account.vendor_despatch_credit_account.id == 0
        ):
            raise UserError(
                "Vendor Despatch Accounts must be Specified in Imports Ledger Setup"
            )
        else:
            custom_currency = env["custom_currency"].search(
                [
                    ("accounting_currency_id", "=", record.accounting_currency_id.id),
                    ("accounting_active", "=", True),
                ],
                limit=1,
            )
            if custom_currency:
                currency_rate = env["custom_currency_rate"].search(
                    [
                        ("custom_currency_id", "=", custom_currency.id),
                        ("start_date", "<=", datetime.datetime.now().date()),
                        ("end_date", ">=", datetime.datetime.now().date()),
                    ],
                    order="start_date desc",
                    limit=1,
                )
                if currency_rate:
                    despatch_lines = []
                    despatch_lines.append(
                        [
                            0,
                            0,
                            {
                                "account_id": despatch_account.vendor_despatch_debit_account.id,
                                "partner_id": record.supplier_id.id,
                                "name": "Vendor Despatch",
                                "debit": record.total_amount
                                * currency_rate.rate,
                            },
                        ]
                    )

                    despatch_lines.append(
                        [
                            0,
                            0,
                            {
                                "account_id": despatch_account.vendor_despatch_credit_account.id,
                                "partner_id": record.supplier_id.id,
                                "name": "Vendor Despatch",
                                "credit": record.total_amount
                                * currency_rate.rate,
                            },
                        ]
                    )

                    vendor_despatch = env["account.move"].create(
                        {
                            "created_from_consignment": record.id,
                            "supplier_invoice_number": record.supplier_invoice_number,
                            "journal_id": 15,
                            "move_type": "entry",
                            "date": record.voucher_date,
                            "line_ids": despatch_lines,
                        }
                    )

                    update_vendor_despatch = env["account.move"].search(
                        [("id", "=", vendor_despatch.id)], limit=1
                    )
                    if update_vendor_despatch:
                        update_vendor_despatch.write({"state": "posted"})

                    record["status"] = "In Transit"
                    record["status_bar"] = "In Transit"

                    action = {
                        "name": "Journal Entries",
                        "domain": [("id", "=", vendor_despatch.id)],
                        "type": "ir.actions.act_window",
                        "res_model": "account.move",
                        "view_mode": "tree,form",
                        "view_type": "form",
                        "view_id": False,
                        "context": False,
                    }
                    record["vendor_dispatch"] = True
                    record["vendor_dispatch_exchange_rate"] = (
                        currency_rate.rate
                    )
                else:
                    raise UserError(
                        "There is no Valid Exchange Rate for the Consignmet Header Currency."
                    )
            else:
                raise UserError(
                    "There is no Active Custom Currency is Setup for the Selected Consignment Header."
                )
    else:
        raise UserError("Imports Ledger Accounts must be Specified.")
else:
    message = (
        "No Vendor Dispatch has been Created based on the Related Delivery Term Setup."
    )
    record["vendor_dispatch"] = False

    record["status"] = "In Transit"
    record["status_bar"] = "In Transit"
    record["vend_dispatch_status"] = message

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
| IMP - Restrict Delete in Consignment | `automation_62_imp_restrict_delete_in_consignment` |  | When a record is deleted on Consignment Header, runs _Execute Code_. | `model consignment_header`<br>`server action BugFix-Stock.action_imp_restrict_delete_in_consignment` |  |
| IMP - Update Cost Allocation Method in Consignment | `automation_86_imp_update_cost_allocation_method_in_consignment` |  | When a watched field changes in the form on Consignment Header, runs _Execute Code_. | `model consignment_header`<br>`server action BugFix-Stock.action_imp_update_cost_allocation_method_in_consignment` |  |
| IMP - Update Supplier Currency in Consignment | `automation_imp_update_supplier_currency_in_consignment` |  | When a watched field changes in the form on Consignment Header, runs _Execute Code_. | `model consignment_header`<br>`server action BugFix-Stock.action_imp_update_supplier_currency_in_consignment` |  |
| JIN - Company Id in Consignment Header | `automation_jin_company_id_in_consignment_header` |  | When a record is created or updated on Consignment Header, runs _Execute Code_. | `model consignment_header`<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_header` |  |
| JIN-Consignment Details Seq.No | `automation_56_jin_consignment_details_seq_no` |  | When a record is created or updated on Consignment Header, runs _Execute Code_. | `model consignment_header`<br>`server action BugFix-Stock.action_imp_consignment_details_seq_no` |  |

**Window actions (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Header (consignment_header) | `action_consignment_header_consignment_header` | Opens **Consignment Header** records (kanban,tree,form). | `model consignment_header` |  |
| Consignment Header (consignment_header) | `action_consignment_header_consignment_header_2` | Opens **Consignment Header** records (kanban,tree,form). | `model consignment_header` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_consignment_header_consignment_header` (BugFix-Studio-Misc) |
| Consignment Header Analysis | `action_consignment_header_analysis` | Opens **Consignment Header** records (graph,pivot). | `model consignment_header` | `menu BugFix-Stock.menu_consignment_header_analysis` |
| Imports - 01 | `action_imports_01` | Opens **Consignment Header** records (tree,form). | `model consignment_header` | `menu BugFix-Stock.menu_imports_01` |
| Purchase Invoice Header | `action_purchase_invoice_header` | Opens **Consignment Header** records (tree,form,kanban). | `model consignment_header` | `menu BugFix-Studio-Misc.menu_purchase_imports_01_purchase_invoices` (BugFix-Studio-Misc) |
| Purchase Invoices | `action_purchase_invoices` | Opens **Consignment Header** records (tree,kanban,form). | `model consignment_header` | `menu BugFix-Studio-Misc.menu_purchase_imports_purchase_invoices` (BugFix-Studio-Misc) |
| Purchase Invoices | `action_purchase_invoices_3` | Opens **Consignment Header** records (kanban,tree,form). | `model consignment_header` |  |
| consignment_header | `action_consignment_header` | Opens **Consignment Header** records (kanban,tree,form). | `model consignment_header` |  |

**Views (7):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for consignment_header | `view_consignment_header_form` | form | full form layout with 7 fields | Consignment Header form with status-driven workflow buttons (Copy/Clear PO Lines, Confirm Invoice, Validate Consolidation, Vendor Dispatch, Port Receipt, header charges, Custom Duty, TP Invoice). Buttons use hardcoded numeric action ids (1962-1987). | `server action BugFix-Stock.action_imp_copy_po_lines_to_consignment`<br>`server action BugFix-Stock.action_imp_clear_po_lines_from_consignment`<br>`server action BugFix-Stock.action_imp_consignment_vendor_despatch`<br>`server action BugFix-Stock.action_imp_consignment_port_receipt`<br>`server action BugFix-Stock.action_imp_create_consignment_header_charges`<details><summary>+13 more</summary>`server action BugFix-Stock.action_imp_allocate_consignment_header_charges`<br>`server action BugFix-Stock.action_imp_consignment_custom_duty`<br>`server action BugFix-Stock.action_imp_confirm_purchase_invoice`<br>`server action BugFix-Stock.action_imp_copy_charges_to_tp_invoice`<br>`server action BugFix-Stock.action_imp_validate_consolidation_in_consignment`<br>`server action BugFix-Stock.action_imp_reset_header_charges_consignment`<br>`consignment_header.active`<br>`consignment_header.name`<br>`consignment_header.allocate_header_charges`<br>`consignment_header.create_header_charges`<br>`consignment_header.header_charges_allocated`<br>`consignment_header.lines_copied`<br>`consignment_header.status`</details> | `view BugFix-Purchase.view_consignment_header_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.view_default_form_view_for_consignment_header_inherit`<br>`view BugFix-Stock.view_bugfix_purchase_consignment_header_form_rewire_vendor_disp` |
| Default kanban view for ir.model(905,) | `view_consignment_header_kanban` | kanban | full kanban layout with 4 fields | Kanban cards for Consignment Headers showing vendor, total amount, reference and status. | `consignment_header.name`<br>`consignment_header.status`<br>`consignment_header.supplier_id`<br>`consignment_header.total_amount` |  |
| Default list view for consignment_header | `view_consignment_header_list` | tree | full tree layout with 2 fields | Base list view of Consignment Headers showing a drag handle (sequence) and the name. | `consignment_header.name`<br>`consignment_header.sequence` | `view BugFix-Stock.view_default_list_view_for_consignment_header_inherit` |
| Default search view for consignment_header | `view_consignment_header_search` | search | full search layout with 1 fields | Search view for Consignment Headers: search by name and an Archived filter. | `consignment_header.active`<br>`consignment_header.name` |  |
| Odoo Studio: Default form view for consignment_header customization | `view_default_form_view_for_consignment_header_inherit` | form | after `//button[@name='1967']`: add field status_bar; before `//form[1]/sheet[1]/widget[@name='web_ribbon']`: add div; set force_save=True, placeholder=New, string=Consignment Reference, readonly=1, required= on `//field[@name='name']`; inside `//group[@name='studio_group_01a9e3_left']`: add field description, field supplier_id, field accounting_currency_id, field supplier_invoice_number, field accounting_invoice_date, field shipment_start_date, field voucher_date; inside `//group[@name='studio_group_01a9e3_right']`: add field container_no, field shipping_mode, field custom_clearance_no, field create_uid, field create_date, field status, field cost_allocation_method, field consolidated, field consolidation_confirmed, field con_validated, field offset_account, field account_tax …; after `//group[@name='studio_group_01a9e3']`: add notebook | Customizes the Consignment Header form: adds a status bar, smart buttons (Header Charges, Line Charges, Custom Clearance entries), read-only 'Consignment Reference' title, vendor/currency/invoice/shipment/clearance and accounting fields mostly locked after Draft, plus a notebook of lines. | `view BugFix-Stock.view_consignment_header_form`<br>`window action BugFix-Stock.action_vendor_despatch`<br>`window action BugFix-Stock.action_custom_clearance`<br>`window action BugFix-Stock.action_header_charges`<br>`window action BugFix-Stock.action_line_charges`<details><summary>+84 more</summary>`consignment_header.active`<br>`consignment_header.account_charge`<br>`consignment_header.account_duty`<br>`consignment_header.account_tax`<br>`consignment_header.allocate_header_charges`<br>`consignment_header.bill_of_lading_filename`<br>`consignment_header.bill_of_lading`<br>`consignment_header.cargo_arrival_notice`<br>`consignment_header.accounting_company_id`<br>`consignment_header.con_validated`<br>`consignment_header.confirm_invoice`<br>`consignment_header.consignment_line_ids`<br>`consignment_header.consolidated`<br>`consignment_header.consolidation_confirmed`<br>`consignment_header.container_no`<br>`consignment_header.cost_allocation_method`<br>`consignment_header.create_header_charges`<br>`consignment_header.accounting_currency_id`<br>`consignment_header.custom_clearance_exchange_rate`<br>`consignment_header.custom_clearance_no`<br>`consignment_header.custom_clearance`<br>`consignment_header.custom_cleared_date`<br>`consignment_header.description`<br>`consignment_header.header_charges_allocated`<br>`consignment_header.accounting_invoice_date`<br>`consignment_header.lines_copied`<br>`consignment_header.offset_account`<br>`consignment_header.packing_list`<br>`consignment_header.shipment_start_date`<br>`consignment_header.shipping_mode`<br>`consignment_header.status_bar`<br>`consignment_header.status`<br>`consignment_header.supplier_document`<br>`consignment_header.supplier_id`<br>`consignment_header.supplier_invoice_number`<br>`consignment_header.total_allocate_amount`<br>`consignment_header.total_amount_cost_allocation_method`<br>`consignment_header.total_amount`<br>`consignment_header.vend_dispatch_status`<br>`consignment_header.vendor_dispatch_exchange_rate`<br>`consignment_header.vendor_dispatch`<br>`consignment_header.voucher_date`<br>`consignment_header.consignment_id__x_consignment_charge_h_count`<br>`consignment_header.consignment_id__x_consignment_charge_l_count`<br>`consignment_header.created_from_consignment_1__account_move_count`<br>`consignment_header.created_from_consignment__account_move_count`<br>`consignment_line.active`<br>`consignment_line.currency_id`<br>`consignment_line.name`<br>`consignment_line.allocate_amount`<br>`consignment_line.amount`<br>`consignment_line.concessional_rate`<br>`consignment_line.consignment_header_id`<br>`consignment_line.cost_allocation_method`<br>`consignment_line.delivery_remainder`<br>`consignment_line.description`<br>`consignment_line.exchange_rate`<br>`consignment_line.header_charges_allocated`<br>`consignment_line.invoice_qty`<br>`consignment_line.order_remainder`<br>`consignment_line.original_delivery_remainder`<br>`consignment_line.product_id`<br>`consignment_line.accounting_purchase_id`<br>`consignment_line.purchase_line_id`<br>`consignment_line.received_qty`<br>`consignment_line.sequence`<br>`consignment_line.status`<br>`consignment_line.stock_move_id`<br>`consignment_line.tariff_code`<br>`consignment_line.tot_charge_cd_ids`<br>`consignment_line.tot_charge_ex_cd_ids`<br>`consignment_line.tot_charge_ex_ids`<br>`consignment_line.tot_charge`<br>`consignment_line.tot_duty_ex_cd_ids`<br>`consignment_line.tot_duty`<br>`consignment_line.tot_tax_ex_cd_ids`<br>`consignment_line.tot_tax`<br>`consignment_line.unit_price`<br>`consignment_line.valid_charge`<br>`consignment_line.valid_duty`<br>`consignment_line.valid_tax`<br>`consignment_line.volume`<br>`consignment_line.warehouse`<br>`consignment_line.weight`</details> |  |
| Odoo Studio: Default list view for consignment_header customization | `view_default_list_view_for_consignment_header_inherit` | tree | set default_order=name desc on `//tree[1]`; before `//field[@name='sequence']`: add xpath, field description, field supplier_id, field accounting_currency_id, field shipment_start_date, field shipping_mode, field create_uid, field create_date, field accounting_invoice_date, field container_no, field supplier_invoice_number, field status; set column_invisible=1 on `//field[@name='sequence']`; set string=Invoice Reference on `//field[@name='name']` | Customizes the Consignment Header list: sorted by name descending, name shown as 'Invoice Reference' first, plus description, supplier, currency, shipment and invoice dates, shipping mode, container, supplier invoice no and status. | `view BugFix-Stock.view_consignment_header_list`<br>`consignment_header.container_no`<br>`consignment_header.accounting_currency_id`<br>`consignment_header.description`<br>`consignment_header.accounting_invoice_date`<details><summary>+5 more</summary>`consignment_header.shipment_start_date`<br>`consignment_header.shipping_mode`<br>`consignment_header.status`<br>`consignment_header.supplier_id`<br>`consignment_header.supplier_invoice_number`</details> |  |
| bugfix_purchase.consignment_header.form.rewire.vendor.dispatch | `view_bugfix_purchase_consignment_header_form_rewire_vendor_disp` | form |  | Inherits the Consignment Header form but contains only comments (its xpaths were stripped), so it changes nothing. | `view BugFix-Stock.view_consignment_header_form` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Header group_system | `access_consignment_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Consignment Header records. | `group base.group_system` (base)<br>`model consignment_header` |  |
| Consignment Header group_user | `access_consignment_header_group_user` | Gives **User types / Internal User** read access to Consignment Header records. | `group base.group_user` (base)<br>`model consignment_header` |  |
| consignment_header user access | `access_consignment_header_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Header records. | `group base.group_user` (base)<br>`model consignment_header` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consignment Header | `rule_jin_multi_company_consignment_header` | For everyone (global rule): read/write/create/delete on Consignment Header only where `['|', ('accounting_company_id', 'in', company_ids), ('accounting_company_id', '=', False)]`. | `model consignment_header`<br>`consignment_header.accounting_company_id` |  |
