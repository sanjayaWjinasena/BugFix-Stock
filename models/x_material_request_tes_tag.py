# -*- coding: utf-8 -*-
"""Studio-ported custom model x_material_request_tes_tag."""
from odoo import fields, models


class XMaterialRequestTesTag(models.Model):
    _name = 'x_material_request_tes_tag'
    _description = 'Material Request Test Tags'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Name')
