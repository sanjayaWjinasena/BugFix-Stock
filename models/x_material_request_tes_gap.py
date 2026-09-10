# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestTesGap(models.Model):
    _inherit = 'x_material_request_tes'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_material_request_tes_line_ids_661d3 = fields.One2many(comodel_name='x_material_request_tes_line_3301b', inverse_name='x_material_request_tes_id', string='New Lines')
    x_name = fields.Char(string='Description', required=True)
    x_studio_stage_id = fields.Many2one(comodel_name='x_material_request_tes_stage', string='Stage', required=True)
    x_studio_tag_ids = fields.Many2many(comodel_name='x_material_request_tes_tag', string='Tags')
