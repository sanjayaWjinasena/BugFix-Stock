# -*- coding: utf-8 -*-
"""Studio-ported custom model x_temp_structure_maste."""
from odoo import fields, models


class XTempStructureMaste(models.Model):
    _name = 'x_temp_structure_maste'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Temp Structure Master'

    x_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   x_studio_temp_structure_details (one2many rel='x_temp_structure_detai' needs inverse)
    #   x_studio_temp_structure_details_id (many2one rel='x_structure_details' not safe)
