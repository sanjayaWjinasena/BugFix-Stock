# BugFix-Stock — `stock.lot`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.lot` — Lot/Serial

*Extends a model created by `stock`.* Python: `models/stock_lot.py`, `models/stock_lot_gap.py`.

Other repos that use this model: `helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<br>`helpdesk.ticket.action_create_repair_serial()` (Fix-repair)<br>`helpdesk.ticket.x_studio_serial_no` (Fix-repair)<br>`helpdesk.ticket.x_studio_serial_number` (Fix-repair)<br>`server action BugFix-MRP.sa_f5_x_mass_produce_serial_mass_produce_serial_nos_find_last` (BugFix-MRP)<br>`server action BugFix-MRP.server_action_1151_mass_produce_serial_numbers_create_original` (BugFix-MRP)<br>`server action BugFix-MRP.server_action_1153_mass_produce_serial_nos_find_last` (BugFix-MRP)<br>`server action BugFix-MRP.server_action_3202_mass_produce_serial_numbers_cancel_serial_no` (BugFix-MRP)<details><summary>+2 more</summary>`x_mass_produce_serial.x_studio_last_serial_no_id` (BugFix-MRP)<br>`x_mass_produce_serial_.x_studio_lot_serial_id` (BugFix-MRP)</details>

**Summary:**

<!-- SUMMARY:model:stock.lot -->
This repo adds serial number generation settings to lots and serials (Serial No Prefix, Starting Serial No, Sequence Size) plus Production Order links, a currency, and several read-only columns such as cost, prices, warehouse and age in days. Many of these read-only fields have no compute in this repo and stay empty, and several leftover Studio related fields are unused. It adds an Inventory Holding Days lots list with these columns and a multi-company record rule.
<!-- /SUMMARY -->

**Fields (20):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_currency_id` | Currency | many2one → `res.currency` | Currency of the lot's product valuation, taken from the product's stock valuation layers (related `product_id.stock_valuation_layer_ids.currency_id`). | related `product_id.stock_valuation_layer_ids.currency_id`; not stored | `model res.currency` (base)<br>`product.product.stock_valuation_layer_ids` (stock_account)<br>`stock.lot.product_id` (stock)<br>`stock.valuation.layer.currency_id` (stock_account) | `default BugFix-Stock.default_362_stock_lot_x_currency_id` |
| `x_studio_cost` | Cost | float | Read-only cost value on the lot/serial, shown in the lots list; this repo declares no compute for it. | stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_no_of_days` | No of Days | char | Read-only 'No of Days' text shown in the lots list; non-stored with no compute in this repo, so it is always empty. | not stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_no_of_days_2` | No of Days 2 | integer | Read-only integer 'No of Days' shown in the lots list; has a default value but no compute in this repo. | stored |  | `default BugFix-Stock.default_359_stock_lot_x_studio_no_of_days_2`<br>`view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_price_1` | Price 1 | char | Read-only 'Price 1' text shown in the lots list; non-stored with no compute in this repo, so it is always empty. | not stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_price_2` | Price 2 | char | Read-only 'Price 2' text shown in the lots list; non-stored with no compute in this repo, so it is always empty. | not stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_production_id` | Production Order | many2one → `mrp.production` | Manufacturing order that produced this lot/serial; shown in the lots list. | stored | `model mrp.production` (mrp) | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_production_order` | Production Order | char | Production order reference stored as text on the lot/serial; shown in the lots list. | stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_related_field_IlrRW` | New Related Field | char | Leftover Studio related field (text); its source path was not ported, it is non-stored and unused, so it is always empty. | not stored |  |  |
| `x_studio_related_field_KzAMe` | New Related Field | char | Leftover Studio related field (text); its source path was not ported, it is non-stored and unused, so it is always empty. | not stored |  |  |
| `x_studio_related_field_Vz7B8` | New Related Field | char | Leftover Studio related field (text), stored read-only without its source path; not used by any view or logic. | stored |  |  |
| `x_studio_related_field_bz0VM` | New Related Field | boolean | Leftover Studio related field (checkbox), stored read-only without its source path; not used by any view or logic. | stored |  |  |
| `x_studio_related_field_e2LSH` | New Related Field | integer | Leftover Studio related field (integer), stored read-only without its source path; not used by any view or logic. | stored |  |  |
| `x_studio_related_field_fTaKf` | New Related Field | char | Leftover Studio related field (text); its source path was not ported, it is non-stored and unused, so it is always empty. | not stored |  |  |
| `x_studio_related_field_jS93T` | New Related Field | integer | Leftover Studio related field (integer), stored read-only without its source path; not used by any view or logic. | stored |  |  |
| `x_studio_related_field_vTORT` | New Related Field | char | Leftover Studio related field (text); its source path was not ported, it is non-stored and unused, so it is always empty. | not stored |  |  |
| `x_studio_sequence_size` | Sequence Size | integer | Number of digits used when generating serial numbers for the lot; has a default and is shown in the lots list. | stored |  | `default BugFix-Stock.default_89_stock_lot_x_studio_sequence_size`<br>`view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_serial_no_prefix` | Serial No Prefix | char | Prefix used when generating serial numbers; shown in the lots list. | stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_starting_serial_no` | Starting Serial No | integer | First number of the serial-number range to generate; has a default and is shown in the lots list. | stored |  | `default BugFix-Stock.default_90_stock_lot_x_studio_starting_serial_no`<br>`view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |
| `x_studio_warehouse` | Warehouse | char | Read-only warehouse name text on the lot/serial, shown in the lots list; no compute in this repo. | stored |  | `view BugFix-Stock.ported_view_2597_studio_stock_production_lot_tree` |

**Window actions (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inventory Holding Days | `aw_f4_stock_lot_inventory_holding_days` | Opens **Lot/Serial** records (tree,form). | `model stock.lot` (stock) |  |
| Inventory Holding Days | `action_2225_inventory_holding_days` | Opens **Lot/Serial** records (tree,form). | `model stock.lot` (stock) | `menu BugFix-Stock.menu_1072_inventory_holding_days` |
| Inventory Holding Days | `act_window_2225_inventory_holding_days` | Opens **Lot/Serial** records (tree,form). | `model stock.lot` (stock) | `menu BugFix-Stock.menu_f6_inventory_holding_days` |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.production.lot.tree customization | `ported_view_2597_studio_stock_production_lot_tree` | tree | after `//field[@name='product_id']`: add field x_studio_cost, field x_studio_price_1, field x_studio_price_2, field x_studio_serial_no_prefix, field x_studio_sequence_size, field x_studio_starting_serial_no, field product_uom_id, field product_qty, field x_studio_warehouse, field x_studio_production_id, field x_studio_production_order; after `//field[@name='create_date']`: add field x_studio_no_of_days, field x_studio_no_of_days_2 | Adds cost, price 1/2, UoM, quantity, warehouse, production order and age-in-days columns to the Lots/Serial Numbers list, with serial-generation fields hidden. | `stock.lot.product_qty` (stock)<br>`stock.lot.product_uom_id` (stock)<br>`stock.lot.x_studio_cost`<br>`stock.lot.x_studio_no_of_days_2`<br>`stock.lot.x_studio_no_of_days`<details><summary>+9 more</summary>`stock.lot.x_studio_price_1`<br>`stock.lot.x_studio_price_2`<br>`stock.lot.x_studio_production_id`<br>`stock.lot.x_studio_production_order`<br>`stock.lot.x_studio_sequence_size`<br>`stock.lot.x_studio_serial_no_prefix`<br>`stock.lot.x_studio_starting_serial_no`<br>`stock.lot.x_studio_warehouse`<br>`view stock.view_production_lot_tree` (stock)</details> |  |

**Access rights (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Administrator | `access_7201_administrator` | Gives **Manufacturing / Administrator** read/write/create/delete access to Lot/Serial records. | `group mrp.group_mrp_manager` (mrp)<br>`model stock.lot` (stock) |  |
| Jin - Administrator | `access_7202_jin___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Lot/Serial records. | `group stock.group_stock_manager` (stock)<br>`model stock.lot` (stock) |  |
| User | `access_6087_user` | Gives **Helpdesk / User** read/write/create access to Lot/Serial records. | `group helpdesk.group_helpdesk_user` (helpdesk)<br>`model stock.lot` (stock) |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Stock Production Lot multi-company | `rule_47_stock_production_lot_multi_company` | For everyone (global rule): read/write/create/delete on Lot/Serial only where `[('company_id','in', company_ids)]`. | `model stock.lot` (stock)<br>`stock.lot.company_id` (stock) |  |
