"""Sentinel declaration for consignment_charge_l."""

from odoo import fields, models

# NOTE (v0.0.118): the Many2one(s) structure_details_line_ids /
# structure_master_id were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XConsignmentChargeL(models.Model):
    _name = "consignment_charge_l"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Consignment Charge Line"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    amount = fields.Float(string="Amount")
    basis = fields.Selection(
        [("Percentage", "Percentage"), ("Fixed Per Document", "Fixed Per Document")],
        string="Basis",
    )
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
        ],
        string="Charge Group",
    )
    charge_name = fields.Char(string="Charge Name")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    consignment_charge_header_id = fields.Many2one(
        "consignment_charge_h", string="Consignment Charge Header Id"
    )
    consignment_id = fields.Many2one(
        "consignment_header", string="Consignment Id"
    )
    formula = fields.Char(string="Formula")
    indent_id = fields.Char(string="Indent_ID")
    percent = fields.Float(string="Percent")
    product = fields.Many2one("product.product", string="Product")
    quantity = fields.Float(string="Quantity")
    sequence = fields.Integer(string="Sequence")
    structure_no = fields.Integer(string="Structure No")
    unit_price = fields.Float(string="Unit Price")


class XConsignmentChargeLGap(models.Model):
    _inherit = "consignment_charge_l"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
