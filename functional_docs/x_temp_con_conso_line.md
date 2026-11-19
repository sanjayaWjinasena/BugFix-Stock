# BugFix-Stock — `x_temp_con_conso_line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_con_conso_line` — Temp Con. Conso. Line

*Created by this repo.* Python: `models/x_temp_con_conso_line.py`, `models/x_temp_con_conso_line_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_temp_con_conso_line_x_temp_con_conso_line_purchase_jin_procurement_end_user_imp` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_con_conso_line -->
A temporary candidate line in the Copy PI Lines to Consolidation wizard, holding one consignment with its vendor, container, customs clearance number, dates, shipping mode and status. Lines the user ticks are turned into consolidation lines when the wizard is applied.
<!-- /SUMMARY -->

**Fields (45):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_temp_con_conso_line.activity_summary`<br>`x_temp_con_conso_line.activity_type_icon`<br>`x_temp_con_conso_line.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_con_conso_line.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_con_conso_line.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_con_conso_line.activity_ids` |  |
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
| `x_active` | Active | boolean | Archive flag; defaults to active. | stored |  | `default BugFix-Stock.default_final_bugfix_stock_field_x_temp_con_conso_line_x_active_true` |
| `x_name` | Name | char | Name of the temporary consolidation candidate line. | stored |  |  |
| `x_studio_consignment_id` | Consignment Id | many2one → `x_consignment_header` | Consignment offered for selection in the Copy PI Lines to Consolidation wizard. | stored | `model x_consignment_header` |  |
| `x_studio_container_no` | Container No | char | Container number of the candidate consignment. | stored |  |  |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Currency of the candidate consignment; has a default value. | stored | `model res.currency` (base) | `default BugFix-Stock.default_229_x_temp_con_conso_line_x_studio_currency_id`<br>`default BugFix-Stock.default_430_x_temp_con_conso_line_x_studio_currency_id` |
| `x_studio_custom_clearance_no` | Custom Clearance No | char | Customs clearance number of the candidate consignment. | stored |  |  |
| `x_studio_invoice_date` | Invoice Date | date | Supplier invoice date of the candidate consignment. | stored |  |  |
| `x_studio_select` | Select | boolean | Tick box in the consolidation wizard; ticked consignments become consolidation lines via 'Apply Selected PI Lines to Consolidation'. | stored |  |  |
| `x_studio_sequence` | Sequence | integer | Ordering number with a default value. | stored |  | `default BugFix-Stock.default_210_x_temp_con_conso_line_x_studio_sequence` |
| `x_studio_shipment_start_date` | Shipment Start Date | date | Shipment start date of the candidate consignment. | stored |  |  |
| `x_studio_shipping_mode` | Shipping Mode | selection: Air=Air; Sea=Sea; Road=Road; Courier=Courier | Shipping mode of the candidate consignment: Air, Sea, Road or Courier. | stored |  |  |
| `x_studio_status` | Status | selection: Draft=Draft; Consignment=Confirmed; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done; TP Invoice=TP Invoice | Status of the candidate consignment (Draft, Confirmed, In Transit, Under Custom Clearance, Done, TP Invoice). | stored |  |  |
| `x_studio_supplier_id` | Vendor | many2one → `res.partner` | Vendor of the candidate consignment. | stored | `model res.partner` (base) |  |
| `x_studio_supplier_invoice_no` | Supplier Invoice No | char | Supplier invoice number of the candidate consignment. | stored |  |  |
| `x_studio_temp_consolidated_header_id` | Temp Consolidated Header Id | many2one → `x_temp_con_consolidate` | Consolidation wizard record this candidate line belongs to. | stored | `model x_temp_con_consolidate` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp Con. Conso. Line group_system | `access_1384_temp_con__conso__line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp Con. Conso. Line records. | `group base.group_system` (base)<br>`model x_temp_con_conso_line` |  |
| Temp Con. Conso. Line group_user | `access_1385_temp_con__conso__line_group_user` | Gives **User types / Internal User** read access to Temp Con. Conso. Line records. | `group base.group_user` (base)<br>`model x_temp_con_conso_line` |  |
