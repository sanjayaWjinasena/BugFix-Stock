# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMtGap(models.Model):
    _inherit = 'x_material_request_mt'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    # STRIPPED x_material_request_mt_line_ids_7737e: O2M inverse lives in another repo (load-order risk)
    x_name = fields.Char(string='Description', required=True)
