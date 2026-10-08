# BugFix-Stock — `x_consignment_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_consignment_line` — Consignment Line

*Created by this repo.* Python: `models/x_consignment_line.py`, `models/x_consignment_line_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_consignment_line_x_consignment_line_purchase_jin_po_goods_receivers` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_x_consignment_line_x_consignment_line_purchase_jin_procurement_end_user_import` (BugFix-Studio-Misc)<br>`purchase.order.line._compute_x_studio_consignment_remainder()` (BugFix-Purchase)<br>`server action BugFix-Accounting.server_action_1370_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_imp_update_consignment_pi` (BugFix-Accounting)<br>`server action BugFix-Purchase.action_consignment_vendor_dispatch` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_consignment_line -->
A Consignment Line is one product from an import purchase order line shipped in a consignment, with the PO and PO line, product, warehouse, unit price, invoice quantity, received quantity, delivery remainder and amount. An automation checks that the invoice quantity is not negative and not above what remains on the PO line, and another sets the company. Most of the many total charge, duty and tax fields and validity flags are not used by any view or logic in this repo.
<!-- /SUMMARY -->

**Fields (99):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_consignment_line.activity_summary`<br>`x_consignment_line.activity_type_icon`<br>`x_consignment_line.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_consignment_line.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_consignment_line.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_consignment_line.activity_ids` |  |
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
| `x_active` | Active | boolean | Archive flag for consignment lines; defaults to active. | stored |  | `default BugFix-Stock.default_140_x_consignment_line_x_active`<br>`view BugFix-Stock.ported_view_2814_default_form_view_for_x_consignment_line`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.view_2815_default_search_view_for_x_consignment_line_e` |
| `x_currency_id` | Currency | many2one → `res.currency` | Read-only currency of the consignment line; has a default value and is shown in the line form and list. | stored | `model res.currency` (base) | `default BugFix-Stock.default_146_x_consignment_line_x_currency_id`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_name` | Name | char | Name of the consignment line. | stored |  | `view BugFix-Stock.ported_view_2813_default_list_view_for_x_consignment_line`<br>`view BugFix-Stock.ported_view_2814_default_form_view_for_x_consignment_line`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.view_2815_default_search_view_for_x_consignment_line_e` |
| `x_studio_allocate_amount` | Allocate Amount | float | Read-only amount of header charges allocated to this line; not shown in any view in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_amount` | Amount | float | Read-only line amount (value of the invoiced quantity); shown in the consignment line form and list. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_boolean_field_Gbd5Y` | Valid Duty | boolean | Extra 'Valid Duty' checkbox left from Studio; not used by any view or logic. | stored |  |  |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the consignment line; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_513_jin_multi_company_consignment_line`<br>`server action BugFix-Stock.sa_f5_x_consignment_line_jin_company_id_in_consignment_line`<br>`server action BugFix-Stock.server_action_2608_jin_company_id_in_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_concessional_rate` | Concessional Rate | boolean | Checkbox marking that a concessional (reduced) duty rate applies to the line; not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_consignment_header_id` | Consignment No | many2one → `x_consignment_header` | Consignment this line belongs to (deletion of the consignment is restricted while lines exist). | stored | `model x_consignment_header` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_cost_allocation_method` | Cost Allocation Method | selection: equal=Equal; by_quantity=By Quantity; by_current_cost_price=By Current Cost; by_weight=By Weight; by_volume=By Volume | Read-only cost allocation method for the line (Equal, By Quantity, By Current Cost, By Weight, By Volume); not shown in any view. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_delivery_remainder` | Delivery Remainder | float | Read-only quantity still to be delivered; recalculated by an automation as Original Delivery Remainder minus Invoice Qty. | stored |  | `server action BugFix-Stock.server_action_2098_imp_delivery_remainder_in_consignment_lines`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_description` | Description | char | Read-only product description of the line, used in the invoice quantity validation error messages; non-stored with no compute in this repo. | not stored |  | `server action BugFix-Stock.sa_f5_x_consignment_line_imp_invoice_qty_validation_in_consignment`<br>`server action BugFix-Stock.server_action_1304_imp_invoice_qty_validation_in_consignment`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_exchange_rate` | Exchange Rate | float | Exchange rate for the line; not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_header_charges_allocated` | Header Charges Allocated | boolean | Read-only flag showing header charges have been allocated to this line; not shown in any view. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_indent_no` | Indent No | char | Read-only indent (purchase order) number of the line; shown in the lines list. | stored |  | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_invoice_qty` | Invoice Qty. | float | Quantity invoiced in this consignment; validated by an automation to be non-negative and not above the PO quantity remaining, and used to recompute the delivery remainder. | stored |  | `server action BugFix-Stock.sa_f5_x_consignment_line_imp_invoice_qty_validation_in_consignment`<br>`server action BugFix-Stock.server_action_1304_imp_invoice_qty_validation_in_consignment`<br>`server action BugFix-Stock.server_action_2098_imp_delivery_remainder_in_consignment_lines`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<details><summary>+1 more</summary>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line`</details> |
| `x_studio_many2many_field_ZvmKu` | tot_tax_ex_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total tax (Ex Cd variant, technical label tot_tax_ex_cd_ids); shown in the consignment lines list. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_order_remainder` | Consignment Remainder | float | Read-only quantity remaining on the purchase order line for consignment; not shown in any view. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_original_delivery_remainder` | Original Delivery Remainder | float | Starting delivery remainder for the line; the automation subtracts Invoice Qty from it to get Delivery Remainder. | stored |  | `server action BugFix-Stock.server_action_2098_imp_delivery_remainder_in_consignment_lines`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_product_id` | Product | many2one → `product.product` | Product being shipped on this consignment line. | stored | `model product.product` (product) | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_purchase_id` | Purchase Order | many2one → `purchase.order` | Purchase order the consignment line comes from. | stored | `model purchase.order` (purchase) | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_purchase_line_id` | Purchase Line Id | many2one → `purchase.order.line` | Purchase order line the consignment line comes from; used to check the invoiced quantity does not exceed the PO quantity. | stored | `model purchase.order.line` (purchase) | `server action BugFix-Stock.sa_f5_x_consignment_line_imp_invoice_qty_validation_in_consignment`<br>`server action BugFix-Stock.server_action_1304_imp_invoice_qty_validation_in_consignment`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_received_qty` | Received Qty. | float | Read-only quantity received for this line; shown in the consignment line form and list. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_sequence` | Sequence | integer | Ordering number for consignment lines (list drag handle). | stored |  | `default BugFix-Stock.default_141_x_consignment_line_x_studio_sequence`<br>`view BugFix-Stock.ported_view_2813_default_list_view_for_x_consignment_line`<br>`view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_status` | Status | selection: Draft=Draft; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done | Read-only status of the line: Draft, In Transit, Under Custom Clearance or Done. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_stock_move_id` | Stock Move Id | many2one → `stock.move` | Stock move linked to the consignment line; not used by any view or logic in this repo. | stored | `model stock.move` (stock) | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_tariff_code` | Tariff Code | many2one → `x_tariffmaster` | Read-only customs tariff code of the line, shown in the form and list; non-stored with no compute in this repo, so it is empty. | not stored | `model x_tariffmaster` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_test1` | Test1 | char | Read-only test text field; not used by any view or logic. | stored |  |  |
| `x_studio_test2` | Test2 | many2one → `x_consignment_header` | Read-only test link to a consignment; not used by any view or logic. | stored | `model x_consignment_header` |  |
| `x_studio_tot_charge` | Tot Charge | float | Total charge amount for the consignment line; a plain number with no compute or view use in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_tot_charge_cd` | Tot Charge Cd | float | Total charge amount for the consignment line (customs-duty basis variant 'Cd'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_charge_cd_ids` | tot_charge_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total charge (customs-duty basis variant 'Cd'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_charge_ex` | Tot Charge Ex | float | Total charge amount for the consignment line (exclusive variant 'Ex'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_charge_ex_cd` | Tot Charge Ex Cd | float | Total charge amount for the consignment line (exclusive customs-duty variant 'Ex Cd'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_charge_ex_cd_ids` | tot_charge_ex_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total charge (exclusive customs-duty variant 'Ex Cd'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_charge_ex_ids` | tot_charge_ex_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total charge (exclusive variant 'Ex'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_charge_ids` | tot_charge_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total charge; shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_duty` | Tot Duty | float | Total duty amount for the consignment line; a plain number with no compute or view use in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_tot_duty_cd` | Tot Duty Cd | float | Total duty amount for the consignment line (customs-duty basis variant 'Cd'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_duty_cd_ids` | tot_duty_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total duty (customs-duty basis variant 'Cd'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_duty_ex` | Tot Duty Ex | float | Total duty amount for the consignment line (exclusive variant 'Ex'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_duty_ex_cd` | Tot Duty Ex Cd | float | Total duty amount for the consignment line (exclusive customs-duty variant 'Ex Cd'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_duty_ex_cd_ids` | tot_duty_ex_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total duty (exclusive customs-duty variant 'Ex Cd'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_duty_ex_ids` | tot_duty_ex_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total duty (exclusive variant 'Ex'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_duty_ids` | tot_duty_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total duty; shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_tax` | Tot Tax | float | Total tax amount for the consignment line; a plain number with no compute or view use in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_tot_tax_cd` | Tot Tax Cd | float | Total tax amount for the consignment line (customs-duty basis variant 'Cd'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_tax_cd_ids` | tot_tax_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total tax (customs-duty basis variant 'Cd'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_tax_ex` | Tot Tax Ex | float | Total tax amount for the consignment line (exclusive variant 'Ex'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_tax_ex_cd` | Tot Tax Ex Cd | float | Total tax amount for the consignment line (exclusive customs-duty variant 'Ex Cd'); a plain number with no compute or view use in this repo. | stored |  |  |
| `x_studio_tot_tax_ex_cd_ids` | tot_tax_ex_cd_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total tax (exclusive customs-duty variant 'Ex Cd'); shown in the consignment lines list. No logic in this repo fills it. Note: the list view shows `x_studio_many2many_field_ZvmKu`, which carries the same technical label. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_tax_ex_ids` | tot_tax_ex_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total tax (exclusive variant 'Ex'); shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_tot_tax_ids` | tot_tax_ids | many2many → `x_misc_charge_codes` | Misc charge codes making up the line's total tax; shown in the consignment lines list. No logic in this repo fills it. | stored | `model x_misc_charge_codes` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_unit_price` | Unit Price | float | Unit price of the product on the consignment line. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_valid_charge` | Valid Charge | boolean | Validity flag for the line's charge calculation; not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_valid_charge_cd` | Valid Charge Cd | boolean | Validity flag for the line's charge calculation (Cd variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_charge_ex` | Valid Charge Ex | boolean | Validity flag for the line's charge calculation (Ex variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_charge_ex_cd` | Valid Charge Ex Cd | boolean | Validity flag for the line's charge calculation (Ex Cd variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_duty` | Valid Duty | boolean | Validity flag for the line's duty calculation; not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_valid_duty_cd` | Valid Duty Cd | boolean | Validity flag for the line's duty calculation (Cd variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_duty_ex` | Valid Duty Ex | boolean | Validity flag for the line's duty calculation (Ex variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_duty_ex_cd` | Valid Duty Ex Cd | boolean | Validity flag for the line's duty calculation (Ex Cd variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_tax` | Valid Tax | boolean | Validity flag for the line's tax calculation; not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_valid_tax_cd` | Valid Tax Cd | boolean | Validity flag for the line's tax calculation (Cd variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_tax_ex` | Valid Tax Ex | boolean | Validity flag for the line's tax calculation (Ex variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_valid_tax_ex_cd` | Valid Tax Ex Cd | boolean | Validity flag for the line's tax calculation (Ex Cd variant); not used by any view or logic in this repo. | stored |  |  |
| `x_studio_volume` | Volume | float | Volume of the line's goods (basis for 'By Volume' cost allocation); not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| `x_studio_warehouse` | Warehouse | many2one → `stock.warehouse` | Read-only destination warehouse of the consignment line; shown in the line form and list. | stored | `model stock.warehouse` (stock) | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header`<br>`view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line`<br>`view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| `x_studio_weight` | Weight | float | Weight of the line's goods (basis for 'By Weight' cost allocation); not used by any view or logic in this repo. | stored |  | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |

**Server actions (6):**

- **Execute Code** (`server_action_1304_imp_invoice_qty_validation_in_consignment`, type `code`)
  - Function: Run by the Invoice Qty Validation automation: raises an error if a consignment line's Invoice Qty is negative or exceeds the PO line quantity minus invoice quantities on other consignment lines.
  - Depends on: `model purchase.order.line` (purchase), `model x_consignment_line`, `x_consignment_line.x_studio_description`, `x_consignment_line.x_studio_invoice_qty`, `x_consignment_line.x_studio_purchase_line_id`
  - Used by: `automation BugFix-Stock.automation_59_imp_invoice_qty_validation_in_consignment`
  <details><summary>code (20 lines)</summary>

```python

if record.x_studio_invoice_qty:
  
  if record.x_studio_invoice_qty < 0.00:
    raise UserError("Negative Quantities are not Allowed in Item No: " + record.x_studio_description)
  
  purch_line = env['purchase.order.line'].search([('id', '=', record.x_studio_purchase_line_id.id)],limit=1)
  result = 0
  if purch_line:
    con_remainder = 0
    if purch_line.product_qty != purch_line.qty_received:
      con_lines = env['x_consignment_line'].search([('x_studio_purchase_line_id', '=', record.x_studio_purchase_line_id.id), ('id', '!=', record.id)])
      if con_lines:
        for sum_lines in con_lines:
          con_remainder += sum_lines.x_studio_invoice_qty
      
    result = (purch_line.product_qty - con_remainder)
 
  if record.x_studio_invoice_qty > result:
    raise UserError("Quantity to Invoice Should not be exceeding the Consignment Remainder in Item No: " + record.x_studio_description)
```
  </details>
- **Execute Code** (`server_action_2608_jin_company_id_in_consignment_line`, type `code`)
  - Function: Run by an automation: sets the Company of a Consignment Line to the user's active company.
  - Depends on: `model res.company` (base), `model x_consignment_line`, `x_consignment_line.x_studio_company_id`
  - Used by: `automation BugFix-Stock.automation_281_jin_company_id_in_consignment_line`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Delivery Remainder in Consignment Lines** (`server_action_2098_imp_delivery_remainder_in_consignment_lines`, type `code`)
  - Function: On a consignment line with an Invoice Qty, sets Delivery Remainder to Original Delivery Remainder minus Invoice Qty.
  - Depends on: `model x_consignment_line`, `x_consignment_line.x_studio_delivery_remainder`, `x_consignment_line.x_studio_invoice_qty`, `x_consignment_line.x_studio_original_delivery_remainder`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_invoice_qty:
  record['x_studio_delivery_remainder'] = record.x_studio_original_delivery_remainder - record.x_studio_invoice_qty
```
  </details>
- **IMP - Invoice Qty. Validation in Consignment** (`sa_f5_x_consignment_line_imp_invoice_qty_validation_in_consignment`, type `code`)
  - Function: Validates a consignment line's Invoice Qty: raises an error if it is negative or exceeds the PO line quantity minus invoice quantities already on other consignment lines for the same PO line.
  - Depends on: `model purchase.order.line` (purchase), `model x_consignment_line`, `x_consignment_line.x_studio_description`, `x_consignment_line.x_studio_invoice_qty`, `x_consignment_line.x_studio_purchase_line_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (19 lines)</summary>

```python
if record.x_studio_invoice_qty:
  
  if record.x_studio_invoice_qty < 0.00:
    raise UserError("Negative Quantities are not Allowed in Item No: " + record.x_studio_description)
  
  purch_line = env['purchase.order.line'].search([('id', '=', record.x_studio_purchase_line_id.id)],limit=1)
  result = 0
  if purch_line:
    con_remainder = 0
    if purch_line.product_qty != purch_line.qty_received:
      con_lines = env['x_consignment_line'].search([('x_studio_purchase_line_id', '=', record.x_studio_purchase_line_id.id), ('id', '!=', record.id)])
      if con_lines:
        for sum_lines in con_lines:
          con_remainder += sum_lines.x_studio_invoice_qty
      
    result = (purch_line.product_qty - con_remainder)
 
  if record.x_studio_invoice_qty > result:
    raise UserError("Quantity to Invoice Should not be exceeding the Consignment Remainder in Item No: " + record.x_studio_description)
```
  </details>
- **JIN - Company Id in Consignment Line** (`sa_f5_x_consignment_line_jin_company_id_in_consignment_line`, type `code`)
  - Function: Sets the Company of a Consignment Line to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_consignment_line`, `x_consignment_line.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **TEST IMP** (`server_action_1665_test_imp`, type `code`)
  - Function: Test action that just raises an error showing the consignment line id; debug only.
  - Depends on: `model x_consignment_line`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
raise UserError(record.id)
```
  </details>
**Automations (3):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Delivery Remainder in Consignment Lines | `base_automation_181_imp_delivery_remainder_in_consignment_lines` | archived | When a record is created or updated on Consignment Line, runs nothing (no action linked). **Archived — does not run.** | `model x_consignment_line` |  |
| IMP - Invoice Qty. Validation in Consignment | `automation_59_imp_invoice_qty_validation_in_consignment` |  | When a record is created or updated on Consignment Line, runs _Execute Code_. | `model x_consignment_line`<br>`server action BugFix-Stock.server_action_1304_imp_invoice_qty_validation_in_consignment` |  |
| JIN - Company Id in Consignment Line | `automation_281_jin_company_id_in_consignment_line` |  | When a record is created or updated on Consignment Line, runs _Execute Code_. | `model x_consignment_line`<br>`server action BugFix-Stock.server_action_2608_jin_company_id_in_consignment_line` |  |

**Window actions (11):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| CONSIGNMENT LINES | `action_1661_consignment_lines` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` |  |
| Consignment Line (x_consignment_line) | `action_2863_consignment_line_x_consignment_line` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_consignment_line_x_consignment_line` (BugFix-Studio-Misc) |
| Consignment Line (x_consignment_line) | `action_2853_consignment_line_x_consignment_line` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` |  |
| Consignment Lines | `action_1664_consignment_lines` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` |  |
| Consignment Lines | `action_2857_consignment_lines` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_consignment_lines` (BugFix-Studio-Misc) |
| Purchase Invoice Line | `action_1257_purchase_invoice_line` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` | `menu BugFix-Stock.menu_f6_consignment_line` |
| Purchase Invoice Line | `action_1663_purchase_invoice_line` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_purchase_invoice_lines` (BugFix-Studio-Misc) |
| Purchase Invoice Lines | `action_1662_purchase_invoice_lines` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` |  |
| Purchase Invoice Lines | `action_2886_purchase_invoice_lines` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_purchase_invoice_lines` (BugFix-Studio-Misc) |
| Purchase Invoice Lines | `action_2053_purchase_invoice_lines` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` |  |
| x_consignment_line | `action_2801_x_consignment_line` | Opens **Consignment Line** records (tree,form). | `model x_consignment_line` |  |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_consignment_line | `ported_view_2814_default_form_view_for_x_consignment_line` | form | full form layout with 2 fields | Base form of a Consignment Line: archived ribbon, required name title and two empty groups filled by the Studio customization view. | `x_consignment_line.x_active`<br>`x_consignment_line.x_name` | `view BugFix-Stock.ported_view_2817_studio_form_x_consignment_line` |
| Default list view for x_consignment_line | `ported_view_2813_default_list_view_for_x_consignment_line` | tree | full tree layout with 2 fields | Base list view of Consignment Lines showing a drag handle (sequence) and the name. | `x_consignment_line.x_name`<br>`x_consignment_line.x_studio_sequence` | `view BugFix-Stock.ported_view_2818_studio_tree_x_consignment_line` |
| Default search view for x_consignment_line | `view_2815_default_search_view_for_x_consignment_line_e` | search | full search layout with 1 fields | Search view for Consignment Lines: search by name and an Archived filter. | `x_consignment_line.x_active`<br>`x_consignment_line.x_name` |  |
| Odoo Studio: Default form view for x_consignment_line customization | `ported_view_2817_studio_form_x_consignment_line` | form | set invisible=1 on `//field[@name='x_name']`; inside `//group[@name='studio_group_0644e6_left']`: add field x_studio_purchase_id, field x_studio_product_id, field x_studio_description, field x_studio_warehouse, field x_studio_tariff_code, field x_studio_consignment_header_id; inside `//group[@name='studio_group_0644e6_right']`: add field x_currency_id, field x_studio_invoice_qty, field x_studio_unit_price, field x_studio_amount, field x_studio_received_qty, field x_studio_status | Customizes the Consignment Line form: hides the name and shows PO, product, description, warehouse, tariff code, header, currency, invoice/received quantities, unit price, amount and status. | `view BugFix-Stock.ported_view_2814_default_form_view_for_x_consignment_line`<br>`x_consignment_line.x_currency_id`<br>`x_consignment_line.x_studio_amount`<br>`x_consignment_line.x_studio_consignment_header_id`<br>`x_consignment_line.x_studio_description`<details><summary>+8 more</summary>`x_consignment_line.x_studio_invoice_qty`<br>`x_consignment_line.x_studio_product_id`<br>`x_consignment_line.x_studio_purchase_id`<br>`x_consignment_line.x_studio_received_qty`<br>`x_consignment_line.x_studio_status`<br>`x_consignment_line.x_studio_tariff_code`<br>`x_consignment_line.x_studio_unit_price`<br>`x_consignment_line.x_studio_warehouse`</details> |  |
| Odoo Studio: Default list view for x_consignment_line customization | `ported_view_2818_studio_tree_x_consignment_line` | tree | set create=false, default_order=x_studio_consignment_header_id desc, delete=false, edit=true, editable=bottom on `//tree[1]`; before `//field[@name='x_studio_sequence']`: add field x_studio_consignment_header_id, field x_studio_purchase_id, field x_studio_indent_no, field x_studio_product_id, field x_studio_description, field x_studio_tariff_code, field x_studio_warehouse, field x_studio_invoice_qty, field x_studio_received_qty, field x_studio_unit_price, field x_studio_amount, field x_studio_company_id …; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set column_invisible=1 on `//field[@name='x_name']` | Customizes the Consignment Line list: editable inline, no create/delete, sorted by header descending, showing header, PO, indent no, product, tariff, warehouse, quantities, price, amount and company; hides sequence and name. | `view BugFix-Stock.ported_view_2813_default_list_view_for_x_consignment_line`<br>`x_consignment_line.x_currency_id`<br>`x_consignment_line.x_studio_amount`<br>`x_consignment_line.x_studio_company_id`<br>`x_consignment_line.x_studio_consignment_header_id`<details><summary>+23 more</summary>`x_consignment_line.x_studio_description`<br>`x_consignment_line.x_studio_indent_no`<br>`x_consignment_line.x_studio_invoice_qty`<br>`x_consignment_line.x_studio_many2many_field_ZvmKu`<br>`x_consignment_line.x_studio_product_id`<br>`x_consignment_line.x_studio_purchase_id`<br>`x_consignment_line.x_studio_received_qty`<br>`x_consignment_line.x_studio_status`<br>`x_consignment_line.x_studio_tariff_code`<br>`x_consignment_line.x_studio_tot_charge_cd_ids`<br>`x_consignment_line.x_studio_tot_charge_ex_cd_ids`<br>`x_consignment_line.x_studio_tot_charge_ex_ids`<br>`x_consignment_line.x_studio_tot_charge_ids`<br>`x_consignment_line.x_studio_tot_duty_cd_ids`<br>`x_consignment_line.x_studio_tot_duty_ex_cd_ids`<br>`x_consignment_line.x_studio_tot_duty_ex_ids`<br>`x_consignment_line.x_studio_tot_duty_ids`<br>`x_consignment_line.x_studio_tot_tax_cd_ids`<br>`x_consignment_line.x_studio_tot_tax_ex_cd_ids`<br>`x_consignment_line.x_studio_tot_tax_ex_ids`<br>`x_consignment_line.x_studio_tot_tax_ids`<br>`x_consignment_line.x_studio_unit_price`<br>`x_consignment_line.x_studio_warehouse`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Line group_system | `access_1293_consignment_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Consignment Line records. | `group base.group_system` (base)<br>`model x_consignment_line` |  |
| Consignment Line group_user | `access_1294_consignment_line_group_user` | Gives **User types / Internal User** read access to Consignment Line records. | `group base.group_user` (base)<br>`model x_consignment_line` |  |
| x_consignment_line user access | `access_x_consignment_line_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Line records. | `group base.group_user` (base)<br>`model x_consignment_line` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consignment Line | `rule_513_jin_multi_company_consignment_line` | For everyone (global rule): read/write/create/delete on Consignment Line only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_consignment_line`<br>`x_consignment_line.x_studio_company_id` |  |
