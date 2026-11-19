# BugFix-Stock — `stock.valuation.layer`

[← back to Functional_Documentation.md](../Functional_Documentation.md)

### `stock.valuation.layer` — Stock Valuation Layer

*Extends a model created by `stock_account`.* Python: `models/stock_valuation_layer.py`, `models/stock_valuation_layer_gap.py`.

Other repos that use this model: `server action BugFix-Accounting.sa_f5_x_sales_report_model_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1144_work_center_costing_model_update_journal_entries` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1384_imp_post_tp_invoice` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1726_srm_auto_populate_data` (BugFix-Accounting)<br>`server action BugFix-Accounting.server_action_1763_srm_rpt_sales_production_purchase_report` (BugFix-Accounting)<br>`server action BugFix-Accounting.srv_tp_invoice_post` (BugFix-Accounting)

**Summary:**

<!-- SUMMARY:model:stock.valuation.layer -->
This repo adds related From and To locations and destination warehouse fields to valuation layers and shows From, To, description, unit cost, remaining value and journal entry columns in the valuation list. It also ships Work Center Costing Model actions that would post labour and overhead journal entries for manufactured products, but both of their automations are archived and do not run.
<!-- /SUMMARY -->

**Fields (4):**

| Field | Label | Type | Function | How it gets its value | Depends on | Used by |
|---|---|---|---|---|---|---|
| `x_studio_related_field_MfcOm` | New Related Field | char | Short code of the destination warehouse of the layer's stock move (related); not used by any view or logic. | related `stock_move_id.location_dest_id.warehouse_id.code`; not stored | `stock.location.warehouse_id` (stock)<br>`stock.move.location_dest_id` (stock)<br>`stock.valuation.layer.stock_move_id` (stock_account)<br>`stock.warehouse.code` (stock) |  |
| `x_studio_related_field_bPlxa` | From | many2one → `stock.location` | Source location of the valuation layer's stock move (related `stock_move_id.location_id`); shown as 'From' in the valuation list. | related `stock_move_id.location_id`; stored | `model stock.location` (stock)<br>`stock.move.location_id` (stock)<br>`stock.valuation.layer.stock_move_id` (stock_account) | `view BugFix-Stock.ported_view_2585_studio_stock_valuation_layer_tree` |
| `x_studio_related_field_dGINH` | New Related Field | many2one → `stock.warehouse` | Destination warehouse of the layer's stock move (related `stock_move_id.location_dest_id.warehouse_id`); not used by any view or logic. | related `stock_move_id.location_dest_id.warehouse_id`; not stored | `model stock.warehouse` (stock)<br>`stock.location.warehouse_id` (stock)<br>`stock.move.location_dest_id` (stock)<br>`stock.valuation.layer.stock_move_id` (stock_account) |  |
| `x_studio_related_field_ygmmJ` | To | many2one → `stock.location` | Destination location of the valuation layer's stock move (related `stock_move_id.location_dest_id`); shown as 'To' in the valuation list. | related `stock_move_id.location_dest_id`; stored | `model stock.location` (stock)<br>`stock.move.location_dest_id` (stock)<br>`stock.valuation.layer.stock_move_id` (stock_account) | `view BugFix-Stock.ported_view_2585_studio_stock_valuation_layer_tree` |

**Server actions (3):**

- **Update Product Cost - Work Center Cost** (`server_action_1141_update_product_cost_work_center_cost`, type `code`)
  - Function: Has no code; running it does nothing.
  - Depends on: `model stock.valuation.layer` (stock_account)
  - Used by: — (not linked to a button, menu or automation)
- **Work Center Costing Model - Create Journal Entries** (`server_action_1138_work_center_costing_model_create_journal_entries`, type `code`)
  - Function: For a finished-product valuation layer from a manufacturing order, creates and posts journal entries (journal id 6) for labour, labour OT and overhead costs using accounts and analytic tags from Work Center Costing record 1. Not referenced by any automation here.
  - Depends on: `model account.move` (account), `model mrp.bom` (mrp), `model mrp.production` (mrp), `model stock.move` (stock), `model stock.valuation.layer` (stock_account)<details><summary>+3 more</summary>`model x_work_center_costing` (BugFix-Studio-Misc), `stock.valuation.layer.product_tmpl_id` (stock_account), `stock.valuation.layer.stock_move_id` (stock_account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (116 lines)</summary>

```python
if record.product_tmpl_id:
  find_bom = env['mrp.bom'].search([('product_tmpl_id', '=', record.product_tmpl_id.id)],limit=1)
  if find_bom:
    ids = []
    ids2 = []
    ids3 = []
    ids4 = []
    if record.stock_move_id:
      stock_move = env['stock.move'].search([('id', '=', record.stock_move_id.id), ('product_tmpl_id', '=', record.product_tmpl_id.id)],limit=1)
      if stock_move:
        prod_order = env['mrp.production'].search([('id', '=', stock_move.production_id.id)],limit=1)
        if prod_order:
          ##########################JC
          work_center_costing = env['x_work_center_costing'].search([('id', '=', 1)], limit=1)
          if work_center_costing:
            if prod_order.x_studio_prod_bom_total_actual_labour_cost_without_ot > 0.0000:
              cost_lines=[]
              #ids =[work_center_costing.x_studio_labour_analytic_tag.id]
              if work_center_costing.x_studio_labour_analytic_tag != []:
                for idds in work_center_costing.x_studio_labour_analytic_tag:
                  ids.append(idds.id)
              cost_lines.append([0,0,{
                'account_id':work_center_costing.x_studio_labour_cost_debit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost'),
                'analytic_tag_ids':[(6, 0, ids)],
                'debit':prod_order.x_studio_prod_bom_total_actual_labour_cost_without_ot}])
          
              cost_lines.append([0,0,{
                'account_id':work_center_costing.x_studio_labour_cost_credit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost'),
                'analytic_tag_ids':[(6, 0, ids)],   
                'credit':prod_order.x_studio_prod_bom_total_actual_labour_cost_without_ot}])	
          
              labour_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Labour Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines})
              #######
              update_labour_cost_entry = env['account.move'].search([('id', '=', labour_cost_entry.id)],limit=1)
              if update_labour_cost_entry:
                update_labour_cost_entry.write({'state':'posted'})
              #######
            ######## - OT - Begin
            if prod_order.x_studio_prod_bom_total_actual_labour_cost_ot > 0.0000:
              cost_lines4=[]
              #ids4 =[work_center_costing.x_studio_labour_analytic_tag.id]
              if work_center_costing.x_studio_labour_analytic_tag != []:
                for idds in work_center_costing.x_studio_labour_analytic_tag:
                  ids4.append(idds.id)
              cost_lines4.append([0,0,{
                'account_id':work_center_costing.x_studio_labour_ot_cost_debit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost - OT'),
                'analytic_tag_ids':[(6, 0, ids4)],
                'debit':prod_order.x_studio_prod_bom_total_actual_labour_cost_ot}])
          
              cost_lines4.append([0,0,{
                'account_id':work_center_costing.x_studio_labour_ot_cost_credit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost - OT'),
                'analytic_tag_ids':[(6, 0, ids4)],   
                'credit':prod_order.x_studio_prod_bom_total_actual_labour_cost_ot}])	
          
              labour_cost_entry_ot = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Labour Cost - OT'),'journal_id':6,'move_type':'entry','line_ids':cost_lines4})
              #######
              update_labour_cost_entry_ot = env['account.move'].search([('id', '=', labour_cost_entry_ot.id)],limit=1)
              if update_labour_cost_entry_ot:
                update_labour_cost_entry_ot.write({'state':'posted'})
              #######  
            ######## - OT - End
            ########        
            if prod_order.x_studio_prod_bom_total_actual_overhead_cost > 0.0000:
              cost_lines2=[]
              #ids2 =[work_center_costing.x_studio_overhead_analytic_tag.id]
              if work_center_costing.x_studio_overhead_analytic_tag != []:
                for idds2 in work_center_costing.x_studio_overhead_analytic_tag:
                  ids2.append(idds2.id)
              cost_lines2.append([0,0,{
                'account_id':work_center_costing.x_studio_overhead_cost_debit_account.id,
                'name':(prod_order.name + ' - ' + 'Overhead Cost'),
                'analytic_tag_ids':[(6, 0, ids2)],
                'debit':prod_order.x_studio_prod_bom_total_actual_overhead_cost}])
              
              cost_lines2.append([0,0,{
                'account_id':work_center_costing.x_studio_overhead_cost_credit_account.id,
                'name':(prod_order.name + ' - ' + 'Overhead Cost'),
                'analytic_tag_ids':[(6, 0, ids2)],
                'credit':prod_order.x_studio_prod_bom_total_actual_overhead_cost}])	
              
              overhead_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Overhead Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines2})
              #######
              update_overhead_cost_entry = env['account.move'].search([('id', '=', overhead_cost_entry.id)],limit=1)
              if update_overhead_cost_entry:
                update_overhead_cost_entry.write({'state':'posted'})
              #######
            ########
            if prod_order.x_studio_total_actual_general_cost > 0.0000:
              cost_lines3=[]
              #ids3 =[work_center_costing.x_studio_general_analytic_tag.id]
              if work_center_costing.x_studio_general_analytic_tag != []:
                for idds3 in work_center_costing.x_studio_general_analytic_tag:
                  ids3.append(idds3.id)
              cost_lines3.append([0,0,{
                'account_id':work_center_costing.x_studio_general_cost_debit_account.id,
                'name':(prod_order.name + ' - ' + 'General Cost'),
                'analytic_tag_ids':[(6, 0, ids3)],
                'debit':prod_order.x_studio_total_actual_general_cost}])
              
              cost_lines3.append([0,0,{
                'account_id':work_center_costing.x_studio_general_cost_credit_account.id,
                'name':(prod_order.name + ' - ' + 'General Cost'),
                'analytic_tag_ids':[(6, 0, ids3)],
                'credit':prod_order.x_studio_total_actual_general_cost}])	
              
              general_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'General Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines3})
              #######
              update_general_cost_entry = env['account.move'].search([('id', '=', general_cost_entry.id)],limit=1)
              if update_general_cost_entry:
                update_general_cost_entry.write({'state':'posted'})
              #######
          ##########################JC
```
  </details>
- **Work Center Costing Model - Create Journal Entries - Original** (`server_action_2566_work_center_costing_model_create_journal_entries_original`, type `code`)
  - Function: Older 'Original' version of the work-center costing action: posts labour and overhead journal entries (no separate OT entry) for a manufacturing order's valuation layer. Not referenced by any automation here.
  - Depends on: `model account.move` (account), `model mrp.bom` (mrp), `model mrp.production` (mrp), `model stock.move` (stock), `model stock.valuation.layer` (stock_account)<details><summary>+3 more</summary>`model x_work_center_costing` (BugFix-Studio-Misc), `stock.valuation.layer.product_tmpl_id` (stock_account), `stock.valuation.layer.stock_move_id` (stock_account)</details>
  - Used by: — (not linked to a button, menu or automation)
  <details><summary>code (89 lines)</summary>

```python
if record.product_tmpl_id:
  find_bom = env['mrp.bom'].search([('product_tmpl_id', '=', record.product_tmpl_id.id)],limit=1)
  if find_bom:
    ids = []
    ids2 = []
    ids3 = []
    if record.stock_move_id:
      stock_move = env['stock.move'].search([('id', '=', record.stock_move_id.id), ('product_tmpl_id', '=', record.product_tmpl_id.id)],limit=1)
      if stock_move:
        prod_order = env['mrp.production'].search([('id', '=', stock_move.production_id.id)],limit=1)
        if prod_order:
          ##########################JC
          work_center_costing = env['x_work_center_costing'].search([('id', '=', 1)], limit=1)
          if work_center_costing:
            if prod_order.x_studio_prod_bom_total_actual_labour_cost > 0.0000:
              cost_lines=[]
              #ids =[work_center_costing.x_studio_labour_analytic_tag.id]
              if work_center_costing.x_studio_labour_analytic_tag != []:
                for idds in work_center_costing.x_studio_labour_analytic_tag:
                  ids.append(idds.id)
              cost_lines.append([0,0,{
                'account_id':work_center_costing.x_studio_labour_cost_debit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost'),
                'analytic_tag_ids':[(6, 0, ids)],
                'debit':prod_order.x_studio_prod_bom_total_actual_labour_cost}])
          
              cost_lines.append([0,0,{
                'account_id':work_center_costing.x_studio_labour_cost_credit_account.id,
                'name':(prod_order.name + ' - ' + 'Labour Cost'),
                'analytic_tag_ids':[(6, 0, ids)],   
                'credit':prod_order.x_studio_prod_bom_total_actual_labour_cost}])	
          
              labour_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Labour Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines})
              #######
              update_labour_cost_entry = env['account.move'].search([('id', '=', labour_cost_entry.id)],limit=1)
              if update_labour_cost_entry:
                update_labour_cost_entry.write({'state':'posted'})
              #######
          ########        
          if prod_order.x_studio_prod_bom_total_actual_overhead_cost > 0.0000:
            cost_lines2=[]
            #ids2 =[work_center_costing.x_studio_overhead_analytic_tag.id]
            if work_center_costing.x_studio_overhead_analytic_tag != []:
              for idds2 in work_center_costing.x_studio_overhead_analytic_tag:
                ids2.append(idds2.id)
            cost_lines2.append([0,0,{
              'account_id':work_center_costing.x_studio_overhead_cost_debit_account.id,
              'name':(prod_order.name + ' - ' + 'Overhead Cost'),
              'analytic_tag_ids':[(6, 0, ids2)],
              'debit':prod_order.x_studio_prod_bom_total_actual_overhead_cost}])
            
            cost_lines2.append([0,0,{
              'account_id':work_center_costing.x_studio_overhead_cost_credit_account.id,
              'name':(prod_order.name + ' - ' + 'Overhead Cost'),
              'analytic_tag_ids':[(6, 0, ids2)],
              'credit':prod_order.x_studio_prod_bom_total_actual_overhead_cost}])	
            
            overhead_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'Overhead Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines2})
            #######
            update_overhead_cost_entry = env['account.move'].search([('id', '=', overhead_cost_entry.id)],limit=1)
            if update_overhead_cost_entry:
              update_overhead_cost_entry.write({'state':'posted'})
            #######
          ########
          if prod_order.x_studio_total_actual_general_cost > 0.0000:
            cost_lines3=[]
            #ids3 =[work_center_costing.x_studio_general_analytic_tag.id]
            if work_center_costing.x_studio_general_analytic_tag != []:
              for idds3 in work_center_costing.x_studio_general_analytic_tag:
                ids3.append(idds3.id)
            cost_lines3.append([0,0,{
              'account_id':work_center_costing.x_studio_general_cost_debit_account.id,
              'name':(prod_order.name + ' - ' + 'General Cost'),
              'analytic_tag_ids':[(6, 0, ids3)],
              'debit':prod_order.x_studio_total_actual_general_cost}])
            
            cost_lines3.append([0,0,{
              'account_id':work_center_costing.x_studio_general_cost_credit_account.id,
              'name':(prod_order.name + ' - ' + 'General Cost'),
              'analytic_tag_ids':[(6, 0, ids3)],
              'credit':prod_order.x_studio_total_actual_general_cost}])	
            
            general_cost_entry = env['account.move'].create({'date':datetime.datetime.today(),'ref':(prod_order.name + ' - ' + 'General Cost'),'journal_id':6,'move_type':'entry','line_ids':cost_lines3})
            #######
            update_general_cost_entry = env['account.move'].search([('id', '=', general_cost_entry.id)],limit=1)
            if update_general_cost_entry:
              update_general_cost_entry.write({'state':'posted'})
            #######
          ##########################JC
```
  </details>
**Automations (2):**

| Name | Record name | State | Function | Depends on | Used by |
|---|---|---|---|---|---|
| Work Center Costing Model - Create Journal Entries | `base_automation_39_work_center_costing_model_create_journal_entries` | archived | When a record is created or updated on Stock Valuation Layer, runs nothing (no action linked). **Archived — does not run.** | `model stock.valuation.layer` (stock_account) |  |
| Work Center Costing Model - Create Journal Entries - Original | `base_automation_255_work_center_costing_model_create_journal_entries_original` | archived | When a record is created on Stock Valuation Layer, runs nothing (no action linked). **Archived — does not run.** | `model stock.valuation.layer` (stock_account) |  |

**Window actions (2):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| stock.valuation.layer | `aw_f4_stock_valuation_layer_stock_valuation_layer` | Opens **Stock Valuation Layer** records (tree,form,pivot). | `model stock.valuation.layer` (stock_account) |  |
| stock.valuation.layer | `act_window_2809_stock_valuation_layer` | Opens **Stock Valuation Layer** records (tree,form,pivot). | `model stock.valuation.layer` (stock_account) | `menu BugFix-Studio-Misc.menu_f6r2_test_app_05_stock_valuation_layer` (BugFix-Studio-Misc) |

**Views (1):**

| Name | Record name | Type | What it changes | Function | Depends on | Used by |
|---|---|---|---|---|---|---|
| Odoo Studio: stock.valuation.layer.tree customization | `ported_view_2585_studio_stock_valuation_layer_tree` | tree | after `//field[@name='create_date']`: add field x_studio_related_field_bPlxa, field x_studio_related_field_ygmmJ; after `//tree[1]/field[@name='product_id']`: add field description; set string=Total Quantity, sum=Sum of Quantity, widget=monetary on `//field[@name='quantity']`; after `//field[@name='uom_id']`: add field unit_cost; after `//field[@name='value']`: add field remaining_value, field account_move_id, field id | Adds From/To location, description, unit cost, remaining value, journal entry and ID columns to the Stock Valuation list and totals Quantity (labelled Total Quantity). | `stock.valuation.layer.account_move_id` (stock_account)<br>`stock.valuation.layer.description` (stock_account)<br>`stock.valuation.layer.remaining_value` (stock_account)<br>`stock.valuation.layer.unit_cost` (stock_account)<br>`stock.valuation.layer.x_studio_related_field_bPlxa`<details><summary>+2 more</summary>`stock.valuation.layer.x_studio_related_field_ygmmJ`<br>`view stock_account.stock_valuation_layer_tree` (stock_account)</details> |  |

**Record rules (1):**

| Name | Record name | Function | Depends on | Used by |
|---|---|---|---|---|
| Stock Valuation Layer Multicompany | `rule_109_stock_valuation_layer_multicompany` | For everyone (global rule): read/write/create/delete on Stock Valuation Layer only where `[('company_id', 'in', company_ids)]`. | `model stock.valuation.layer` (stock_account)<br>`stock.valuation.layer.company_id` (stock_account) |  |
