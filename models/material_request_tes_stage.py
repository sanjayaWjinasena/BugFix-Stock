"""Studio-ported custom model material_request_tes_stage."""

from odoo import fields, models


class XMaterialRequestTesStage(models.Model):
    _name = "material_request_tes_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request Test Stages"

    name = fields.Char(string="Stage Name")
    sequence = fields.Integer()


class XMaterialRequestTesStageGap(models.Model):
    _inherit = "material_request_tes_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Stage Name", required=True)
