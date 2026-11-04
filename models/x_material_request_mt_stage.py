"""Studio-ported custom model x_material_request_mt_stage."""

from odoo import fields, models


class XMaterialRequestMtStage(models.Model):
    _name = "x_material_request_mt_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request MT Stages"

    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence")


class XMaterialRequestMtStageGap(models.Model):
    _inherit = "x_material_request_mt_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Stage Name", required=True)
