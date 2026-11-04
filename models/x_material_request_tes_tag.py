"""Studio-ported custom model x_material_request_tes_tag."""

from odoo import fields, models


class XMaterialRequestTesTag(models.Model):
    _name = "x_material_request_tes_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request Test Tags"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name")


class XMaterialRequestTesTagGap(models.Model):
    _inherit = "x_material_request_tes_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)
