# BugFix-Stock — `x_temp_consignment_lin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_consignment_lin` — Temp Consignment Line

*Created by this repo.* Python: `models/x_temp_consignment_lin.py`, `models/x_temp_consignment_lin_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_temp_consignment_lin_x_temp_consignment_lin_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_consignment_lin -->
A temporary candidate line in the Copy Import Order Lines wizard, holding one import PO line with its product, vendor, quantities, remainders, unit price, subtotal, weight and volume. Lines the user ticks are copied into the consignment when the wizard is applied.
<!-- /SUMMARY -->

**Fields (52):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_temp_consignment_lin.activity_summary`<br>`x_temp_consignment_lin.activity_type_icon`<br>`x_temp_consignment_lin.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_consignment_lin.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_consignment_lin.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_consignment_lin.activity_ids` |  |
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
| `x_active` | Active | boolean | Archive flag for temporary PO lines in the Copy PO Lines wizard; has a default. | stored |  | `default BugFix-Stock.default_150_x_temp_consignment_lin_x_active` |
| `x_currency_id` | Currency | many2one → `res.currency` | Currency of the candidate PO line; has a default value. | stored | `model res.currency` (base) | `default BugFix-Stock.default_152_x_temp_consignment_lin_x_currency_id` |
| `x_name` | Name | char | Name of the temporary PO line record. | stored |  |  |
| `x_studio_concessional_rate` | Concessional Rate | boolean | Concessional duty rate flag of the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_consignment_remainder` | Consignment Remainder | float | PO quantity still not assigned to a consignment for this candidate line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_delivery_date` | Delivery Date | datetime | Expected delivery date of the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_delivery_remainder` | Delivery Remainder | float | Quantity still to be delivered for the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_description` | Description | text | Description of the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_indent_no` | Indent No | char | Indent (purchase order) number of the candidate line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_product_id` | Product | many2one → `product.product` | Product of the candidate PO line. | stored | `model product.product` (product) | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_purchase_id` | Order Reference | many2one → `purchase.order` | Purchase order of the candidate line. | stored | `model purchase.order` (purchase) | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_purchase_line_id` | Purchase Line Id | many2one → `purchase.order.line` | Purchase order line represented by this candidate line. | stored | `model purchase.order.line` (purchase) | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_quantity` | Quantity | float | Quantity of the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_select` | Select | boolean | Tick box in the Copy PO Lines wizard; ticked lines are copied to the consignment by the 'Apply Selected PO Lines' action. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_sequence` | Sequence | integer | Ordering number with a default; not shown in any view. | stored |  | `default BugFix-Stock.default_151_x_temp_consignment_lin_x_studio_sequence` |
| `x_studio_subtotal` | Subtotal | float | Subtotal value of the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_supplier_id` | Vendor | many2one → `res.partner` | Vendor of the candidate PO line. | stored | `model res.partner` (base) | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_temp_consignment_header_id` | Temp Consignment Header Id | many2one → `x_temp_consignment_hea` | Copy PO Lines wizard record this candidate line belongs to. | stored | `model x_temp_consignment_hea` |  |
| `x_studio_unit_price` | Unit Price | float | Unit price of the candidate PO line. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_uom_id` | UOM | many2one → `uom.uom` | Unit of measure of the candidate PO line. | stored | `model uom.uom` (uom) | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_volume` | Volume | float | Volume of the candidate PO line's goods. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_weight` | Weight | float | Weight of the candidate PO line's goods. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |

**Window actions (9):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Lines | `action_2847_consignment_lines` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` |  |
| TEMP CONN LINE | `action_1656_temp_conn_line` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp_conn_line` (BugFix-Studio-Misc) |
| TEMP123 | `action_1657_temp123` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp123` (BugFix-Studio-Misc) |
| TEST66 | `action_1658_test66` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` |  |
| Temp Consignment Line | `action_1262_temp_consignment_line` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` | `menu BugFix-Stock.menu_778_temp_consignment_line`<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_temp_consignment_line` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp_consignment_line` (BugFix-Studio-Misc) |
| Temp Consignment Line | `action_1300_temp_consignment_line` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` |  |
| Temp Consignment Line | `action_1356_temp_consignment_line` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` | `menu BugFix-Stock.menu_f6_temp_consignment_line` |
| Temp Consignment Line | `action_2850_temp_consignment_line` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` |  |
| Temp Consignment Line | `action_2860_temp_consignment_line` | Opens **Temp Consignment Line** records (tree,form). | `model x_temp_consignment_lin` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp Consignment Line group_system | `access_1297_temp_consignment_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp Consignment Line records. | `group base.group_system` (base)<br>`model x_temp_consignment_lin` |  |
| Temp Consignment Line group_user | `access_1298_temp_consignment_line_group_user` | Gives **User types / Internal User** read access to Temp Consignment Line records. | `group base.group_user` (base)<br>`model x_temp_consignment_lin` |  |
| x_temp_consignment_lin user access | `access_x_temp_consignment_lin_user` | Gives **User types / Internal User** read/write/create/delete access to Temp Consignment Line records. | `group base.group_user` (base)<br>`model x_temp_consignment_lin` |  |
