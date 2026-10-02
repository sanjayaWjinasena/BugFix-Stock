# -*- coding: utf-8 -*-
from odoo import models, fields

# NOTE (v0.0.118): the Many2one(s) x_studio_temp_structure_details_id were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.

class XTempStructureMasteGap(models.Model):
    _inherit = 'x_temp_structure_maste'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_temp_structure_details = fields.One2many(comodel_name='x_temp_structure_detai', inverse_name='x_studio_temp_structure_master_id', string='Temp Structure Details')
