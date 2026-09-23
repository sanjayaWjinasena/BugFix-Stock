# -*- coding: utf-8 -*-
"""Sentinel declaration for x_mr_config so x_material_request's O2M inverse
resolves at BugFix-Stock load time.

Full x_mr_config declaration lives in BugFix-Purchase — that module loads
AFTER BugFix-Stock (purchase depends on stock in Odoo core, so
BugFix-Purchase inherits that ordering). Without this sentinel, when
BugFix-Stock declares
  x_material_request.x_studio_request_lines =
      fields.One2many('x_mr_config', 'x_studio_many2one_field_6yqbk', ...)
Odoo tries to resolve the inverse M2O at model setup time and fails with
  KeyError: 'x_studio_many2one_field_6yqbk'
because BugFix-Purchase hasn't declared it yet.

The sentinel provides just the inverse M2O field. BugFix-Purchase's
full declaration merges in later via Odoo's _name-based class union
(all other x_mr_config fields declared there get added to the same model).
"""
from odoo import fields, models


class XMrConfig(models.Model):
    _name = 'x_mr_config'
    _description = 'MR config'

    x_studio_many2one_field_6yqbk = fields.Many2one(
        'x_material_request', string='Material Request',
        ondelete='set null')
