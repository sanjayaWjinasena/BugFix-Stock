# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Inventory',
    'version': '17.0.0.0.15',
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
    'depends': ['base_setup', 'stock', 'Jinasena_Masterdata_Reporting'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/server_actions.xml',
        'data/automations.xml',
        'data/act_windows.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}