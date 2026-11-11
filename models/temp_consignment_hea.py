"""Sentinel declaration for temp_consignment_hea."""

from odoo import fields, models


class XTempConsignmentHea(models.Model):
    _name = "temp_consignment_hea"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Temp Consignment Header"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    select_all = fields.Boolean(string="Select All")
    sequence = fields.Integer(string="Sequence")
    temp_consignment_header_id = fields.Many2one(
        "consignment_header", string="Temp Consignment Header Id"
    )
    temp_consignment_line_ids = fields.One2many(
        "temp_consignment_lin",
        "temp_consignment_header_id",
        string="Temp Consignment Line Ids",
    )


class XTempConsignmentHeaGap(models.Model):
    _inherit = "temp_consignment_hea"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
