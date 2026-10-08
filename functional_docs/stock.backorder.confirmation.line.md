# BugFix-Stock — `stock.backorder.confirmation.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.backorder.confirmation.line` — Backorder Confirmation Line

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.backorder.confirmation.line -->
This repo only ships access rights for the backorder confirmation wizard lines, including one for the Jin - Administrator group. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Administrator | `access_6872_jin___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Backorder Confirmation Line records. | `group stock.group_stock_manager` (stock)<br>`model stock.backorder.confirmation.line` (stock) |  |
| stock.backorder.confirmation.line | `access_6877_stock_backorder_confirmation_line` | Gives **Sales / Jin - Sales - POS Users** read/create access to Backorder Confirmation Line records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model stock.backorder.confirmation.line` (stock) |  |
