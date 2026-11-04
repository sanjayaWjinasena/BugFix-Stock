"""Studio-ported custom model x_material_request_tes_stage."""

from odoo import fields, models


class XMaterialRequestTesStage(models.Model):
    _name = "x_material_request_tes_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request Test Stages"

    name = fields.Char(string="Stage Name")
    sequence = fields.Integer(string="Sequence")


class XMaterialRequestTesStageGap(models.Model):
    _inherit = "x_material_request_tes_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Stage Name", required=True)
