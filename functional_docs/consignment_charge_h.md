# BugFix-Stock — `consignment_charge_h`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `consignment_charge_h` — Consignment Charge Header

*Created by this repo.* Python: `models/consignment_charge_h.py`. Record name field: `name`.

Other repos that use this model: `access right BugFix-Accounting.access_consignment_charge_header_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_consignment_charge_header_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_consignment_charge_h_user` (BugFix-Accounting)<br>`access right BugFix-Studio-Misc.access_g_consignment_charge_h_consignment_charge_h_purchase_jin_po_invoicing_payment_i` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_consignment_charge_h_consignment_charge_h_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)<br>`automation BugFix-Accounting.automation_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_jin_multi_company_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<details><summary>+10 more</summary>`server action BugFix-Accounting.action_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`window action BugFix-Accounting.action_consignment_charge_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_header_charges` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_consignment_charge_header_2` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_consignment_charge_header_3` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_purchase_invoices` (BugFix-Accounting)<br>`temp_tp_invoice_line.consignment_charge_header_id` (BugFix-Accounting)<br>`tp_invoice_line.consignment_charge_header_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:consignment_charge_h -->
A Consignment Charge Header is a charge, duty or tax at consignment level, with a charge name and group, basis (percentage or fixed per document), amount, formula, structure number and ledger-post and tax-applicable flags. It is created from the charge structure on the consignment and then allocated to the consignment lines. It has an action that calculates and shows the consignment's assessable value; the company is set by an automation in BugFix-Accounting.
<!-- /SUMMARY -->

**Fields (22):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Accounting.automation_jin_company_id_in_consignment_charge_header` (BugFix-Accounting) |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `active` | Active | boolean | Archive flag for consignment header charges; defaults to active. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_active` (BugFix-Accounting)<br>`view BugFix-Accounting.view_consignment_charge_h_form` (BugFix-Accounting)<br>`view BugFix-Accounting.view_consignment_charge_h_search` (BugFix-Accounting) |
| `name` | Name | char | Name of the consignment header charge record. | stored |  | `view BugFix-Accounting.view_consignment_charge_h_list` (BugFix-Accounting)<br>`view BugFix-Accounting.view_consignment_charge_h_form` (BugFix-Accounting)<br>`view BugFix-Accounting.view_consignment_charge_h_search` (BugFix-Accounting) |
| `allocate_header_charges` | Allocate Header Charges | boolean | Flag showing whether this header charge is to be allocated to consignment lines. | stored |  | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `amount` | Amount | float | Amount of the header charge (fixed amount or percentage base), entered by the user. | stored |  | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `basis` | Basis | selection: Percentage=Percentage; Percentage=Percentage; Fixed Per Document=Fixed Per Document; Fixed Per Document=Fixed Per Document | How the charge is calculated: Percentage or Fixed Per Document. | stored |  | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `charge_group` | Charge Group | selection: None=None; None=None; Charges=Charges; Charges=Charges; Duty=Duty; Duty=Duty; Taxes=Taxes; Taxes=Taxes | Group of the charge: None, Charges, Duty or Taxes; used when checking the consignment's assessable value. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_charge_group` (BugFix-Accounting)<br>`server action BugFix-Stock.action_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `charge_name` | Charge Name | char | Name of the charge (e.g. freight, duty); used in the assessable value check. | stored |  | `server action BugFix-Stock.action_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `accounting_company_id` | Company | many2one → `res.company` | Company of the header charge; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_jin_multi_company_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.action_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_header`<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `consignment_id` | Consignment Id | many2one → `consignment_header` | Consignment this header charge belongs to; used to filter the Header Charges action. | stored | `model consignment_header` | `server action BugFix-Stock.action_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_header_charges` (BugFix-Accounting)<br>`window action BugFix-Stock.action_header_charges` |
| `formula` | Formula | char | Text formula describing how the charge is calculated. | stored |  | `view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `ledger_post` | Ledger Post | boolean | Flag indicating the charge is posted to the ledger; has a default value. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_ledger_post` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `sequence` | Sequence | integer | Ordering number for header charges (list drag handle). | stored |  | `default BugFix-Accounting.default_consignment_charge_h_sequence` (BugFix-Accounting)<br>`view BugFix-Accounting.view_consignment_charge_h_list` (BugFix-Accounting) |
| `structure_no` | Structure No | integer | Charge structure number this charge comes from; has a default value. | stored |  | `default BugFix-Accounting.default_consignment_charge_h_structure_no` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `tax_appicable` | Tax Applicable | boolean | Flag marking the charge as tax-applicable; used in the consignment assessable value check. | stored |  | `server action BugFix-Stock.action_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.view_default_form_view_for_consignment_charge_h_inherit` (BugFix-Accounting)<br>`view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `tax_appicable2` | Tax Applicable2 | boolean | Second tax-applicable flag shown on the header charge form; no logic uses it. | stored |  | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |
| `tp_processed` | TP Processed | boolean | Flag showing the charge has been processed into a TP invoice. | stored |  | `view BugFix-Accounting.view_default_list_view_for_consignment_charge_h_inherit` (BugFix-Accounting) |

**Server actions (2):**

- **Execute Code** (`action_jin_company_id_in_consignment_charge_header`, type `code`)
  - Function: Sets the Company of a Consignment Charge Header to the user's active company; run by an automation defined in BugFix-Accounting.
  - Depends on: `model res.company` (base), `model consignment_charge_h`, `consignment_charge_h.accounting_company_id`
  - Used by: `automation BugFix-Stock.automation_jin_company_id_in_consignment_charge_header`
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get("allowed_company_ids", [env.user.company_id.id])[0]
company = env["res.company"].browse(company_id)

record["accounting_company_id"] = company.id
```
  </details>
- **IMP - Check Consignment Assessable Value** (`action_imp_check_consignment_assessable_value`, type `code`)
  - Function: Calculates a consignment's Assessable Value (total amount plus tax-applicable delivery-term charges) and shows it in a sticky notification; changes no data.
  - Depends on: `model consignment_charge_h`, `model consignment_header`, `model delivery_term_charge` (BugFix-Purchase), `consignment_charge_h.charge_group`, `consignment_charge_h.charge_name`<details><summary>+2 more</summary>`consignment_charge_h.consignment_id`, `consignment_charge_h.tax_appicable`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (45 lines)</summary>

```python
av = 0

c_f_i = 0


for header_lines in records:
    con_header = env["consignment_header"].search(
        [("id", "=", header_lines.consignment_id.id)], limit=1
    )

    if con_header:
        delivery_term = env["delivery_term_charge"].search(
            [
                (
                    "delivery_terms_id",
                    "=",
                    con_header.delivery_term.id,
                ),
                ("tax_appicable", "=", True),
            ]
        )

        if delivery_term:
            for valid_terms in delivery_term:
                header_charges = env["consignment_charge_h"].search(
                    [
                        ("consignment_id", "=", con_header.id),
                        ("charge_group", "=", "Charges"),
                        ("charge_name", "=", valid_terms.name),
                    ],
                    limit=1,
                )

                if header_charges:
                    c_f_i += header_charges.amount

            av = con_header.total_amount + c_f_i

            title = "Calculate Assessable Value"

            message = "Assessable Value: " + str(av)

            action = {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": title,
                    "message": message,
                    "sticky": True,
                },
            }

            break
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Consignment Charge Header | `automation_jin_company_id_in_consignment_charge_header` |  | When a record is created or updated on Consignment Charge Header, runs _Execute Code_. | `model consignment_charge_h`<br>`server action BugFix-Stock.action_jin_company_id_in_consignment_charge_header` |  |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Charge Header | `action_consignment_charge_header` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` |  |
| Consignment Charge Header | `action_consignment_charge_header_2` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` |  |
| Consignment Charge Header | `action_consignment_charge_header_3` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` |  |
| Header Charges | `action_header_charges` | Opens **Consignment Charge Header** records (tree,form), filtered to `[('consignment_id', '=', active_id)]`. | `model consignment_charge_h`<br>`consignment_charge_h.consignment_id` | `view BugFix-Stock.view_default_form_view_for_consignment_header_inherit` |
| Purchase Invoices | `action_purchase_invoices_2` | Opens **Consignment Charge Header** records (tree,form). | `model consignment_charge_h` |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| consignment_charge_h user access | `access_consignment_charge_h_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Charge Header records. | `group base.group_user` (base)<br>`model consignment_charge_h` |  |
