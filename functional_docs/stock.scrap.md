# BugFix-Stock — `stock.scrap`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.scrap` — Scrap

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.scrap -->
This repo only ships an access right and a multi-company record rule for scrap orders. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.scrap | `access_6860_stock_scrap` | Gives **Sales / Jin - Sales - POS Users** read access to Scrap records. | `group BugFix-Approvals.group_132_jin_sales_pos_users` (BugFix-Approvals)<br>`model stock.scrap` (stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock_scrap_company multi-company | `rule_59_stock_scrap_company_multi_company` | For everyone (global rule): read/write/create/delete on Scrap only where `[('company_id', 'in', company_ids)]`. | `model stock.scrap` (stock)<br>`stock.scrap.company_id` (stock) |  |
