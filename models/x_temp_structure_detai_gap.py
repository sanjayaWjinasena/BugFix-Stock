# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempStructureDetaiGap(models.Model):
    _inherit = 'x_temp_structure_detai'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_structure_details_line_ids = fields.Many2one(comodel_name='x_structure_details', string='Structure Details Line Ids')
