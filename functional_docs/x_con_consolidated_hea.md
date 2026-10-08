# BugFix-Stock — `x_con_consolidated_hea`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_con_consolidated_hea` — Con. Consolidated Header

*Created by this repo.* Python: `models/x_con_consolidated_hea.py`, `models/x_con_consolidated_hea_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_con_consolidated_hea_x_con_consolidated_hea_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)<br>`server action BugFix-Purchase.server_action_2375_reverse_pr_status_in_po_2` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_con_consolidated_hea -->
A Consolidated Header groups several import consignments into one consolidation, with a generated reference, description, company and a Draft or Confirmed status. From its form users copy eligible consignments in through a selection wizard, clear them, or confirm the consolidation, which marks every included consignment as consolidation confirmed. Automations number new records, set the company and block deleting a consolidation that is not in Draft.
<!-- /SUMMARY -->

**Fields (39):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`<br>`x_con_consolidated_hea.activity_summary`<br>`x_con_consolidated_hea.activity_type_icon`<br>`x_con_consolidated_hea.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_con_consolidated_hea.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_con_consolidated_hea.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_con_consolidated_hea.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for consolidation headers; defaults to active, inactive records show an Archived ribbon. | stored |  | `default BugFix-Stock.default_200_x_con_consolidated_hea_x_active`<br>`view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`<br>`view BugFix-Stock.view_3069_default_search_view_for_x_con_consolidated_hea_e` |
| `x_name` | Con. Reference | char | Consolidation reference number, generated by the 'Con. Consolidated Seq. No' action when the record is created. | stored |  | `default BugFix-Stock.default_204_x_con_consolidated_hea_x_name`<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_hea_con_consolidated_seq_no`<br>`server action BugFix-Stock.server_action_1412_con_consolidated_seq_no`<br>`view BugFix-Stock.ported_primary_3067_tree_x_con_consolidated_hea`<br>`view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`<details><summary>+1 more</summary>`view BugFix-Stock.view_3069_default_search_view_for_x_con_consolidated_hea_e`</details> |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the consolidation header; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_514_jin_multi_company_consolidated_header`<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_hea_jin_company_id_in_consolidated_header`<br>`server action BugFix-Stock.server_action_2609_jin_company_id_in_consolidated_header`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_con_line_ids` | Con. Line Ids | one2many → `x_con_consolidated_lin` | Consolidated lines (consignments) grouped under this header; used by the Confirm Consolidation action. | stored | `model x_con_consolidated_lin` | `server action BugFix-Stock.server_action_1421_imp_confirm_consolidation`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_description` | Description | char | Free-text description of the consolidation, shown in its form and list. | stored |  | `view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3075_odoo_studio_default_list_view_for_x_con_` |
| `x_studio_lines_copied` | Lines Copied | boolean | Flag showing consignment lines have been copied into the consolidation; reset by the 'Clear Consignment Lines' action and used for button visibility. | stored |  | `server action BugFix-Stock.server_action_1414_imp_clear_consignment_lines_from_consolidation`<br>`view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_pipeline_status_bar` | Pipeline Status Bar | selection: Draft=Draft; Confirmed=Confirmed | Status bar value (Draft/Confirmed) of the consolidation; defaults to Draft and set to Confirmed by the Confirm Consolidation action. | stored |  | `default BugFix-Stock.default_205_x_con_consolidated_hea_x_studio_pipeline_status_bar`<br>`server action BugFix-Stock.server_action_1421_imp_confirm_consolidation`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_` |
| `x_studio_sequence` | Sequence | integer | Ordering number for consolidation headers (list drag handle). | stored |  | `default BugFix-Stock.default_201_x_con_consolidated_hea_x_studio_sequence`<br>`view BugFix-Stock.ported_primary_3067_tree_x_con_consolidated_hea` |
| `x_studio_status` | Status | selection: Draft=Draft; Confirmed=Confirmed | Consolidation status: Draft or Confirmed. Defaults to Draft; checked when copying lines and deleting, set by the Confirm Consolidation action. | stored |  | `default BugFix-Stock.default_206_x_con_consolidated_hea_x_studio_status`<br>`server action BugFix-Stock.sa_f5_x_con_consolidated_hea_imp_restrict_delete_in_consolidation`<br>`server action BugFix-Stock.server_action_1413_imp_copy_consignment_lines_to_consolidation`<br>`server action BugFix-Stock.server_action_1421_imp_confirm_consolidation`<br>`server action BugFix-Stock.server_action_1423_imp_restrict_delete_in_consolidation`<details><summary>+3 more</summary>`view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_`<br>`view BugFix-Stock.ported_view_3075_odoo_studio_default_list_view_for_x_con_`</details> |

**Server actions (9):**

- **Con. Consolidated Seq.No** (`sa_f5_x_con_consolidated_hea_con_consolidated_seq_no`, type `code`)
  - Function: When a Consolidated Header still has the name 'New', assigns it the next number from the 'con.consolidated.seq' sequence.
  - Depends on: `model ir.sequence` (base), `model x_con_consolidated_hea`, `x_con_consolidated_hea.x_name`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (5 lines)</summary>

```python
#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('con.consolidated.seq')
 record.write({'x_name': seq})
```
  </details>
- **Execute Code** (`server_action_1412_con_consolidated_seq_no`, type `code`)
  - Function: Run by the Consignment Consolidated Seq No automation: when a Consolidated Header is named 'New', assigns the next 'con.consolidated.seq' number.
  - Depends on: `model ir.sequence` (base), `model x_con_consolidated_hea`, `x_con_consolidated_hea.x_name`
  - Used by: `automation BugFix-Stock.automation_74_jin_consignment_consolidated_seq_no`
  <details><summary>code (6 lines)</summary>

```python

#record['x_name'] = env['ir.sequence'].next_by_code('purchase.request.seq')

if record.x_name == 'New':
 seq = env['ir.sequence'].next_by_code('con.consolidated.seq')
 record.write({'x_name': seq})
```
  </details>
- **Execute Code** (`server_action_1423_imp_restrict_delete_in_consolidation`, type `code`)
  - Function: Run by the Restrict Delete in Consolidation automation: blocks deleting a consolidation that is not in Draft status.
  - Depends on: `model x_con_consolidated_hea`, `x_con_consolidated_hea.x_studio_status`
  - Used by: `automation BugFix-Stock.automation_75_imp_restrict_delete_in_consolidation`
  <details><summary>code (3 lines)</summary>

```python

if record.x_studio_status != 'Draft':
  raise UserError("Only the consolidations in Draft status can be deleted.")
```
  </details>
- **Execute Code** (`server_action_2609_jin_company_id_in_consolidated_header`, type `code`)
  - Function: Run by an automation: sets the Company of a Consolidated Header to the user's active company.
  - Depends on: `model res.company` (base), `model x_con_consolidated_hea`, `x_con_consolidated_hea.x_studio_company_id`
  - Used by: `automation BugFix-Stock.automation_282_jin_company_id_in_consolidated_header`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **IMP - Clear Consignment Lines from Consolidation** (`server_action_1414_imp_clear_consignment_lines_from_consolidation`, type `code`)
  - Function: Button on the consolidation form: deletes all consolidation lines, un-flags their consignments as Consolidated and resets the header's Lines Copied flag.
  - Depends on: `model x_con_consolidated_hea`, `model x_con_consolidated_lin`, `model x_consignment_header`, `x_con_consolidated_hea.x_studio_lines_copied`
  - Used by: `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`
  <details><summary>code (11 lines)</summary>

```python
if record.id:
  temp_rec = env['x_con_consolidated_lin'].search([('x_studio_consolidated_header_id', '=', record.id)])
  if temp_rec:
    for del_temp_rec in temp_rec:
      con_update = env['x_consignment_header'].search([('id', '=', del_temp_rec.x_studio_consignment_id.id)],limit=1)
      if con_update:
        con_update.write({'x_studio_consolidated': False}) 
      
      del_temp_rec.unlink()   

    record['x_studio_lines_copied'] = False
```
  </details>
- **IMP - Confirm Consolidation** (`server_action_1421_imp_confirm_consolidation`, type `code`)
  - Function: Confirm button on the consolidation form: marks every included consignment as Consolidation Confirmed and sets the consolidation status and pipeline bar to Confirmed.
  - Depends on: `model x_con_consolidated_hea`, `model x_con_consolidated_lin`, `model x_consignment_header`, `x_con_consolidated_hea.x_studio_con_line_ids`, `x_con_consolidated_hea.x_studio_pipeline_status_bar`<details><summary>+1 more</summary>`x_con_consolidated_hea.x_studio_status`</details>
  - Used by: `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`
  <details><summary>code (17 lines)</summary>

```python
if record.id:
  for val in record.x_studio_con_line_ids:
    con_lines = env['x_consignment_header'].search([('id', '=', val.x_studio_consignment_id.id)],limit=1)
    if con_lines:
      con_lines.write({'x_studio_consolidation_confirmed': True})

  record['x_studio_status'] = 'Confirmed'
  record['x_studio_pipeline_status_bar'] = 'Confirmed'

"""c = 0
  con_lines = env['x_con_consolidated_lin'].search([('x_studio_consolidated_header_id', '=', record.id)])
  if con_lines:
    for val in con_lines:
      c += 1

  if c < 2:
    raise UserError("Atleast One PI Should be Consolidated.")"""
```
  </details>
- **IMP - Copy Consignment Lines to Consolidation** (`server_action_1413_imp_copy_consignment_lines_to_consolidation`, type `code`)
  - Function: Button on the consolidation form: opens the Copy PIs wizard (`x_temp_con_consolidate`) pre-filled with all non-draft consignments not yet consolidated, so the user can pick which to consolidate.
  - Depends on: `model x_con_consolidated_hea`, `model x_consignment_header`, `x_con_consolidated_hea.x_studio_status`
  - Used by: `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`
  <details><summary>code (30 lines)</summary>

```python
if record.id:
  con_lines=[]
  
  con_header = env['x_consignment_header'].search([('x_studio_status', '!=', 'Draft'), ('x_studio_consolidated', '=', False)])
  if con_header:
    for validate_lines in con_header:
      con_lines.append([0,0,{
        'x_studio_consignment_id':validate_lines.id,
        'x_studio_container_no':validate_lines.x_studio_container_no,
        'x_studio_currency_id':validate_lines.x_studio_currency_id.id,
        'x_studio_custom_clearance_no':validate_lines.x_studio_custom_clearance_no,
        'x_studio_delivery_term':validate_lines.x_studio_delivery_term.id,
        'x_studio_invoice_date':validate_lines.x_studio_invoice_date,
        'x_studio_shipment_start_date':validate_lines.x_studio_shipment_start_date,
        'x_studio_shipping_mode':validate_lines.x_studio_shipping_mode,
        'x_studio_supplier_invoice_no':validate_lines.x_studio_supplier_invoice_number,
        'x_studio_supplier_id':validate_lines.x_studio_supplier_id.id,
        'x_studio_status':validate_lines.x_studio_status}])

  ctx = env.context
  ctx.update({'default_x_studio_consolidated_header_id':record.id,'default_x_studio_con_lines':con_lines})
  action = {
            'name': 'Copy PIs',
            'type': 'ir.actions.act_window',
            'res_model': 'x_temp_con_consolidate',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': ctx,
            }
```
  </details>
- **IMP - Restrict Delete in Consolidation** (`sa_f5_x_con_consolidated_hea_imp_restrict_delete_in_consolidation`, type `code`)
  - Function: Blocks deletion of a Consolidated Header unless its status is Draft, raising an error otherwise.
  - Depends on: `model x_con_consolidated_hea`, `x_con_consolidated_hea.x_studio_status`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_status != 'Draft':
  raise UserError("Only the consolidations in Draft status can be deleted.")
```
  </details>
- **JIN - Company Id in Consolidated Header** (`sa_f5_x_con_consolidated_hea_jin_company_id_in_consolidated_header`, type `code`)
  - Function: Sets the Company of a Consolidated Header to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_con_consolidated_hea`, `x_con_consolidated_hea.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (3):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| IMP - Restrict Delete in Consolidation | `automation_75_imp_restrict_delete_in_consolidation` |  | When a record is deleted on Con. Consolidated Header, runs _Execute Code_. | `model x_con_consolidated_hea`<br>`server action BugFix-Stock.server_action_1423_imp_restrict_delete_in_consolidation` |  |
| JIN - Company Id in Consolidated Header | `automation_282_jin_company_id_in_consolidated_header` |  | When a record is created or updated on Con. Consolidated Header, runs _Execute Code_. | `model x_con_consolidated_hea`<br>`server action BugFix-Stock.server_action_2609_jin_company_id_in_consolidated_header` |  |
| JIN-Consignment Consolidated Seq.No | `automation_74_jin_consignment_consolidated_seq_no` |  | When a record is created or updated on Con. Consolidated Header, runs _Execute Code_. | `model x_con_consolidated_hea`<br>`server action BugFix-Stock.server_action_1412_con_consolidated_seq_no` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Con. Consolidated Header | `action_1410_con_consolidated_header` | Opens **Con. Consolidated Header** records (tree,form). | `model x_con_consolidated_hea` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_consolidated_consignments` (BugFix-Studio-Misc) |
| Consolidated Consignments | `action_2054_consolidated_consignments` | Opens **Con. Consolidated Header** records (tree,form). | `model x_con_consolidated_hea` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_consolidated_consignments` (BugFix-Studio-Misc) |
| Consolidated Consignments | `action_2888_consolidated_consignments` | Opens **Con. Consolidated Header** records (tree,form). | `model x_con_consolidated_hea` |  |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_con_consolidated_hea | `ported_primary_3068_form_x_con_consolidated_hea` | form | full form layout with 7 fields | Consolidated Header form with Copy PI Header, Clear PI Header and Confirm buttons driven by status and Lines Copied, an archived ribbon, 'Con. Reference' title and chatter. Buttons use hardcoded action ids (1966, 1969, 1976). | `server action BugFix-Stock.server_action_1413_imp_copy_consignment_lines_to_consolidation`<br>`server action BugFix-Stock.server_action_1414_imp_clear_consignment_lines_from_consolidation`<br>`server action BugFix-Stock.server_action_1421_imp_confirm_consolidation`<br>`x_con_consolidated_hea.activity_ids`<br>`x_con_consolidated_hea.message_follower_ids`<details><summary>+5 more</summary>`x_con_consolidated_hea.message_ids`<br>`x_con_consolidated_hea.x_active`<br>`x_con_consolidated_hea.x_name`<br>`x_con_consolidated_hea.x_studio_lines_copied`<br>`x_con_consolidated_hea.x_studio_status`</details> | `view BugFix-Purchase.view_x_con_consolidated_hea_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_` |
| Default list view for x_con_consolidated_hea | `ported_primary_3067_tree_x_con_consolidated_hea` | tree | full tree layout with 2 fields | Base list view of Consolidated Headers showing a drag handle (sequence) and the name. | `x_con_consolidated_hea.x_name`<br>`x_con_consolidated_hea.x_studio_sequence` | `view BugFix-Stock.ported_view_3075_odoo_studio_default_list_view_for_x_con_` |
| Default search view for x_con_consolidated_hea | `view_3069_default_search_view_for_x_con_consolidated_hea_e` | search | full search layout with 1 fields | Search view for Consolidated Headers: search by name and an Archived filter. | `x_con_consolidated_hea.x_active`<br>`x_con_consolidated_hea.x_name` |  |
| Odoo Studio: Default form view for x_con_consolidated_hea customization | `ported_view_3073_odoo_studio_default_form_view_for_x_con_` | form | after `//button[@name='1966']`: add field x_studio_pipeline_status_bar; set force_save=True, readonly=1 on `//form[1]/sheet[1]/div[1]/h1[1]/field[@name='x_name']`; inside `//group[@name='studio_group_bc4ef6_left']`: add field x_studio_description; inside `//group[@name='studio_group_bc4ef6_right']`: add field create_uid, field create_date, field x_studio_status, field x_studio_company_id, field x_studio_lines_copied; after `//group[@name='studio_group_bc4ef6']`: add notebook | Customizes the Consolidated Header form: pipeline status bar, read-only reference, description (locked once Confirmed), creator/date/status, and a Lines tab listing the consolidated consignments (read-only once not Draft). | `view BugFix-Stock.ported_primary_3068_form_x_con_consolidated_hea`<br>`x_con_consolidated_hea.x_studio_company_id`<br>`x_con_consolidated_hea.x_studio_con_line_ids`<br>`x_con_consolidated_hea.x_studio_description`<br>`x_con_consolidated_hea.x_studio_lines_copied`<details><summary>+14 more</summary>`x_con_consolidated_hea.x_studio_pipeline_status_bar`<br>`x_con_consolidated_hea.x_studio_status`<br>`x_con_consolidated_lin.x_name`<br>`x_con_consolidated_lin.x_studio_consignment_id`<br>`x_con_consolidated_lin.x_studio_container_no`<br>`x_con_consolidated_lin.x_studio_currency_id`<br>`x_con_consolidated_lin.x_studio_custom_clearance_no`<br>`x_con_consolidated_lin.x_studio_invoice_date`<br>`x_con_consolidated_lin.x_studio_sequence`<br>`x_con_consolidated_lin.x_studio_shipment_start_date`<br>`x_con_consolidated_lin.x_studio_shipping_mode_1`<br>`x_con_consolidated_lin.x_studio_status`<br>`x_con_consolidated_lin.x_studio_supplier_id`<br>`x_con_consolidated_lin.x_studio_supplier_invoice_no`</details> |  |
| Odoo Studio: Default list view for x_con_consolidated_hea customization | `ported_view_3075_odoo_studio_default_list_view_for_x_con_` | tree | set default_order=x_name desc on `//tree[1]`; before `//field[@name='x_studio_sequence']`: add xpath, field x_studio_description, field create_uid, field create_date, field x_studio_status; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set string=Con. Reference on `//field[@name='x_name']` | Customizes the Consolidated Header list: sorted by reference descending, reference labelled 'Con. Reference' first, plus description, creator, created on and a status badge (Draft muted, Confirmed green); hides the sequence handle. | `view BugFix-Stock.ported_primary_3067_tree_x_con_consolidated_hea`<br>`x_con_consolidated_hea.x_studio_description`<br>`x_con_consolidated_hea.x_studio_status` |  |

**Access rights (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Con. Consolidated Header group_system | `access_1378_con__consolidated_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Con. Consolidated Header records. | `group base.group_system` (base)<br>`model x_con_consolidated_hea` |  |
| Con. Consolidated Header group_system | `access_1378_con_consolidated_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Con. Consolidated Header records. | `group base.group_system` (base)<br>`model x_con_consolidated_hea` |  |
| Con. Consolidated Header group_user | `access_1379_con__consolidated_header_group_user` | Gives **User types / Internal User** read access to Con. Consolidated Header records. | `group base.group_user` (base)<br>`model x_con_consolidated_hea` |  |
| Con. Consolidated Header group_user | `access_1379_con_consolidated_header_group_user` | Gives **User types / Internal User** read access to Con. Consolidated Header records. | `group base.group_user` (base)<br>`model x_con_consolidated_hea` |  |
| x_con_consolidated_hea user access | `access_x_con_consolidated_hea_user` | Gives **User types / Internal User** read/write/create/delete access to Con. Consolidated Header records. | `group base.group_user` (base)<br>`model x_con_consolidated_hea` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consolidated Header | `rule_514_jin_multi_company_consolidated_header` | For everyone (global rule): read/write/create/delete on Con. Consolidated Header only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_con_consolidated_hea`<br>`x_con_consolidated_hea.x_studio_company_id` |  |
