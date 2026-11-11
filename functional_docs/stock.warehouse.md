# BugFix-Stock — `stock.warehouse`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.warehouse` — Warehouse

*Extends a model created by `stock`.*

Other repos that use this model: `account.analytic.account.bugfix_analytics_warehouse_id` (BugFix-Analytics)<br>`record rule Fix-repair.rule_stock_data_warehouse` (Fix-repair)<br>`sale.order.line.sales_warehouse_id` (BugFix-Sales)<br>`server action BugFix-Sales.action_rr_insufficient_transfer_inventory_details` (BugFix-Sales)<br>`server action BugFix-Sales.action_proj_item_related_details_in_project_so` (BugFix-Sales)<br>`server action BugFix-Sales.action_proj_create_pr_from_sales_quotation` (BugFix-Sales)<br>`stock.return.picking.default_get()` (Fix-repair)<br>`stock.warehouse._seed_factory_repair_locations()` (Fix-repair)<details><summary>+3 more</summary>`window action Fix-repair.action_warehouse` (Fix-repair)<br>`window action Fix-repair.action_warehouse_2` (Fix-repair)<br>`bve.salesreport.bve_t1_warehouse_id` (BugFix-Studio-Misc)</details>

**Summary:**

<!-- SUMMARY:model:stock.warehouse -->
This repo makes the warehouse list non-editable, adds the ID column and adds two warehouse window actions. It adds no fields or logic.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| WareHouse | `action_warehouse` | Opens **Warehouse** records (tree,form). | `model stock.warehouse` (stock) | `menu BugFix-Stock.menu_warehouse`<br>`menu Fix-repair.menu_warehouse` (Fix-repair) |
| Warehouse | `action_warehouse_2` | Opens **Warehouse** records (tree,form). | `model stock.warehouse` (stock) | `menu BugFix-Stock.menu_warehouse_2`<br>`menu Fix-repair.menu_warehouse_1` (Fix-repair) |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.warehouse.tree customization | `view_stock_warehouse_tree_inherit` | tree | set edit=false on `//tree[1]`; after `//field[@name='sequence']`: add field id | Makes the Warehouse list non-editable and adds the record ID column. | `view stock.view_warehouse_tree` (stock) |  |
