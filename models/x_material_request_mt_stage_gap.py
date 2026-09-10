# -*- coding: utf-8 -*-
from odoo import models, fields

class XMaterialRequestMtStageGap(models.Model):
    _inherit = 'x_material_request_mt_stage'

    x_name = fields.Char(string='Stage Name', required=True)
