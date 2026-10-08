# BugFix-Stock — `x_consignment_charge_h`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `x_consignment_charge_h` — Consignment Charge Header

*Created by this repo.* Python: `models/x_consignment_charge_h.py`. Record name field: `x_name`.

Other repos that use this model: `access right BugFix-Accounting.access_1333_consignment_charge_header_group_system` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_1334_consignment_charge_header_group_user` (BugFix-Accounting)<br>`access right BugFix-Accounting.access_x_consignment_charge_h_user` (BugFix-Accounting)<br>`access right BugFix-Studio-Misc.access_g_x_consignment_charge_h_x_consignment_charge_h_purchase_jin_po_invoicing_payment_i` (BugFix-Studio-Misc)<br>`access right BugFix-Studio-Misc.access_g_x_consignment_charge_h_x_consignment_charge_h_purchase_jin_procurement_end_user_i` (BugFix-Studio-Misc)<br>`automation BugFix-Accounting.base_automation_289_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`record rule BugFix-Accounting.rule_521_jin_multi_company_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1378_imp_apply_selected_charge_lines_to_tp_invoice` (BugFix-Accounting)<details><summary>+10 more</summary>`server action BugFix-Accounting.server_action_2617_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_apply_charges` (BugFix-Accounting)<br>`server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`window action BugFix-Accounting.action_1314_consignment_charge_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1317_header_charges` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2848_consignment_charge_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2858_consignment_charge_header` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_2885_purchase_invoices` (BugFix-Accounting)<br>`x_temp_tp_invoice_line.x_studio_consignment_charge_header_id` (BugFix-Accounting)<br>`x_tp_invoice_line.x_studio_consignment_charge_header_id` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:x_consignment_charge_h -->
A Consignment Charge Header is a charge, duty or tax at consignment level, with a charge name and group, basis (percentage or fixed per document), amount, formula, structure number and ledger-post and tax-applicable flags. It is created from the charge structure on the consignment and then allocated to the consignment lines. It has an action that calculates and shows the consignment's assessable value; the company is set by an automation in BugFix-Accounting.
<!-- /SUMMARY -->

**Fields (22):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `create_date` | Created on | datetime | Date and time the record was created (automatic). | stored |  | `automation BugFix-Accounting.base_automation_289_jin_company_id_in_consignment_charge_header` (BugFix-Accounting) |
| `create_uid` | Created by | many2one → `res.users` | User who created the record (automatic). | stored | `model res.users` (base) |  |
| `display_name` | Display Name | char | Name shown for the record in lists, dropdowns and links (computed automatically by Odoo). | not stored |  |  |
| `id` | ID | integer | Unique database ID of the record (automatic). | stored |  |  |
| `write_date` | Last Updated on | datetime | Date and time the record was last changed (automatic). | stored |  |  |
| `write_uid` | Last Updated by | many2one → `res.users` | User who last changed the record (automatic). | stored | `model res.users` (base) |  |
| `x_active` | Active | boolean | Archive flag for consignment header charges; defaults to active. | stored |  | `default BugFix-Accounting.default_159_x_consignment_charge_h_x_active` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2933_default_form_view_fo_6b5f65f9_e9e6_48d2_a1cf_f0ede8a5353b` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2934_default_search_view_3c397656_7f61_48f0_a2f4_97463f10e99e` (BugFix-Accounting) |
| `x_name` | Name | char | Name of the consignment header charge record. | stored |  | `view BugFix-Accounting.ported_view_2932_default_list_view_fo_66cf53c7_1e15_4a6b_b733_c7571ac71a02` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2933_default_form_view_fo_6b5f65f9_e9e6_48d2_a1cf_f0ede8a5353b` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2934_default_search_view_3c397656_7f61_48f0_a2f4_97463f10e99e` (BugFix-Accounting) |
| `x_studio_allocate_header_charges` | Allocate Header Charges | boolean | Flag showing whether this header charge is to be allocated to consignment lines. | stored |  | `view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_amount` | Amount | float | Amount of the header charge (fixed amount or percentage base), entered by the user. | stored |  | `view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_basis` | Basis | selection: Percentage=Percentage; Percentage=Percentage; Fixed Per Document=Fixed Per Document; Fixed Per Document=Fixed Per Document | How the charge is calculated: Percentage or Fixed Per Document. | stored |  | `view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting) |
| `x_studio_charge_group` | Charge Group | selection: None=None; None=None; Charges=Charges; Charges=Charges; Duty=Duty; Duty=Duty; Taxes=Taxes; Taxes=Taxes | Group of the charge: None, Charges, Duty or Taxes; used when checking the consignment's assessable value. | stored |  | `default BugFix-Accounting.default_161_x_consignment_charge_h_x_studio_charge_group` (BugFix-Accounting)<br>`server action BugFix-Stock.server_action_1320_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_charge_name` | Charge Name | char | Name of the charge (e.g. freight, duty); used in the assessable value check. | stored |  | `server action BugFix-Stock.server_action_1320_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_company_id` | Company | many2one → `res.company` | Company of the header charge; set to the current company on create and used by the multi-company record rule. | stored | `model res.company` (base) | `record rule BugFix-Accounting.rule_521_jin_multi_company_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_2617_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)<br>`server action BugFix-Stock.server_action_2617_jin_company_id_in_consignment_charge_header`<br>`view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_consignment_id` | Consignment Id | many2one → `x_consignment_header` | Consignment this header charge belongs to; used to filter the Header Charges action. | stored | `model x_consignment_header` | `server action BugFix-Stock.server_action_1320_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting)<br>`window action BugFix-Accounting.action_1317_header_charges` (BugFix-Accounting)<br>`window action BugFix-Stock.action_1317_header_charges` |
| `x_studio_formula` | Formula | char | Text formula describing how the charge is calculated. | stored |  | `view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting) |
| `x_studio_ledger_post` | Ledger Post | boolean | Flag indicating the charge is posted to the ledger; has a default value. | stored |  | `default BugFix-Accounting.default_165_x_consignment_charge_h_x_studio_ledger_post` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_sequence` | Sequence | integer | Ordering number for header charges (list drag handle). | stored |  | `default BugFix-Accounting.default_160_x_consignment_charge_h_x_studio_sequence` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2932_default_list_view_fo_66cf53c7_1e15_4a6b_b733_c7571ac71a02` (BugFix-Accounting) |
| `x_studio_structure_no` | Structure No | integer | Charge structure number this charge comes from; has a default value. | stored |  | `default BugFix-Accounting.default_162_x_consignment_charge_h_x_studio_structure_no` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting) |
| `x_studio_tax_appicable` | Tax Applicable | boolean | Flag marking the charge as tax-applicable; used in the consignment assessable value check. | stored |  | `server action BugFix-Stock.server_action_1320_imp_check_consignment_assessable_value`<br>`view BugFix-Accounting.ported_view_2936_odoo_studio_default_f7a79ca0_c28b_426a_9cee_c3ad87d51662` (BugFix-Accounting)<br>`view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_tax_appicable2` | Tax Applicable2 | boolean | Second tax-applicable flag shown on the header charge form; no logic uses it. | stored |  | `view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |
| `x_studio_tp_processed` | TP Processed | boolean | Flag showing the charge has been processed into a TP invoice. | stored |  | `view BugFix-Accounting.ported_view_2940_odoo_studio_default_c78a0618_af64_45b3_83da_c3a75d23a5d5` (BugFix-Accounting) |

**Server actions (2):**

- **IMP - Check Consignment Assessable Value** (`server_action_1320_imp_check_consignment_assessable_value`, type `code`)
  - Function: Calculates a consignment's Assessable Value (total amount plus tax-applicable delivery-term charges) and shows it in a sticky notification; changes no data.
  - Depends on: `model x_consignment_charge_h`, `model x_consignment_header`, `model x_delivery_term_charge` (BugFix-Purchase), `x_consignment_charge_h.x_studio_charge_group`, `x_consignment_charge_h.x_studio_charge_name`<details><summary>+2 more</summary>`x_consignment_charge_h.x_studio_consignment_id`, `x_consignment_charge_h.x_studio_tax_appicable`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (45 lines)</summary>

```python
av = 0

c_f_i = 0



for header_lines in records:

  con_header = env['x_consignment_header'].search([('id', '=', header_lines.x_studio_consignment_id.id)],limit=1)

  if con_header:

    delivery_term = env['x_delivery_term_charge'].search([('x_studio_delivery_terms_id', '=', con_header.x_studio_delivery_term.id), ('x_studio_tax_appicable', '=', True)]) 

    if delivery_term:

      for valid_terms in delivery_term:

        header_charges = env['x_consignment_charge_h'].search([('x_studio_consignment_id', '=', con_header.id), ('x_studio_charge_group', '=', 'Charges'), ('x_studio_charge_name', '=', valid_terms.x_name)],limit=1)

        if header_charges:

          c_f_i += header_charges.x_studio_amount

          

      av = con_header.x_studio_total_amount + c_f_i

      title = "Calculate Assessable Value"

      message = "Assessable Value: " + str(av)

      

      action = {

                'type': 'ir.actions.client',

                'tag': 'display_notification',

                'params': {'title': title,'message': message,'sticky': True,}

                } 

      break
```
  </details>
- **JIN - Company Id in Consignment Charge Header** (`server_action_2617_jin_company_id_in_consignment_charge_header`, type `code`)
  - Function: Sets the Company of a Consignment Charge Header to the user's active company; run by an automation defined in BugFix-Accounting.
  - Depends on: `model res.company` (base), `model x_consignment_charge_h`, `x_consignment_charge_h.x_studio_company_id`
  - Used by: `automation BugFix-Accounting.base_automation_289_jin_company_id_in_consignment_charge_header` (BugFix-Accounting)
  <details><summary>code (4 lines)</summary>

```python
company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
company = env['res.company'].browse(company_id)

record['x_studio_company_id'] = company.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| JIN - Company Id in Consignment Charge Header | `automation_289_jin_company_id_in_consignment_charge_header` |  | When a record is created or updated on Consignment Charge Header, runs nothing (no action linked). | `model x_consignment_charge_h` |  |

**Window actions (5):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Consignment Charge Header | `action_1314_consignment_charge_header` | Opens **Consignment Charge Header** records (tree,form). | `model x_consignment_charge_h` |  |
| Consignment Charge Header | `action_2848_consignment_charge_header` | Opens **Consignment Charge Header** records (tree,form). | `model x_consignment_charge_h` |  |
| Consignment Charge Header | `action_2858_consignment_charge_header` | Opens **Consignment Charge Header** records (tree,form). | `model x_consignment_charge_h` |  |
| Header Charges | `action_1317_header_charges` | Opens **Consignment Charge Header** records (tree,form), filtered to `[('x_studio_consignment_id', '=', active_id)]`. | `model x_consignment_charge_h`<br>`x_consignment_charge_h.x_studio_consignment_id` | `view BugFix-Stock.ported_view_2816_studio_form_x_consignment_header` |
| Purchase Invoices | `action_2885_purchase_invoices` | Opens **Consignment Charge Header** records (tree,form). | `model x_consignment_charge_h` |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| x_consignment_charge_h user access | `access_x_consignment_charge_h_user` | Gives **User types / Internal User** read/write/create/delete access to Consignment Charge Header records. | `group base.group_user` (base)<br>`model x_consignment_charge_h` |  |
