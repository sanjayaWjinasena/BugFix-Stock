# -*- coding: utf-8 -*-
"""Studio-ported custom model x_material_request_mt_stage."""
from odoo import fields, models


class XMaterialRequestMtStage(models.Model):
    _name = 'x_material_request_mt_stage'
    _description = 'Material Request MT Stages'

    x_name = fields.Char(string='Stage Name', required=True)
    x_studio_sequence = fields.Integer(string='Sequence')
