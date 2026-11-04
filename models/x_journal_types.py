"""Sentinel declaration for x_journal_types so cross-references resolve."""

from odoo import fields, models


class XJournalTypes(models.Model):
    _name = "x_journal_types"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "X Journal Types"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Journal Type")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    description = fields.Char(string="Description")
    x_studio_offset_account = fields.Many2one(
        "account.account", string="Offset Account"
    )
    sequence = fields.Integer(string="Sequence")
