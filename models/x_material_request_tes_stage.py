# -*- coding: utf-8 -*-
"""Studio-ported custom model x_material_request_tes_stage."""
from odoo import fields, models


class XMaterialRequestTesStage(models.Model):
    _name = 'x_material_request_tes_stage'
    _description = 'Material Request Test Stages'

    x_name = fields.Char(string='Stage Name')
    x_studio_sequence = fields.Integer(string='Sequence')
