# BugFix-Stock — `material_request_tes`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `material_request_tes` — Material Request Test

*Created by this repo.* Python: `models/material_request_tes.py`, `models/x_material_request_tes_gap.py`. Record name field: `name`.

Other repos that use this model: `material_request_tes_line_3301b.material_request_tes_id` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:material_request_tes -->
Material Request Test is a Studio-generated kanban app with stages, tags, contact, responsible user, dates, value and priority, and the standard Studio calendar, gantt, map, pivot and graph views. Purpose not evident from code; it has no automations or business logic, and its name suggests a test copy of the material request app.
<!-- /SUMMARY -->

**Fields (50):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`material_request_tes.activity_summary`<br>`material_request_tes.activity_type_icon`<br>`material_request_tes.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`material_request_tes.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`material_request_tes.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`material_request_tes.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag for the test request; defaults to active. | stored |  | `default BugFix-Stock.default_final_bugfix_stock_field_x_material_request_tes_x_active_true`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e` |
| `color` | Color | integer | Color index of the test request card; shown in list and kanban. | stored |  | `view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `name` | Description | char | Description of the test material request. | stored; required |  | `view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `accounting_company_id` | Company | many2one → `res.company` | Company of the test request; has defaults and is used by the multi-company record rule. | stored | `model res.company` (base) | `default BugFix-Stock.default_597_x_material_request_tes_accounting_company_id`<br>`default BugFix-Stock.default_598_x_material_request_tes_accounting_company_id`<br>`default BugFix-Stock.default_599_x_material_request_tes_accounting_company_id`<br>`record rule BugFix-Stock.rule_881_material_request_test_multi_company`<br>`view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<details><summary>+1 more</summary>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`</details> |
| `accounting_currency_id` | Currency | many2one → `res.currency` | Currency for the test request's Value; has defaults. | stored | `model res.currency` (base) | `default BugFix-Stock.default_600_x_material_request_tes_accounting_currency_id`<br>`default BugFix-Stock.default_601_x_material_request_tes_accounting_currency_id`<br>`default BugFix-Stock.default_602_x_material_request_tes_accounting_currency_id`<br>`view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<details><summary>+1 more</summary>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e`</details> |
| `date` | Date | date | Date of the test request; used in form, search and pivot. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8715_default_pivot_view_for_x_material_request_tes_e` |
| `date_start` | Start Date | datetime | Start date/time of the test request. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e` |
| `date_stop` | End Date | datetime | End date/time of the test request. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e` |
| `image` | Image | binary | Image attached to the test request; shown on the form and kanban. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `kanban_state` | Kanban State | selection: normal=In Progress; done=Ready; blocked=Blocked | Kanban state of the test request: In Progress, Ready or Blocked. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `notes` | Notes | html | Rich-text notes on the test request form. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e` |
| `partner_email` | Email | char | Email of the test request contact. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e` |
| `partner_id` | Contact | many2one → `res.partner` | Contact linked to the test request; shown in list, form, search and map. | stored | `model res.partner` (base) | `view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8714_default_map_view_for_x_material_request_tes_e` |
| `partner_phone` | Phone | char | Phone of the test request contact. | stored |  | `view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e` |
| `custom_reports_priority` | High Priority | boolean | High-priority star on the test request kanban card. | stored |  | `view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `sequence` | Sequence | integer | Ordering number with a default value. | stored |  | `default BugFix-Stock.default_603_x_material_request_tes_sequence` |
| `stage_id` | Stage | many2one → `material_request_tes_stage` | Kanban stage of the test request (required); has a default stage. | stored; required | `model material_request_tes_stage` | `default BugFix-Stock.default_BugFix_Stock_field_material_request_tes__x_studi_1`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8715_default_pivot_view_for_x_material_request_tes_e` |
| `tag_ids` | Tags | many2many → `material_request_tes_tag` | Tags categorizing the test request. | stored | `model material_request_tes_tag` | `view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `user_id` | Responsible | many2one → `res.users` | User responsible for the test request. | stored | `model res.users` (base) | `view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8710_default_search_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e` |
| `value` | Value | monetary | Monetary value of the test request; shown in list, form, kanban, pivot and graph. | stored |  | `view BugFix-Stock.view_8708_default_list_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8709_default_form_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8713_default_kanban_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8715_default_pivot_view_for_x_material_request_tes_e`<br>`view BugFix-Stock.view_8716_default_graph_view_for_x_material_request_tes_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test | `act_window_3374_material_request_test` | Opens **Material Request Test** records (kanban,tree,form,calendar,gantt,map,pivot,graph). | `model material_request_tes` | `menu BugFix-Stock.menu_f6_material_request_test` |

**Views (9):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default calendar view for material_request_tes | `view_8711_default_calendar_view_for_x_material_request_tes_e` | calendar | full calendar layout with 0 fields | Calendar of Material Request Test records by Date. |  |  |
| Default form view for material_request_tes | `view_8709_default_form_view_for_x_material_request_tes_e` | form | full form layout with 20 fields | Base Material Request Test form generated by Studio: stage bar, kanban state, image, partner, dates, responsible, value, tags, notes and chatter. | `group base.group_multi_company` (base)<br>`material_request_tes.activity_ids`<br>`material_request_tes.message_follower_ids`<br>`material_request_tes.message_ids`<br>`material_request_tes.active`<details><summary>+16 more</summary>`material_request_tes.name`<br>`material_request_tes.accounting_company_id`<br>`material_request_tes.accounting_currency_id`<br>`material_request_tes.date_start`<br>`material_request_tes.date_stop`<br>`material_request_tes.date`<br>`material_request_tes.image`<br>`material_request_tes.kanban_state`<br>`material_request_tes.notes`<br>`material_request_tes.partner_email`<br>`material_request_tes.partner_id`<br>`material_request_tes.partner_phone`<br>`material_request_tes.stage_id`<br>`material_request_tes.tag_ids`<br>`material_request_tes.user_id`<br>`material_request_tes.value`</details> |  |
| Default gantt view for material_request_tes | `view_8712_default_gantt_view_for_x_material_request_tes_e` | gantt | full gantt layout with 0 fields | Gantt view of Material Request Test records from start to end date. |  |  |
| Default graph view for material_request_tes | `view_8716_default_graph_view_for_x_material_request_tes_e` | graph | full graph layout with 2 fields | Graph of Material Request Test Value by creation date. | `material_request_tes.value` |  |
| Default kanban view for material_request_tes | `view_8713_default_kanban_view_for_x_material_request_tes_e` | kanban | full kanban layout with 9 fields | Kanban of Material Request Test records grouped by stage, with priority, image, responsible, value progress bar and colors. | `material_request_tes.color`<br>`material_request_tes.name`<br>`material_request_tes.accounting_currency_id`<br>`material_request_tes.image`<br>`material_request_tes.kanban_state`<details><summary>+4 more</summary>`material_request_tes.custom_reports_priority`<br>`material_request_tes.tag_ids`<br>`material_request_tes.user_id`<br>`material_request_tes.value`</details> |  |
| Default list view for material_request_tes | `view_8708_default_list_view_for_x_material_request_tes_e` | tree | full tree layout with 8 fields | List of Material Request Test records: name, partner, responsible, company, value (totalled), tags and color. | `group base.group_multi_company` (base)<br>`material_request_tes.color`<br>`material_request_tes.name`<br>`material_request_tes.accounting_company_id`<br>`material_request_tes.accounting_currency_id`<details><summary>+4 more</summary>`material_request_tes.partner_id`<br>`material_request_tes.tag_ids`<br>`material_request_tes.user_id`<br>`material_request_tes.value`</details> |  |
| Default map view for material_request_tes | `view_8714_default_map_view_for_x_material_request_tes_e` | map | full map layout with 1 fields | Map view placing Material Request Test records at their partner's address. | `material_request_tes.partner_id` |  |
| Default pivot view for material_request_tes | `view_8715_default_pivot_view_for_x_material_request_tes_e` | pivot | full pivot layout with 3 fields | Pivot of Material Request Test Value by stage (columns) and date (rows). | `material_request_tes.date`<br>`material_request_tes.stage_id`<br>`material_request_tes.value` |  |
| Default search view for material_request_tes | `view_8710_default_search_view_for_x_material_request_tes_e` | search | full search layout with 8 fields | Search view for Material Request Test: search by name, partner, responsible, tags; filters My requests, date ranges and Archived; group by partner, responsible or stage. | `material_request_tes.active`<br>`material_request_tes.name`<br>`material_request_tes.date_start`<br>`material_request_tes.date_stop`<br>`material_request_tes.date`<details><summary>+4 more</summary>`material_request_tes.partner_id`<br>`material_request_tes.stage_id`<br>`material_request_tes.tag_ids`<br>`material_request_tes.user_id`</details> |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test group_system | `access_8267_material_request_test_group_system` | Gives **Administration / Settings** read/write/create/delete access to Material Request Test records. | `group base.group_system` (base)<br>`model material_request_tes` |  |
| Material Request Test group_user | `access_8268_material_request_test_group_user` | Gives **User types / Internal User** read/write/create access to Material Request Test records. | `group base.group_user` (base)<br>`model material_request_tes` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test - Multi-Company | `rule_881_material_request_test_multi_company` | For everyone (global rule): read/write/create/delete on Material Request Test only where `['|', ('accounting_company_id', '=', False), ('accounting_company_id', 'in', company_ids)]`. | `model material_request_tes`<br>`material_request_tes.accounting_company_id` |  |
