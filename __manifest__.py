# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Inventory',
    'version': '17.0.0.0.18',
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
    'depends': ['base_setup', 'stock', 'stock_landed_costs', 'helpdesk_stock', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
        'views/x_consignment_studio_ported.xml',
        'views/stock_studio_ported.xml',
        'views/stock_studio_ported_v2.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}