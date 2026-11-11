"""Studio-ported custom model material_request_mt_stage."""

from odoo import fields, models


class XMaterialRequestMtStage(models.Model):
    _name = "material_request_mt_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request MT Stages"

    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer()


class XMaterialRequestMtStageGap(models.Model):
    _inherit = "material_request_mt_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Stage Name", required=True)
