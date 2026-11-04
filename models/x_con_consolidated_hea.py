"""Sentinel declaration for x_con_consolidated_hea."""

from odoo import fields, models


class XConConsolidatedHea(models.Model):
    _name = "x_con_consolidated_hea"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Con. Consolidated Header"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Con. Reference")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    x_studio_con_line_ids = fields.One2many(
        "x_con_consolidated_lin",
        "x_studio_consolidated_header_id",
        string="Con. Line Ids",
    )
    description = fields.Char(string="Description")
    x_studio_lines_copied = fields.Boolean(string="Lines Copied")
    x_studio_pipeline_status_bar = fields.Selection(
        [("Draft", "Draft"), ("Confirmed", "Confirmed")], string="Pipeline Status Bar"
    )
    sequence = fields.Integer(string="Sequence")
    x_studio_status = fields.Selection(
        [("Draft", "Draft"), ("Confirmed", "Confirmed")], string="Status"
    )


class XConConsolidatedHeaGap(models.Model):
    _inherit = "x_con_consolidated_hea"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Con. Reference")
