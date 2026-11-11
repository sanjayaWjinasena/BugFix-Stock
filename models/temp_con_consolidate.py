"""Studio-ported custom model temp_con_consolidate."""

from odoo import fields, models


class XTempConConsolidate(models.Model):
    _name = "temp_con_consolidate"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Temp Con. Consolidated Header"

    name = fields.Char()
    consolidated_header_id = fields.Many2one(
        "con_consolidated_hea", string="Consolidated Header Id"
    )
    select_all = fields.Boolean()
    sequence = fields.Integer()

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   con_lines (one2many rel='temp_con_conso_line' needs inverse)


class XTempConConsolidateGap(models.Model):
    _inherit = "temp_con_consolidate"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
    con_lines = fields.One2many(
        comodel_name="temp_con_conso_line",
        inverse_name="temp_consolidated_header_id",
        string="Con. Lines",
    )
