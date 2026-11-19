# BugFix-Stock — `stock.quantity.history`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.quantity.history` — Stock Quantity History

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.quantity.history -->
This repo only ships an access right for the Jin - Administrator group on the stock quantity history wizard. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Jin - Administrator | `access_7079_jin___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Stock Quantity History records. | `group stock.group_stock_manager` (stock)<br>`model stock.quantity.history` (stock) |  |
