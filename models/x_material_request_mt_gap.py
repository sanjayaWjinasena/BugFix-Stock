# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMtGap(models.Model):
    _inherit = 'x_material_request_mt'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_material_request_mt_line_ids_7737e = fields.One2many(comodel_name='x_material_request_mt_line_9a011', inverse_name='x_material_request_mt_id', string='New Lines')
    x_name = fields.Char(string='Description', required=True)
