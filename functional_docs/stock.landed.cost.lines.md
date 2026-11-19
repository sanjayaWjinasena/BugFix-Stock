# BugFix-Stock — `stock.landed.cost.lines`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.landed.cost.lines` — Stock Landed Cost Line

*Extends a model created by `stock_landed_costs`.*

Other repos that use this model: `window action BugFix-Studio-Misc.act_window_2814_stock_landed_cost_line_d7` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:stock.landed.cost.lines -->
This repo only adds a window action for landed cost lines. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.landed.cost.line | `act_window_2814_stock_landed_cost_line` | Opens **Stock Landed Cost Line** records (tree,form). | `model stock.landed.cost.lines` (stock_landed_costs) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_landed_cost_line` (BugFix-Studio-Misc) |
