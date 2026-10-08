# BugFix-Stock — `stock.rule`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.rule` — Stock Rule

*Extends a model created by `stock`.*

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2831_mst_odoo_data_clean_up_001` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2835_stock_rule_d7` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:stock.rule -->
This repo adds an optional Warehouse column to the stock rules list, a window action and a multi-company record rule. It adds no fields or logic.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.rule | `act_window_2835_stock_rule` | Opens **Stock Rule** records (tree,form). | `model stock.rule` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_rule` (BugFix-Studio-Misc) |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.rule.tree customization | `ported_view_6071_odoo_studio_stock_rule_tree_customizatio` | tree | after `//field[@name='location_dest_id']`: add field warehouse_id | Adds an optional Warehouse column to the stock Rules list. | `stock.rule.warehouse_id` (stock)<br>`view stock.view_stock_rule_tree` (stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| product_pulled_flow multi-company | `rule_56_product_pulled_flow_multi_company` | For everyone (global rule): read/write/create/delete on Stock Rule only where `[('company_id', 'in', company_ids + [False])]`. | `model stock.rule` (stock)<br>`stock.rule.company_id` (stock) |  |
