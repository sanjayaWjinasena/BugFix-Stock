"""Studio-ported custom model material_request_mt_tag."""

from odoo import fields, models


class XMaterialRequestMtTag(models.Model):
    _name = "material_request_mt_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Material Request MT Tags"

    color = fields.Integer()
    name = fields.Char(required=True)


class XMaterialRequestMtTagGap(models.Model):
    _inherit = "material_request_mt_tag"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    color = fields.Integer()
    name = fields.Char(required=True)
