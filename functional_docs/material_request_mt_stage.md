# BugFix-Stock — `material_request_mt_stage`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `material_request_mt_stage` — Material Request MT Stages

*Created by this repo.* Python: `models/material_request_mt_stage.py`, `models/x_material_request_mt_stage_gap.py`. Record name field: `name`.

**Summary:**

<!-- SUMMARY:model:material_request_mt_stage -->
A stage of the Material Request MT kanban app, with a name and a sequence for ordering. Users maintain stages under Material Management Module, Configuration.
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
| `name` | Stage Name | char | Name of the material request kanban stage. | stored; required |  | `view BugFix-Stock.view_material_request_mt_stage_list`<br>`view BugFix-Stock.view_material_request_mt_stage_form`<br>`view BugFix-Stock.view_material_request_mt_stage_search` |
| `sequence` | Sequence | integer | Integer sort order of a Material Request MT stage; entered by the user and shown in the stage list view to order the stages. | stored |  | `view BugFix-Stock.view_material_request_mt_stage_list` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request MT Stages | `action_material_request_mt_stages` | Opens **Material Request MT Stages** records (tree,form). | `model material_request_mt_stage` | `menu BugFix-Stock.menu_material_request_mt_stages_2`<br>`menu BugFix-Stock.menu_material_request_mt_stages` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for material_request_mt_stage | `view_material_request_mt_stage_form` | form | full form layout with 1 fields | Form for a Material Request (MT) stage: just the stage name. | `material_request_mt_stage.name` |  |
| Default list view for material_request_mt_stage | `view_material_request_mt_stage_list` | tree | full tree layout with 2 fields | Inline-editable, reorderable list of Material Request (MT) stages. | `material_request_mt_stage.name`<br>`material_request_mt_stage.sequence` |  |
| Default search view for material_request_mt_stage | `view_material_request_mt_stage_search` | search | full search layout with 1 fields | Search Material Request (MT) stages by name. | `material_request_mt_stage.name` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request MT Stages group_system | `access_material_request_mt_stages_group_system` | Gives **Administration / Settings** read/write/create/delete access to Material Request MT Stages records. | `group base.group_system` (base)<br>`model material_request_mt_stage` |  |
| Material Request MT Stages group_user | `access_material_request_mt_stages_group_user` | Gives **User types / Internal User** read/write/create access to Material Request MT Stages records. | `group base.group_user` (base)<br>`model material_request_mt_stage` |  |
