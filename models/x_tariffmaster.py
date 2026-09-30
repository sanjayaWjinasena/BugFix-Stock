# -*- coding: utf-8 -*-
"""x_tariffmaster — Studio custom model port.

CDB has an O2M `x_studio_tariff_master_ids` on this model whose inverse
M2O on x_tariff_date shares the same name (`x_studio_tariff_master_ids`).
That naming collision made the v0.0.28 port punt on the O2M with the
comment "would need renaming the inverse — destructive". However:

    - The M2O on x_tariff_date is defined by BugFix-Purchase (loaded in
      a different pass from BugFix-Stock).
    - By the time Odoo's setup_nonrelated processes this O2M, the M2O
      is already fully registered in x_tariff_date._fields.
    - The O2M inverse lookup (`comodel._fields[inverse_name]`) finds
      the M2O by name, and since both fields correctly reference each
      other's comodel, the pair is valid.

Ship as a real stored Python O2M (state='base', matches everywhere-else
port convention). Fallback to `compute=/store=False` only if the setup
still errors — this variant is documented in the v0.0.99 port notes.
"""
from odoo import fields, models


class XTariffmaster(models.Model):
    _name = 'x_tariffmaster'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TariffMaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    # O2M inverse to x_tariff_date via its M2O of the same name (Studio
    # convention — see docstring for the naming-collision analysis).
    x_studio_tariff_master_ids = fields.One2many(
        'x_tariff_date',
        'x_studio_tariff_master_ids',
        string='Date Range',
    )
