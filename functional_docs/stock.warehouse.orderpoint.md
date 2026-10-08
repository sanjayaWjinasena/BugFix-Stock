# BugFix-Stock — `stock.warehouse.orderpoint`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.warehouse.orderpoint` — Minimum Inventory Rule

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.warehouse.orderpoint -->
This repo only ships an access right and a multi-company record rule for reordering rules. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.warehouse.orderpoint | `access_6856_stock_warehouse_orderpoint` | Gives **Sales / Jin - Sales - POS Users** read access to Minimum Inventory Rule records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model stock.warehouse.orderpoint` (stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock_warehouse.orderpoint multi-company | `rule_55_stock_warehouse_orderpoint_multi_company` | For everyone (global rule): read/write/create/delete on Minimum Inventory Rule only where `[('company_id', 'in', company_ids)]`. | `model stock.warehouse.orderpoint` (stock)<br>`stock.warehouse.orderpoint.company_id` (stock) |  |
