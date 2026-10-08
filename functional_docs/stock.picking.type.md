# BugFix-Stock — `stock.picking.type`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.picking.type` — Picking Type

*Extends a model created by `stock`.* Python: `models/stock_picking_type.py`.

Other repos that use this model: `helpdesk.ticket._create_repair_transfer()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_route()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<br>`server action BugFix-Purchase.server_action_2406_create_material_transfer` (BugFix-Purchase)<br>`server action BugFix-Sales.server_action_2188_proj_create_pr_from_sales_quotation` (BugFix-Sales)<br>`stock.return.picking.default_get()` (Fix-repair)<br>`x_po_line_non_inventor.x_studio_warehouse` (BugFix-Purchase)<br>`x_po_non_inventory.x_studio_warehouse` (BugFix-Purchase)<details><summary>+7 more</summary>`x_pr_line_cash.x_studio_warehouse` (BugFix-Purchase)<br>`x_pr_line_non_inventor.x_studio_warehouse_1` (BugFix-Purchase)<br>`x_pr_non_inventory.x_studio_warehouse` (BugFix-Purchase)<br>`x_purchase.request.line.make.purchase.order.x_studio_warehouse` (BugFix-Purchase)<br>`x_purchase_request.x_studio_warehouse` (BugFix-Purchase)<br>`x_purchase_request_cas.x_studio_warehouse_1` (BugFix-Purchase)<br>`x_purchase_request_lin.x_studio_warehouse` (BugFix-Purchase)</details>

**Summary:**

<!-- SUMMARY:model:stock.picking.type -->
This repo adds Movement Journal, MJ IN and MJ OUT flags to operation types, set on the operation type form. It also adds columns to the operation types list, disables Create on the form, enables Create on the manufacturing kanban and ships record rules that limit operation types, including movement journal blocks.
<!-- /SUMMARY -->

**Fields (3):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_mj_in` | MJ IN | boolean | Checkbox marking the operation type as a movement journal IN; set on the operation type form. | stored |  | `view BugFix-Stock.ported_view_5328_studio_stock_picking_type_form` |
| `x_studio_mj_out` | MJ OUT | boolean | Checkbox marking the operation type as a movement journal OUT; set on the operation type form. | stored |  | `view BugFix-Stock.ported_view_5328_studio_stock_picking_type_form` |
| `x_studio_movement_journal` | Movement Journal | boolean | Checkbox marking the operation type as a movement journal type; set on the operation type form. | stored |  | `view BugFix-Stock.ported_view_5328_studio_stock_picking_type_form` |

**Window actions (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Operations | `act_window_2019_operations` | Opens **Picking Type** records (kanban,form), filtered to `[('code', 'in', ('incoming', 'outgoing', 'internal', 'mrp_operation'))]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.code` (stock) |  |
| stock.picking.type | `aw_f4_stock_picking_type_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) |  |
| stock.picking.type | `action_2784_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_picking_type` (BugFix-Studio-Misc) |
| stock.picking.type | `action_2837_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) |  |
| stock.picking.type | `action_2408_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) |  |
| stock.picking.type | `act_window_2784_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) |  |
| stock.picking.type | `act_window_2837_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) |  |
| stock.picking.type | `act_window_2408_stock_picking_type` | Opens **Picking Type** records (kanban,tree,form). | `model stock.picking.type` (stock) |  |

**Views (3):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: Operation Types customization | `ported_view_5328_studio_stock_picking_type_form` | form | set create=false on `//form[1]`; set groups= on `//field[@name='sequence_id']`; after `//field[@name='create_backorder']`: add field x_studio_movement_journal, field x_studio_mj_out, field x_studio_mj_in | Disables Create on the Operation Type form, shows Sequence to all users, and adds Movement Journal, MJ OUT and MJ IN checkboxes after Create Backorder. | `stock.picking.type.x_studio_mj_in`<br>`stock.picking.type.x_studio_mj_out`<br>`stock.picking.type.x_studio_movement_journal`<br>`view stock.view_picking_type_form` (stock) |  |
| Odoo Studio: Operation types customization | `ported_view_5334_studio_stock_picking_type_tree` | tree | after `//tree[1]/field[@name='name']`: add field code; after `//field[@name='warehouse_id']`: add field sequence_code; set groups= on `//field[@name='sequence_id']` | Adds Type of Operation (code) and Sequence Prefix columns to the Operation Types list and shows the Sequence field to all users. | `stock.picking.type.code` (stock)<br>`stock.picking.type.sequence_code` (stock)<br>`view stock.view_picking_type_tree` (stock) |  |
| Odoo Studio: stock.picking.type.kanban customization | `view_5288_odoo_studio_stock_picking_type_kanban_customization_e` | kanban | set create=true, quick_create=true on `//kanban[1]` | Enables Create and Quick Create on the manufacturing operation-type kanban. | `view mrp.stock_production_type_kanban` (mrp) |  |

**Record rules (8):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Block Transfers | `rule_450_block_transfers` | For everyone (global rule): read on Picking Type only where `[('code', "=", 'Transfer')]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.code` (stock) |  |
| Internal Transfer Test | `rule_459_internal_transfer_test` | For everyone (global rule): read on Picking Type only where `[('code', '!=', ('incoming','outgoing','mrp_operation'))]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.code` (stock) |  |
| Inventory No Actions | `rule_911_inventory_no_actions` | For Inventory / Administrator: read on Picking Type with no record filter (empty domain = all records). | `group stock.group_stock_manager` (stock)<br>`model stock.picking.type` (stock) |  |
| Kap-Movement Journal Block | `rule_461_kap_movement_journal_block` | For everyone (global rule): read/write/create/delete on Picking Type only where `[('sequence_code', '!=',('MJ/OUT','MJ/IN'))]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.sequence_code` (stock) |  |
| Kap-Movement Journal Only | `rule_464_kap_movement_journal_only` | For everyone (global rule): read/write/create/delete on Picking Type only where `[('sequence_code', '=',('MJ/OUT','MJ/IN'))]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.sequence_code` (stock) |  |
| Stock Operation Type multi-company | `rule_45_stock_operation_type_multi_company` | For everyone (global rule): read/write/create/delete on Picking Type only where `[('company_id','in', company_ids)]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.company_id` (stock) |  |
| Stock data admin | `rule_915_stock_data_admin` | For Inventory / Administrator: read/write/create/delete on Picking Type with no record filter (empty domain = all records). | `group stock.group_stock_manager` (stock)<br>`model stock.picking.type` (stock) |  |
| Test | `rule_463_test` | For everyone (global rule): read/write/create/delete on Picking Type only where `[('sequence_code', '=',('INT'))]`. | `model stock.picking.type` (stock)<br>`stock.picking.type.sequence_code` (stock) |  |
