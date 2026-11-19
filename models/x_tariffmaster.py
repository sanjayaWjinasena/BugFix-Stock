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
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TariffMaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')

    # x_studio_tariff_master_ids field NOT shipped — permanent skip.
    #
    # Attempts made (all documented in commit history):
    #   v0.0.28: skipped from initial port (documented naming collision)
    #   v0.0.100: real Python O2M with inverse_name → KeyError at
    #             setup_nonrelated (line 4458) — same as v0.0.28 predicted
    #   v0.0.102: One2many(compute=/store=False) — Odoo can't resolve
    #             comodel without inverse_name; ir.model.fields row
    #             gets relation='_unknown' permanently
    #   v0.0.103: switched to Many2many(compute=/store=False) — same
    #             _unknown persistence; ORM refuses to write comodel
    #             record instances to a field with _unknown relation
    #   v0.0.104: field removed entirely (this version); the audit
    #             generator MANUAL_OVERRIDES marks this as wont_ship
    #             with reason "CDB naming self-conflict + no pure-code
    #             recovery path on envs where earlier port attempts
    #             left a stale ir.model.fields row"
    #
    # The stale ir.model.fields row (state='base', relation='_unknown')
    # on Dev is inert — no Python backing, no widget references, no
    # queries hit it. It will be cleaned up automatically if BugFix-Stock
    # is ever uninstalled+reinstalled (dropping all its ir.model.fields
    # state cleanly). New environments installing from v0.0.104 fresh
    # will never see the row — install ships without the field, matching
    # the audit's wont_ship classification.
