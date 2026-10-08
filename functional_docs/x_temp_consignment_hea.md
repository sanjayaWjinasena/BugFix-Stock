# BugFix-Stock — `x_temp_consignment_hea`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_consignment_hea` — Temp Consignment Header

*Created by this repo.* Python: `models/x_temp_consignment_hea.py`, `models/x_temp_consignment_hea_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_temp_consignment_hea_x_temp_consignment_hea_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_temp_consignment_hea -->
The temporary wizard record behind Copy Import Order Lines, opened from a consignment. It lists candidate import PO lines with Select All and Clear All buttons, and its Apply action creates consignment lines from the ticked PO lines.
<!-- /SUMMARY -->

**Fields (36):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_temp_consignment_hea.activity_summary`<br>`x_temp_consignment_hea.activity_type_icon`<br>`x_temp_consignment_hea.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_consignment_hea.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_consignment_hea.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_consignment_hea.activity_ids` |  |
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
| `x_active` | Active | boolean | Archive flag for the temporary 'Copy PO Lines' wizard header; has a default. | stored |  | `default BugFix-Stock.default_148_x_temp_consignment_hea_x_active` |
| `x_name` | Name | char | Name of the temporary Copy PO Lines record. | stored |  | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_select_all` | Select All | boolean | Checkbox in the Copy PO Lines wizard; used by the Select All / Clear All actions to tick or untick every PO line. | stored |  | `server action BugFix-Stock.server_action_1298_imp_select_all_in_copy_po_lines`<br>`server action BugFix-Stock.server_action_1301_imp_clear_all_in_copy_po_lines`<br>`view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_sequence` | Sequence | integer | Ordering number with a default; not shown in any view. | stored |  | `default BugFix-Stock.default_149_x_temp_consignment_hea_x_studio_sequence` |
| `x_studio_temp_consignment_header_id` | Temp Consignment Header Id | many2one → `x_consignment_header` | Consignment the selected PO lines will be copied into by the 'Apply Selected PO Lines' action. | stored | `model x_consignment_header` | `server action BugFix-Stock.server_action_1302_imp_apply_selected_po_lines_to_consignment`<br>`view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |
| `x_studio_temp_consignment_line_ids` | Temp Consignment Line Ids | one2many → `x_temp_consignment_lin` | Candidate PO lines listed in the Copy PO Lines wizard for selection. | stored | `model x_temp_consignment_lin` | `server action BugFix-Stock.server_action_1298_imp_select_all_in_copy_po_lines`<br>`server action BugFix-Stock.server_action_1301_imp_clear_all_in_copy_po_lines`<br>`server action BugFix-Stock.server_action_1302_imp_apply_selected_po_lines_to_consignment`<br>`view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |

**Server actions (3):**

- **IMP - Apply Selected PO Lines to Consignment** (`server_action_1302_imp_apply_selected_po_lines_to_consignment`, type `code`)
  - Function: Button on the Copy PO Lines wizard: creates consignment lines from the selected PO lines (requires at least one, all with the same structure, and LC posted/paid for LC payment methods), marks the consignment Lines Copied with that structure, then deletes the wizard record.
  - Depends on: `model x_consignment_header`, `model x_consignment_line`, `model x_lc_header` (BugFix-Accounting), `model x_temp_consignment_hea`, `x_temp_consignment_hea.x_studio_temp_consignment_header_id`<details><summary>+1 more</summary>`x_temp_consignment_hea.x_studio_temp_consignment_line_ids`</details>
  - Used by: `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea`
  <details><summary>code (61 lines)</summary>

```python
select = 0



for valid_line in record.x_studio_temp_consignment_line_ids:

  if (valid_line.x_studio_select == True):

    select += 1

    

    if select == 1:

      structure = valid_line.x_studio_structure_name.id

    if select > 1:

      if valid_line.x_studio_structure_name.id != structure:

          raise UserError("PO Lines with Same Structure Should be Selected!")

    

    if valid_line.x_studio_payment_method.x_studio_lc == True:

      search_lc = env['x_lc_header'].search([('x_studio_created_from_purchase_order', '=', valid_line.x_studio_purchase_id.id), ('x_studio_status', '=', ('Posted','Paid'))],limit=1)

      if not search_lc:

        raise UserError('The LC of all the Selected PO Line/ Lines Should be in Posted or Paid State.')

    

    create_con_lines = env['x_consignment_line'].create({'x_studio_consignment_header_id':record.x_studio_temp_consignment_header_id.id,'x_studio_purchase_id':valid_line.x_studio_purchase_id.id,'x_studio_product_id':valid_line.x_studio_product_id.id,'x_studio_description':valid_line.x_studio_description,'x_studio_payment_method':valid_line.x_studio_payment_method.id,

      'x_studio_tariff_code':valid_line.x_studio_product_id.x_studio_tariff_code.id,'x_studio_unit_price':valid_line.x_studio_unit_price,'x_currency_id':valid_line.x_currency_id.id,'x_studio_delivery_remainder':valid_line.x_studio_delivery_remainder,'x_studio_original_delivery_remainder':valid_line.x_studio_delivery_remainder,'x_studio_purchase_line_id':valid_line.x_studio_purchase_line_id.id,'x_studio_concessional_rate':valid_line.x_studio_concessional_rate,

      'x_studio_volume':valid_line.x_studio_volume,'x_studio_weight':valid_line.x_studio_weight})

      

if select == 0:

 raise UserError("Atleast One Line Should be Selected to Proceed.")

 

header_update = env['x_consignment_header'].search([('id', '=', record.x_studio_temp_consignment_header_id.id)],limit=1)

if header_update:

  header_update.write({'x_studio_lines_copied': True, 'x_studio_structure_name': structure}) 



temp_rec = env['x_temp_consignment_hea'].search([('id', '=', record.id)],limit=1)

if temp_rec:

  temp_rec.unlink()
```
  </details>
- **IMP - Clear All in Copy PO Lines** (`server_action_1301_imp_clear_all_in_copy_po_lines`, type `code`)
  - Function: Clear All button on the Copy PO Lines wizard: unticks Select on every wizard line and Select All, then reopens the same wizard popup.
  - Depends on: `model x_temp_consignment_hea`, `x_temp_consignment_hea.x_studio_select_all`, `x_temp_consignment_hea.x_studio_temp_consignment_line_ids`
  - Used by: `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea`
  <details><summary>code (15 lines)</summary>

```python
# PATCHED IN-PLACE (Clear All): toggle x_studio_select=False on
# every existing line and REOPEN the same wizard record so the popup
# stays visible with the updated checkboxes.
if record.id:
  record.x_studio_temp_consignment_line_ids.write({'x_studio_select': False})
  record.write({'x_studio_select_all': False})
  action = {
    'name': 'Copy PO Lines',
    'type': 'ir.actions.act_window',
    'res_model': 'x_temp_consignment_hea',
    'view_mode': 'form',
    'res_id': record.id,
    'target': 'new',
    'context': env.context,
  }
```
  </details>
- **IMP - Select All in Copy PO Lines** (`server_action_1298_imp_select_all_in_copy_po_lines`, type `code`)
  - Function: Select All button on the Copy PO Lines wizard: ticks Select on every wizard line and Select All, then reopens the same wizard popup.
  - Depends on: `model x_temp_consignment_hea`, `x_temp_consignment_hea.x_studio_select_all`, `x_temp_consignment_hea.x_studio_temp_consignment_line_ids`
  - Used by: `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea`
  <details><summary>code (16 lines)</summary>

```python
# PATCHED IN-PLACE (Select All): toggle x_studio_select=True on
# every existing line and REOPEN the same wizard record so the popup
# stays visible with the updated checkboxes. Returning no action was
# closing the popup.
if record.id:
  record.x_studio_temp_consignment_line_ids.write({'x_studio_select': True})
  record.write({'x_studio_select_all': True})
  action = {
    'name': 'Copy PO Lines',
    'type': 'ir.actions.act_window',
    'res_model': 'x_temp_consignment_hea',
    'view_mode': 'form',
    'res_id': record.id,
    'target': 'new',
    'context': env.context,
  }
```
  </details>
**Window actions (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp Consignment Header | `action_1259_temp_consignment_header` | Opens **Temp Consignment Header** records (tree,form). | `model x_temp_consignment_hea` | `menu BugFix-Stock.menu_779_temp_consignment_header`<br>`menu BugFix-Studio-Misc.menu_f6f_temp_consignment_header` (BugFix-Studio-Misc) |
| Temp Consignment Header | `action_2851_temp_consignment_header` | Opens **Temp Consignment Header** records (form). | `model x_temp_consignment_hea` |  |
| Temp Consignment Header | `action_1299_temp_consignment_header` | Opens **Temp Consignment Header** records (form). | `model x_temp_consignment_hea` |  |
| Temp Consignment Header | `action_1260_temp_consignment_header` | Opens **Temp Consignment Header** records (tree,form). | `model x_temp_consignment_hea` |  |
| Temp Consignment Header | `action_1357_temp_consignment_header` | Opens **Temp Consignment Header** records (form). | `model x_temp_consignment_hea` |  |
| Temp Consignment Header | `action_2861_temp_consignment_header` | Opens **Temp Consignment Header** records (form). | `model x_temp_consignment_hea` | `menu BugFix-Stock.menu_f6_temp_consignment_header_1`<br>`menu BugFix-Stock.menu_f6_temp_consignment_header` |
| Temp Consignment Header | `action_1261_temp_consignment_header` | Opens **Temp Consignment Header** records (tree,form). | `model x_temp_consignment_hea` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_temp_consignment_header` (BugFix-Studio-Misc) |
| temp Consignment Header | `action_1295_temp_consignment_header` | Opens **Temp Consignment Header** records (form). | `model x_temp_consignment_hea` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_temp_consignment_header` (BugFix-Studio-Misc) |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| IMP Copy PO Line to Consignment | `ported_primary_2905_form_x_temp_consignment_hea` | form | full form layout with 21 fields | 'Copy Import Order Lines' wizard form: Select All / Clear All buttons and an editable list of PO lines to tick (PO, vendor, indent, product, quantities, weight, volume, remainders, prices, dates) for copying into a consignment. | `server action BugFix-Stock.server_action_1298_imp_select_all_in_copy_po_lines`<br>`server action BugFix-Stock.server_action_1301_imp_clear_all_in_copy_po_lines`<br>`server action BugFix-Stock.server_action_1302_imp_apply_selected_po_lines_to_consignment`<br>`x_temp_consignment_hea.x_name`<br>`x_temp_consignment_hea.x_studio_select_all`<details><summary>+19 more</summary>`x_temp_consignment_hea.x_studio_temp_consignment_header_id`<br>`x_temp_consignment_hea.x_studio_temp_consignment_line_ids`<br>`x_temp_consignment_lin.x_studio_concessional_rate`<br>`x_temp_consignment_lin.x_studio_consignment_remainder`<br>`x_temp_consignment_lin.x_studio_delivery_date`<br>`x_temp_consignment_lin.x_studio_delivery_remainder`<br>`x_temp_consignment_lin.x_studio_description`<br>`x_temp_consignment_lin.x_studio_indent_no`<br>`x_temp_consignment_lin.x_studio_product_id`<br>`x_temp_consignment_lin.x_studio_purchase_id`<br>`x_temp_consignment_lin.x_studio_purchase_line_id`<br>`x_temp_consignment_lin.x_studio_quantity`<br>`x_temp_consignment_lin.x_studio_select`<br>`x_temp_consignment_lin.x_studio_subtotal`<br>`x_temp_consignment_lin.x_studio_supplier_id`<br>`x_temp_consignment_lin.x_studio_unit_price`<br>`x_temp_consignment_lin.x_studio_uom_id`<br>`x_temp_consignment_lin.x_studio_volume`<br>`x_temp_consignment_lin.x_studio_weight`</details> | `view BugFix-Purchase.view_x_temp_consignment_hea_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_3018_odoo_studio_imp_copy_po_line_to_consignm` |
| Odoo Studio: IMP Copy PO Line to Consignment customization | `ported_view_3018_odoo_studio_imp_copy_po_line_to_consignm` | form |  | Empty customization of the Copy PO Line wizard; its only change was moved to BugFix-Purchase, so it has no effect. | `view BugFix-Stock.ported_primary_2905_form_x_temp_consignment_hea` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp Consignment Header group_system | `access_1295_temp_consignment_header_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp Consignment Header records. | `group base.group_system` (base)<br>`model x_temp_consignment_hea` |  |
| Temp Consignment Header group_user | `access_1296_temp_consignment_header_group_user` | Gives **User types / Internal User** read access to Temp Consignment Header records. | `group base.group_user` (base)<br>`model x_temp_consignment_hea` |  |
| x_temp_consignment_hea user access | `access_x_temp_consignment_hea_user` | Gives **User types / Internal User** read/write/create/delete access to Temp Consignment Header records. | `group base.group_user` (base)<br>`model x_temp_consignment_hea` |  |
