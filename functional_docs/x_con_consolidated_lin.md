# BugFix-Stock — `x_con_consolidated_lin`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_con_consolidated_lin` — Con. Consolidated Line

*Created by this repo.* Python: `models/x_con_consolidated_lin.py`, `models/x_con_consolidated_lin_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_con_consolidated_line_x_con_consolidated_lin_purchase_jin_procurement_end_user_` (BugFix-Studio-Misc)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_con_consolidated_lin -->
A Consolidated Line is one consignment included in a consolidation, holding the consignment link and copied details such as vendor, container number, customs clearance number, invoice date, shipping mode and status. When a line is deleted an automation makes its consignment available for consolidation again, and another sets the line's company.
<!-- /SUMMARY -->

**Fields (45):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.ported_primary_3071_form_x_con_consolidated_lin`<br>`x_con_consolidated_lin.activity_summary`<br>`x_con_consolidated_lin.activity_type_icon`<br>`x_con_consolidated_lin.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_con_consolidated_lin.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_con_consolidated_lin.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_con_consolidated_lin.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.ported_primary_3071_form_x_con_consolidated_lin` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.ported_primary_3071_form_x_con_consolidated_lin` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for consolidation lines; defaults to active. | stored |  | `default BugFix-Stock.default_202_x_con_consolidated_lin_x_active`<br>`view BugFix-Stock.ported_primary_3071_form_x_con_consolidated_lin`<br>`view BugFix-Stock.view_3072_default_search_view_for_x_con_consolidated_lin_e` |
| `x_name` | Name | char | Name of the consolidation line. | stored |  | `view BugFix-Stock.ported_primary_3070_tree_x_con_consolidated_lin`<br>`view BugFix-Stock.ported_primary_3071_form_x_con_consolidated_lin`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.view_3072_default_search_view_for_x_con_consolidated_lin_e` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the consolidation line; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_515_jin_multi_company_consolidated_line`<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_lin_jin_company_id_in_consolidated_line`<br>`server action BugFix-Stock.server_action_2611_jin_company_id_in_consolidated_line`<br>`view BugFix-Stock.ported_view_5564_odoo_studio_default_list_view_for_x_con_` |
| `x_studio_consignment_id` | Consignment Id | many2one → `x_consignment_header` | Consignment included in this consolidation line; made available again when the line is deleted. | stored | `model x_consignment_header` | `server action BugFix-Stock.sa_f5_x_con_consolidated_lin_imp_con_lines_make_available_in_delete`<br>`server action BugFix-Stock.server_action_1424_imp_con_lines_make_available_in_delete`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_consolidated_header_id` | Consolidated Header Id | many2one → `x_con_consolidated_hea` | Parent consolidation header of the line (deletion of the header is restricted while lines exist). | stored | `model x_con_consolidated_hea` | `server action BugFix-Stock.sa_f5_x_con_consolidated_lin_imp_con_lines_make_available_in_delete`<br>`server action BugFix-Stock.server_action_1424_imp_con_lines_make_available_in_delete`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_container_no` | Container No | char | Container number copied from the consignment. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Currency of the consignment line; has a default value. | stored | `model res.currency` (base) | `default BugFix-Stock.default_228_x_con_consolidated_lin_x_studio_currency_id`<br>`default BugFix-Stock.default_429_x_con_consolidated_lin_x_studio_currency_id`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_custom_clearance_no` | Custom Clearance No | char | Customs clearance number of the consignment. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_invoice_date` | Invoice Date | date | Supplier invoice date of the consignment. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_sequence` | Sequence | integer | Ordering number for consolidation lines (list drag handle). | stored |  | `default BugFix-Stock.default_203_x_con_consolidated_lin_x_studio_sequence`<br>`view BugFix-Stock.ported_primary_3070_tree_x_con_consolidated_lin`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_shipment_start_date` | Shipment Start Date | date | Shipment start date of the consignment. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_shipping_mode_1` | Shipping Mode | selection: Air=Air; Sea=Sea; Road=Road; Courier=Courier | Shipping mode of the consignment: Air, Sea, Road or Courier. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_status` | Status | selection: Draft=Draft; Consignment=Confirmed; In Transit=In Transit; Under Custom Clearance=Under Custom Clearance; Done=Done; TP Invoice=TP Invoice | Status of the consignment in the line: Draft, Confirmed, In Transit, Under Custom Clearance, Done or TP Invoice. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_supplier_id` | Vendor | many2one → `res.partner` | Vendor of the consignment. | stored | `model res.partner` (base) | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_supplier_invoice_no` | Supplier Invoice No | char | Supplier invoice number of the consignment. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |

**Server actions (4):**

- **Execute Code** (`server_action_1424_imp_con_lines_make_available_in_delete`, type `code`)
  - Function: Run by the Con Lines Make Available in Delete automation: un-flags the deleted consolidation line's consignment as Consolidated and, if no other lines remain on the header, resets its Lines Copied flag.
  - Depends on: `model x_con_consolidated_hea`, `model x_con_consolidated_lin`, `model x_consignment_header`, `x_con_consolidated_lin.x_studio_consignment_id`, `x_con_consolidated_lin.x_studio_consolidated_header_id`
  - Used by: `automation BugFix-Stock.automation_76_imp_con_lines_make_available_in_delete`
  <details><summary>code (11 lines)</summary>

```python

if record.id:
  con_update = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_id.id)],limit=1)
  if con_update:
    con_update.write({'x_studio_consolidated': False}) 
    
  last_line = env['x_con_consolidated_lin'].search([('x_studio_consolidated_header_id', '=', record.x_studio_consolidated_header_id.id), ('id', '!=', record.id)],limit=1)
  if not last_line:
    update_con = env['x_con_consolidated_hea'].search([('id', '=', record.x_studio_consolidated_header_id.id)],limit=1)
    if update_con:
        update_con.write({'x_studio_lines_copied': False})
```
  </details>
- **Execute Code** (`server_action_2611_jin_company_id_in_consolidated_line`, type `code`)
  - Function: Run by an automation: sets the Company of a Consolidated Line to the user's active company.
  - Depends on: `model res.company` (base), `model x_con_consolidated_lin`, `x_con_consolidated_lin.x_studio_company_id`
  - Used by: `automation BugFix-Stock.automation_283_jin_company_id_in_consolidated_line`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Con. Lines Make Available in Delete** (`sa_f5_x_con_consolidated_lin_imp_con_lines_make_available_in_delete`, type `code`)
  - Function: On a consolidation line, un-flags its consignment as Consolidated so it can be consolidated again, and if it is the last line of its header resets the header's Lines Copied flag. Intended to run when a line is deleted.
  - Depends on: `model x_con_consolidated_hea`, `model x_con_consolidated_lin`, `model x_consignment_header`, `x_con_consolidated_lin.x_studio_consignment_id`, `x_con_consolidated_lin.x_studio_consolidated_header_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (10 lines)</summary>

```python
if record.id:
  con_update = env['x_consignment_header'].search([('id', '=', record.x_studio_consignment_id.id)],limit=1)
  if con_update:
    con_update.write({'x_studio_consolidated': False}) 
    
  last_line = env['x_con_consolidated_lin'].search([('x_studio_consolidated_header_id', '=', record.x_studio_consolidated_header_id.id), ('id', '!=', record.id)],limit=1)
  if not last_line:
    update_con = env['x_con_consolidated_hea'].search([('id', '=', record.x_studio_consolidated_header_id.id)],limit=1)
    if update_con:
        update_con.write({'x_studio_lines_copied': False})
```
  </details>
- **JIN - Company Id in Consolidated Line** (`sa_f5_x_con_consolidated_lin_jin_company_id_in_consolidated_line`, type `code`)
  - Function: Sets the Company of a Consolidated Line to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_con_consolidated_lin`, `x_con_consolidated_lin.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Con. Lines Make Available in Delete | `automation_76_imp_con_lines_make_available_in_delete` |  | When a record is deleted on Con. Consolidated Line, runs _Execute Code_. | `model x_con_consolidated_lin`<br>`server action BugFix-Stock.server_action_1424_imp_con_lines_make_available_in_delete` |  |
| JIN - Company Id in Consolidated Line | `automation_283_jin_company_id_in_consolidated_line` |  | When a record is created or updated on Con. Consolidated Line, runs _Execute Code_. | `model x_con_consolidated_lin`<br>`server action BugFix-Stock.server_action_2611_jin_company_id_in_consolidated_line` |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Con. Consolidated Line | `action_1411_con_consolidated_line` | Opens **Con. Consolidated Line** records (tree,form). | `model x_con_consolidated_lin` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_con_consolidated_line` (BugFix-Studio-Misc) |
| x_con_consolidated_lin | `action_2610_x_con_consolidated_lin` | Opens **Con. Consolidated Line** records (tree,form). | `model x_con_consolidated_lin` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_x_con_consolidated_lin` (BugFix-Studio-Misc) |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_con_consolidated_lin | `ported_primary_3071_form_x_con_consolidated_lin` | form | full form layout with 5 fields | Base form of a Consolidated Line: archived ribbon, name title, two empty groups filled by the Studio customization, and chatter. | `x_con_consolidated_lin.activity_ids`<br>`x_con_consolidated_lin.message_follower_ids`<br>`x_con_consolidated_lin.message_ids`<br>`x_con_consolidated_lin.x_active`<br>`x_con_consolidated_lin.x_name` | `view BugFix-Purchase.view_x_con_consolidated_lin_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_` |
| Default list view for x_con_consolidated_lin | `ported_primary_3070_tree_x_con_consolidated_lin` | tree | full tree layout with 2 fields | Base list view of Consolidated Lines showing a drag handle (sequence) and the name. | `x_con_consolidated_lin.x_name`<br>`x_con_consolidated_lin.x_studio_sequence` | `view BugFix-Stock.ported_view_5564_odoo_studio_default_list_view_for_x_con_` |
| Default search view for x_con_consolidated_lin | `view_3072_default_search_view_for_x_con_consolidated_lin_e` | search | full search layout with 1 fields | Search view for Consolidated Lines: search by name and an Archived filter. | `x_con_consolidated_lin.x_active`<br>`x_con_consolidated_lin.x_name` |  |
| Odoo Studio: Default form view for x_con_consolidated_lin customization | `ported_view_3074_odoo_studio_default_form_view_for_x_con_` | form | set invisible=1, required= on `//field[@name='x_name']`; inside `//group[@name='studio_group_759e62_left']`: add field x_studio_supplier_id, field x_studio_currency_id, field x_studio_shipment_start_date, field x_studio_invoice_date, field x_studio_supplier_invoice_no, field x_studio_consignment_id, field x_studio_consolidated_header_id; inside `//group[@name='studio_group_759e62_right']`: add field x_studio_container_no, field x_studio_shipping_mode_1, field x_studio_custom_clearance_no, field x_studio_status | Customizes the Consolidated Line form: hides the name and shows read-only vendor, currency, dates, supplier invoice no, container, shipping mode, clearance no and status (consignment and header links hidden). | `view BugFix-Stock.ported_primary_3071_form_x_con_consolidated_lin`<br>`x_con_consolidated_lin.x_studio_consignment_id`<br>`x_con_consolidated_lin.x_studio_consolidated_header_id`<br>`x_con_consolidated_lin.x_studio_container_no`<br>`x_con_consolidated_lin.x_studio_currency_id`<details><summary>+7 more</summary>`x_con_consolidated_lin.x_studio_custom_clearance_no`<br>`x_con_consolidated_lin.x_studio_invoice_date`<br>`x_con_consolidated_lin.x_studio_shipment_start_date`<br>`x_con_consolidated_lin.x_studio_shipping_mode_1`<br>`x_con_consolidated_lin.x_studio_status`<br>`x_con_consolidated_lin.x_studio_supplier_id`<br>`x_con_consolidated_lin.x_studio_supplier_invoice_no`</details> |  |
| Odoo Studio: Default list view for x_con_consolidated_lin customization | `ported_view_5564_odoo_studio_default_list_view_for_x_con_` | tree | after `//field[@name='x_name']`: add field x_studio_company_id | Adds a hidden Company column after the name in the Consolidated Lines list. | `view BugFix-Stock.ported_primary_3070_tree_x_con_consolidated_lin`<br>`x_con_consolidated_lin.x_studio_company_id` |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Con. Consolidated Line group_system | `access_1380_con__consolidated_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Con. Consolidated Line records. | `group base.group_system` (base)<br>`model x_con_consolidated_lin` |  |
| Con. Consolidated Line group_system | `access_1380_con_consolidated_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Con. Consolidated Line records. | `group base.group_system` (base)<br>`model x_con_consolidated_lin` |  |
| Con. Consolidated Line group_user | `access_1381_con__consolidated_line_group_user` | Gives **User types / Internal User** read access to Con. Consolidated Line records. | `group base.group_user` (base)<br>`model x_con_consolidated_lin` |  |
| Con. Consolidated Line group_user | `access_1381_con_consolidated_line_group_user` | Gives **User types / Internal User** read access to Con. Consolidated Line records. | `group base.group_user` (base)<br>`model x_con_consolidated_lin` |  |
| x_con_consolidated_lin user access | `access_x_con_consolidated_lin_user` | Gives **User types / Internal User** read/write/create/delete access to Con. Consolidated Line records. | `group base.group_user` (base)<br>`model x_con_consolidated_lin` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consolidated Line | `rule_515_jin_multi_company_consolidated_line` | For everyone (global rule): read/write/create/delete on Con. Consolidated Line only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_con_consolidated_lin`<br>`x_con_consolidated_lin.x_studio_company_id` |  |
