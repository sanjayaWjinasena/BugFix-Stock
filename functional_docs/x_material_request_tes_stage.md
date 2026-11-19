# BugFix-Stock — `x_material_request_tes_stage`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request_tes_stage` — Material Request Test Stages

*Created by this repo.* Python: `models/x_material_request_tes_stage.py`, `models/x_material_request_tes_stage_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_material_request_tes_stage -->
A stage of the Material Request Test app, with a name and a sequence for ordering. Purpose not evident from code beyond serving that app.
<!-- /SUMMARY -->

**Fields (8):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  |  |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_name` | Stage Name | char | Name of a Material Request Test stage, entered by the user; shown in the stage list, form and search views. | stored; required |  | `view BugFix-Stock.view_8720_default_list_view_for_x_material_request_tes_stage_e`<br>`view BugFix-Stock.view_8721_default_form_view_for_x_material_request_tes_stage_e`<br>`view BugFix-Stock.view_8722_default_search_view_for_x_material_request_tes_stage_e` |
| `x_studio_sequence` | Sequence | integer | Integer sort order of a Material Request Test stage; entered by the user and shown in the stage list view. | stored |  | `view BugFix-Stock.view_8720_default_list_view_for_x_material_request_tes_stage_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test Stages | `act_window_3375_material_request_test_stages` | Opens **Material Request Test Stages** records (tree,form). | `model x_material_request_tes_stage` | `menu BugFix-Stock.menu_f6_material_request_test_stages` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_material_request_tes_stage | `view_8721_default_form_view_for_x_material_request_tes_stage_e` | form | full form layout with 1 fields | Form for a Material Request Test stage: just the stage name. | `x_material_request_tes_stage.x_name` |  |
| Default list view for x_material_request_tes_stage | `view_8720_default_list_view_for_x_material_request_tes_stage_e` | tree | full tree layout with 2 fields | Inline-editable, reorderable list of Material Request Test stages. | `x_material_request_tes_stage.x_name`<br>`x_material_request_tes_stage.x_studio_sequence` |  |
| Default search view for x_material_request_tes_stage | `view_8722_default_search_view_for_x_material_request_tes_stage_e` | search | full search layout with 1 fields | Search Material Request Test stages by name. | `x_material_request_tes_stage.x_name` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test Stages group_system | `access_8271_material_request_test_stages_group_system` | Gives **Administration / Settings** read/write/create/delete access to Material Request Test Stages records. | `group base.group_system` (base)<br>`model x_material_request_tes_stage` |  |
| Material Request Test Stages group_user | `access_8272_material_request_test_stages_group_user` | Gives **User types / Internal User** read/write/create access to Material Request Test Stages records. | `group base.group_user` (base)<br>`model x_material_request_tes_stage` |  |
