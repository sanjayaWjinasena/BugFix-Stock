# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempStructureMasteGap(models.Model):
    _inherit = 'x_temp_structure_maste'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_temp_structure_details = fields.One2many(comodel_name='x_temp_structure_detai', inverse_name='x_studio_temp_structure_master_id', string='Temp Structure Details')
    x_studio_temp_structure_details_id = fields.Many2one(comodel_name='x_structure_details', string='Temp Structure Details Id')
