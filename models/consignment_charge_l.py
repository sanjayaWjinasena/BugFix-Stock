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

    active = fields.Boolean()
    name = fields.Char()
    amount = fields.Float()
    basis = fields.Selection(
        [("Percentage", "Percentage"), ("Fixed Per Document", "Fixed Per Document")],
    )
    charge_group = fields.Selection(
        [
            ("None", "None"),
            ("Charges", "Charges"),
            ("Duty", "Duty"),
            ("Taxes", "Taxes"),
        ],
    )
    charge_name = fields.Char()
    accounting_company_id = fields.Many2one("res.company", string="Company")
    consignment_charge_header_id = fields.Many2one(
        "consignment_charge_h", string="Consignment Charge Header Id"
    )
    consignment_id = fields.Many2one("consignment_header", string="Consignment Id")
    formula = fields.Char()
    indent_id = fields.Char(string="Indent_ID")
    percent = fields.Float()
    product = fields.Many2one("product.product")
    quantity = fields.Float()
    sequence = fields.Integer()
    structure_no = fields.Integer()
    unit_price = fields.Float()


class XConsignmentChargeLGap(models.Model):
    _inherit = "consignment_charge_l"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
