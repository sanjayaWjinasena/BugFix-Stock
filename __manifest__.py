# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Inventory',
    'version': '17.0.0.0.28',
    'summary': 'Studio-to-Python port for BugFix-Stock',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Inventory',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
    # v0.0.28: close the field-coverage gap identified by Stock audit.
    # 21 CDB fields on 9 models had no pin on target. Breakdown:
    #   * 16 auto-fields (activity_exception_decoration + activity_
    #     exception_icon) on 8 custom models -> add _inherit =
    #     ['mail.thread', 'mail.activity.mixin']. Fields are Odoo-
    #     managed once inherit is present. All 8 CDB models already
    #     have the thread/activity fields, so this matches source
    #     of truth.
    #   * 2 O2Ms declared:
    #     - x_con_consolidated_hea.x_studio_con_line_ids -> x_con_
    #       consolidated_lin (inverse x_studio_consolidated_header_id)
    #     - x_temp_consignment_hea.x_studio_temp_consignment_line_ids
    #       -> x_temp_consignment_lin (inverse x_studio_temp_
    #       consignment_header_id)
    #   * SKIP 1 O2M: x_tariffmaster.x_studio_tariff_master_ids ->
    #     x_tariff_date. Comodel x_tariff_date does not exist on target
    #     (never ported). Would fail install with KeyError. Left as
    #     TODO in x_tariffmaster.py.
    #   * SKIP 2 related fields on product.product (rating_avg_text,
    #     rating_last_text). Both exist unpinned on target (auto-
    #     generated via _inherits from product.template). No action
    #     needed.
    # Files touched: 8 model files (inherit added on all, O2M added
    # on 2). No new deps (stock already pulls mail).
    # Effective coverage after landing: 100% of Sales-safe fields.
    # v0.0.27: cross-repo companion fix for BugFix-Purchase v0.1.0.71.
    # Purchase added _inherit = ['mail.thread', 'mail.activity.mixin']
    # to its x_material_request declaration. Both this module and
    # BugFix-Purchase declare that model via _name; Odoo merges field
    # declarations at load time. The later-loaded module's class
    # definition wins for _inherit. Without matching the inherit
    # here, chatter/activity fields would get shadowed and view
    # ports referencing them would fail. Mirroring the inherit.
    # v0.0.26: cross-repo fix for BugFix-Purchase v0.1.0.32.
    # This module also declares x_material_request as a sentinel with
    # x_active = fields.Boolean(string='Active') (no default). Since both
    # BugFix-Purchase and BugFix-Stock declare the model via _name, Odoo
    # merges field declarations at load time; whichever module loads LAST
    # wins for defaults. BugFix-Stock was overriding BugFix-Purchase's
    # v0.1.0.32 default=True fix, so records still got x_active=False.
    # Fix: add default=True to the sentinel too. Only x_material_request
    # is affected (verified via grep: no other Stock model overlaps with
    # a Purchase model name).
    # v0.0.13: added Jinasena_Masterdata_Reporting - owns x_sales_report_type
    # which our stock.move + stock.move.line Many2ones target. Previously
    # each of BugFix-Stock/MRP/Sales/Accounting had a sentinel Python
    # class declaring _name = 'x_sales_report_type' just to make those
    # M2O refs resolve. The consolidated masterdata module removes the
    # need for that scaffold.
    # v0.0.16: first view-port wave — 6 records for x_consignment_header +
    # x_consignment_line (3 primary Default views + 3 Studio priority-99
    # inherit overlays). Byte-verbatim from Clear-DB views 2810/2813/
    # 2814/2817/2818/2819 except:
    #   * 2814 oe_chatter block stripped (x_consignment_line does not
    #     inherit mail.thread/mail.activity.mixin).
    # NOT ported this wave: 2811+2816 (x_consignment_header form + its
    # 14.8KB Studio inherit) - hardcoded action refs + cross-repo conflict
    # with BugFix-Purchase draft view 9609 need coordination first.
    # See VIEWS_TODO.md for the remaining 21 substantive views.
    # v0.0.15: wired 14 base.automation stubs to their local server actions.
    #   * data/automations.xml: every TODO comment
    #     `<!-- TODO: wire action_server_ids to actual server_action xmlids: [NNNN] -->`
    #     replaced by
    #     `<field name="action_server_ids" eval="[(6, 0, [ref('server_action_NNNN_...')])]"/>`.
    #   * All 14 referenced action xmlids already existed in
    #     data/server_actions.xml - no server-action ports needed. Trigger
    #     semantics preserved (on_create_or_write / on_change / on_unlink).
    #   * 14 base.automation records now actually invoke their code on
    #     trigger; previously they were silent no-ops.
    # v0.0.17: 6 more Studio inherit views on standard stock.* models
    # (see views/stock_studio_ported.xml). NEW DEP stock_landed_costs -
    # needed for view 4892's inherit_id ref on
    # stock_landed_costs.view_stock_landed_cost_form.
    # v0.0.18: 6 more mid-size Studio inherits (see
    # views/stock_studio_ported_v2.xml). NEW DEP helpdesk_stock -
    # needed for view 4617 (stock.return.picking form) which inherits
    # helpdesk_stock.view_stock_return_picking_form_inherit_helpdesk_stock.
    # Already installed on repair-test-101 (module id 197).
    # v0.0.19: re-adds models/stock_valuation_layer.py (previously
    # deleted in v0.0.12 CRITICAL because stock_account was absent on
    # dev). Now safe because stock_account is installed on repair-
    # test-101 and transitively pulled by stock_landed_costs. Only 2
    # of the 4 previously-declared fields are re-added
    # (x_studio_related_field_bPlxa, _ygmmJ) with the proper Clear-DB
    # `related=` attribute; the other 2 (MfcOm, dGINH) are not
    # referenced by any view currently being ported. Also adds view
    # 2585 (Studio inherit on stock.valuation.layer tree) to
    # views/stock_studio_ported_v2.xml.
    # v0.0.25: 2 views for x_consignment_header + 1 field port.
    # See views/stock_studio_ported_v5.xml.
    #
    # models/x_consignment_header.py: x_studio_consignment_line_ids
    # One2many field ported from Clear-DB (was TODO on-disk). Inverse:
    # x_consignment_line.x_studio_consignment_header_id (already
    # declared). Used by view 2816's "Consignment Lines" tab.
    #
    #   * 2811 primary form (2938b -> 3208b after strip + sentinels).
    #     oe_chatter stripped, 5 sentinel <field invisible="1"/>
    #     elements injected for x_studio_status, _lines_copied,
    #     _allocate_header_charges, _create_header_charges,
    #     _header_charges_allocated (Odoo 17 strict-modifier
    #     validation). 11 numeric name= refs interpolated.
    #   * 2816 Studio inherit (14.8 KB -> 14.6 KB after strip). TP
    #     Invoices button (name="1383") removed via lxml etree (see
    #     v0.0.24 comment for deferral rationale). 5 numeric refs
    #     interpolated.
    #
    # First v0.0.25 attempt (c68189d) crashed on missing sentinels
    # (fixed at retry #1). Second attempt (22c6de3) got past 2811 but
    # crashed on 2816 referencing x_studio_consignment_line_ids which
    # was a TODO on-disk. Retry #2 ports the missing field.
    #
    # v0.0.24: 2 more act_windows in data/act_windows.xml on
    # account.move (prep for views 2811+2816 in v0.0.25):
    #   1306 Vendor Despatch    domain x_studio_created_from_consignment=active_id
    #   1322 Custom Clearance   domain x_studio_created_from_consignment_1=active_id
    #
    # v0.0.24 first attempt shipped 3 act_windows including 1383
    # (TP Invoices on x_tp_invoice_header). Crashed at install:
    # "Invalid model name 'x_tp_invoice_header' in action definition".
    # BugFix-Accounting owns that model but isn't a dep here, so at
    # BugFix-Stock's data-load time the model wasn't yet in the
    # registry. Reverted. Shipping only 1306+1322 which target
    # standard-Odoo account.move (always in registry).
    #
    # 1383 (TP Invoices) permanently deferred - view 2816's TP Invoices
    # button will need to be stripped from its arch when we land 2816.
    #
    # v0.0.23 skipped: view 4732 blocked by Odoo minor-version drift.
    # 3 standard-Odoo stock.picking fields referenced in modifier
    # expressions do not exist on repair-test-101:
    # show_mark_as_todo, show_validate, immediate_transfer. 4732
    # permanently deferred.
    #
    # v0.0.22: view 2387 only (main Studio inherit on stock.picking
    # form, 13.5 KB). See views/stock_studio_ported_v3.xml. Adds
    # Update Consignment / Dispatch / Retun Reject Reason / Vend.
    # Dispatch Reversal / Custom Clearance Reversal stat buttons +
    # wraps 50+ x_studio_* fields into the form + adjusts several
    # standard-field attributes.
    #
    # Byte-verbatim from Clear-DB except numeric name= refs are
    # interpolated to %(xmlid)d (both quote styles via
    # `\bname=["'](\d+)["']` regex). Pattern works inside xpath expr=
    # attribute values - confirmed by finding it in standard Odoo:
    # account_budget/views/account_analytic_account_views.xml:40.
    #
    # NOT ported: view 4732 (priority 999905 "stock.picking.form_button",
    # 6.8 KB). Fails on `xpath expr="//header/button[@name='action_set_
    # quantities_to_reservation']"` - a standard-Odoo button that
    # Clear-DB's stock.view_picking_form has but repair-test-101's
    # version doesn't (Odoo version drift). 4732 only added Request/
    # Approve/Reject Transfer + Update Offset Account + Validate
    # Reject Reason buttons - workflow needs a separate lower-priority
    # inherit anchored to buttons that exist on both envs.
    # v0.0.21: infra-only prep for the big stock.picking form view
    # ports (2387 + 4732 deferred to v0.0.22). Ships:
    #   * 3 byte-verbatim server actions in data/server_actions.xml:
    #     1367 IMP Update Consignment Final (1488b, stock.picking)
    #     2181 PROJ Show Validate Block Errors (101b, stock.picking)
    #     2448 Movement Journals Update Offset Account (2445b, stock.picking)
    #   * 2 act_windows in data/act_windows.xml on account.move:
    #     1362 Vend. Dispatch Reversal (domain
    #     x_studio_created_from_transfer=active_id)
    #     1363 Custom Clearance Reversal (domain
    #     x_studio_create_from_transfer_1=active_id)
    #     Live in BugFix-Stock because they are only referenced by
    #     BugFix-Stock's future view arch; avoids adding a
    #     BugFix-Stock -> BugFix-Accounting dep.
    # Original attempt in v0.0.21 shipped both views AND infra in one
    # commit but crashed at view validation because my Python
    # interpolation regex \bname="(\d+)" only matched double-quoted
    # button-add attributes and missed the single-quoted xpath
    # anchors (name='NNN' inside expr="..."). Reverted immediately.
    # Splitting the retry: land the infra safely here, tackle the
    # view arch separately with a corrected regex + an empirical
    # test of whether Odoo's %(xmlid)d interpolation works inside
    # xpath expr= attribute values.
    # v0.0.20: ports server action 1997 (RR - RUG Return from Help
    # desk, ~3.6 KB Python on stock.return.picking) + wires view 4619
    # to it via %(BugFix-Stock.server_action_1997_...)d ref. The
    # button rewrite is per feedback-hardcoded-action-ids. RR-prefix
    # is Studio naming semantics ("Repair Return"), NOT a module
    # boundary - action operates on stock.return.picking and fits the
    # existing pattern of 7 other RR_* actions in BugFix-Stock.
    # Runtime deps (helpdesk.ticket.x_studio_*, stock.picking.
    # x_studio_helpdesk_ticket_id) verified as state='base' on
    # repair-test-101 before landing.
    'depends': ['base_setup', 'stock', 'stock_account', 'stock_landed_costs', 'helpdesk_stock', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_consignment_studio_ported.xml',
        'views/stock_studio_ported.xml',
        'views/stock_studio_ported_v2.xml',
        'views/stock_studio_ported_v3.xml',
        'views/stock_studio_ported_v5.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}