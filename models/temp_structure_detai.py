"""Studio-ported custom model temp_structure_detai."""

from odoo import fields, models


class XTempStructureDetai(models.Model):
    _name = "temp_structure_detai"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Temp Structure Details"

    name = fields.Char(string="Name")
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
            ("Assessable Value", "Assessable Value"),
        ],
        string="Charge Group",
    )
    charge_name = fields.Char(string="Charge Name")
    accounting_select = fields.Boolean(string="Select")
    sequence = fields.Integer(string="Sequence")
    temp_structure_master_id = fields.Many2one(
        "temp_structure_maste", string="Temp Structure Master Id", ondelete="cascade"
    )

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    # structure_details_line_ids (many2one rel='structure_details' not safe)


class XTempStructureDetaiGap(models.Model):
    _inherit = "temp_structure_detai"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
