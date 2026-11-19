# BugFix-Stock — `x_material_request`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request` — Material Request

*Created by this repo.* Python: `models/x_material_request.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Purchase.access_1429_material_request_group_system` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_1430_material_request_group_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_6042_jin___maintenance___equipment_manager` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_6042_jin_maintenance_equipment_manager` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_6085_user` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_6242_inv___administrator` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_6242_inv_administrator` (BugFix-Purchase)<br>`access right BugFix-Purchase.access_6972_user` (BugFix-Purchase)<details><summary>+34 more</summary>`access right BugFix-Purchase.access_x_material_request_user` (BugFix-Purchase)<br>`access right BugFix-Studio-Misc.access_g_jin_maintenance_maintenance_users_x_material_request_maintenance_jin_maintenance__1` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_jin_maintenance_maintenance_users_x_material_request_maintenance_jin_maintenance_` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_jin_manufacturing_minimum_rights_x_material_request_manufacturing_jin_manufacturi` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_jin_manufacturing_mo_full_writes_x_material_request_manufacturing_jin_manufacturi` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_jin_repair_minimum_rights_x_material_request_helpdesk_jin_repair_full_rights` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_jin_repair_minimum_rights_x_material_request_helpdesk_jin_repair_minimum_rights` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_material_request_group_system_x_material_request_manufacturing_jin_manufacturing_` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_material_request_group_user_x_material_request_manufacturing_jin_manufacturing_mo` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_user_x_material_request_helpdesk_jin_repair_ticket_creater` (BugFix-Studio-Misc)<br>`automation BugFix-Purchase.base_automation_230_mr_validate_delete` (BugFix-Purchase)<br>`automation BugFix-Purchase.base_automation_95_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Maintenance.server_action_1646_mr_create_for_mnt` (BugFix-Maintenance)<br>`server action BugFix-Maintenance.server_action_1649_mr_create_for_mnt` (BugFix-Maintenance)<br>`server action BugFix-Maintenance.server_action_2326_mr_create_mr_from_maintenance_request` (BugFix-Maintenance)<br>`server action BugFix-Purchase.sa_f5_x_material_request_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_material_request_mr_validate_delete` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1563_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1650_pr_create_for_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1652_pr_non_create_for_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2388_confirm_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2391_reset_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2394_request_approval_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2397_approve_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2400_reject_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2410_mr_validate_delete` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2440_mr_request_approval_notify_user` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2441_request_approval_mr_update_status` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2443_mr_request_approve_confirm_notify_user` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2444_approve_mr_status_update` (BugFix-Purchase)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`x_pr_non_inventory.x_studio_material_request_ref` (BugFix-Purchase)<br>`x_purchase_request.x_studio_material_request_ref` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:x_material_request -->
A Material Request is an internal request for products from a stores warehouse, raised by a department, optionally for a maintenance request. It moves from Draft to Confirmed, To Be Approved, Approved or Rejected through buttons on its form, which check that lines have quantities and schedule approval activities. Actions also create an outgoing material transfer from the warehouse for the quantities still to transfer, and purchase requests; the request tracks its transfers and is computed Done when they are all finished. Automations number new requests and block deleting a request that is not in Draft.
<!-- /SUMMARY -->

**Fields (53):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `activity_calendar_event_id` | Next Activity Calendar Event | many2one → `calendar.event` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model calendar.event` (calendar) |  |
| `activity_date_deadline` | Next Activity Deadline | date | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_decoration` | Activity Exception Decoration | selection: warning=Alert; warning=Alert; danger=Error; danger=Error | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_exception_icon` | Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_ids` | Activities | one2many → `mail.activity` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | stored | `model mail.activity` (mail) | `view BugFix-Stock.ported_primary_3243_form_x_material_request`<br>`x_material_request.activity_summary`<br>`x_material_request.activity_type_icon`<br>`x_material_request.activity_type_id` |
| `activity_state` | Activity State | selection: overdue=Overdue; overdue=Overdue; today=Today; today=Today; planned=Planned; planned=Planned | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored |  |  |
| `activity_summary` | Next Activity Summary | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.summary`; not stored | `mail.activity.summary` (mail)<br>`x_material_request.activity_ids` |  |
| `activity_type_icon` | Activity Type Icon | char | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.icon`; not stored | `mail.activity.icon` (mail)<br>`x_material_request.activity_ids` |  |
| `activity_type_id` | Next Activity Type | many2one → `mail.activity.type` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | related `activity_ids.activity_type_id`; not stored | `mail.activity.activity_type_id` (mail)<br>`model mail.activity.type` (mail)<br>`x_material_request.activity_ids` |  |
| `activity_user_id` | Responsible User | many2one → `res.users` | Standard activity field (scheduled to-dos, calls, meetings on the record) provided by Odoo’s activity mixin. | not stored | `model res.users` (base) |  |
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Purchase.base_automation_95_material_req_gen` (BugFix-Purchase)<br>`automation BugFix-Stock.base_automation_95_material_req_gen` |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `has_message` | Has Message | boolean | Standard chatter field: tells whether the record has messages. | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `message_attachment_count` | Attachment Count | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_follower_ids` | Followers | one2many → `mail.followers` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.followers` (mail) | `view BugFix-Stock.ported_primary_3243_form_x_material_request` |
| `message_has_error` | Message Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_error_counter` | Number of errors | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_has_sms_error` | SMS Delivery error | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_ids` | Messages | one2many → `mail.message` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | stored | `model mail.message` (mail) | `view BugFix-Stock.ported_primary_3243_form_x_material_request` |
| `message_is_follower` | Is Follower | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction` | Action Needed | boolean | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_needaction_counter` | Number of Actions | integer | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored |  |  |
| `message_partner_ids` | Followers (Partners) | many2many → `res.partner` | Standard chatter field (messages, followers, attachments) provided by Odoo’s mail thread mixin. | not stored | `model res.partner` (base) |  |
| `my_activity_date_deadline` | My Activity Deadline | date | Standard activity field: deadline of the current user’s next activity on the record. | not stored |  |  |
| `rating_ids` | Ratings | one2many → `rating.rating` | Standard customer-rating field provided by Odoo’s rating mixin. | stored | `model rating.rating` (rating) |  |
| `website_message_ids` | Website Messages | one2many → `mail.message` | Standard chatter field: messages shown on the website/portal for this record. | stored | `model mail.message` (mail) |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for material requests; defaults to active. | default `True`; stored |  | `default BugFix-Purchase.default_233_x_material_request_x_active` (BugFix-Purchase)<br>`view BugFix-Purchase.view_3244_default_search_view_for_x_material_request_e` (BugFix-Purchase)<br>`view BugFix-Stock.ported_primary_3243_form_x_material_request`<br>`view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| `x_name` | Request Reference | char | Material request reference number, generated by the 'Material Req Gen' action; used when creating purchase requests and confirming the request. | stored |  | `default BugFix-Purchase.default_382_x_material_request_x_name` (BugFix-Purchase)<br>`server action BugFix-Purchase.sa_f5_x_material_request_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1563_material_req_gen` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_1650_pr_create_for_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2388_confirm_mr` (BugFix-Purchase)<details><summary>+6 more</summary>`server action BugFix-Stock.server_action_1563_material_req_gen`<br>`server action BugFix-Stock.server_action_1650_pr_create_for_mr`<br>`server action BugFix-Stock.server_action_2388_confirm_mr`<br>`view BugFix-Purchase.view_3244_default_search_view_for_x_material_request_e` (BugFix-Purchase)<br>`view BugFix-Stock.ported_primary_3242_tree_x_material_request`<br>`view BugFix-Stock.ported_primary_3243_form_x_material_request`</details> |
| `x_studio_done` | Done | boolean | Computed flag that is True when all transfers created from the request are done/cancelled and no line has a transfer remainder; it also sets Status to 'Done' once. | computed by `_compute_done`; stored | `x_material_request._compute_done()` | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`x_material_request._compute_done()` |
| `x_studio_done_stage_updated` | Done Stage Updated | boolean | Flag set by the Done compute after it moves the request's Status to 'Done', so this happens only once. | stored |  | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`x_material_request._compute_done()` |
| `x_studio_journal_type` | Journal Type | many2one → `x_journal_types` | Journal type used when the 'Create Material Transfer' action builds the transfer. | stored | `model x_journal_types` (BugFix-Maintenance) | `server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_2406_create_material_transfer`<br>`view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| `x_studio_many2one_field_6f0Gc` | Department | many2one → `hr.department` | Department making the material request, entered on the request form. | stored | `model hr.department` (hr) | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| `x_studio_many2one_field_THFu6` | Maintenance Request No | many2one → `maintenance.request` | Maintenance request this material request relates to, entered on the request form. | stored | `model maintenance.request` (maintenance) | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| `x_studio_many2one_field_W3qKf` | Warehouse-1 | many2one → `stock.warehouse` | Warehouse link ('Warehouse-1'); not used by any view or logic. | stored | `model stock.warehouse` (stock) |  |
| `x_studio_new` | NEW | char | Text field 'NEW' with a default value; not shown in any view or used by logic. | stored |  | `default BugFix-Purchase.default_246_x_material_request_x_studio_new` (BugFix-Purchase) |
| `x_studio_notes` | Notes | char | Free-text notes on the material request form. | stored |  | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| `x_studio_one2many_field_9DTZS` | New One2many | one2many → `x_mr_config` | Unused second list of material request lines left from Studio; not shown in any view. | stored | `model x_mr_config` |  |
| `x_studio_request_lines` | Request Lines | one2many → `x_mr_config` | Lines (products and quantities) of the material request; used by the Done compute. | stored | `model x_mr_config` | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`x_material_request._compute_done()` |
| `x_studio_requested_by` | Requested by | many2one → `res.users` | User who raised the material request; shown on its form and list. | stored | `model res.users` (base) | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`view BugFix-Stock.ported_view_5300_odoo_studio_default_list_view_for_x_mate` |
| `x_studio_requested_date` | Requested Date | date | Date the material was requested. | stored |  | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| `x_studio_selection_field_BupKG` | Status | selection: Draft=Draft; Draft=Draft; Confirmed=Confirmed; Confirmed=Confirmed; To Be Approved=To Be Approved; To Be Approved=To Be Approved; Approved=Approved; Approved=Approved … | Material request status: Draft, Confirmed, To Be Approved, Approved or Rejected; changed by the reset, reject, request-approval and approve actions (the Done compute can also set 'Done'). | stored |  | `default BugFix-Purchase.default_381_x_material_request_x_studio_selection_field_BupKG` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2391_reset_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2400_reject_mr` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2441_request_approval_mr_update_status` (BugFix-Purchase)<br>`server action BugFix-Purchase.server_action_2444_approve_mr_status_update` (BugFix-Purchase)<details><summary>+9 more</summary>`server action BugFix-Stock.server_action_2391_reset_mr`<br>`server action BugFix-Stock.server_action_2400_reject_mr`<br>`server action BugFix-Stock.server_action_2441_request_approval_mr_update_status`<br>`server action BugFix-Stock.server_action_2444_approve_mr_status_update`<br>`view BugFix-Stock.ported_primary_3243_form_x_material_request`<br>`view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`view BugFix-Stock.ported_view_5300_odoo_studio_default_list_view_for_x_mate`<br>`x_material_request._compute_done()`<br>`x_mr_config.x_studio_status`</details> |
| `x_studio_selection_field_X1Bue` | Pipeline status bar | selection: status1=Create MR; status1=Create MR; status2=Create PR; status2=Create PR | Pipeline status bar value (Create MR / Create PR) with a default; not shown in any view or used by logic. | stored |  | `default BugFix-Purchase.default_245_x_material_request_x_studio_selection_field_X1Bue` (BugFix-Purchase) |
| `x_studio_sequence` | Sequence | integer | Ordering number for material requests (list drag handle). | stored |  | `default BugFix-Purchase.default_234_x_material_request_x_studio_sequence` (BugFix-Purchase)<br>`view BugFix-Stock.ported_primary_3242_tree_x_material_request` |
| `x_studio_test` | Test | char | Test text field; not used by any view or logic. | stored |  |  |
| `x_studio_type` | Type | selection: Local=Local; Local=Local; Import=Import; Import=Import | Request type: Local or Import; used when creating purchase requests from the material request. | stored |  | `server action BugFix-Purchase.server_action_1650_pr_create_for_mr` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_1650_pr_create_for_mr` |
| `x_studio_warehouse` | Warehouse | many2one → `stock.location` | Warehouse/stock location the material is requested from; used to create the material transfer and passed to the request lines. | stored | `model stock.location` (stock) | `server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<br>`server action BugFix-Stock.server_action_2406_create_material_transfer`<br>`view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`view BugFix-Stock.ported_view_5300_odoo_studio_default_list_view_for_x_mate`<br>`x_mr_config.x_studio_warehouse` |
| `x_x_studio_created_from_material_request_no_stock_picking_count` | Created from Material Request No count | integer | Computed number of transfers created from this material request; shown on its smart button. | computed by `_compute_related_stock_picking_count`; stored | `x_material_request._compute_related_stock_picking_count()` | `view BugFix-Stock.ported_primary_3243_form_x_material_request`<br>`view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate`<br>`x_material_request._compute_related_stock_picking_count()` |
| `x_x_studio_material_request_ref__x_pr_non_inventory_count` | Material Request ref count | integer | Computed number of non-inventory purchase requests referencing this material request. | computed by `_compute_related_x_pr_non_inventory_count`; stored | `x_material_request._compute_related_x_pr_non_inventory_count()` | `x_material_request._compute_related_x_pr_non_inventory_count()` |
| `x_x_studio_material_request_ref__x_purchase_request_count` | Material Request ref count | integer | Computed number of purchase requests referencing this material request. | computed by `_compute_related_x_purchase_request_count`; stored | `x_material_request._compute_related_x_purchase_request_count()` | `x_material_request._compute_related_x_purchase_request_count()` |

**Python methods (4):**

| Method | Function | Decorators | Extends standard | Depends on | Used by | Where |
|---|---|---|---|---|---|---|
| `_compute_done` | Compute for the Done flag of a Material Request: true when deliveries created from the request exist and are all done/cancelled and no request line has a transfer remainder. When it first becomes true it also sets the request status to 'Done' and marks Done Stage Updated. | api.depends('x_studio_done_stage_updated') |  | `model stock.picking` (stock)<br>`x_material_request.x_studio_done_stage_updated`<br>`x_material_request.x_studio_done`<br>`x_material_request.x_studio_request_lines`<br>`x_material_request.x_studio_selection_field_BupKG` | `x_material_request.x_studio_done` | `models/x_material_request.py:51` |
| `_compute_related_stock_picking_count` | Computes how many stock transfers (pickings) were created from this Material Request (via `x_studio_created_from_material_request_no`), for the smart-button counter; returns 0 if that picking field does not exist. |  |  | `model stock.picking` (stock)<br>`x_material_request.x_x_studio_created_from_material_request_no_stock_picking_count` | `x_material_request.x_x_studio_created_from_material_request_no_stock_picking_count` | `models/x_material_request.py:79` |
| `_compute_related_x_pr_non_inventory_count` | Computes the number of Non-Inventory Purchase Requests (`x_pr_non_inventory`) that reference this Material Request, for the related-records smart-button counter. |  |  | `model x_pr_non_inventory` (BugFix-Purchase)<br>`x_material_request.x_x_studio_material_request_ref__x_pr_non_inventory_count` | `x_material_request.x_x_studio_material_request_ref__x_pr_non_inventory_count` | `models/x_material_request.py:89` |
| `_compute_related_x_purchase_request_count` | Computes the number of Purchase Requests (`x_purchase_request`) that reference this Material Request, for the related-records smart-button counter. |  |  | `model x_purchase_request` (BugFix-Purchase)<br>`x_material_request.x_x_studio_material_request_ref__x_purchase_request_count` | `x_material_request.x_x_studio_material_request_ref__x_purchase_request_count` | `models/x_material_request.py:94` |

**Server actions (14):**

- **Approve MR** (`server_action_2397_approve_mr`, type `multi`)
  - Function: Runs two steps on the Material Request: set status to 'Approved' and schedule an approval-confirm To-Do activity; called by the Approve button.
  - Depends on: `model x_material_request`, `server action BugFix-Stock.server_action_2443_mr_request_approve_confirm_notify_user`, `server action BugFix-Stock.server_action_2444_approve_mr_status_update`
  - Used by: `view BugFix-Stock.ported_primary_3243_form_x_material_request`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Approve MR - Status Update** (`server_action_2444_approve_mr_status_update`, type `object_write`)
  - Function: Sets the Material Request status (`x_studio_selection_field_BupKG`) to 'Approved'; child step of Approve MR.
  - Depends on: `model x_material_request`, `x_material_request.x_studio_selection_field_BupKG`
  - Used by: `server action BugFix-Stock.server_action_2397_approve_mr`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Confirm MR** (`server_action_2388_confirm_mr`, type `code`)
  - Function: Checks the Material Request has lines and that every line quantity is above zero (errors otherwise), then sets status to 'Confirmed'; called by the Confirm button. Note: it searches lines by matching the M2O to the request name, not id.
  - Depends on: `model x_material_request`, `model x_mr_config`, `x_material_request.x_name`
  - Used by: `view BugFix-Stock.ported_primary_3243_form_x_material_request`
  <details><summary>code (10 lines)</summary>

```python
if record.x_name:
  null_Mr_lines = env['x_mr_config'].search([('x_studio_many2one_field_6yqbk', '=', record.x_name)])
  if not null_Mr_lines:
   raise UserError("Valid MR Lines Should Exists to Confirm!")
   
  invalid_mr_lines = env['x_mr_config'].search([('x_studio_many2one_field_6yqbk', '=', record.x_name), ('x_studio_quantity', '<=', 0)])
  if invalid_mr_lines:
    raise UserError("Quantity of Individual MR Lines Should be Greater than Zero!")
    
record.write({'x_studio_selection_field_BupKG': 'Confirmed'})
```
  </details>
- **Create Material Transfer** (`server_action_2406_create_material_transfer`, type `code`)
  - Function: Creates an outgoing transfer from the request's warehouse to 'Virtual Locations/MJ' with moves for each line having quantity left to transfer, updates transferred quantities, and opens the new transfer; errors if no valid lines, location or operation type.
  - Depends on: `model stock.location` (stock), `model stock.move.line` (stock), `model stock.move` (stock), `model stock.picking.type` (stock), `model stock.picking` (stock)<details><summary>+4 more</summary>`model x_material_request`, `model x_mr_config`, `x_material_request.x_studio_journal_type`, `x_material_request.x_studio_warehouse`</details>
  - Used by: `view BugFix-Stock.ported_primary_3243_form_x_material_request`
  <details><summary>code (71 lines)</summary>

```python
valid_req_lines = env['x_mr_config'].search([('x_studio_many2one_field_6yqbk', '=', record.id),('x_studio_transfer_remainder', '>', 0)],limit=1)

if not valid_req_lines:

  raise UserError('There are no valid item lines to transfer.')

  

dest_loc = env['stock.location'].search([('usage', '=', 'inventory'),('complete_name', '=', 'Virtual Locations/MJ')],limit=1)

if dest_loc:

  opt_type = env['stock.picking.type'].search([('default_location_src_id', '=', record.x_studio_warehouse.id),('default_location_dest_id', '=', dest_loc.id),('code', '=', 'outgoing')],limit=1)

  if opt_type:

    prod_move = env['stock.picking'].create({'x_studio_created_from_material_request_no':record.id,'picking_type_id':opt_type.id,'location_id':record.x_studio_warehouse.id,'location_dest_id':dest_loc.id,'x_studio_journal_type':record.x_studio_journal_type.id})

     

    update_prod_move = env['stock.picking'].search([('id', '=', prod_move.id)],limit=1)

    if update_prod_move:

      valid_req_lines_2 = env['x_mr_config'].search([('x_studio_many2one_field_6yqbk', '=', record.id),('x_studio_transfer_remainder', '>', 0)])

      if valid_req_lines_2:

        for valid_lines in valid_req_lines_2: 

          stock_move = env['stock.move'].create({'picking_id':update_prod_move.id,'name':('New Move:'+valid_lines.x_studio_product.name),'reference':update_prod_move.name,'picking_type_id':update_prod_move.picking_type_id.id,'product_id':valid_lines.x_studio_product.id,'location_id':update_prod_move.location_id.id,'location_dest_id':update_prod_move.location_dest_id.id,'product_uom_qty':valid_lines.x_studio_qty_to_transfer,'product_uom':valid_lines.x_studio_product.uom_id.id,'state':'draft'}) 

          stock_move_line = env['stock.move.line'].create({'move_id':stock_move.id,'picking_id':update_prod_move.id,'picking_type_id':update_prod_move.picking_type_id.id,'product_id':valid_lines.x_studio_product.id,'product_uom_id':valid_lines.x_studio_product.uom_id.id,'location_id':update_prod_move.location_id.id,'location_dest_id':update_prod_move.location_dest_id.id,'qty_done':valid_lines.x_studio_qty_to_transfer}) 



          #cal = 0

          #if valid_lines.x_studio_available_qty_to_transfer

          #cal = 

          valid_lines.write({'x_studio_qty_transfered': (valid_lines.x_studio_qty_transfered + valid_lines.x_studio_qty_to_transfer), 'x_studio_qty_to_transfer': 0}) #valid_lines.x_studio_available_qty_to_transfer 

    action = {

              'name': 'RFQ',

              'domain': [('id', '=', prod_move.id)],

              'type': 'ir.actions.act_window',

              'res_model': 'stock.picking',

              'view_mode': 'tree,form',

              'view_type': 'form',

              'view_id': False,

              'context': False,

              } 

  else:

    raise UserError('There is no valid operation type has been setup.')  

else:

  raise UserError('There is no valid Location has been setup.')
```
  </details>
- **Execute Code** (`server_action_2410_mr_validate_delete`, type `code`)
  - Function: Blocks deletion of a Material Request whose status is not Draft with an error; run by the MR Validate Delete automation.
  - Depends on: `model x_material_request`
  - Used by: `automation BugFix-Stock.base_automation_230_mr_validate_delete`
  <details><summary>code (2 lines)</summary>

```python
if record.x_studio_selection_field_BupKG != 'Draft':
  raise UserError('Processed material request can not be deleted.')
```
  </details>
- **Execute Code** (`server_action_1563_material_req_gen`, type `code`)
  - Function: Assigns the next number from sequence `mtrl.req.seq` as the Material Request name; run by the Material Req GEN automation.
  - Depends on: `model ir.sequence` (base), `model x_material_request`, `x_material_request.x_name`
  - Used by: `automation BugFix-Stock.base_automation_95_material_req_gen`
  <details><summary>code (1 lines)</summary>

```python
record['x_name'] =env['ir.sequence'].next_by_code('mtrl.req.seq')
```
  </details>
- **MR Request Approval - Notify User** (`server_action_2440_mr_request_approval_notify_user`, type `next_activity`)
  - Function: Schedules a To-Do activity (summary 'Approve RUG Repair') on the Material Request for a specific user; child step of Request Approval MR. No assignee is set in the repo and the summary looks copied from a repair flow.
  - Depends on: `model x_material_request`
  - Used by: `server action BugFix-Stock.server_action_2394_request_approval_mr`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **MR Request Approve Confirm - Notify User** (`server_action_2443_mr_request_approve_confirm_notify_user`, type `next_activity`)
  - Function: Schedules a generic To-Do activity (summary 'Approve RUG Repair') on the Material Request; child step of Approve MR. The summary text looks copied from a repair flow.
  - Depends on: `model x_material_request`
  - Used by: `server action BugFix-Stock.server_action_2397_approve_mr`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **PR create For MR** (`server_action_1650_pr_create_for_mr`, type `code`)
  - Function: Creates a Purchase Request linked to the Material Request (MR number, reference, type) with one line per request line (product, quantity). Not referenced by any view or automation in this repo.
  - Depends on: `model x_material_request`, `model x_purchase_request` (BugFix-Purchase), `x_material_request.x_name`, `x_material_request.x_studio_type`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (7 lines)</summary>

```python
pr_lines=[]

for pr_line in record.x_studio_one2many_field_9DTZS:

  pr_lines.append([0,0,{'x_studio_many2one_field_WAqP4':pr_line.x_studio_many2one_field_2LV9q.id,'x_studio_quantity':pr_line.x_studio_qty}])

env['x_purchase_request'].create({'x_studio_mr_number':record.x_name,'x_studio_material_request_ref':record.id,'x_studio_type':record.x_studio_type, 'x_studio_order_lines_1':pr_lines})
```
  </details>
- **PR-non create For MR** (`server_action_1652_pr_non_create_for_mr`, type `code`)
  - Function: Creates an empty non-inventory Purchase Request linked to the Material Request. Not referenced by any view or automation in this repo.
  - Depends on: `model x_material_request`, `model x_pr_non_inventory` (BugFix-Purchase)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
prn_lines=[]
env['x_pr_non_inventory'].create({'x_studio_material_request_ref':record.id, 'x_studio_one2many_field_rSJtb':prn_lines})
```
  </details>
- **Reject MR** (`server_action_2400_reject_mr`, type `object_write`)
  - Function: Sets the Material Request status to 'Rejected'; called by the Reject button on the Material Request form.
  - Depends on: `model x_material_request`, `x_material_request.x_studio_selection_field_BupKG`
  - Used by: `view BugFix-Stock.ported_primary_3243_form_x_material_request`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Request Approval MR** (`server_action_2394_request_approval_mr`, type `multi`)
  - Function: Runs two steps on the Material Request: schedule an approval To-Do activity and set status to 'To Be Approved'; called by the Request Approval button.
  - Depends on: `model x_material_request`, `server action BugFix-Stock.server_action_2440_mr_request_approval_notify_user`, `server action BugFix-Stock.server_action_2441_request_approval_mr_update_status`
  - Used by: `view BugFix-Stock.ported_primary_3243_form_x_material_request`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Request Approval MR - Update Status** (`server_action_2441_request_approval_mr_update_status`, type `object_write`)
  - Function: Sets the Material Request status to 'To Be Approved'; child step of Request Approval MR.
  - Depends on: `model x_material_request`, `x_material_request.x_studio_selection_field_BupKG`
  - Used by: `server action BugFix-Stock.server_action_2394_request_approval_mr`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
- **Reset MR** (`server_action_2391_reset_mr`, type `object_write`)
  - Function: Sets the Material Request status back to 'Draft'; called by the Reset button on the Material Request form.
  - Depends on: `model x_material_request`, `x_material_request.x_studio_selection_field_BupKG`
  - Used by: `view BugFix-Stock.ported_primary_3243_form_x_material_request`
  <details><summary>code (12 lines)</summary>

```python
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| MR Validate Delete | `base_automation_230_mr_validate_delete` |  | When a record is deleted on Material Request, runs _Execute Code_. | `model x_material_request`<br>`server action BugFix-Stock.server_action_2410_mr_validate_delete` |  |
| Material Req GEN | `base_automation_95_material_req_gen` |  | When a record is created or updated on Material Request, runs _Execute Code_. | `model x_material_request`<br>`server action BugFix-Stock.server_action_1563_material_req_gen`<br>`x_material_request.create_date` |  |

**Window actions (4):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request | `act_window_1562_material_request` | Opens **Material Request** records (tree,form). | `model x_material_request` | `menu BugFix-Stock.menu_828_material_request`<br>`menu BugFix-Studio-Misc.menu_f6_material_request` (BugFix-Studio-Misc) |
| Material Requests | `act_window_1647_material_requests` | Opens **Material Request** records (tree,form), filtered to `[('x_studio_many2one_field_THFu6', '=', active_id)]`. | `model x_material_request` |  |
| Material Requests | `act_window_1648_material_requests` | Opens **Material Request** records (tree,form), filtered to `[('x_studio_many2one_field_THFu6', '=', active_id)]`. | `model x_material_request` |  |
| x_material_request | `act_window_2810_x_material_request` | Opens **Material Request** records (tree,form). | `model x_material_request` | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_x_material_request` (BugFix-Studio-Misc) |

**Views (4):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_material_request | `ported_primary_3243_form_x_material_request` | form | full form layout with 7 fields | Material Request form with status-driven buttons Reset, Confirm, Request approval, Approve, Reject and Create Transfer (Reset/Reject hidden once transfers exist), 'Request Reference' title and chatter. Buttons use hardcoded action ids (2014-2037). | `server action BugFix-Stock.server_action_2388_confirm_mr`<br>`server action BugFix-Stock.server_action_2391_reset_mr`<br>`server action BugFix-Stock.server_action_2394_request_approval_mr`<br>`server action BugFix-Stock.server_action_2397_approve_mr`<br>`server action BugFix-Stock.server_action_2400_reject_mr`<details><summary>+8 more</summary>`server action BugFix-Stock.server_action_2406_create_material_transfer`<br>`x_material_request.activity_ids`<br>`x_material_request.message_follower_ids`<br>`x_material_request.message_ids`<br>`x_material_request.x_active`<br>`x_material_request.x_name`<br>`x_material_request.x_studio_selection_field_BupKG`<br>`x_material_request.x_x_studio_created_from_material_request_no_stock_picking_count`</details> | `view BugFix-Stock.ported_view_3245_odoo_studio_default_form_view_for_x_mate` |
| Default list view for x_material_request | `ported_primary_3242_tree_x_material_request` | tree | full tree layout with 2 fields | Base list view of Material Requests showing a drag handle (sequence) and the name. | `x_material_request.x_name`<br>`x_material_request.x_studio_sequence` | `view BugFix-Stock.ported_view_5300_odoo_studio_default_list_view_for_x_mate` |
| Odoo Studio: Default form view for x_material_request customization | `ported_view_3245_odoo_studio_default_form_view_for_x_mate` | form | inside `//sheet`: add field x_studio_selection_field_BupKG, field x_x_studio_created_from_material_request_no_stock_picking_count; after `//button[@name='2014']`: add field x_studio_selection_field_BupKG; before `//form[1]/sheet[1]/widget[@name='web_ribbon']`: add div; set force_save=True, readonly=1, required= on `//field[@name='x_name']`; inside `//group[@name='studio_group_8ed6cf_left']`: add field x_studio_warehouse, field x_studio_many2one_field_6f0Gc, field x_studio_notes, field x_studio_requested_date; inside `//group[@name='studio_group_8ed6cf_right']`: add field x_studio_many2one_field_THFu6, field x_studio_journal_type, field create_uid, field create_date, field x_studio_requested_by, field x_studio_done_stage_updated, field x_studio_done; after `//group[@name='studio_group_8ed6cf']`: add notebook | Customizes the Material Request form: status bar, Transfers smart button, read-only reference, warehouse, requested date/by and notes (editable only in Draft), maintenance request no, journal type, done flags, and a lines notebook. | `view BugFix-Stock.ported_primary_3243_form_x_material_request`<br>`window action BugFix-Stock.action_2409_transfers`<br>`x_material_request.x_active`<br>`x_material_request.x_studio_done_stage_updated`<br>`x_material_request.x_studio_done`<details><summary>+27 more</summary>`x_material_request.x_studio_journal_type`<br>`x_material_request.x_studio_many2one_field_6f0Gc`<br>`x_material_request.x_studio_many2one_field_THFu6`<br>`x_material_request.x_studio_notes`<br>`x_material_request.x_studio_request_lines`<br>`x_material_request.x_studio_requested_by`<br>`x_material_request.x_studio_requested_date`<br>`x_material_request.x_studio_selection_field_BupKG`<br>`x_material_request.x_studio_warehouse`<br>`x_material_request.x_x_studio_created_from_material_request_no_stock_picking_count`<br>`x_mr_config.x_active`<br>`x_mr_config.x_name`<br>`x_mr_config.x_studio_available_qty_to_transfer`<br>`x_mr_config.x_studio_description_1`<br>`x_mr_config.x_studio_many2one_field_6yqbk`<br>`x_mr_config.x_studio_on_hand_qty_2`<br>`x_mr_config.x_studio_product`<br>`x_mr_config.x_studio_qty_to_transfer`<br>`x_mr_config.x_studio_qty_transfered`<br>`x_mr_config.x_studio_quantity`<br>`x_mr_config.x_studio_requested_by`<br>`x_mr_config.x_studio_sequence`<br>`x_mr_config.x_studio_status`<br>`x_mr_config.x_studio_text_1`<br>`x_mr_config.x_studio_transfer_remainder`<br>`x_mr_config.x_studio_uom_2`<br>`x_mr_config.x_studio_warehouse`</details> |  |
| Odoo Studio: Default list view for x_material_request customization | `ported_view_5300_odoo_studio_default_list_view_for_x_mate` | tree | set create=true, delete=true, edit=true on `//tree[1]`; set string=Request Reference on `//field[@name='x_name']`; after `//field[@name='x_name']`: add field x_studio_warehouse, field x_studio_requested_by, field create_uid, field create_date, field x_studio_selection_field_BupKG | Customizes the Material Request list: allows create/edit/delete, labels name 'Request Reference' and adds warehouse, requested by, creator, created on and status columns. | `view BugFix-Stock.ported_primary_3242_tree_x_material_request`<br>`x_material_request.x_studio_requested_by`<br>`x_material_request.x_studio_selection_field_BupKG`<br>`x_material_request.x_studio_warehouse` |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_material_request user access | `access_x_material_request_user` | Gives **User types / Internal User** read/write/create/delete access to Material Request records. | `group base.group_user` (base)<br>`model x_material_request` |  |
