"""Sentinel declaration for temp_consignment_lin."""

from odoo import fields, models

# NOTE (v0.0.118): the Many2one(s) payment_method / structure_name
# were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XTempConsignmentLin(models.Model):
    _name = "temp_consignment_lin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Temp Consignment Line"

    active = fields.Boolean()
    currency_id = fields.Many2one("res.currency")
    name = fields.Char()
    concessional_rate = fields.Boolean()
    consignment_remainder = fields.Float()
    delivery_date = fields.Datetime()
    delivery_remainder = fields.Float()
    description = fields.Text()
    indent_no = fields.Char()
    product_id = fields.Many2one("product.product")
    accounting_purchase_id = fields.Many2one("purchase.order", string="Order Reference")
    purchase_line_id = fields.Many2one("purchase.order.line", string="Purchase Line Id")
    quantity = fields.Float()
    accounting_select = fields.Boolean(string="Select")
    sequence = fields.Integer()
    subtotal = fields.Float()  # was Monetary
    supplier_id = fields.Many2one("res.partner", string="Vendor")
    temp_consignment_header_id = fields.Many2one(
        "temp_consignment_hea",
        string="Temp Consignment Header Id",
        ondelete="cascade",
    )
    unit_price = fields.Float()
    uom_id = fields.Many2one("uom.uom", string="UOM")
    volume = fields.Float()
    weight = fields.Float()


class XTempConsignmentLinGap(models.Model):
    _inherit = "temp_consignment_lin"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    currency_id = fields.Many2one(comodel_name="res.currency")
    name = fields.Char()
