# BugFix-Stock — `stock.move`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.move` — Stock Move

*Extends a model created by `stock`.* Python: `models/stock_move.py`.

Other repos that use this model: `helpdesk.ticket._repair_studio_auto_create_repair_route()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<br>`server action BugFix-Accounting.server_action_1144_work_center_costing_model_update_journal_entries` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1519_sls_payment_reconciliation_automate` (BugFix-Accounting)<br>`server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<br>`stock.return.picking.default_get()` (Fix-repair)<br>`x_mrp_bom_material_cos.x_studio_prod_bom_line_id` (BugFix-MRP)<br>`x_product_test.x_studio_stock_move` (BugFix-Studio-Misc)<details><summary>+2 more</summary>`x_sales_report_model.x_studio_related_field_PaCjA` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_production_variance_id` (Jinasena_Masterdata_Reporting)</details>

**Summary:**

<!-- SUMMARY:model:stock.move -->
This repo adds an Original Qty field, a report type link for Production Job Variance and several read-only flags (melt item, variance, consignment update) that are unused or always empty. Two active automations create and update a Production BOM Material Cost record for raw-material moves of manufacturing orders. It also adds manufacturing and cost columns to the moves list and makes the transfer move list editable.
<!-- /SUMMARY -->

**Fields (8):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_melt_item` | Melt Item | boolean | Read-only 'Melt Item' flag on the stock move; non-stored with no compute and unused, so it is always unchecked. | not stored |  |  |
| `x_studio_melt_item_2` | Melt Item 2 | boolean | Read-only 'Melt Item 2' flag on the stock move; non-stored with no compute and unused, so it is always unchecked. | not stored |  |  |
| `x_studio_melt_item_3` | Melt Item 3 | boolean | Read-only 'Melt Item 3' flag on the stock move; non-stored with no compute and unused, so it is always unchecked. | not stored |  |  |
| `x_studio_original_qty` | Original Qty | float | Original quantity of the move, written by the 'Production Job Variance - Write Original' server action and shown in the moves list for variance reporting. | stored |  | `server action BugFix-Stock.server_action_1758_srm_production_job_variance_write_original`<br>`view BugFix-Stock.ported_view_2579_studio_stock_move_tree2` |
| `x_studio_pr_type` | PR Type | selection: Local=Local; Import=Import | Read-only purchase request type of the move: Local or Import. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_report_type_production_job_variance` | Report Type - Production Job Variance | many2one → `x_sales_report_type` | Sales report type (`x_sales_report_type`) assigned to this record for reporting; filled automatically by the server action that auto-populates report types on production job variance moves. | stored | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) | `server action BugFix-Stock.server_action_1755_srm_auto_populate_report_type_in_product_variance_moves` |
| `x_studio_update_consignment` | Update Consignment | boolean | Read-only flag on the move indicating consignment update; not used by any view or logic in this repo. | stored |  |  |
| `x_studio_variance` | Variance | float | Read-only variance quantity shown in the moves list; non-stored with no compute in this repo, so it is always 0. | not stored |  | `view BugFix-Stock.ported_view_2579_studio_stock_move_tree2` |

**Server actions (5):**

- **Create Production BOM Material Cost** (`server_action_1058_create_production_bom_material_cost`, type `code`)
  - Function: Creates a BOM Material Cost record (`x_mrp_bom_material_cos`) from the stock move's BOM line, operation, product, planned qty and UoM. Older variant, not referenced by any automation in this repo.
  - Depends on: `model stock.move` (stock), `model x_mrp_bom_material_cos` (BugFix-MRP), `stock.move.bom_line_id` (mrp), `stock.move.operation_id` (mrp), `stock.move.product_id` (stock)<details><summary>+2 more</summary>`stock.move.product_qty` (stock), `stock.move.product_uom` (stock)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (2 lines)</summary>

```python
if record.id:
  bom_material_cost = env['x_mrp_bom_material_cos'].create({'x_studio_bom_material_cost_ids':record.bom_line_id.id,'x_studio_prod_bom_line_id':record.id,'x_studio_operation_id':record.operation_id.id,'x_studio_product_id':record.product_id.id,'x_studio_planned_qty':record.product_qty,'x_studio_uom_id':record.product_uom.id})
```
  </details>
- **Execute Code** (`server_action_1066_create_production_bom_material_cost`, type `code`)
  - Function: For a raw-material move of a manufacturing order with a BOM line, creates a Production BOM Material Cost record with operation, product, planned and actual quantities and UoM; run by the matching automation.
  - Depends on: `model stock.move` (stock), `model x_mrp_bom_material_cos` (BugFix-MRP), `stock.move.bom_line_id` (mrp), `stock.move.operation_id` (mrp), `stock.move.product_id` (stock)<details><summary>+4 more</summary>`stock.move.product_qty` (stock), `stock.move.product_uom` (stock), `stock.move.quantity` (stock), `stock.move.raw_material_production_id` (mrp)</details>
  - Used by: `automation BugFix-Stock.base_automation_28_create_production_bom_material_cost`
  <details><summary>code (2 lines)</summary>

```python
if record.bom_line_id and record.raw_material_production_id:
  prod_bom_material_cost = env['x_mrp_bom_material_cos'].create({'x_studio_prod_bom_material_cost_ids':record.raw_material_production_id.id,'x_studio_bom_line_id':record.bom_line_id.id,'x_studio_prod_bom_line_id':record.id,'x_studio_operation_id':record.operation_id.id,'x_studio_product_id':record.product_id.id,'x_studio_planned_qty':record.product_qty,'x_studio_actual_qty':record.quantity,'x_studio_uom_id':record.product_uom.id})
```
  </details>
- **Execute Code** (`server_action_1073_update_production_bom_material_cost`, type `code`)
  - Function: Finds the Production BOM Material Cost record for this raw-material move and refreshes its operation, product, planned/actual quantities and UoM; run by the matching automation.
  - Depends on: `model stock.move` (stock), `model x_mrp_bom_material_cos` (BugFix-MRP), `stock.move.bom_line_id` (mrp), `stock.move.operation_id` (mrp), `stock.move.product_id` (stock)<details><summary>+4 more</summary>`stock.move.product_qty` (stock), `stock.move.product_uom` (stock), `stock.move.quantity` (stock), `stock.move.raw_material_production_id` (mrp)</details>
  - Used by: `automation BugFix-Stock.base_automation_29_update_production_bom_material_cost`
  <details><summary>code (4 lines)</summary>

```python
if record.bom_line_id and record.raw_material_production_id:
  update = env['x_mrp_bom_material_cos'].search([('x_studio_prod_bom_line_id', '=', record.id), ('x_studio_prod_bom_material_cost_ids', '=', record.raw_material_production_id.id), ('x_studio_bom_line_id', '=', record.bom_line_id.id)], limit=1)
  if update:
    update.write({'x_studio_operation_id':record.operation_id.id,'x_studio_product_id':record.product_id.id,'x_studio_planned_qty':record.product_qty,'x_studio_actual_qty':record.quantity,'x_studio_uom_id':record.product_uom.id})
```
  </details>
- **SRM - Auto Populate Report Type in Product Variance Moves** (`server_action_1755_srm_auto_populate_report_type_in_product_variance_moves`, type `code`)
  - Function: Sets the move's 'Production Job Variance' report type field to the Sales Report Type with code 'Production Job Variance'. Not referenced by any automation in this repo.
  - Depends on: `model stock.move` (stock), `model x_sales_report_type` (Jinasena_Masterdata_Reporting), `stock.move.x_studio_report_type_production_job_variance` (Jinasena_Masterdata_Reporting)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.id:
  rpt_id= env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Production Job Variance')],limit=1)
  if rpt_id:
   record['x_studio_report_type_production_job_variance'] = rpt_id.id
```
  </details>
- **SRM - Production Job Variance - Write Original** (`server_action_1758_srm_production_job_variance_write_original`, type `code`)
  - Function: Copies the move's Demand quantity (`product_uom_qty`) into Original Qty. Not referenced by any automation in this repo.
  - Depends on: `model stock.move` (stock), `stock.move.product_uom_qty` (stock), `stock.move.x_studio_original_qty`
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (1 lines)</summary>

```python
record['x_studio_original_qty'] = record.product_uom_qty
```
  </details>
**Automations (4):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Create Production BOM Material Cost | `base_automation_28_create_production_bom_material_cost` |  | When a record is created or updated on Stock Move, runs _Execute Code_. | `model stock.move` (stock)<br>`server action BugFix-Stock.server_action_1066_create_production_bom_material_cost`<br>`stock.move.create_date` (stock) |  |
| SRM - Auto Populate Report Type in Product Variance Moves | `base_automation_129_srm_auto_populate_report_type_in_product_variance_moves` | archived | When a record is created or updated on Stock Move and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model stock.move` (stock) |  |
| SRM - Production Job Variance - Write Original | `base_automation_130_srm_production_job_variance_write_original` | archived | When a record is created on Stock Move and `[]`, runs nothing (no action linked). **Archived — does not run.** | `model stock.move` (stock) |  |
| Update Production BOM Material Cost | `base_automation_29_update_production_bom_material_cost` |  | When a record is created or updated on Stock Move, runs _Execute Code_. | `model stock.move` (stock)<br>`server action BugFix-Stock.server_action_1073_update_production_bom_material_cost` |  |

**Window actions (6):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Stock.Move | `aw_f4_stock_move_stock_move` | Opens **Stock Move** records (kanban,tree,form,pivot,graph). | `model stock.move` (stock) |  |
| Stock.Move | `action_1757_stock_move` | Opens **Stock Move** records (kanban,tree,form,pivot,graph). | `model stock.move` (stock) | `menu BugFix-Studio-Misc.menu_f6f_stock_move` (BugFix-Studio-Misc) |
| Stock.Move | `act_window_1757_stock_move` | Opens **Stock Move** records (kanban,tree,form,pivot,graph). | `model stock.move` (stock) |  |
| stock.move | `aw_f4_stock_move_stock_move_1` | Opens **Stock Move** records (kanban,tree,form,pivot,graph). | `model stock.move` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_move` (BugFix-Studio-Misc) |
| stock.move | `action_1065_stock_move` | Opens **Stock Move** records (kanban,tree,form,pivot,graph). | `model stock.move` (stock) |  |
| stock.move | `act_window_1065_stock_move` | Opens **Stock Move** records (kanban,tree,form,pivot,graph). | `model stock.move` (stock) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.move.tree2 customization | `ported_view_2579_studio_stock_move_tree2` | tree | after `//field[@name='origin']`: add field bom_line_id, field created_production_id, field raw_material_production_id, field production_id; after `//field[@name='product_uom_qty']`: add field unit_factor, field x_studio_original_qty, field x_studio_variance, field product_qty, field should_consume_qty, field availability, field forecast_availability, field price_unit | Adds manufacturing links (BOM line, created/raw-material/production order) and quantity/cost columns (unit factor, Original Qty, Variance, product qty, should consume, availability, price unit) to the stock move list. | `stock.move.availability` (stock)<br>`stock.move.bom_line_id` (mrp)<br>`stock.move.created_production_id` (mrp)<br>`stock.move.forecast_availability` (stock)<br>`stock.move.price_unit` (stock)<details><summary>+8 more</summary>`stock.move.product_qty` (stock)<br>`stock.move.production_id` (mrp)<br>`stock.move.raw_material_production_id` (mrp)<br>`stock.move.should_consume_qty` (mrp)<br>`stock.move.unit_factor` (mrp)<br>`stock.move.x_studio_original_qty`<br>`stock.move.x_studio_variance`<br>`view stock.view_move_tree_receipt_picking` (stock)</details> |  |
| Odoo Studio: stock.picking.move.tree customization | `view_6051_odoo_studio_stock_picking_move_tree_customization_e` | tree | set edit=true, multi_edit=true on `//tree[1]` | Makes the transfer move-lines list editable, including multi-record editing. | `view stock.view_picking_move_tree` (stock) |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Stock Move | `access_7004_stock_move` | Gives **Purchase / Jin - PO Approvers: PO Amount <= 500,000** read/write/create access to Stock Move records. | `group BugFix-Approvals.group_112_jin_po_approvers_po_amount_500_000` (BugFix-Approvals)<br>`model stock.move` (stock) |  |
| User | `access_6088_user` | Gives **Helpdesk / User** read/write/create access to Stock Move records. | `group helpdesk.group_helpdesk_user` (helpdesk)<br>`model stock.move` (stock) |  |
| stock.move | `access_6853_stock_move` | Gives **Sales / Jin - Sales - POS Users** read/write/create access to Stock Move records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model stock.move` (stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock_move multi-company | `rule_50_stock_move_multi_company` | For everyone (global rule): read/write/create/delete on Stock Move only where `[('company_id', 'in', company_ids)]`. | `model stock.move` (stock)<br>`stock.move.company_id` (stock) |  |
