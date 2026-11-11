# BugFix-Stock — `journal_types`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `journal_types` — Journal Types

*Extends a model created by `BugFix-Maintenance`.* Python: `models/journal_types.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Accounting.access_journal_types_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_journal_types_group_user` (BugFix-Accounting)<br>`automation BugFix-Accounting.automation_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`maintenance.equipment.category.journal_type` (BugFix-Maintenance)<br>`maintenance.request.journal_type_1` (BugFix-Maintenance)<br>`record rule BugFix-Accounting.rule_jin_multi_company_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_journal_types_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_jin_company_id_in_journal_types` (BugFix-Accounting)<details><summary>+1 more</summary>`window action BugFix-Accounting.action_journal_types` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:journal_types -->
This repo adds fields to Journal Types (a model created by BugFix-Maintenance): name, description, company, sequence, archive flag and an Offset Account. Movement journal transfers and material requests pick a journal type, and its offset account is used when the transfer's entries are updated.
<!-- /SUMMARY -->

**Fields (12):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Accounting.automation_jin_company_id_in_journal_types` (BugFix-Accounting) |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag for Journal Types; inactive records are hidden and show an Archived ribbon. Defaults to active. | stored |  | `default BugFix-Accounting.default_journal_types_active` (BugFix-Accounting)<br>`view BugFix-Accounting.view_journal_types_form` (BugFix-Accounting)<br>`view BugFix-Accounting.view_journal_types_search` (BugFix-Accounting) |
| `name` | Journal Type | char | Name of the journal type (e.g. a movement journal category), entered by the user; shown in the list, form and search views. | stored; required |  | `view BugFix-Accounting.view_journal_types_list` (BugFix-Accounting)<br>`view BugFix-Accounting.view_journal_types_form` (BugFix-Accounting)<br>`view BugFix-Accounting.view_journal_types_search` (BugFix-Accounting) |
| `accounting_company_id` | Company | many2one → `res.company` | Company that owns the journal type; set automatically to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_jin_multi_company_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_journal_types_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_jin_company_id_in_journal_types` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_journal_types_inherit` (BugFix-Accounting) |
| `description` | Description | char | Free-text description of the journal type, entered on its form. | stored |  | `view BugFix-Accounting.view_default_list_view_for_journal_types_inherit` (BugFix-Accounting) |
| `offset_account` | Offset Account | many2one → `account.account` | G/L offset account linked to this journal type; picked up when movement journals update the offset account on transfers. | stored | `model account.account` (account) | `view BugFix-Accounting.view_default_list_view_for_journal_types_inherit` (BugFix-Accounting) |
| `sequence` | Sequence | integer | Ordering number for journal types (drag handle in the list view). | stored |  | `default BugFix-Accounting.default_journal_types_sequence` (BugFix-Accounting)<br>`view BugFix-Accounting.view_journal_types_list` (BugFix-Accounting) |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| journal_types user access | `access_journal_types_user` | Gives **User types / Internal User** read/write/create/delete access to Journal Types records. | `group base.group_user` (base)<br>`model journal_types` (BugFix-Maintenance) |  |
