# -*- coding: utf-8 -*-
"""x_tariffmaster — Studio custom model port.

The Studio O2M `x_studio_tariff_master_ids` on this model shares its
name with the inverse M2O on the comodel `x_tariff_date`. Shipping
that O2M as a real stored One2many crashes registry setup with:

  File "/home/odoo/src/odoo/odoo/fields.py", line 4458, in setup_nonrelated
      invf = comodel._fields[self.inverse_name]
  KeyError: 'x_studio_tariff_master_ids'

Odoo's setup_nonrelated does `comodel._fields[inverse_name]` — when
inverse_name matches the O2M's own name, the lookup hits an internal
resolution collision (v0.0.28 first documented this, v0.0.100 confirmed
the same KeyError). Different modules do not help — registry setup
runs one pass per-model across ALL classes.

v0.0.102 fix (Path A): ship the O2M as compute=/store=False. No
inverse_name is declared, so setup_nonrelated never runs for this
field, no collision. The compute method searches x_tariff_date for
rows whose M2O points back at this master.

Trade-offs vs stored O2M:
  + Read-only display works — form widget shows the linked date ranges
  + Portable to new environments as pure Python (no destructive rename
    of the M2O column on x_tariff_date, no data migration needed)
  - No inline-create via the O2M widget — users add x_tariff_date rows
    via that model's own list/form + set the M2O manually
  - Field is not searchable/filterable in the standard sense (compute
    result is not stored) — for filtering on x_tariff_date presence,
    use the M2O side directly.
"""
from odoo import api, fields, models


class XTariffmaster(models.Model):
    _name = 'x_tariffmaster'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TariffMaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')

    # Note: shipped as computed Many2many (not One2many) because
    # `fields.One2many` without an `inverse_name` positional arg gets
    # relation='_unknown' during setup, and specifying inverse_name
    # triggers the setup_nonrelated KeyError from v0.0.100. Many2many
    # avoids both problems — it doesn't need inverse_name, resolves
    # the comodel cleanly, and the form widget renders it as a list
    # of x_tariff_date records exactly like the O2M would.
    x_studio_tariff_master_ids = fields.Many2many(
        'x_tariff_date',
        string='Date Range',
        compute='_compute_x_studio_tariff_master_ids',
        store=False,
    )

    def _compute_x_studio_tariff_master_ids(self):
        Date = self.env['x_tariff_date']
        for rec in self:
            rec.x_studio_tariff_master_ids = Date.search([
                ('x_studio_tariff_master_ids', '=', rec.id),
            ])
