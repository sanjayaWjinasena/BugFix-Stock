# BugFix-Stock — `x_journal_types`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_journal_types` — Journal Types

*Extends a model created by `BugFix-Maintenance`.* Python: `models/x_journal_types.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Accounting.access_5950_journal_types_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_5951_journal_types_group_user` (BugFix-Accounting)<br>`automation BugFix-Accounting.base_automation_337_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`maintenance.equipment.category.x_studio_journal_type` (BugFix-Maintenance)<br>`maintenance.request.x_studio_journal_type_1` (BugFix-Maintenance)<br>`record rule BugFix-Accounting.rule_629_jin_multi_company_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_journal_types_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2871_jin_company_id_in_journal_types` (BugFix-Accounting)<details><summary>+1 more</summary>`window action BugFix-Accounting.action_2447_journal_types` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:x_journal_types -->
This repo adds fields to Journal Types (a model created by BugFix-Maintenance): name, description, company, sequence, archive flag and an Offset Account. Movement journal transfers and material requests pick a journal type, and its offset account is used when the transfer's entries are updated.
<!-- /SUMMARY -->

**Fields (12):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Accounting.base_automation_337_jin_company_id_in_journal_types` (BugFix-Accounting) |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for Journal Types; inactive records are hidden and show an Archived ribbon. Defaults to active. | stored |  | `default BugFix-Accounting.default_390_x_journal_types_x_active` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_5322_default_search_view_d3c181ad_9bc3_4cfc_9d60_2500bd38fe9f` (BugFix-Accounting) |
| `x_name` | Journal Type | char | Name of the journal type (e.g. a movement journal category), entered by the user; shown in the list, form and search views. | stored; required |  | `view BugFix-Accounting.ported_view_5320_default_list_view_fo_02152264_7fd7_4b5e_8a84_ca3714db9fad` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_5321_default_form_view_fo_dbddc8a1_ea9d_47ba_8335_c08e4a53fc5c` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_5322_default_search_view_d3c181ad_9bc3_4cfc_9d60_2500bd38fe9f` (BugFix-Accounting) |
| `x_studio_company_id` | Company | many2one → `res.company` | Company that owns the journal type; set automatically to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_629_jin_multi_company_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.sa_f5_x_journal_types_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2871_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` (BugFix-Accounting) |
| `x_studio_description` | Description | char | Free-text description of the journal type, entered on its form. | stored |  | `view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` (BugFix-Accounting) |
| `x_studio_offset_account` | Offset Account | many2one → `account.account` | G/L offset account linked to this journal type; picked up when movement journals update the offset account on transfers. | stored | `model account.account` (account) | `view BugFix-Accounting.ported_view_5326_odoo_studio_default_7879380a_9ecc_4ca6_bfd3_fa82b991c3ce` (BugFix-Accounting) |
| `x_studio_sequence` | Sequence | integer | Ordering number for journal types (drag handle in the list view). | stored |  | `default BugFix-Accounting.default_391_x_journal_types_x_studio_sequence` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_5320_default_list_view_fo_02152264_7fd7_4b5e_8a84_ca3714db9fad` (BugFix-Accounting) |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_journal_types user access | `access_x_journal_types_user` | Gives **User types / Internal User** read/write/create/delete access to Journal Types records. | `group base.group_user` (base)<br>`model x_journal_types` (BugFix-Maintenance) |  |
