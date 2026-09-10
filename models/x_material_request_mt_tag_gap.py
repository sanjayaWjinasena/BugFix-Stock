# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMtTagGap(models.Model):
    _inherit = 'x_material_request_mt_tag'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name', required=True)
