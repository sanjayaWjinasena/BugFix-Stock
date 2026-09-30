# -*- coding: utf-8 -*-
"""x_tariffmaster — Studio custom model port.

v0.0.100 tried to ship the O2M `x_studio_tariff_master_ids` as a real
Python fields.One2many. Odoo crashed with the same KeyError as
v0.0.28 predicted:

  File "/home/odoo/src/odoo/odoo/fields.py", line 4458, in setup_nonrelated
      invf = comodel._fields[self.inverse_name]
  KeyError: 'x_studio_tariff_master_ids'

Reason: when Odoo's setup_nonrelated processes the O2M, it looks up
its inverse M2O on the comodel by `comodel._fields[inverse_name]`.
The inverse_name is `x_studio_tariff_master_ids` — SAME NAME as the
O2M itself. Odoo's field registry stores field-name uniqueness per
model, but the cross-model self-reference through an identical name
runs a lookup ordering that fails when the M2O is still mid-setup
in the same registry pass.

Reverted in v0.0.101 to unbreak the server. The O2M is deferred to
a future Plan B (see notes) — a compute=/store=False variant that
bypasses setup_nonrelated by not registering an inverse_name at all.
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
    # O2M x_studio_tariff_master_ids — see docstring for the naming-
    # collision analysis. Ship deferred until we validate the compute=
    # /store=False variant on a scratch env.
