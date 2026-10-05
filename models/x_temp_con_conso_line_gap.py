# -*- coding: utf-8 -*-
from odoo import models, fields

# NOTE (v0.0.118): the Many2one(s) x_studio_delivery_term were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.

class XTempConConsoLineGap(models.Model):
    _inherit = 'x_temp_con_conso_line'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
