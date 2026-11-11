"""Sentinel declaration for con_consolidated_hea."""

from odoo import fields, models


class XConConsolidatedHea(models.Model):
    _name = "con_consolidated_hea"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Con. Consolidated Header"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Con. Reference")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    con_line_ids = fields.One2many(
        "con_consolidated_lin",
        "consolidated_header_id",
        string="Con. Line Ids",
    )
    description = fields.Char(string="Description")
    lines_copied = fields.Boolean(string="Lines Copied")
    pipeline_status_bar = fields.Selection(
        [("Draft", "Draft"), ("Confirmed", "Confirmed")], string="Pipeline Status Bar"
    )
    sequence = fields.Integer(string="Sequence")
    status = fields.Selection(
        [("Draft", "Draft"), ("Confirmed", "Confirmed")], string="Status"
    )


class XConConsolidatedHeaGap(models.Model):
    _inherit = "con_consolidated_hea"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Con. Reference")
