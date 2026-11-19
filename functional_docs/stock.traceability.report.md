# BugFix-Stock — `stock.traceability.report`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.traceability.report` — Traceability Report

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.traceability.report -->
This repo only ships access rights for the traceability report, including one for the Inv - Administrator group. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inv - Administrator | `access_6271_inv___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Traceability Report records. | `group stock.group_stock_manager` (stock)<br>`model stock.traceability.report` (stock) |  |
| User | `access_6094_user` | Gives **Inventory / User** read access to Traceability Report records. | `group stock.group_stock_user` (stock)<br>`model stock.traceability.report` (stock) |  |
