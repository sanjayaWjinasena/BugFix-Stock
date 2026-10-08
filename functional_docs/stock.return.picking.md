# BugFix-Stock — `stock.return.picking`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.return.picking` — Return Picking

*Extends a model created by `stock`.* Python: `models/stock_return_picking.py`.

Other repos that use this model: `helpdesk.ticket.fix_repair_action_direct_dispatch()` (Fix-repair)<br>`helpdesk.ticket.fix_repair_action_direct_return()` (Fix-repair)

**Summary:**

<!-- SUMMARY:model:stock.return.picking -->
This repo adds repair return support to the Return wizard: flags for RUG repairs and normal repairs with or without a serial number, and suggested return locations for each of two companies. An automation blocks a ticket-linked RUG or serial-number repair return unless the return location matches the suggested one, and a RUG Return from Help desk button validates the user's locations before processing the return. The wizard form shows these fields and makes the source transfer read-only for repair returns.
<!-- /SUMMARY -->

**Fields (5):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_repair_normal_with_serial_no` | Repair – Normal with Serial No | boolean | Read-only flag on the Return wizard for normal repairs with a serial number; used by the 'Auto Select Product for RUG Repairs' action. Non-stored with no compute here. | not stored |  | `server action BugFix-Stock.sa_f5_stock_return_picking_rr_auto_select_product_for_rug_repairs_3`<br>`server action BugFix-Stock.server_action_1991_rr_auto_select_product_for_rug_repairs_3`<br>`view BugFix-Stock.ported_view_4617_studio_stock_return_picking_form` |
| `x_studio_repair_normal_without_serial_no` | Repair – Normal without Serial No | boolean | Read-only flag on the Return wizard for normal repairs without a serial number; shown on the wizard form. | stored |  | `view BugFix-Stock.ported_view_4617_studio_stock_return_picking_form` |
| `x_studio_repair_rug` | Repair – RUG | boolean | Read-only flag on the Return wizard indicating a RUG repair return; used by the 'Auto Select Product for RUG Repairs' action. Non-stored with no compute here. | not stored |  | `server action BugFix-Stock.sa_f5_stock_return_picking_rr_auto_select_product_for_rug_repairs_3`<br>`server action BugFix-Stock.server_action_1991_rr_auto_select_product_for_rug_repairs_3`<br>`view BugFix-Stock.ported_view_4617_studio_stock_return_picking_form` |
| `x_studio_suggested_location_id` | Suggested Location | many2one → `stock.location` | Suggested return location on the Return wizard, set by the RUG repair return actions. | stored | `model stock.location` (stock) | `server action BugFix-Stock.sa_f5_stock_return_picking_rr_auto_select_product_for_rug_repairs_3`<br>`server action BugFix-Stock.server_action_1991_rr_auto_select_product_for_rug_repairs_3`<br>`server action BugFix-Stock.server_action_1997_rr_rug_return_from_help_desk`<br>`view BugFix-Stock.ported_view_4619_studio_stock_return_picking_form_2` |
| `x_studio_suggested_location_id_1` | Suggested Location (Company 2) | many2one → `stock.location` | Suggested return location for the second company on the Return wizard, set by the RUG repair return actions. | stored | `model stock.location` (stock) | `server action BugFix-Stock.sa_f5_stock_return_picking_rr_auto_select_product_for_rug_repairs_3`<br>`server action BugFix-Stock.server_action_1991_rr_auto_select_product_for_rug_repairs_3`<br>`server action BugFix-Stock.server_action_1997_rr_rug_return_from_help_desk`<br>`view BugFix-Stock.ported_view_4619_studio_stock_return_picking_form_2` |

**Server actions (3):**

- **Execute Code** (`server_action_1991_rr_auto_select_product_for_rug_repairs_3`, type `code`)
  - Function: On a ticket-linked return for RUG or serial-numbered repairs, raises an error unless the Return Location equals the Suggested Return Location (company-specific field for company 1 vs others); run by the matching automation.
  - Depends on: `model helpdesk.ticket` (helpdesk), `model res.company` (base), `model stock.return.picking` (stock), `stock.return.picking.location_id` (stock), `stock.return.picking.ticket_id` (helpdesk_stock)<details><summary>+4 more</summary>`stock.return.picking.x_studio_repair_normal_with_serial_no`, `stock.return.picking.x_studio_repair_rug`, `stock.return.picking.x_studio_suggested_location_id_1`, `stock.return.picking.x_studio_suggested_location_id`</details>
  - Used by: `automation BugFix-Stock.base_automation_174_rr_auto_select_product_for_rug_repairs_3`
  <details><summary>code (16 lines)</summary>

```python

if record.ticket_id:
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  if (record.x_studio_repair_rug == True or record.x_studio_repair_normal_with_serial_no == True):
    if company.id == 1:
      ticket = env['helpdesk.ticket'].search([('id', '=', record.ticket_id.id),('company_id', '=', company.id)],limit=1)
      if ticket:
        if record.location_id.id != record.x_studio_suggested_location_id.id:
          raise UserError("Return Location should be equal to Suggested Return Location.")
    else:
      ticket = env['helpdesk.ticket'].search([('id', '=', record.ticket_id.id),('company_id', '=', company.id)],limit=1)
      if ticket:
        if record.location_id.id != record.x_studio_suggested_location_id_1.id:
          raise UserError('Return Location should be equal to Suggested Return Location.')
```
  </details>
- **RR - Auto Select Product for RUG Repairs-3** (`sa_f5_stock_return_picking_rr_auto_select_product_for_rug_repairs_3`, type `code`)
  - Function: On a return wizard linked to a helpdesk ticket and flagged as RUG or serial-number repair, raises an error unless the return location equals the Suggested Return Location (a different suggested-location field is checked for company 1 vs other companies). Despite its name it selects no product.
  - Depends on: `model helpdesk.ticket` (helpdesk), `model res.company` (base), `model stock.return.picking` (stock), `stock.return.picking.location_id` (stock), `stock.return.picking.ticket_id` (helpdesk_stock)<details><summary>+4 more</summary>`stock.return.picking.x_studio_repair_normal_with_serial_no`, `stock.return.picking.x_studio_repair_rug`, `stock.return.picking.x_studio_suggested_location_id_1`, `stock.return.picking.x_studio_suggested_location_id`</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (15 lines)</summary>

```python
if record.ticket_id:
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)
  
  if (record.x_studio_repair_rug == True or record.x_studio_repair_normal_with_serial_no == True):
    if company.id == 1:
      ticket = env['helpdesk.ticket'].search([('id', '=', record.ticket_id.id),('company_id', '=', company.id)],limit=1)
      if ticket:
        if record.location_id.id != record.x_studio_suggested_location_id.id:
          raise UserError("Return Location should be equal to Suggested Return Location.")
    else:
      ticket = env['helpdesk.ticket'].search([('id', '=', record.ticket_id.id),('company_id', '=', company.id)],limit=1)
      if ticket:
        if record.location_id.id != record.x_studio_suggested_location_id_1.id:
          raise UserError('Return Location should be equal to Suggested Return Location.')
```
  </details>
- **RR - RUG Return from Help desk** (`server_action_1997_rr_rug_return_from_help_desk`, type `code`)
  - Function: Button on the return wizard for RUG returns from a helpdesk ticket: validates user virtual/source locations, suggested return location and qty 1 per line, then creates a receipt transfer with a move and serial-numbered move line for the ticket product, links it to the ticket and opens it.
  - Depends on: `model helpdesk.ticket` (helpdesk), `model procurement.group` (stock), `model res.company` (base), `model stock.location` (stock), `model stock.move.line` (stock)<details><summary>+12 more</summary>`model stock.move` (stock), `model stock.picking.type` (stock), `model stock.picking` (stock), `model stock.return.picking` (stock), `stock.return.picking.location_id` (stock), `stock.return.picking.partner_id` (helpdesk_stock), `stock.return.picking.picking_id` (stock), `stock.return.picking.product_return_moves` (stock), `stock.return.picking.sale_order_id` (helpdesk_stock), `stock.return.picking.ticket_id` (helpdesk_stock), `stock.return.picking.x_studio_suggested_location_id_1`, `stock.return.picking.x_studio_suggested_location_id`</details>
  - Used by: `view BugFix-Stock.ported_view_4619_studio_stock_return_picking_form_2`
  <details><summary>code (56 lines)</summary>

```python
if record.id:
  company_id = env.context.get('allowed_company_ids', [env.user.company_id.id])[0]
  company = env['res.company'].browse(company_id)

  if company.id == 1:
    if record.ticket_id.x_studio_virtual_location == False or record.ticket_id.x_studio_source_location == False:
      raise UserError('Virtual & Source Locations must be setup for Current Logged in User.')
    
    if record.location_id.id != record.x_studio_suggested_location_id.id:
      raise UserError('Return Location should be equal to Suggested Return Location.')
  else:
    if record.ticket_id.x_studio_virtual_location_1 == False or record.ticket_id.x_studio_source_location_1 == False:
      raise UserError('Virtual & Source Locations must be setup for Current Logged in User.')
    
    if record.location_id.id != record.x_studio_suggested_location_id_1.id:
      raise UserError('Return Location should be equal to Suggested Return Location.')
  
  for qtys in record.product_return_moves:
    if qtys.quantity != 1:
      raise UserError('Quantity should be 1 for all the return lines.' )
    
  source_loc = env['stock.location'].search([('usage', '=', 'customer')],limit=1)
  if source_loc:
    if company.id == 1:
      opt_type = env['stock.picking.type'].search([('default_location_dest_id', '=', record.ticket_id.x_studio_return_receipt_location.id),('code', '=', 'incoming'),('name', '=', 'Returns'),('company_id', '=', company.id)],limit=1)
    else:
      opt_type = env['stock.picking.type'].search([('default_location_dest_id', '=', record.ticket_id.x_studio_return_receipt_location.id),('code', '=', 'incoming'),('name', '=', 'Receipts'),('company_id', '=', company.id)],limit=1)
    
    if opt_type:
     #prod_move = env['stock.picking'].create({'x_studio_created_from_help_ticket':record.ticket_id.id,'picking_type_id':opt_type.id,'location_id':source_loc.id,'location_dest_id':record.location_id.id,'origin':('Return of '+ record.picking_id.name),'partner_id':record.partner_id.id})
     prod_move = env['stock.picking'].create({'x_studio_helpdesk_ticket_id':record.ticket_id.id,'picking_type_id':opt_type.id,'location_id':source_loc.id,'location_dest_id':record.location_id.id,'origin':('Return of '+ record.picking_id.name),'partner_id':record.partner_id.id,'company_id':company.id})
     
     
     update_prod_move = env['stock.picking'].search([('id', '=', prod_move.id),('company_id', '=', company.id)],limit=1)
     if update_prod_move:
      pro_group = env['procurement.group'].search([('sale_id', '=', record.sale_order_id.id)],limit=1)
      stock_move = env['stock.move'].create({'picking_id':update_prod_move.id,'name':('New Move:'+record.ticket_id.product_id.name),'reference':update_prod_move.name,'picking_type_id':update_prod_move.picking_type_id.id,'product_id':record.ticket_id.product_id.id,'location_id':update_prod_move.location_id.id,'location_dest_id':update_prod_move.location_dest_id.id,'product_uom_qty':1.00,'product_uom':record.ticket_id.product_id.uom_id.id,'state':'assigned','group_id':pro_group.id,'company_id':company.id}) 
      stock_move_line = env['stock.move.line'].create({'move_id':stock_move.id,'picking_id':update_prod_move.id,'picking_type_id':update_prod_move.picking_type_id.id,'product_id':record.ticket_id.product_id.id,'product_uom_id':record.ticket_id.product_id.uom_id.id,'location_id':update_prod_move.location_id.id,'location_dest_id':update_prod_move.location_dest_id.id,'lot_id':record.ticket_id.x_studio_serial_no.id,'qty_done':1.00,'company_id':company.id}) 
      
      update_ticket = env['helpdesk.ticket'].search([('id', '=', record.ticket_id.id),('company_id', '=', company.id)],limit=1)
      if update_ticket:
        update_ticket.write({'picking_ids':[(4, update_prod_move.id)]})
        
      action = {
              'name': 'Return',
              'domain': [('id', '=', update_prod_move.id)],
              'type': 'ir.actions.act_window',
              'res_model': 'stock.picking',
              'view_mode': 'tree,form',
              'view_type': 'form',
              'view_id': False,
              'context': False,
              }
      
    else:
      raise UserError('The selected return receipt location is not correct.')
```
  </details>
**Automations (1):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| RR - Auto Select Product for RUG Repairs-3 | `base_automation_174_rr_auto_select_product_for_rug_repairs_3` |  | When a record is created or updated on Return Picking, runs _Execute Code_. | `model stock.return.picking` (stock)<br>`server action BugFix-Stock.server_action_1991_rr_auto_select_product_for_rug_repairs_3` |  |

**Views (2):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: Return customization | `ported_view_4617_studio_stock_return_picking_form` | form | after `//field[@name='ticket_id']`: add field x_studio_repair_rug, field x_studio_repair_normal_with_serial_no, field x_studio_repair_normal_without_serial_no; set readonly=(x_studio_repair_normal_without_serial_no != False) or ((x_studio_repair_normal_with_serial_no != False) or (x_studio_repair_rug != False)), required=ticket_id != False on `//field[@name='picking_id']` | On the helpdesk Return wizard adds hidden repair-type flags, makes the source transfer read-only for repair returns and required when a ticket is set. | `stock.return.picking.x_studio_repair_normal_with_serial_no`<br>`stock.return.picking.x_studio_repair_normal_without_serial_no`<br>`stock.return.picking.x_studio_repair_rug`<br>`view helpdesk_stock.view_stock_return_picking_form_inherit_helpdesk_stock` (helpdesk_stock) |  |
| Odoo Studio: Return lines customization-2 | `ported_view_4619_studio_stock_return_picking_form_2` | form | before `//field[@name='location_id']`: add field x_studio_suggested_location_id, field x_studio_suggested_location_id_1; after `//footer/button[@name='create_returns']`: add button 'Return' | On the Return wizard adds the Suggested Return Location (company-specific field for company 1 or 2) and a 'Return' button for ticket returns. Button uses hardcoded action id 2006, which may not exist on a fresh install. | `server action BugFix-Stock.server_action_1997_rr_rug_return_from_help_desk`<br>`stock.return.picking.company_id` (stock)<br>`stock.return.picking.ticket_id` (helpdesk_stock)<br>`stock.return.picking.x_studio_suggested_location_id_1`<br>`stock.return.picking.x_studio_suggested_location_id`<details><summary>+1 more</summary>`view stock.view_stock_return_picking_form` (stock)</details> |  |

**Access rights (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Inv - Administrator | `access_6272_inv___administrator` | Gives **Inventory / Administrator** read/write/create/delete access to Return Picking records. | `group stock.group_stock_manager` (stock)<br>`model stock.return.picking` (stock) |  |
