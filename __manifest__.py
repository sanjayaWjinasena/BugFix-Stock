# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Module : Inventory',
    'version': '17.0.0.0.14',
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