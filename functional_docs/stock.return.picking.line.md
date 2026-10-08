# BugFix-Stock — `stock.return.picking.line`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.return.picking.line` — Return Picking Line

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.return.picking.line -->
This repo only ships an access right for the Inv - Administrator group on return wizard lines. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inv - Administrator | `access_6274_inv___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Return Picking Line records. | `group stock.group_stock_manager` (stock)<br>`model stock.return.picking.line` (stock) |  |
