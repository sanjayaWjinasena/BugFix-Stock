# BugFix-Stock — views to hand-port

34 views need hand-porting from Clear-DB. Do NOT 
auto-copy the arch — each has Studio xpath quirks that need 
human review before commit.

| # | Clear-DB view ID | Type | Target model | Name | Inherits |
|---|---|---|---|---|---|
| 1 | 2948 | dashboard | `x_consignment_header` | Default dashboard view for ir.model(905,) | — |
| 2 | 2811 | form | `x_consignment_header` | Default form view for x_consignment_header | — |
| 3 | 2814 | form | `x_consignment_line` | Default form view for x_consignment_line | — |
| 4 | 2949 | kanban | `x_consignment_header` | Default kanban view for ir.model(905,) | — |
| 5 | 2810 | tree | `x_consignment_header` | Default list view for x_consignment_header | — |
| 6 | 2813 | tree | `x_consignment_line` | Default list view for x_consignment_line | — |
| 7 | 2812 | search | `x_consignment_header` | Default search view for x_consignment_header | — |
| 8 | 2815 | search | `x_consignment_line` | Default search view for x_consignment_line | — |
| 9 | 2816 | form | `x_consignment_header` | Odoo Studio: Default form view for x_consignment_header customization | Default form view for x_consignment_header |
| 10 | 2817 | form | `x_consignment_line` | Odoo Studio: Default form view for x_consignment_line customization | Default form view for x_consignment_line |
| 11 | 2819 | tree | `x_consignment_header` | Odoo Studio: Default list view for x_consignment_header customization | Default list view for x_consignment_header |
| 12 | 2818 | tree | `x_consignment_line` | Odoo Studio: Default list view for x_consignment_line customization | Default list view for x_consignment_line |
| 13 | 5328 | form | `stock.picking.type` | Odoo Studio: Operation Types customization | Operation Types |
| 14 | 5334 | tree | `stock.picking.type` | Odoo Studio: Operation types customization | Operation types |
| 15 | 4617 | form | `stock.return.picking` | Odoo Studio: Return customization | Return |
| 16 | 4619 | form | `stock.return.picking` | Odoo Studio: Return lines customization-2 | Return lines |
| 17 | 4892 | form | `stock.landed.cost` | Odoo Studio: stock.landed.cost.form customization | stock.landed.cost.form |
| 18 | 2389 | form | `stock.location` | Odoo Studio: stock.location.form customization | stock.location.form |
| 19 | 4866 | tree | `stock.route` | Odoo Studio: stock.location.route.tree customization | stock.location.route.tree |
| 20 | 4616 | tree | `stock.location` | Odoo Studio: stock.location.tree customization | stock.location.tree |
| 21 | 3912 | tree | `stock.move.line` | Odoo Studio: stock.move.line.tree customization | stock.move.line.tree |
| 22 | 2579 | tree | `stock.move` | Odoo Studio: stock.move.tree2 customization | stock.move.tree2 |
| 23 | 2387 | form | `stock.picking` | Odoo Studio: stock.picking.form customization | stock.picking.form |
| 24 | 4732 | form | `stock.picking` | Odoo Studio: stock.picking.form_button | stock.picking.form |
| 25 | 6051 | tree | `stock.move` | Odoo Studio: stock.picking.move.tree customization | stock.picking.move.tree |
| 26 | 5299 | tree | `stock.picking` | Odoo Studio: stock.picking.tree customization | stock.picking.tree |
| 27 | 5288 | kanban | `stock.picking.type` | Odoo Studio: stock.picking.type.kanban customization | stock.picking.type.kanban |
| 28 | 2597 | tree | `stock.lot` | Odoo Studio: stock.production.lot.tree customization | stock.production.lot.tree |
| 29 | 5462 | tree | `stock.putaway.rule` | Odoo Studio: stock.putaway.rule.tree customization | stock.putaway.rule.tree |
| 30 | 6071 | tree | `stock.rule` | Odoo Studio: stock.rule.tree customization | stock.rule.tree |
| 31 | 2585 | tree | `stock.valuation.layer` | Odoo Studio: stock.valuation.layer.tree customization | stock.valuation.layer.tree |
| 32 | 5484 | form | `stock.warehouse` | Odoo Studio: stock.warehouse customization | stock.warehouse |
| 33 | 3943 | tree | `stock.warehouse` | Odoo Studio: stock.warehouse.tree customization | stock.warehouse.tree |
| 34 | 9609 | form | `x_consignment_header` | bugfix_purchase.x_consignment_header.form.rewire.vendor.dispatch | Default form view for x_consignment_header |
