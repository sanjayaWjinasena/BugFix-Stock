# BugFix-Stock — `x_temp_structure_maste`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_temp_structure_maste` — Temp Structure Master

*Created by this repo.* Python: `models/x_temp_structure_maste.py`, `models/x_temp_structure_maste_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_temp_structure_maste -->
The temporary wizard record behind Apply Structure Formula. It lists charge lines to choose from, and its Apply Formula action builds a formula from the selected charge names and appends it to the structure detail.
<!-- /SUMMARY -->

**Fields (34):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `x_temp_structure_maste.activity_summary`<br>`x_temp_structure_maste.activity_type_icon`<br>`x_temp_structure_maste.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_temp_structure_maste.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_temp_structure_maste.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_temp_structure_maste.activity_ids` |  |
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
| `x_active` | Active | boolean | Archive flag; defaults to active. | stored |  | `default BugFix-Stock.default_final_bugfix_stock_field_x_temp_structure_maste_x_active_true` |
| `x_name` | Name | char | Name of the temporary Apply Formula wizard record. | stored |  | `view BugFix-Stock.view_2705_imp_apply_formula_e` |
| `x_studio_sequence` | Sequence | integer | Ordering number with a default value. | stored |  | `default BugFix-Stock.default_126_x_temp_structure_maste_x_studio_sequence` |
| `x_studio_temp_structure_details` | Temp Structure Details | one2many → `x_temp_structure_detai` | Charge lines offered in the Apply Formula wizard; the selected ones are appended to the structure detail's formula. | stored | `model x_temp_structure_detai` | `server action BugFix-Stock.server_action_1204_imp_apply_formula`<br>`view BugFix-Stock.view_2705_imp_apply_formula_e` |

**Server actions (1):**

- **IMP - Apply Formula** (`server_action_1204_imp_apply_formula`, type `code`)
  - Function: Builds a formula string from the selected charge names (as [Charge]) in the temporary structure wizard, appends it to the Structure Detail's Formula, errors if nothing selected, then deletes the wizard record.
  - Depends on: `model x_structure_details` (BugFix-Purchase), `model x_temp_structure_maste`, `x_temp_structure_maste.x_studio_temp_structure_details_id` (BugFix-Purchase), `x_temp_structure_maste.x_studio_temp_structure_details`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (45 lines)</summary>

```python
select = 0

formula = ''

formula2 = ''

for indicator_line in record.x_studio_temp_structure_details:

  if (indicator_line.x_studio_select == True):

    select += 1

    formula += "[" + indicator_line.x_studio_charge_name + "]"



if select == 0:

 raise UserError("Atleast One Line Should be Selected.")

 

update_formula = env['x_structure_details'].search([('id', '=', record.x_studio_temp_structure_details_id.id)],limit=1)

if update_formula:

  if update_formula.x_studio_formula:

    formula2 = update_formula.x_studio_formula + formula

  else:

    formula2 = formula

    

  update_formula.write({'x_studio_formula':formula2})



if record.id:

  temp_rec = env['x_temp_structure_maste'].search([('id', '=', record.id)],limit=1)

  temp_rec.unlink()
```
  </details>
**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| ttt structure master | `act_window_1203_ttt_structure_master` | Opens **Temp Structure Master** records (form). | `model x_temp_structure_maste` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_ttt_structure_master` (BugFix-Studio-Misc) |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| IMP Apply Formula | `view_2705_imp_apply_formula_e` | form | full form layout with 2 fields | 'Apply Structure Formula' wizard with a list of charge indicators and an Apply button (runs IMP - Apply Formula). Its list columns (charge name, group) were stripped by the porter, so the list shows no columns. | `server action account_auto_transfer.ir_cron_auto_transfer_ir_actions_server` (account_auto_transfer)<br>`x_temp_structure_maste.x_name`<br>`x_temp_structure_maste.x_studio_temp_structure_details` | `view BugFix-Purchase.view_x_temp_structure_maste_form_upstream_link_fields` (BugFix-Purchase) |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Temp Structure Master group_system | `access_1247_temp_structure_master_group_system` | Gives **Administration / Settings** read/write/create/delete access to Temp Structure Master records. | `group base.group_system` (base)<br>`model x_temp_structure_maste` |  |
| Temp Structure Master group_user | `access_1248_temp_structure_master_group_user` | Gives **User types / Internal User** read access to Temp Structure Master records. | `group base.group_user` (base)<br>`model x_temp_structure_maste` |  |
