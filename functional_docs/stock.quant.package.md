# BugFix-Stock — `stock.quant.package`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.quant.package` — Packages

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.quant.package -->
This repo only ships a multi-company record rule for packages. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock_quant_package multi-company | `rule_58_stock_quant_package_multi_company` | For everyone (global rule): read/write/create/delete on Packages only where `[('company_id', 'in', company_ids + [False])]`. | `model stock.quant.package` (stock)<br>`stock.quant.package.company_id` (stock) |  |
