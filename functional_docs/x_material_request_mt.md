# BugFix-Stock — `x_material_request_mt`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request_mt` — Material Request MT

*Created by this repo.* Python: `models/x_material_request_mt.py`, `models/x_material_request_mt_gap.py`. Record name field: `x_name`.

Other repos that use this model: `x_material_request_mt_line_9a011.x_material_request_mt_id` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:x_material_request_mt -->
Material Request MT is a Studio-generated kanban app for material requests, with stages, tags, a responsible user, department, dates, value and priority, and calendar, gantt, map, pivot and graph views. An automation gives each record a number from the material request sequence. Purpose not evident from code beyond these generic app features; many of its text fields are unused.
<!-- /SUMMARY -->

**Fields (62):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`x_material_request_mt.activity_summary`<br>`x_material_request_mt.activity_type_icon`<br>`x_material_request_mt.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; today=Today; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_material_request_mt.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_material_request_mt.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_material_request_mt.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for the request; defaults to active. | stored |  | `default BugFix-Stock.default_final_bugfix_stock_field_x_material_request_mt_x_active_true`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e` |
| `x_color` | Color | integer | Color index of the request card; shown in list and kanban. | stored |  | `view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_name` | Description | char | Request description/reference; set from the 'material.request.sequence' number by an automation. | stored; required |  | `server action BugFix-Stock.server_action_3399_execute_code`<br>`view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the request; has defaults and is used by the multi-company record rule. | stored | `model res.company` (base) | `default BugFix-Stock.default_624_x_material_request_mt_x_studio_company_id`<br>`default BugFix-Stock.default_625_x_material_request_mt_x_studio_company_id`<br>`default BugFix-Stock.default_626_x_material_request_mt_x_studio_company_id`<br>`record rule BugFix-Stock.rule_884_material_request_mt_multi_company`<br>`view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<details><summary>+1 more</summary>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`</details> |
| `x_studio_created_by` | Created by | char | 'Created by' stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_created_on` | Created on | char | 'Created on' stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_currency_id` | Currency | many2one → `res.currency` | Currency for the request's Value; has defaults. | stored | `model res.currency` (base) | `default BugFix-Stock.default_627_x_material_request_mt_x_studio_currency_id`<br>`default BugFix-Stock.default_628_x_material_request_mt_x_studio_currency_id`<br>`default BugFix-Stock.default_629_x_material_request_mt_x_studio_currency_id`<br>`view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<details><summary>+1 more</summary>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e`</details> |
| `x_studio_date` | Date | date | Date of the request; used in the form, search and pivot views. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8769_default_pivot_view_for_x_material_request_mt_e` |
| `x_studio_date_start` | Start Date | datetime | Start date/time of the request; shown in the form and search. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e` |
| `x_studio_date_stop` | End Date | datetime | End date/time of the request; shown in the form and search. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e` |
| `x_studio_department` | Department | char | Department stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_image` | Image | binary | Image attached to the request; shown on the form and kanban card. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_studio_journal_type` | Journal Type | char | Journal type stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_kanban_state` | Kanban State | selection: normal=In Progress; done=Ready; blocked=Blocked | Kanban state of the request: In Progress, Ready or Blocked. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_studio_maintenance_request_no` | Maintenance Request No | char | Maintenance request number stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_many2one_field_32i_1j8i1f37m` | Department | many2one → `hr.department` | Department (HR) of the request; added to the request form and list by the customization views. | stored | `model hr.department` (hr) | `view BugFix-Stock.view_final_x_material_request_mt_odoo_studio_default_form_view_for_x_material_request_mt_c`<br>`view BugFix-Stock.view_final_x_material_request_mt_odoo_studio_default_list_view_for_x_material_request_mt_c` |
| `x_studio_notes` | Notes | html | Rich-text notes on the request form. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e` |
| `x_studio_notes_1` | Notes | char | Second notes text field; not used by any view or logic. | stored |  |  |
| `x_studio_partner_email` | Email | char | Email of the request contact, shown on the form. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e` |
| `x_studio_partner_id` | Contact | many2one → `res.partner` | Contact linked to the request; shown in list, form, search and map views. | stored | `model res.partner` (base) | `view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8768_default_map_view_for_x_material_request_mt_e` |
| `x_studio_partner_phone` | Phone | char | Phone of the request contact, shown on the form. | stored |  | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e` |
| `x_studio_priority` | High Priority | boolean | High-priority star on the kanban card. | stored |  | `view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_studio_request_reference` | Request Reference | char | Request reference stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_requested_by` | Requested By | char | Requested-by stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_requested_date` | Requested Date | char | Requested date stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_sequence` | Sequence | integer | Ordering number with a default value. | stored |  | `default BugFix-Stock.default_630_x_material_request_mt_x_studio_sequence` |
| `x_studio_stage_id` | Stage | many2one → `x_material_request_mt_stage` | Kanban stage of the request; has a default stage and is used in form, search and pivot. | stored; required | `model x_material_request_mt_stage` | `default BugFix-Stock.default_631_x_material_request_mt_x_studio_stage_id`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8769_default_pivot_view_for_x_material_request_mt_e` |
| `x_studio_status` | Status | char | Status stored as text; not used by any view or logic. | stored |  |  |
| `x_studio_tag_ids` | Tags | many2many → `x_material_request_mt_tag` | Tags categorizing the request. | stored | `model x_material_request_mt_tag` | `view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_studio_user_id` | Responsible | many2one → `res.users` | User responsible for the request. | stored | `model res.users` (base) | `view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8764_default_search_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |
| `x_studio_value` | Value | monetary | Monetary value of the request; shown in list, form, kanban, pivot and graph. | stored |  | `view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8769_default_pivot_view_for_x_material_request_mt_e`<br>`view BugFix-Stock.view_8770_default_graph_view_for_x_material_request_mt_e` |
| `x_studio_warehouse` | Warehouse | char | Warehouse stored as text; not used by any view or logic. | stored |  |  |

**Server actions (1):**

- **Execute Code** (`server_action_3399_execute_code`, type `code`)
  - Function: Assigns the next number from sequence `material.request.sequence` as the Material Request (MT) name; run by the Generate Sequence Number for MR automation.
  - Depends on: `model ir.sequence` (base), `model x_material_request_mt`, `x_material_request_mt.x_name`
  - Used by: `automation BugFix-Stock.base_automation_346_generate_sequence_number_for_mr`
  <details><summary>code (1 lines)</summary>

```python
record['x_name'] = env['ir.sequence'].next_by_code('material.request.sequence')
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Generate Sequence Number for MR | `base_automation_346_generate_sequence_number_for_mr` |  | When a watched field changes in the form on Material Request MT, runs _Execute Code_. | `model x_material_request_mt`<br>`server action BugFix-Stock.server_action_3399_execute_code` |  |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request MT | `act_window_3384_material_request_mt` | Opens **Material Request MT** records (kanban,tree,form,calendar,gantt,map,pivot,graph). | `model x_material_request_mt` | `menu BugFix-Stock.menu_1746_material_request_mt`<br>`menu BugFix-Stock.menu_f6_material_request_mt` |

**Views (12):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default calendar view for x_material_request_mt | `view_8765_default_calendar_view_for_x_material_request_mt_e` | calendar | full calendar layout with 0 fields | Calendar of Material Request (MT) records by Date. |  |  |
| Default form view for x_material_request_mt | `view_8763_default_form_view_for_x_material_request_mt_e` | form | full form layout with 20 fields | Base Material Request (MT) form generated by Studio: clickable stage bar, kanban state, image, partner, dates, responsible, value, tags, notes and chatter; its Details lines tab is empty (lines field stripped). | `group base.group_multi_company` (base)<br>`x_material_request_mt.activity_ids`<br>`x_material_request_mt.message_follower_ids`<br>`x_material_request_mt.message_ids`<br>`x_material_request_mt.x_active`<details><summary>+16 more</summary>`x_material_request_mt.x_name`<br>`x_material_request_mt.x_studio_company_id`<br>`x_material_request_mt.x_studio_currency_id`<br>`x_material_request_mt.x_studio_date_start`<br>`x_material_request_mt.x_studio_date_stop`<br>`x_material_request_mt.x_studio_date`<br>`x_material_request_mt.x_studio_image`<br>`x_material_request_mt.x_studio_kanban_state`<br>`x_material_request_mt.x_studio_notes`<br>`x_material_request_mt.x_studio_partner_email`<br>`x_material_request_mt.x_studio_partner_id`<br>`x_material_request_mt.x_studio_partner_phone`<br>`x_material_request_mt.x_studio_stage_id`<br>`x_material_request_mt.x_studio_tag_ids`<br>`x_material_request_mt.x_studio_user_id`<br>`x_material_request_mt.x_studio_value`</details> | `view BugFix-Stock.view_final_x_material_request_mt_odoo_studio_default_form_view_for_x_material_request_mt_c` |
| Default gantt view for x_material_request_mt | `view_8766_default_gantt_view_for_x_material_request_mt_e` | gantt | full gantt layout with 0 fields | Gantt view of Material Request (MT) records from start to end date. |  |  |
| Default graph view for x_material_request_mt | `view_8770_default_graph_view_for_x_material_request_mt_e` | graph | full graph layout with 2 fields | Graph of Material Request (MT) Value by creation date. | `x_material_request_mt.x_studio_value` |  |
| Default kanban view for x_material_request_mt | `view_8767_default_kanban_view_for_x_material_request_mt_e` | kanban | full kanban layout with 9 fields | Kanban of Material Request (MT) records grouped by stage, with priority star, image, responsible, value progress bar by kanban state and colors. | `x_material_request_mt.x_color`<br>`x_material_request_mt.x_name`<br>`x_material_request_mt.x_studio_currency_id`<br>`x_material_request_mt.x_studio_image`<br>`x_material_request_mt.x_studio_kanban_state`<details><summary>+4 more</summary>`x_material_request_mt.x_studio_priority`<br>`x_material_request_mt.x_studio_tag_ids`<br>`x_material_request_mt.x_studio_user_id`<br>`x_material_request_mt.x_studio_value`</details> | `view BugFix-Stock.view_final_x_material_request_mt_odoo_studio_default_kanban_view_for_x_material_request_mt` |
| Default list view for x_material_request_mt | `view_8762_default_list_view_for_x_material_request_mt_e` | tree | full tree layout with 8 fields | Base list of Material Request (MT) records: name, partner, responsible, company, value (totalled), tags and color. | `group base.group_multi_company` (base)<br>`x_material_request_mt.x_color`<br>`x_material_request_mt.x_name`<br>`x_material_request_mt.x_studio_company_id`<br>`x_material_request_mt.x_studio_currency_id`<details><summary>+4 more</summary>`x_material_request_mt.x_studio_partner_id`<br>`x_material_request_mt.x_studio_tag_ids`<br>`x_material_request_mt.x_studio_user_id`<br>`x_material_request_mt.x_studio_value`</details> | `view BugFix-Stock.view_final_x_material_request_mt_odoo_studio_default_list_view_for_x_material_request_mt_c` |
| Default map view for x_material_request_mt | `view_8768_default_map_view_for_x_material_request_mt_e` | map | full map layout with 1 fields | Map view placing Material Request (MT) records at their partner's address. | `x_material_request_mt.x_studio_partner_id` |  |
| Default pivot view for x_material_request_mt | `view_8769_default_pivot_view_for_x_material_request_mt_e` | pivot | full pivot layout with 3 fields | Pivot of Material Request (MT) Value by stage (columns) and date (rows). | `x_material_request_mt.x_studio_date`<br>`x_material_request_mt.x_studio_stage_id`<br>`x_material_request_mt.x_studio_value` |  |
| Default search view for x_material_request_mt | `view_8764_default_search_view_for_x_material_request_mt_e` | search | full search layout with 8 fields | Search view for Material Request (MT): search by name, partner, responsible, tags; filters My requests, date ranges and Archived; group by partner, responsible or stage. | `x_material_request_mt.x_active`<br>`x_material_request_mt.x_name`<br>`x_material_request_mt.x_studio_date_start`<br>`x_material_request_mt.x_studio_date_stop`<br>`x_material_request_mt.x_studio_date`<details><summary>+4 more</summary>`x_material_request_mt.x_studio_partner_id`<br>`x_material_request_mt.x_studio_stage_id`<br>`x_material_request_mt.x_studio_tag_ids`<br>`x_material_request_mt.x_studio_user_id`</details> |  |
| Odoo Studio: Default form view for x_material_request_mt customization | `view_final_x_material_request_mt_odoo_studio_default_form_view_for_x_material_request_mt_c` | form | remove `//form[1]/sheet[1]/notebook[1]`; remove `//form[1]/sheet[1]/group[not(@name)][1]`; remove `//group[@name='studio_group_a56f01_right']`; replace `//field[@name='x_studio_date_start']`: add field x_studio_many2one_field_32i_1j8i1f37m; remove `//field[@name='x_studio_date']`; remove `//field[@name='x_studio_partner_email']`; remove `//field[@name='x_studio_partner_phone']`; remove `//field[@name='x_studio_partner_id']` … | Simplifies the Material Request (MT) form: removes partner, contact, date fields, right group, notes and lines tab, adds a Department field, and makes the name a read-only 'Description'. | `view BugFix-Stock.view_8763_default_form_view_for_x_material_request_mt_e`<br>`x_material_request_mt.x_studio_many2one_field_32i_1j8i1f37m` |  |
| Odoo Studio: Default kanban view for x_material_request_mt customization | `view_final_x_material_request_mt_odoo_studio_default_kanban_view_for_x_material_request_mt` | kanban | set string=Description on `//field[@name='x_name']` | Relabels the name as 'Description' on the Material Request (MT) kanban. | `view BugFix-Stock.view_8767_default_kanban_view_for_x_material_request_mt_e` |  |
| Odoo Studio: Default list view for x_material_request_mt customization | `view_final_x_material_request_mt_odoo_studio_default_list_view_for_x_material_request_mt_c` | tree | remove `//field[@name='x_color']`; remove `//field[@name='x_studio_tag_ids']`; remove `//field[@name='x_studio_value']`; remove `//field[@name='x_studio_currency_id']`; remove `//field[@name='x_studio_company_id']`; remove `//field[@name='x_studio_user_id']`; remove `//field[@name='x_studio_partner_id']`; before `//field[@name='x_name']`: add field x_studio_many2one_field_32i_1j8i1f37m | Simplifies the Material Request (MT) list to Department and name, removing partner, responsible, company, currency, value, tags and color. | `view BugFix-Stock.view_8762_default_list_view_for_x_material_request_mt_e`<br>`x_material_request_mt.x_studio_many2one_field_32i_1j8i1f37m` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request MT group_system | `access_8291_material_request_mt_group_system` | Gives **Administration / Settings** read/write/create/delete access to Material Request MT records. | `group base.group_system` (base)<br>`model x_material_request_mt` |  |
| Material Request MT group_user | `access_8292_material_request_mt_group_user` | Gives **User types / Internal User** read/write/create access to Material Request MT records. | `group base.group_user` (base)<br>`model x_material_request_mt` |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request MT - Multi-Company | `rule_884_material_request_mt_multi_company` | For everyone (global rule): read/write/create/delete on Material Request MT only where `['|', ('x_studio_company_id', '=', False), ('x_studio_company_id', 'in', company_ids)]`. | `model x_material_request_mt`<br>`x_material_request_mt.x_studio_company_id` |  |
