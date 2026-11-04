"""Studio-ported custom model x_material_request_mt_tag."""

from odoo import fields, models


class XMaterialRequestMtTag(models.Model):
    _name = "x_material_request_mt_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request MT Tags"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)


class XMaterialRequestMtTagGap(models.Model):
    _inherit = "x_material_request_mt_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer(string="Color")
    name = fields.Char(string="Name", required=True)
