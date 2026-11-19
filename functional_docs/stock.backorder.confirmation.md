# BugFix-Stock — `stock.backorder.confirmation`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.backorder.confirmation` — Backorder Confirmation

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.backorder.confirmation -->
This repo only ships access rights for the backorder confirmation wizard, including one for the Jin - Administrator group. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Administrator | `access_6873_jin___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Backorder Confirmation records. | `group stock.group_stock_manager` (stock)<br>`model stock.backorder.confirmation` (stock) |  |
| stock.backorder.confirmation | `access_6876_stock_backorder_confirmation` | Gives **Sales / Jin - Sales - POS Users** read/create access to Backorder Confirmation records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model stock.backorder.confirmation` (stock) |  |
