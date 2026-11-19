# BugFix-Stock — `stock.putaway.rule`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.putaway.rule` — Putaway Rule

*Extends a model created by `stock`.*

**Summary:**

<!-- SUMMARY:model:stock.putaway.rule -->
This repo only ships a multi-company record rule for putaway rules. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Stock Operation Type multi-company | `rule_46_stock_operation_type_multi_company` | For everyone (global rule): read/write/create/delete on Putaway Rule only where `[('company_id','in', company_ids)]`. | `model stock.putaway.rule` (stock)<br>`stock.putaway.rule.company_id` (stock) |  |
