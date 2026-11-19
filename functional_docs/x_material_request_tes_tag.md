# BugFix-Stock — `x_material_request_tes_tag`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_material_request_tes_tag` — Material Request Test Tags

*Created by this repo.* Python: `models/x_material_request_tes_tag.py`, `models/x_material_request_tes_tag_gap.py`. Record name field: `x_name`.

**Summary:**

<!-- SUMMARY:model:x_material_request_tes_tag -->
A tag for the Material Request Test app, with a name and a colour. Purpose not evident from code beyond serving that app.
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
| `x_color` | Color | integer | Color index of a Material Request Test tag, used to color the tag badge; shown in the tag list view. | stored |  | `view BugFix-Stock.view_8723_default_list_view_for_x_material_request_tes_tag_e` |
| `x_name` | Name | char | Name of a Material Request Test tag, entered by the user; shown in the tag list, form and search views. | stored; required |  | `view BugFix-Stock.view_8723_default_list_view_for_x_material_request_tes_tag_e`<br>`view BugFix-Stock.view_8724_default_form_view_for_x_material_request_tes_tag_e`<br>`view BugFix-Stock.view_8725_default_search_view_for_x_material_request_tes_tag_e` |

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test Tags | `act_window_3376_material_request_test_tags` | Opens **Material Request Test Tags** records (tree,form). | `model x_material_request_tes_tag` | `menu BugFix-Stock.menu_f6_material_request_test_tags` |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Default form view for x_material_request_tes_tag | `view_8724_default_form_view_for_x_material_request_tes_tag_e` | form | full form layout with 1 fields | Form for a Material Request Test tag: just the tag name. | `x_material_request_tes_tag.x_name` |  |
| Default list view for x_material_request_tes_tag | `view_8723_default_list_view_for_x_material_request_tes_tag_e` | tree | full tree layout with 2 fields | Inline-editable list of Material Request Test tags with name and color. | `x_material_request_tes_tag.x_color`<br>`x_material_request_tes_tag.x_name` |  |
| Default search view for x_material_request_tes_tag | `view_8725_default_search_view_for_x_material_request_tes_tag_e` | search | full search layout with 1 fields | Search Material Request Test tags by name. | `x_material_request_tes_tag.x_name` |  |

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Material Request Test Tags group_system | `access_8273_material_request_test_tags_group_system` | Gives **Administration / Settings** read/write/create/delete access to Material Request Test Tags records. | `group base.group_system` (base)<br>`model x_material_request_tes_tag` |  |
| Material Request Test Tags group_user | `access_8274_material_request_test_tags_group_user` | Gives **User types / Internal User** read/write/create access to Material Request Test Tags records. | `group base.group_user` (base)<br>`model x_material_request_tes_tag` |  |
