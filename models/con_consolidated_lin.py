"""Sentinel declaration for con_consolidated_lin."""

from odoo import fields, models

# NOTE (v0.0.118): the Many2one(s) delivery_term were MOVED to BugFix-Purchase
# v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XConConsolidatedLin(models.Model):
    _name = "con_consolidated_lin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Con. Consolidated Line"

    active = fields.Boolean()
    name = fields.Char()
    accounting_company_id = fields.Many2one("res.company", string="Company")
    consignment_id = fields.Many2one("consignment_header", string="Consignment Id")
    consolidated_header_id = fields.Many2one(
        "con_consolidated_hea", string="Consolidated Header Id", ondelete="restrict"
    )
    container_no = fields.Char()
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    custom_clearance_no = fields.Char()
    accounting_invoice_date = fields.Date(string="Invoice Date")
    sequence = fields.Integer()
    shipment_start_date = fields.Date()
    shipping_mode_1 = fields.Selection(
        [("Air", "Air"), ("Sea", "Sea"), ("Road", "Road"), ("Courier", "Courier")],
        string="Shipping Mode",
    )
    status = fields.Selection(
        [
            ("Draft", "Draft"),
            ("Consignment", "Confirmed"),
            ("In Transit", "In Transit"),
            ("Under Custom Clearance", "Under Custom Clearance"),
            ("Done", "Done"),
            ("TP Invoice", "TP Invoice"),
        ],
    )
    supplier_id = fields.Many2one("res.partner", string="Vendor")
    supplier_invoice_no = fields.Char()


class XConConsolidatedLinGap(models.Model):
    _inherit = "con_consolidated_lin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()
