# BugFix-Stock — `stock.landed.cost`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.landed.cost` — Stock Landed Cost

*Extends a model created by `stock_landed_costs`.*

Other repos that use this model: `server action BugFix-Studio-Misc.server_action_2799_mst_odoo_data_clean_up` (BugFix-Studio-Misc)<br>`window action BugFix-Studio-Misc.act_window_2813_stock_landed_cos_d7` (BugFix-Studio-Misc)

**Summary:**

<!-- SUMMARY:model:stock.landed.cost -->
This repo adds one form customisation that makes the Vendor Bill on a landed cost read-only once the landed cost is no longer in Draft. It adds no fields or logic.
<!-- /SUMMARY -->

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.landed.cost.form customization | `ported_view_4892_studio_stock_landed_cost_form` | form | set force_save=True, readonly=state != 'draft' on `//field[@name='vendor_bill_id']` | Makes the Vendor Bill on the Landed Cost form read-only once the cost is no longer Draft (value still saved). | `view stock_landed_costs.view_stock_landed_cost_form` (stock_landed_costs) |  |
