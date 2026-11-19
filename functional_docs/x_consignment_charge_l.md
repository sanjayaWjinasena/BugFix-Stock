# BugFix-Stock — `x_consignment_charge_l`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_consignment_charge_l` — Consignment Charge Line

*Created by this repo.* Python: `models/x_consignment_charge_l.py`, `models/x_consignment_charge_l_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_x_consignment_charge_l_x_consignment_charge_l_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_consignment_charge_l -->
A Consignment Charge Line is the part of a consignment charge, duty or tax allocated to one product on a consignment, with the product, quantity, unit price, percent, amount, charge group and links to its consignment and header charge. These lines are created by the header charge allocation and viewed through the Line Charges and Custom Duty actions; an automation sets the company.
<!-- /SUMMARY -->

**Fields (47):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.ported_primary_2938_form_x_consignment_charge_l`<br>`x_consignment_charge_l.activity_summary`<br>`x_consignment_charge_l.activity_type_icon`<br>`x_consignment_charge_l.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_consignment_charge_l.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_consignment_charge_l.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_consignment_charge_l.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.ported_primary_2938_form_x_consignment_charge_l` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.ported_primary_2938_form_x_consignment_charge_l` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for consignment line charges; defaults to active. | stored |  | `default BugFix-Stock.default_163_x_consignment_charge_l_x_active`<br>`view BugFix-Stock.ported_primary_2938_form_x_consignment_charge_l`<br>`view BugFix-Stock.view_2939_default_search_view_for_x_consignment_charge_l_e` |
| `x_name` | Name | char | Name of the consignment line charge record. | stored |  | `view BugFix-Stock.ported_primary_2937_tree_x_consignment_charge_l`<br>`view BugFix-Stock.ported_primary_2938_form_x_consignment_charge_l`<br>`view BugFix-Stock.view_2939_default_search_view_for_x_consignment_charge_l_e` |
| `x_studio_amount` | Amount | float | Charge amount allocated to the consignment line/product. | stored |  | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_basis` | Basis | selection: Percentage=Percentage; Fixed Per Document=Fixed Per Document | How the line charge is calculated: Percentage or Fixed Per Document. | stored |  | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons` |
| `x_studio_charge_group` | Charge Group | selection: None=None; Charges=Charges; Duty=Duty; Taxes=Taxes | Group of the line charge: None, Charges, Duty or Taxes. | stored |  | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_charge_name` | Charge Name | char | Name of the charge applied to the line. | stored |  | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the line charge; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_522_jin_multi_company_consignment_charge_line`<br>`server action BugFix-Stock.sa_f5_x_consignment_charge_l_jin_company_id_in_consignment_charge_line`<br>`server action BugFix-Stock.server_action_2618_jin_company_id_in_consignment_charge_line`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_consignment_charge_header_id` | Consignment Charge Header Id | many2one → `x_consignment_charge_h` | Header charge this line charge was allocated from. | stored | `model x_consignment_charge_h` | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons` |
| `x_studio_consignment_id` | Consignment Id | many2one → `x_consignment_header` | Consignment this line charge belongs to; used to filter the Line Charges action. | stored | `model x_consignment_header` | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons`<br>`window action BugFix-Stock.action_1319_line_charges` |
| `x_studio_formula` | Formula | char | Text formula describing how the line charge is calculated. | stored |  | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons` |
| `x_studio_indent_id` | Indent_ID | char | Indent (purchase order) identifier the charge relates to. | stored |  | `view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_percent` | Percent | float | Percentage rate of the charge. | stored |  | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_product` | Product | many2one → `product.product` | Product the charge is allocated to. | stored | `model product.product` (product) | `view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons`<br>`view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_quantity` | Quantity | float | Quantity of the product the charge applies to. | stored |  | `view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| `x_studio_sequence` | Sequence | integer | Ordering number for line charges (list drag handle). | stored |  | `default BugFix-Stock.default_164_x_consignment_charge_l_x_studio_sequence`<br>`view BugFix-Stock.ported_primary_2937_tree_x_consignment_charge_l` |
| `x_studio_structure_no` | Structure No | integer | Charge structure number; has a default value. | stored |  | `default BugFix-Stock.default_166_x_consignment_charge_l_x_studio_structure_no`<br>`view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons` |
| `x_studio_unit_price` | Unit Price | float | Unit price of the product the charge applies to. | stored |  | `view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |

**Server actions (2):**

- **Execute Code** (`server_action_2618_jin_company_id_in_consignment_charge_line`, type `code`)
  - Function: Run by an automation: sets the Company of a Consignment Charge Line to the user's active company.
  - Depends on: `model res.company` (base), `model x_consignment_charge_l`, `x_consignment_charge_l.x_studio_company_id`
  - Used by: `automation BugFix-Stock.automation_290_jin_company_id_in_consignment_charge_line`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **JIN - Company Id in Consignment Charge Line** (`sa_f5_x_consignment_charge_l_jin_company_id_in_consignment_charge_line`, type `code`)
  - Function: Sets the Company of a Consignment Charge Line to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_consignment_charge_l`, `x_consignment_charge_l.x_studio_company_id`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Consignment Charge Line | `automation_290_jin_company_id_in_consignment_charge_line` |  | When a record is created or updated on Consignment Charge Line, runs _Execute Code_. | `model x_consignment_charge_l`<br>`server action BugFix-Stock.server_action_2618_jin_company_id_in_consignment_charge_line` |  |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Charge Line | `action_2859_consignment_charge_line` | Opens **Consignment Charge Line** records (tree,form). | `model x_consignment_charge_l` |  |
| Consignment Charge Line | `action_1315_consignment_charge_line` | Opens **Consignment Charge Line** records (tree,form). | `model x_consignment_charge_l` |  |
| Consignment Charge Line | `action_2849_consignment_charge_line` | Opens **Consignment Charge Line** records (tree,form). | `model x_consignment_charge_l` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_consignment_charge_line` (BugFix-Studio-Misc) |
| Custom Duty | `action_2231_custom_duty` | Opens **Consignment Charge Line** records (tree,form). | `model x_consignment_charge_l` | `menu BugFix-Stock.menu_1075_custom_duty`<br>`menu BugFix-Stock.menu_f6_custom_duty` |
| Line Charges | `action_1319_line_charges` | Opens **Consignment Charge Line** records (tree,form), filtered to `[('x_studio_consignment_id', '=', active_id)]`. | `model x_consignment_charge_l`<br>`x_consignment_charge_l.x_studio_consignment_id` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_consignment_charge_l | `ported_primary_2938_form_x_consignment_charge_l` | form | full form layout with 5 fields | Base form of a Consignment Charge Line: archived ribbon, name title, two empty groups filled by the Studio customization, and chatter. | `x_consignment_charge_l.activity_ids`<br>`x_consignment_charge_l.message_follower_ids`<br>`x_consignment_charge_l.message_ids`<br>`x_consignment_charge_l.x_active`<br>`x_consignment_charge_l.x_name` | `view BugFix-Purchase.view_x_consignment_charge_l_form_upstream_link_fields` (BugFix-Purchase)<br>`view BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons` |
| Default list view for x_consignment_charge_l | `ported_primary_2937_tree_x_consignment_charge_l` | tree | full tree layout with 2 fields | Base list view of Consignment Charge Lines showing a drag handle (sequence) and the name. | `x_consignment_charge_l.x_name`<br>`x_consignment_charge_l.x_studio_sequence` | `view BugFix-Stock.ported_view_2942_odoo_studio_default_list_view_for_x_cons` |
| Default search view for x_consignment_charge_l | `view_2939_default_search_view_for_x_consignment_charge_l_e` | search | full search layout with 1 fields | Search view for Consignment Charge Lines: search by name and an Archived filter. | `x_consignment_charge_l.x_active`<br>`x_consignment_charge_l.x_name` |  |
| Odoo Studio: Default form view for x_consignment_charge_l customization | `ported_view_2941_odoo_studio_default_form_view_for_x_cons` | form | inside `//group[@name='studio_group_da7bc0_left']`: add field x_studio_product, field x_studio_charge_group, field x_studio_charge_name, field x_studio_percent, field x_studio_amount, field x_studio_basis, field x_studio_formula; inside `//group[@name='studio_group_da7bc0_right']`: add field x_studio_consignment_id, field x_studio_consignment_charge_header_id, field x_studio_structure_no | Customizes the Consignment Charge Line form: shows product, charge group, charge name, percent and amount (basis and formula hidden), plus consignment, charge header and structure no. | `view BugFix-Stock.ported_primary_2938_form_x_consignment_charge_l`<br>`x_consignment_charge_l.x_studio_amount`<br>`x_consignment_charge_l.x_studio_basis`<br>`x_consignment_charge_l.x_studio_charge_group`<br>`x_consignment_charge_l.x_studio_charge_name`<details><summary>+6 more</summary>`x_consignment_charge_l.x_studio_consignment_charge_header_id`<br>`x_consignment_charge_l.x_studio_consignment_id`<br>`x_consignment_charge_l.x_studio_formula`<br>`x_consignment_charge_l.x_studio_percent`<br>`x_consignment_charge_l.x_studio_product`<br>`x_consignment_charge_l.x_studio_structure_no`</details> |  |
| Odoo Studio: Default list view for x_consignment_charge_l customization | `ported_view_2942_odoo_studio_default_list_view_for_x_cons` | tree | set create=false, delete=false, edit=false, editable=bottom on `//tree[1]`; set column_invisible=1 on `//field[@name='x_studio_sequence']`; after `//field[@name='x_studio_sequence']`: add field x_studio_indent_id, field x_studio_consignment_id, field x_studio_product, field x_studio_charge_group, field x_studio_charge_name, field x_studio_quantity, field x_studio_unit_price, field x_studio_percent, field x_studio_amount, field x_studio_company_id; set column_invisible=1 on `//field[@name='x_name']` | Customizes the Consignment Charge Line list: no create/edit/delete, showing indent, consignment, product, charge group and name, quantity, unit price, percent, amount and company; hides sequence and name. | `view BugFix-Stock.ported_primary_2937_tree_x_consignment_charge_l`<br>`x_consignment_charge_l.x_studio_amount`<br>`x_consignment_charge_l.x_studio_charge_group`<br>`x_consignment_charge_l.x_studio_charge_name`<br>`x_consignment_charge_l.x_studio_company_id`<details><summary>+6 more</summary>`x_consignment_charge_l.x_studio_consignment_id`<br>`x_consignment_charge_l.x_studio_indent_id`<br>`x_consignment_charge_l.x_studio_percent`<br>`x_consignment_charge_l.x_studio_product`<br>`x_consignment_charge_l.x_studio_quantity`<br>`x_consignment_charge_l.x_studio_unit_price`</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Charge Line group_system | `access_1335_consignment_charge_line_group_system` | Gives **Administration / Settings** read/write/create/delete access to Consignment Charge Line records. | `group base.group_system` (base)<br>`model x_consignment_charge_l` |  |
| Consignment Charge Line group_user | `access_1336_consignment_charge_line_group_user` | Gives **User types / Internal User** read access to Consignment Charge Line records. | `group base.group_user` (base)<br>`model x_consignment_charge_l` |  |
| x_consignment_charge_l user access | `access_x_consignment_charge_l_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Charge Line records. | `group base.group_user` (base)<br>`model x_consignment_charge_l` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - Consignment Charge Line | `rule_522_jin_multi_company_consignment_charge_line` | For everyone (global rule): read/write/create/delete on Consignment Charge Line only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_consignment_charge_l`<br>`x_consignment_charge_l.x_studio_company_id` |  |
