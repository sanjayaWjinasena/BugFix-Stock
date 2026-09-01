# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Inventory',
    'version': '17.0.0.0.21',
    'summary': 'Studio-to-Python port for BugFix-Stock',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Inventory',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization -- Odoo SH does not ship
    # a manifest for it, listing it causes install skip.
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
    # v0.0.21: 2 big Studio inherit views on stock.picking form
    # (2387 = 13.5 KB main customization; 4732 = 6.8 KB priority-999905
    # button rewire). See views/stock_studio_ported_v3.xml.
    # Ships supporting infra in one commit:
    #   * 3 new server actions in data/server_actions.xml: 1367 IMP
    #     Update Consignment Final (1488b), 2181 PROJ Show Validate
    #     Block Errors (101b), 2448 Movement Journals Update Offset
    #     Account (2445b) - all on stock.picking.
    #   * 2 new act_windows in data/act_windows.xml: 1362 Vend.
    #     Dispatch Reversal + 1363 Custom Clearance Reversal, both
    #     on account.move with domain traversing
    #     x_studio_created_from_transfer / x_studio_create_from_transfer_1.
    #     Live in BugFix-Stock (not BugFix-Accounting) because they
    #     are only referenced by BugFix-Stock's stock.picking form
    #     view - avoids adding a BugFix-Stock -> BugFix-Accounting
    #     manifest dep. Res_model account.move is fine here; Odoo
    #     doesn't require the act_window's target model to be owned
    #     by the same module.
    #   * View archs interpolate all 10 hardcoded numeric refs to
    #     %(...)d xmlids, covering both button-add name= attributes
    #     AND xpath anchors ([@name='NNNN']). Uses stock.
    #     act_stock_return_picking (195), stock.action_report_delivery
    #     (175), stock.action_stock_report (168) for standard-Odoo
    #     refs; local xmlids for the RR_* server actions + the 5 new
    #     records shipped in this same commit.
    # No new manifest deps.
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
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}