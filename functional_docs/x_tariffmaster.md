# BugFix-Stock — `x_tariffmaster`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_tariffmaster` — TariffMaster

*Created by this repo.* Python: `models/x_tariffmaster.py`, `models/x_tariffmaster_gap.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Studio-Misc.access_g_tariff_master_x_tariffmaster_purchase_jin_procurement_end_user_import` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_x_tariffmaster_x_tariffmaster_purchase_jin_pr_view_only` (BugFix-Studio-Misc)<br>`product.product.x_studio_many2one_field_AS0wC` (BugFix-Sales)<br>`product.product.x_studio_tariff_code` (BugFix-Sales)<br>`product.template.x_studio_tariff_code` (BugFix-Sales)<br>`x_tariff_date.x_studio_tariff_master_ids` (BugFix-Purchase)

**Summary:**

<!-- SUMMARY:model:x_tariffmaster -->
A Tariff Master record is a customs tariff (HS) code with a description and company. Products and consignment lines link to it to record their tariff code. Users maintain codes under Purchase, and an automation sets the company.
<!-- /SUMMARY -->

**Fields (35):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.ported_primary_2633_form_x_tariffmaster`<br>`x_tariffmaster.activity_summary`<br>`x_tariffmaster.activity_type_icon`<br>`x_tariffmaster.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_tariffmaster.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_tariffmaster.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_tariffmaster.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Stock.base_automation_320_jin_company_id_in_tariffmaster` |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.ported_primary_2633_form_x_tariffmaster` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.ported_primary_2633_form_x_tariffmaster` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for tariff codes; defaults to active. | stored |  | `default BugFix-Stock.default_91_x_tariffmaster_x_active`<br>`view BugFix-Stock.ported_primary_2633_form_x_tariffmaster`<br>`view BugFix-Stock.view_2634_default_search_view_for_x_tariffmaster_e` |
| `x_name` | Tarrif Code | char | Customs tariff (HS) code, shown in the tariff list, form and search. | stored |  | `view BugFix-Stock.ported_primary_2632_tree_x_tariffmaster`<br>`view BugFix-Stock.ported_primary_2633_form_x_tariffmaster`<br>`view BugFix-Stock.view_2634_default_search_view_for_x_tariffmaster_e` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the tariff code; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Stock.rule_572_jin_multi_company_tariffmaster`<br>`server action BugFix-Stock.sa_f5_x_tariffmaster_jin_company_id_in_tariffmaster`<br>`server action BugFix-Stock.server_action_2686_jin_company_id_in_tariffmaster`<br>`view BugFix-Stock.ported_view_2635_odoo_studio_default_form_view_for_x_tari`<br>`view BugFix-Stock.ported_view_2636_odoo_studio_default_list_view_for_x_tari` |
| `x_studio_description` | Description | char | Description of the tariff code. | stored |  | `view BugFix-Stock.ported_view_2635_odoo_studio_default_form_view_for_x_tari`<br>`view BugFix-Stock.ported_view_2636_odoo_studio_default_list_view_for_x_tari` |
| `x_studio_sequence` | Sequence | integer | Ordering number for tariff codes (list drag handle). | stored |  | `default BugFix-Stock.default_92_x_tariffmaster_x_studio_sequence`<br>`view BugFix-Stock.ported_primary_2632_tree_x_tariffmaster` |

**Server actions (2):**

- **Execute Code** (`server_action_2686_jin_company_id_in_tariffmaster`, type `code`)
  - Function: Sets the Tariff Master record's Company to the user's current active company; run by the matching automation.
  - Depends on: `model res.company` (base), `model x_tariffmaster`, `x_tariffmaster.x_studio_company_id`
  - Used by: `automation BugFix-Stock.base_automation_320_jin_company_id_in_tariffmaster`
  <details><summary>code (5 lines)</summary>

```python

company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
- **JIN - Company Id in TariffMaster** (`sa_f5_x_tariffmaster_jin_company_id_in_tariffmaster`, type `code`)
  - Function: Sets the Company of a Tariff Master record to the user's currently active company.
  - Depends on: `model res.company` (base), `model x_tariffmaster`, `x_tariffmaster.x_studio_company_id`
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
| JIN - Company Id in TariffMaster | `base_automation_320_jin_company_id_in_tariffmaster` |  | When a record is created or updated on TariffMaster, runs _Execute Code_. | `model x_tariffmaster`<br>`server action BugFix-Stock.server_action_2686_jin_company_id_in_tariffmaster`<br>`x_tariffmaster.create_date` |  |

**Window actions (10):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Tariff | `act_window_2044_tariff` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |
| Tariff Master | `act_window_2041_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` | `menu BugFix-Stock.menu_f6_tariff_master`<br>`menu BugFix-Studio-Misc.menu_f6r2_test_app_05_imports_tariff_tariff_master` (BugFix-Studio-Misc) |
| Tariff Master | `act_window_2045_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |
| Tariff Master | `act_window_2048_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |
| Tariff Master | `act_window_2049_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |
| Tariff Master | `act_window_2057_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |
| Tariff Master | `act_window_2069_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` | `menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_imports_configurations_tariff_tariff_` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_imports_01_imports_configuration_tariff_tariff_mast` (BugFix-Studio-Misc)<br>`menu BugFix-Studio-Misc.menu_f6r3_tariff_tariff_master` (BugFix-Studio-Misc) |
| Tariff Master | `act_window_2867_tariff_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |
| TariffMaster | `act_window_1159_tariffmaster` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` | `menu BugFix-Stock.menu_f6_setups`<br>`menu BugFix-Stock.menu_f6_tariffs_master`<br>`menu BugFix-Studio-Misc.menu_f6r3_purchase_configuration_setups_tariffs` (BugFix-Studio-Misc) |
| Tariffs Master | `act_window_2038_tariffs_master` | Opens **TariffMaster** records (tree,form). | `model x_tariffmaster` |  |

**Views (5):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_tariffmaster | `ported_primary_2633_form_x_tariffmaster` | form | full form layout with 5 fields | Base Tariff Master form: archived ribbon, name title, two empty groups and chatter. | `x_tariffmaster.activity_ids`<br>`x_tariffmaster.message_follower_ids`<br>`x_tariffmaster.message_ids`<br>`x_tariffmaster.x_active`<br>`x_tariffmaster.x_name` | `view BugFix-Stock.ported_view_2635_odoo_studio_default_form_view_for_x_tari` |
| Default list view for x_tariffmaster | `ported_primary_2632_tree_x_tariffmaster` | tree | full tree layout with 2 fields | Base list view of Tariff Masters showing a drag handle (sequence) and the name. | `x_tariffmaster.x_name`<br>`x_tariffmaster.x_studio_sequence` | `view BugFix-Stock.ported_view_2636_odoo_studio_default_list_view_for_x_tari` |
| Default search view for x_tariffmaster | `view_2634_default_search_view_for_x_tariffmaster_e` | search | full search layout with 1 fields | Search view for Tariff Masters: search by name and an Archived filter. | `x_tariffmaster.x_active`<br>`x_tariffmaster.x_name` |  |
| Odoo Studio: Default form view for x_tariffmaster customization | `ported_view_2635_odoo_studio_default_form_view_for_x_tari` | form | set string=Tarrif Code on `//form[1]/sheet[1]/div[1]/h1[1]/field[@name='x_name']`; inside `//group[@name='studio_group_f8209d_left']`: add field x_studio_description, field x_studio_company_id; after `//group[@name='studio_group_f8209d']`: add notebook | Customizes the Tariff Master form: labels name 'Tarrif Code', adds description and company, and an empty 'Date Range' tab (its field was dropped as orphan). | `view BugFix-Stock.ported_primary_2633_form_x_tariffmaster`<br>`x_tariffmaster.x_studio_company_id`<br>`x_tariffmaster.x_studio_description` |  |
| Odoo Studio: Default list view for x_tariffmaster customization | `ported_view_2636_odoo_studio_default_list_view_for_x_tari` | tree | before `//field[@name='x_studio_sequence']`: add xpath, field x_studio_description, field x_studio_company_id; set column_invisible=1 on `//field[@name='x_studio_sequence']`; set required=1 on `//field[@name='x_name']` | Customizes the Tariff Master list: name (required) first, then description and optional company; hides the sequence handle. | `view BugFix-Stock.ported_primary_2632_tree_x_tariffmaster`<br>`x_tariffmaster.x_studio_company_id`<br>`x_tariffmaster.x_studio_description` |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| TariffMaster group_system | `access_1220_tariffmaster_group_system` | Gives **Administration / Settings** read/write/create/delete access to TariffMaster records. | `group base.group_system` (base)<br>`model x_tariffmaster` |  |
| TariffMaster group_user | `access_1221_tariffmaster_group_user` | Gives **User types / Internal User** no access to TariffMaster records. | `group base.group_user` (base)<br>`model x_tariffmaster` |  |
| x_tariffmaster user access | `access_x_tariffmaster_user` | Gives **User types / Internal User** read/write/create/delete access to TariffMaster records. | `group base.group_user` (base)<br>`model x_tariffmaster` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| JIN - Multi-Company - TariffMaster | `rule_572_jin_multi_company_tariffmaster` | For everyone (global rule): read/write/create/delete on TariffMaster only where `['|', ('x_studio_company_id', 'in', company_ids), ('x_studio_company_id', '=', False)]`. | `model x_tariffmaster`<br>`x_tariffmaster.x_studio_company_id` |  |
