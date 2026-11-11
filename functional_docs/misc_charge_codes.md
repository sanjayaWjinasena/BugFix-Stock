# BugFix-Stock — `misc_charge_codes`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `misc_charge_codes` — Misc Charge Codes

*Created by this repo.* Python: `models/misc_charge_codes.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Accounting.access_misc_charge_codes_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_misc_charge_codes_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_misc_charge_codes_user` (BugFix-Accounting)<br>`access right BugFix-Purchase.access_misc_charge_codes_user` (BugFix-Purchase)<br>`account.move.line.tags` (BugFix-Accounting)<br>`automation BugFix-Accounting.automation_jin_company_id_in_misc_charge_codes` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_jin_multi_company_misc_charge_codes` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_misc_charge_codes_jin_company_id_in_misc_charge_codes` (BugFix-Accounting)<details><summary>+17 more</summary>`server action BugFix-Accounting.action_imp_validate_debit_acc_type` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_jin_company_id_in_misc_charge_codes` (BugFix-Accounting)<br>`server action BugFix-Purchase.action_tariff_date_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_trf_charges_imp_create_charges_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_trf_taxes_imp_create_taxes_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_charges_for_tariff_dates` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_charges_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_duties_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_taxes_in_misc_charge_codes` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_copy_charges_to_structure_details` (BugFix-Purchase)<br>`server action BugFix-Purchase.action_imp_create_duties_in_misc_charge_codes_2` (BugFix-Purchase)<br>`server action BugFix-Sales.action_imp_copy_charges_to_delivery_terms` (BugFix-Sales)<br>`window action BugFix-Accounting.action_misc_charge_codes` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_misc_charge_codes_2` (BugFix-Accounting)<br>`structure_details.misc_charge_line_id` (BugFix-Purchase)<br>`tariff_rates.misc_charge_line_id` (BugFix-Purchase)<br>`x_test02.x_studio_many2many_field_JKvVx` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:misc_charge_codes -->
A Misc Charge Code defines a charge, duty or tax used in imports, with its charge group, description, debit and credit accounts and whether the cost loads onto the item or a G/L account. Delivery Terms copy their charges from the codes in the Charges group, and consignment lines link to charge codes for their totals. A Validate Debit Acc Type action outside this repo checks the debit account.
<!-- /SUMMARY -->

**Fields (17):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Accounting.automation_jin_company_id_in_misc_charge_codes` (BugFix-Accounting) |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag for misc charge codes; defaults to active. | stored |  | `default BugFix-Accounting.default_misc_charge_codes_active` (BugFix-Accounting)<br>`default BugFix-Studio-Misc.default_misc_charge_codes_accounting_active` (BugFix-Studio-Misc)<br>`view BugFix-Accounting.view_misc_charge_codes_form` (BugFix-Accounting)<br>`view BugFix-Accounting.view_misc_charge_codes_search` (BugFix-Accounting) |
| `name` | Misc. Charge Code | char | The misc charge code itself, shown in the list, form and search. | stored |  | `view BugFix-Accounting.view_misc_charge_codes_list` (BugFix-Accounting)<br>`view BugFix-Accounting.view_misc_charge_codes_form` (BugFix-Accounting)<br>`view BugFix-Accounting.view_misc_charge_codes_search` (BugFix-Accounting) |
| `charge_group` | Charge Group | selection: None=None; None=None; Charges=Charges; Charges=Charges; Duty=Duty; Duty=Duty; Taxes=Taxes; Taxes=Taxes | Group of the charge code: None, Charges, Duty or Taxes. | stored |  | `view BugFix-Accounting.view_default_form_view_for_misc_charge_codes_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `accounting_company_id` | Company | many2one → `res.company` | Company of the charge code; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_jin_multi_company_misc_charge_codes` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_misc_charge_codes_jin_company_id_in_misc_charge_codes` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_jin_company_id_in_misc_charge_codes` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `credit_acc_type` | Credit Acc. Type | selection: Item=Item; Item=Item; G/L Account=G/L Account; G/L Account=G/L Account | Type of the credit side: Item or G/L Account. | stored |  | `view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `credit_account` | Credit Account | many2one → `account.account` | G/L account credited for this charge code. | stored | `model account.account` (account) | `view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `debit_acc_type` | Cost Load Type | selection: Item=Item; Item=Item; G/L Account=G/L Account; G/L Account=G/L Account | Cost load type of the debit side: Item (loaded onto product cost) or G/L Account; validated by the 'Validate Debit Acc Type' action. | stored |  | `server action BugFix-Accounting.action_imp_validate_debit_acc_type` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_form_view_for_misc_charge_codes_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `debit_account` | Debit Account | many2one → `account.account` | G/L account debited for this charge code; checked by the 'Validate Debit Acc Type' action. | stored | `model account.account` (account) | `server action BugFix-Accounting.action_imp_validate_debit_acc_type` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `description` | Description | char | Description of the charge code. | stored |  | `view BugFix-Accounting.view_default_form_view_for_misc_charge_codes_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |
| `sequence` | Sequence | integer | Ordering number for charge codes (list drag handle). | stored |  | `default BugFix-Accounting.default_misc_charge_codes_sequence` (BugFix-Accounting)<br>`default BugFix-Studio-Misc.default_misc_charge_codes_sequence` (BugFix-Studio-Misc)<br>`view BugFix-Accounting.view_misc_charge_codes_list` (BugFix-Accounting) |
| `system_entry` | System Entry | boolean | Flag marking the charge code as a system entry; shown on the form. | stored |  | `view BugFix-Accounting.view_default_list_view_for_misc_charge_codes_inherit` (BugFix-Accounting) |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| misc_charge_codes user access | `access_misc_charge_codes_user` | Gives **User types / Internal User** read/write/create/delete access to Misc Charge Codes records. | `group base.group_user` (base)<br>`model misc_charge_codes` |  |
