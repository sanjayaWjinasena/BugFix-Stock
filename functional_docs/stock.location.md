# BugFix-Stock — `stock.location`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.location` — Inventory Locations

*Extends a model created by `stock`.* Python: `models/stock_location.py`, `models/stock_location_gap.py`.

Other repos that use this model: `helpdesk.ticket._compute_has_return_picking()` (Fix-repair)<br>`helpdesk.ticket._compute_user_location_validation()` (Fix-repair)<br>`helpdesk.ticket._get_factory_repair_location()` (Fix-repair)<br>`helpdesk.ticket._get_so_from_serial()` (Fix-repair)<br>`helpdesk.ticket._repair_auto_select_product_for_rug()` (Fix-repair)<br>`helpdesk.ticket._repair_auto_select_product_for_rug_no_company()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_route()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_auto_create_repair_serial_nos()` (Fix-repair)<details><summary>+26 more</summary>`helpdesk.ticket._repair_studio_send_to_factory()` (Fix-repair)<br>`helpdesk.ticket._repair_studio_user_location_validation()` (Fix-repair)<br>`helpdesk.ticket.repair_location` (Fix-repair)<br>`helpdesk.ticket.return_receipt_location` (Fix-repair)<br>`helpdesk.ticket.source_location_1` (Fix-repair)<br>`helpdesk.ticket.source_location` (Fix-repair)<br>`helpdesk.ticket.virtual_location_1` (Fix-repair)<br>`helpdesk.ticket.virtual_location` (Fix-repair)<br>`mrp.production.finished_product_location` (BugFix-MRP)<br>`project.task._compute_valid_delivered_so()` (Fix-repair)<br>`res.config.settings.factory_repair_location_id` (Fix-repair)<br>`res.config.settings.get_values()` (Fix-repair)<br>`res.config.test.factory_repair_location_id` (Fix-repair)<br>`res.users.many2many_field_Q50dg` (studio_usermodel_migration)<br>`res.users.many2many_field_bQRSA` (studio_usermodel_migration)<br>`res.users.source_location_1` (studio_usermodel_migration)<br>`res.users.source_location` (studio_usermodel_migration)<br>`res.users.virtual_location_1` (studio_usermodel_migration)<br>`res.users.virtual_location` (studio_usermodel_migration)<br>`sale.order._get_repair_stock_source_locations()` (Fix-repair)<br>`server action BugFix-MRP.action_finished_products_location_updated` (BugFix-MRP)<br>`server action BugFix-Purchase.action_create_material_transfer` (BugFix-Purchase)<br>`stock.picking._fix_repair_compute_user_location_validation()` (Fix-repair)<br>`stock.return.picking.default_get()` (Fix-repair)<br>`stock.warehouse._ensure_child_location()` (Fix-repair)<br>`rm_production_orders.warehouse` (BugFix-Accounting)</details>

**Summary:**

<!-- SUMMARY:model:stock.location -->
This repo adds location settings used by repairs and access control: Repair Return Location, Repair Factory Location, Finished Good Location and Temp Location flags, a Return Receipt Location, a Return Sequence for return transfers, and user lists for stock locations and internal transfers that the transfer User Location Validation checks against. These fields are added to the location form and list, and the repo ships location multi-company and stock data record rules.
<!-- /SUMMARY -->

**Fields (10):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `color` | Color | integer | Color index for the location; not used by any view or logic in this repo. | stored |  |  |
| `finished_good_location` | Finished Good Location | boolean | Checkbox marking the location as a finished-goods location; set on the location form and shown in the locations list. | stored |  | `view BugFix-Stock.view_stock_location_form_inherit`<br>`view BugFix-Stock.view_stock_location_tree_inherit` |
| `many2many_field_7kpUe` | Users (Scope 7kpUe) | many2many → `res.users` | List of users linked to the location (labelled 'Users (Cell Visibility)' in code); maintained on the location form. | stored | `model res.users` (base) | `view BugFix-Stock.view_stock_location_form_inherit` |
| `repair_factory_location` | Repair Factory Location | boolean | Checkbox marking the location as the repair factory location; set on the location form and shown in the locations list. | stored |  | `view BugFix-Stock.view_stock_location_form_inherit`<br>`view BugFix-Stock.view_stock_location_tree_inherit` |
| `repair_return_location` | Repair Return Location | boolean | Checkbox marking the location as a repair return location; set on the location form and shown in the locations list. | stored |  | `view BugFix-Stock.view_stock_location_form_inherit`<br>`view BugFix-Stock.view_stock_location_tree_inherit` |
| `return_receipt_location` | Return Receipt Location | many2one → `stock.location` | Location to which repaired items from this location are returned/received; configured on the location form. | stored | `model stock.location` (stock) | `view BugFix-Stock.view_stock_location_form_inherit` |
| `return_sequence` | Return Sequence | many2one → `ir.sequence` | Sequence used to number return transfers for this location; configured on the location form. | stored | `model ir.sequence` (base) | `view BugFix-Stock.view_stock_location_form_inherit` |
| `temp_location` | Temp Location | boolean | Checkbox marking the location as a temporary location; set on the location form and shown in the locations list. | stored |  | `view BugFix-Stock.view_stock_location_form_inherit`<br>`view BugFix-Stock.view_stock_location_tree_inherit` |
| `users_internal_transfer` | Users (Internal Transfer) | many2many → `res.users` | Users allowed to receive internal transfers into this location; checked by the transfer User Location Validation and used to filter the Internal Locations menu action. | stored | `model res.users` (base) | `view BugFix-Stock.view_stock_location_form_inherit`<br>`window action BugFix-Stock.action_internal_locations_2`<br>`window action BugFix-Stock.action_internal_locations`<br>`window action BugFix-Stock.aw_f4_stock_location_internal_locations` |
| `users_stock_location` | Users (Stock Location) | many2many → `res.users` | Users assigned to this stock location; checked by the transfer User Location Validation for deliveries/receipts and used to filter the Stock Locations menu action. | stored | `model res.users` (base) | `view BugFix-Stock.view_stock_location_form_inherit`<br>`window action BugFix-Stock.action_stock_locations_2`<br>`window action BugFix-Stock.action_stock_locations`<br>`window action BugFix-Stock.aw_f4_stock_location_stock_locations` |

**Window actions (12):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Internal Locations | `aw_f4_stock_location_internal_locations` | Opens **Inventory Locations** records (tree,form), filtered to `[('users_internal_transfer', '=', active_id)]`. | `model stock.location` (stock)<br>`stock.location.users_internal_transfer` |  |
| Internal Locations | `action_internal_locations` | Opens **Inventory Locations** records (tree,form), filtered to `[('users_internal_transfer', '=', active_id)]`. | `model stock.location` (stock)<br>`stock.location.users_internal_transfer` |  |
| Internal Locations | `action_internal_locations_2` | Opens **Inventory Locations** records (tree,form), filtered to `[('users_internal_transfer', '=', active_id)]`. | `model stock.location` (stock)<br>`stock.location.users_internal_transfer` |  |
| Location | `aw_f4_stock_location_location` | Opens **Inventory Locations** records (tree,form). | `model stock.location` (stock) |  |
| Location | `action_location` | Opens **Inventory Locations** records (tree,form). | `model stock.location` (stock) | `menu BugFix-Stock.menu_location_2` |
| Location | `action_location_2` | Opens **Inventory Locations** records (tree,form). | `model stock.location` (stock) | `menu BugFix-Stock.menu_location` |
| Stock Locations | `aw_f4_stock_location_stock_locations` | Opens **Inventory Locations** records (tree,form), filtered to `[('users_stock_location', '=', active_id)]`. | `model stock.location` (stock)<br>`stock.location.users_stock_location` |  |
| Stock Locations | `action_stock_locations` | Opens **Inventory Locations** records (tree,form), filtered to `[('users_stock_location', '=', active_id)]`. | `model stock.location` (stock)<br>`stock.location.users_stock_location` |  |
| Stock Locations | `action_stock_locations_2` | Opens **Inventory Locations** records (tree,form), filtered to `[('users_stock_location', '=', active_id)]`. | `model stock.location` (stock)<br>`stock.location.users_stock_location` |  |
| stock.location | `aw_f4_stock_location_stock_location` | Opens **Inventory Locations** records (tree,form). | `model stock.location` (stock) |  |
| stock.location | `action_stock_location` | Opens **Inventory Locations** records (tree,form). | `model stock.location` (stock) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_location` (BugFix-Studio-Misc) |
| stock.location | `action_stock_location_2` | Opens **Inventory Locations** records (tree,form). | `model stock.location` (stock) |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.location.form customization | `view_stock_location_form_inherit` | form | set edit=true on `//form[1]`; after `//field[@name='return_location']`: add field repair_return_location, field repair_factory_location, field finished_good_location, field temp_location, field return_receipt_location, field return_sequence, field many2many_field_7kpUe, field users_internal_transfer, field users_stock_location | Adds location flags and settings to the Location form after Return Location: repair return/factory, finished good, temp, return receipt (hidden), return sequence, and allowed-user lists for internal transfers and stock location. | `stock.location.finished_good_location`<br>`stock.location.many2many_field_7kpUe`<br>`stock.location.repair_factory_location`<br>`stock.location.repair_return_location`<br>`stock.location.return_receipt_location`<details><summary>+5 more</summary>`stock.location.return_sequence`<br>`stock.location.temp_location`<br>`stock.location.users_internal_transfer`<br>`stock.location.users_stock_location`<br>`view stock.view_location_form` (stock)</details> |  |
| Odoo Studio: stock.location.tree customization | `view_stock_location_tree_inherit` | tree | set invisible= on `//field[@name='active']`; after `//field[@name='complete_name']`: add field barcode; after `//field[@name='usage']`: add field repair_return_location, field repair_factory_location, field finished_good_location, field temp_location, field id | Adds barcode, repair return/factory, finished good, temp location flags and ID columns to the Locations list and clears the active field's invisibility. | `stock.location.barcode` (stock)<br>`stock.location.finished_good_location`<br>`stock.location.repair_factory_location`<br>`stock.location.repair_return_location`<br>`stock.location.temp_location`<details><summary>+1 more</summary>`view stock.view_location_tree2` (stock)</details> |  |

**Record rules (3):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Location multi-company | `rule_49_location_multi_company` | For everyone (global rule): read/write/create/delete on Inventory Locations only where `[('company_id', 'in', company_ids + [False])]`. | `model stock.location` (stock)<br>`stock.location.company_id` (stock) |  |
| Stock data admin location | `rule_stock_data_admin_location` | For Inventory / Administrator: read/write/create/delete on Inventory Locations only where `[(1, '=', 1),]`. | `group stock.group_stock_manager` (stock)<br>`model stock.location` (stock) |  |
| Stock data restrict Location | `rule_stock_data_restrict_location` | For Inventory / Administrator: read/write/create/delete on Inventory Locations with no record filter (empty domain = all records). | `group stock.group_stock_manager` (stock)<br>`model stock.location` (stock) |  |
