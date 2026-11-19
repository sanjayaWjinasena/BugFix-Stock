# BugFix-Stock — `stock.quant`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.quant` — Quants

*Extends a model created by `stock`.*

Other repos that use this model: `server action BugFix-Sales.server_action_2096_rr_insufficient_transfer_inventory_details` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2162_proj_item_related_details_in_project_so` (BugFix-Sales)<br>`server action BugFix-Sales.server_action_2188_proj_create_pr_from_sales_quotation` (BugFix-Sales)<br>`server action BugFix-Studio-Misc.server_action_2599_sample_server_action_update_stock_quant` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2187_stock_quant_d7` (BugFix-Studio-Misc)<br>`x_mr_config._compute_on_hand_qty_2()` (BugFix-Purchase, BugFix-Stock)

**Summary:**

<!-- SUMMARY:model:stock.quant -->
This repo only adds a window action, an access right for the Inv - Administrator group and a multi-company record rule for quants. It adds no fields, views or logic.
<!-- /SUMMARY -->

**Window actions (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.quant | `action_2187_stock_quant` | Opens **Quants** records (kanban,tree,form,pivot,graph). | `model stock.quant` (stock) |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inv - Administrator | `access_6266_inv___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Quants records. | `group stock.group_stock_manager` (stock)<br>`model stock.quant` (stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock_quant multi-company | `rule_52_stock_quant_multi_company` | For everyone (global rule): read/write/create/delete on Quants only where `[('company_id', 'in', company_ids + [False])]`. | `model stock.quant` (stock)<br>`stock.quant.company_id` (stock) |  |
