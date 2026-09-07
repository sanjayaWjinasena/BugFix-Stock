# -*- coding: utf-8 -*-
"""Studio-ported custom model x_material_request_mt_tag."""
from odoo import fields, models


class XMaterialRequestMtTag(models.Model):
    _name = 'x_material_request_mt_tag'
    _description = 'Material Request MT Tags'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name', required=True)
