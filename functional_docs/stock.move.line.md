# BugFix-Stock — `stock.move.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.move.line` — Product Moves (Stock Move Line)

*Extends a model created by `stock`.* Python: `models/stock_move_line.py`.

Other repos that use this model: `helpdesk.ticket._compute_has_return_picking()` (Fix-repair)<br>`helpdesk.ticket._create_repair_transfer()` (Fix-repair)<br>`helpdesk.ticket._get_so_from_serial()` (Fix-repair)<br>`helpdesk.ticket._repair_auto_select_product_for_rug()` (Fix-repair)<br>`helpdesk.ticket._repair_auto_select_product_for_rug_no_company()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_route()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<br>`server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<details><summary>+10 more</summary>`stock.lot._compute_is_issued()` (Fix-repair)<br>`stock.lot._search_is_issued()` (Fix-repair)<br>`stock.return.picking._create_returns()` (Fix-repair)<br>`stock.return.picking.default_get()` (Fix-repair)<br>`x_sales_report_model.x_studio_related_field_NsCKm` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_XCKXu` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_model.x_studio_related_field_bCtVj` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_prod_summary_split_id` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_sales_prod_purch_id` (Jinasena_Masterdata_Reporting)<br>`x_sales_report_type.x_studio_slow_moving_item_id` (Jinasena_Masterdata_Reporting)</details>

**Summary:**

<!-- SUMMARY:model:stock.move.line -->
This repo adds a PR Type field and three Sales Report Type links (Slow Moving Items, Sales-Production-Purchase, Production Summary Split) to product moves. An automation fills the three report type links when a move line is in progress, and the Moves History list gets extra columns and a quantity total.
<!-- /SUMMARY -->

**Fields (4):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_pr_type` | PR Type | selection: Local=Local; Import=Import | Read-only purchase request type of the move line: Local or Import. Not used by any view or logic in this repo. | stored |  |  |
| `x_studio_report_type_production_summary_split` | Report Type - Production Summary Split | many2one → `x_sales_report_type` | Sales report type (`x_sales_report_type`) assigned to this record for reporting; filled automatically by the server action that auto-populates report types on product moves; shown in the product moves list. Used for the Production Summary Split report. | stored | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) | `server action BugFix-Stock.server_action_1742_srm_auto_populate_report_type_in_product_moves`<br>`view BugFix-Stock.ported_view_3912_studio_stock_move_line_tree` |
| `x_studio_report_type_sales_prod_purch` | Report Type - Sales prod. purch. | many2one → `x_sales_report_type` | Sales report type (`x_sales_report_type`) assigned to this record for reporting; filled automatically by the server action that auto-populates report types on product moves; shown in the product moves list. Used for the Sales/Production/Purchase report. | stored | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) | `server action BugFix-Stock.server_action_1742_srm_auto_populate_report_type_in_product_moves`<br>`view BugFix-Stock.ported_view_3912_studio_stock_move_line_tree` |
| `x_studio_report_type_slow_moving_items` | Report Type - Slow Moving Items | many2one → `x_sales_report_type` | Sales report type (`x_sales_report_type`) assigned to this record for reporting; filled automatically by the server action that auto-populates report types on product moves; shown in the product moves list. Used for the Slow Moving Items report. | stored | `model x_sales_report_type` (Jinasena_Masterdata_Reporting) | `server action BugFix-Stock.server_action_1742_srm_auto_populate_report_type_in_product_moves`<br>`view BugFix-Stock.ported_view_3912_studio_stock_move_line_tree` |

**Server actions (2):**

- **Execute Code** (`server_action_1742_srm_auto_populate_report_type_in_product_moves`, type `code`)
  - Function: When a move line is in state 'progress', fills its three report-type links (Slow Moving Items, Sales-Production-Purchase, Production Summary - Split) from Sales Report Types by code; run by the matching automation.
  - Depends on: `model stock.move.line` (stock), `model x_sales_report_type` (Jinasena_Masterdata_Reporting), `stock.move.line.state` (stock), `stock.move.line.x_studio_report_type_production_summary_split` (Jinasena_Masterdata_Reporting), `stock.move.line.x_studio_report_type_sales_prod_purch` (Jinasena_Masterdata_Reporting)<details><summary>+1 more</summary>`stock.move.line.x_studio_report_type_slow_moving_items` (Jinasena_Masterdata_Reporting)</details>
  - Used by: `automation BugFix-Stock.base_automation_124_srm_auto_populate_report_type_in_product_moves`
  <details><summary>code (12 lines)</summary>

```python
if record.state == 'progress':
  rpt_id= env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Slow Moving Items')],limit=1)
  if rpt_id:
   record['x_studio_report_type_slow_moving_items'] = rpt_id.id
   
  rpt_id= env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Sales - Production - Purchase Report')],limit=1)
  if rpt_id:
   record['x_studio_report_type_sales_prod_purch'] = rpt_id.id
   
  rpt_id= env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Production Summary - Split')],limit=1)
  if rpt_id:
   record['x_studio_report_type_production_summary_split'] = rpt_id.id
```
  </details>
- **SRM - Auto Populate Report Type in Product Moves - 2** (`server_action_1752_srm_auto_populate_report_type_in_product_moves_2`, type `code`)
  - Function: Intended to set the Sales-Production-Purchase report type on a move line, but writes to a non-existent field name ('Sales - Production - Purchase Report') and would fail if run. Not referenced by any automation.
  - Depends on: `model stock.move.line` (stock), `model x_sales_report_type` (Jinasena_Masterdata_Reporting), `stock.move.line.state` (stock)
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (4 lines)</summary>

```python
if record.state == 'progress':
  rpt_id= env['x_sales_report_type'].search([('x_studio_report_code', '=', 'Sales - Production - Purchase Report')],limit=1)
  if rpt_id:
   record['Sales - Production - Purchase Report'] = rpt_id.id
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| SRM - Auto Populate Report Type in Product Moves | `base_automation_124_srm_auto_populate_report_type_in_product_moves` |  | When a record is created or updated on Product Moves (Stock Move Line) and `[]`, runs _Execute Code_. | `model stock.move.line` (stock)<br>`server action BugFix-Stock.server_action_1742_srm_auto_populate_report_type_in_product_moves` |  |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.move.line | `aw_f4_stock_move_line_stock_move_line` | Opens **Product Moves (Stock Move Line)** records (kanban,tree,form). | `model stock.move.line` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_move_line` (BugFix-Studio-Misc) |
| stock.move.line | `action_1364_stock_move_line` | Opens **Product Moves (Stock Move Line)** records (kanban,tree,form). | `model stock.move.line` (stock) |  |
| stock.move.line | `act_window_1364_stock_move_line` | Opens **Product Moves (Stock Move Line)** records (kanban,tree,form). | `model stock.move.line` (stock) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.move.line.tree customization | `ported_view_3912_studio_stock_move_line_tree` | tree | set options={"show_time":false}, widget=datetime on `//field[@name='date']`; set sum=Sum of Quantity Done, widget=monetary on `//field[@name='quantity']`; after `//field[@name='state']`: add field origin, field picking_id, field picking_code, field x_studio_report_type_sales_prod_purch, field x_studio_report_type_slow_moving_items, field x_studio_report_type_production_summary_split | On the Moves History list shows date without time, totals Quantity, and adds source document, transfer, operation code and three report-type columns. | `stock.move.line.origin` (stock)<br>`stock.move.line.picking_code` (stock)<br>`stock.move.line.picking_id` (stock)<br>`stock.move.line.x_studio_report_type_production_summary_split` (Jinasena_Masterdata_Reporting)<br>`stock.move.line.x_studio_report_type_sales_prod_purch` (Jinasena_Masterdata_Reporting)<details><summary>+2 more</summary>`stock.move.line.x_studio_report_type_slow_moving_items` (Jinasena_Masterdata_Reporting)<br>`view stock.view_move_line_tree` (stock)</details> |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock_move_line multi-company | `rule_51_stock_move_line_multi_company` | For everyone (global rule): read/write/create/delete on Product Moves (Stock Move Line) only where `[('company_id', 'in', company_ids + [False])]`. | `model stock.move.line` (stock)<br>`stock.move.line.company_id` (stock) |  |
