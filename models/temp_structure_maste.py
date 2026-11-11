"""Studio-ported custom model temp_structure_maste."""

from odoo import fields, models


class XTempStructureMaste(models.Model):
    _name = "temp_structure_maste"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Temp Structure Master"

    name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence")

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    # temp_structure_details (one2many rel='temp_structure_detai' needs
    # inverse)
    #   temp_structure_details_id (many2one rel='structure_details' not safe)


class XTempStructureMasteGap(models.Model):
    _inherit = "temp_structure_maste"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    temp_structure_details = fields.One2many(
        comodel_name="temp_structure_detai",
        inverse_name="temp_structure_master_id",
        string="Temp Structure Details",
    )
