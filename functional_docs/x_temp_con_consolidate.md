# BugFix-Stock — `x_temp_con_consolidate`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_con_consolidate` — Temp Con. Consolidated Header

*Created by this repo.* Python: `models/x_temp_con_consolidate.py`, `models/x_temp_con_consolidate_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_temp_con_consolidate_x_temp_con_consolidate_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_con_consolidate -->
The temporary wizard record behind Copy PI Lines to Consolidation, opened from a Consolidated Header. It lists candidate consignments with Select All and Clear All buttons, and its Apply action copies the selected consignments into the consolidation and marks them consolidated.
<!-- /SUMMARY -->

**Fields (36):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_temp_con_consolidate.activity_summary`<br>`x_temp_con_consolidate.activity_type_icon`<br>`x_temp_con_consolidate.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_con_consolidate.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_con_consolidate.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_con_consolidate.activity_ids` |  |
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
| `x_active` | Active | boolean | Archive flag; defaults to active. | stored |  | `default BugFix-Stock.default_final_bugfix_stock_field_x_temp_con_consolidate_x_active_true` |
| `x_name` | Name | char | Name of the temporary consolidation wizard record. | stored |  | `view BugFix-Stock.view_3085_imp_copy_pi_line_to_consolidation_e` |
| `x_studio_con_lines` | Con. Lines | one2many → `x_temp_con_conso_line` | Candidate consignments listed in the consolidation wizard; ticked ones are applied to the consolidation. | stored | `model x_temp_con_conso_line` | `server action BugFix-Stock.server_action_1420_imp_apply_selected_pi_lines_to_consolidation`<br>`view BugFix-Stock.view_3085_imp_copy_pi_line_to_consolidation_e` |
| `x_studio_consolidated_header_id` | Consolidated Header Id | many2one → `x_con_consolidated_hea` | Consolidation that selected consignments will be added to by the wizard's select/clear/apply actions. | stored | `model x_con_consolidated_hea` | `server action BugFix-Stock.server_action_1417_imp_select_all_in_copy_pi_lines`<br>`server action BugFix-Stock.server_action_1419_imp_clear_all_in_copy_po_lines`<br>`server action BugFix-Stock.server_action_1420_imp_apply_selected_pi_lines_to_consolidation`<br>`view BugFix-Stock.view_3085_imp_copy_pi_line_to_consolidation_e` |
| `x_studio_select_all` | Select All | boolean | Select-all checkbox shown in the Copy PI Lines to Consolidation wizard. | stored |  | `view BugFix-Stock.view_3085_imp_copy_pi_line_to_consolidation_e` |
| `x_studio_sequence` | Sequence | integer | Ordering number with a default value. | stored |  | `default BugFix-Stock.default_208_x_temp_con_consolidate_x_studio_sequence` |

**Server actions (3):**

- **IMP - Apply Selected PI Lines to Consolidation** (`server_action_1420_imp_apply_selected_pi_lines_to_consolidation`, type `code`)
  - Function: Copies the selected lines of the temporary consolidation wizard into Consolidated lines, marks those consignments Consolidated and the header Lines Copied, errors if none selected, then deletes the wizard record.
  - Depends on: `model x_con_consolidated_hea`, `model x_con_consolidated_lin`, `model x_consignment_header`, `model x_temp_con_consolidate`, `x_temp_con_consolidate.x_studio_con_lines`<details><summary>+1 more</summary>`x_temp_con_consolidate.x_studio_consolidated_header_id`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (63 lines)</summary>

```python
select = 0

for valid_line in record.x_studio_con_lines:

  if (valid_line.x_studio_select == True):

    select += 1

    

    create_con_lines = env['x_con_consolidated_lin'].create({'x_studio_consolidated_header_id':record.x_studio_consolidated_header_id.id,

      'x_studio_consignment_id':valid_line.x_studio_consignment_id.id,

      'x_studio_container_no':valid_line.x_studio_container_no,

      'x_studio_currency_id':valid_line.x_studio_currency_id.id,

      'x_studio_custom_clearance_no':valid_line.x_studio_custom_clearance_no,

      'x_studio_delivery_term':valid_line.x_studio_delivery_term.id,

      'x_studio_invoice_date':valid_line.x_studio_invoice_date,

      'x_studio_shipment_start_date':valid_line.x_studio_shipment_start_date,

      'x_studio_shipping_mode_1':valid_line.x_studio_shipping_mode,

      'x_studio_supplier_invoice_no':valid_line.x_studio_supplier_invoice_no,

      'x_studio_supplier_id':valid_line.x_studio_supplier_id.id,

      'x_studio_status':valid_line.x_studio_status})

      

    con_update = env['x_consignment_header'].search([('id', '=', valid_line.x_studio_consignment_id.id)],limit=1)

    if con_update:

      con_update.write({'x_studio_consolidated': True}) 

      

if select == 0:

 raise UserError("Atleast One Line Should be Selected to Proceed.")

 

header_update = env['x_con_consolidated_hea'].search([('id', '=', record.x_studio_consolidated_header_id.id)],limit=1)

if header_update:

  header_update.write({'x_studio_lines_copied': True}) 



temp_rec = env['x_temp_con_consolidate'].search([('id', '=', record.id)],limit=1)

if temp_rec:

  temp_rec.unlink()
```
  </details>
- **IMP - Clear All in Copy PO Lines** (`server_action_1419_imp_clear_all_in_copy_po_lines`, type `code`)
  - Function: Reopens the Copy PIs consolidation wizard with all consignment lines unselected (Select All off).
  - Depends on: `model x_temp_con_conso_line`, `model x_temp_con_consolidate`, `x_temp_con_consolidate.x_studio_consolidated_header_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (61 lines)</summary>

```python
if record.id:

  pi_lines=[]

  con_lines = env['x_temp_con_conso_line'].search([('x_studio_temp_consolidated_header_id', '=', record.id)])

  if con_lines:

    for update_lines in con_lines:

      pi_lines.append([0,0,{

        'x_studio_select':False,

        'x_studio_consignment_id':update_lines.x_studio_consignment_id.id,

        'x_studio_container_no':update_lines.x_studio_container_no,

        'x_studio_currency_id':update_lines.x_studio_currency_id.id,

        'x_studio_custom_clearance_no':update_lines.x_studio_custom_clearance_no,

        'x_studio_delivery_term':update_lines.x_studio_delivery_term.id,

        'x_studio_invoice_date':update_lines.x_studio_invoice_date,

        'x_studio_shipment_start_date':update_lines.x_studio_shipment_start_date,

        'x_studio_shipping_mode':update_lines.x_studio_shipping_mode,

        'x_studio_supplier_invoice_no':update_lines.x_studio_supplier_invoice_no,

        'x_studio_supplier_id':update_lines.x_studio_supplier_id.id,

        'x_studio_status':update_lines.x_studio_status}])

        

  ctx = env.context

  ctx.update({'default_x_studio_consolidated_header_id':record.x_studio_consolidated_header_id.id,'default_x_studio_select_all':False,'default_x_studio_con_lines':pi_lines})

  action = {

            'name': 'Copy PIs',

            'type': 'ir.actions.act_window',

            'res_model': 'x_temp_con_consolidate',

            'view_mode': 'form',

            'view_type': 'form',

            'target': 'new',

#            'res_id': record.id,

            'context': ctx,

            }
```
  </details>
- **IMP - Select All in Copy PI Lines** (`server_action_1417_imp_select_all_in_copy_pi_lines`, type `code`)
  - Function: Reopens the Copy PIs consolidation wizard with all consignment lines selected (Select All on).
  - Depends on: `model x_temp_con_conso_line`, `model x_temp_con_consolidate`, `x_temp_con_consolidate.x_studio_consolidated_header_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (61 lines)</summary>

```python
if record.id:

  pi_lines=[]

  con_lines = env['x_temp_con_conso_line'].search([('x_studio_temp_consolidated_header_id', '=', record.id)])

  if con_lines:

    for update_lines in con_lines:

      pi_lines.append([0,0,{

        'x_studio_select':True,

        'x_studio_consignment_id':update_lines.x_studio_consignment_id.id,

        'x_studio_container_no':update_lines.x_studio_container_no,

        'x_studio_currency_id':update_lines.x_studio_currency_id.id,

        'x_studio_custom_clearance_no':update_lines.x_studio_custom_clearance_no,

        'x_studio_delivery_term':update_lines.x_studio_delivery_term.id,

        'x_studio_invoice_date':update_lines.x_studio_invoice_date,

        'x_studio_shipment_start_date':update_lines.x_studio_shipment_start_date,

        'x_studio_shipping_mode':update_lines.x_studio_shipping_mode,

        'x_studio_supplier_invoice_no':update_lines.x_studio_supplier_invoice_no,

        'x_studio_supplier_id':update_lines.x_studio_supplier_id.id,

        'x_studio_status':update_lines.x_studio_status}])

        

  ctx = env.context

  ctx.update({'default_x_studio_consolidated_header_id':record.x_studio_consolidated_header_id.id,'default_x_studio_select_all':True,'default_x_studio_con_lines':pi_lines})

  action = {

            'name': 'Copy PIs',

            'type': 'ir.actions.act_window',

            'res_model': 'x_temp_con_consolidate',

            'view_mode': 'form',

            'view_type': 'form',

            'target': 'new',

#            'res_id': record.id,

            'context': ctx,

            }
```
  </details>
**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| IMP Copy PI Line to Consolidation | `view_3085_imp_copy_pi_line_to_consolidation_e` | form | full form layout with 4 fields | 'Copy Purchase Invoice Lines' wizard: Select All / Clear All and Apply buttons over a list of consignment lines. All list columns were stripped by the porter (checked against the wrong model), so the list shows no columns. | `client action stock_barcode_mrp.stock_barcode_mo_client_action` (stock_barcode_mrp)<br>`window action sale.product_template_action` (sale)<br>`window action stock_barcode_mrp.mrp_action_kanban` (stock_barcode_mrp)<br>`x_temp_con_consolidate.x_name`<br>`x_temp_con_consolidate.x_studio_con_lines`<details><summary>+2 more</summary>`x_temp_con_consolidate.x_studio_consolidated_header_id`<br>`x_temp_con_consolidate.x_studio_select_all`</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp Con. Consolidated Header group_system | `access_1382_temp_con__consolidated_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp Con. Consolidated Header records. | `group base.group_system` (base)<br>`model x_temp_con_consolidate` |  |
| Temp Con. Consolidated Header group_user | `access_1383_temp_con__consolidated_header_group_user` | Gives **User types / Internal User** read access to Temp Con. Consolidated Header records. | `group base.group_user` (base)<br>`model x_temp_con_consolidate` |  |
