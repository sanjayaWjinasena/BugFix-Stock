# BugFix-Stock — `stock.route`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.route` — Inventory Routes

*Extends a model created by `stock`.*

Other repos that use this model: `window action BugFix-Studio-Misc.act_window_2095_stock_location_route_d7` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2494_inventory_routes_d7` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:stock.route -->
This repo adds optional ID, Products, Supplying and Supplied Warehouse columns to the routes list and two window actions. It adds no fields or logic.
<!-- /SUMMARY -->

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inventory routes | `act_window_2494_inventory_routes` | Opens **Inventory Routes** records (tree,form). | `model stock.route` (stock) |  |
| stock.location.route | `act_window_2095_stock_location_route` | Opens **Inventory Routes** records (tree,form). | `model stock.route` (stock) |  |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.location.route.tree customization | `ported_view_4866_studio_stock_route_tree` | tree | after `//field[@name='sequence']`: add field id, field product_ids; after `//tree[1]/field[@name='name']`: add field supplier_wh_id, field supplied_wh_id | Adds ID, Products, Supplying and Supplied Warehouse columns (optional) to the Routes list. | `stock.route.product_ids` (stock)<br>`stock.route.supplied_wh_id` (stock)<br>`stock.route.supplier_wh_id` (stock)<br>`view stock.stock_location_route_tree` (stock) |  |
