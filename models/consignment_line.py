from odoo import fields, models

# NOTE (v0.0.118): the Many2one(s) payment_method / structure_name
# were MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XConsignmentLine(models.Model):
    """Studio-ported custom model consignment_line."""

    _name = "consignment_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Consignment Line"

    active = fields.Boolean(string="Active")
    currency_id = fields.Many2one("res.currency", string="Currency", readonly=True)
    name = fields.Char(string="Name")
    allocate_amount = fields.Float(string="Allocate Amount", readonly=True)
    amount = fields.Float(
        string="Amount", readonly=True
    )  # was Monetary (no currency_field)
    boolean_field_Gbd5Y = fields.Boolean(string="Valid Duty")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    concessional_rate = fields.Boolean(string="Concessional Rate")
    consignment_header_id = fields.Many2one(
        "consignment_header", string="Consignment No", ondelete="restrict"
    )
    cost_allocation_method = fields.Selection(
        [
            ("equal", "Equal"),
            ("by_quantity", "By Quantity"),
            ("by_current_cost_price", "By Current Cost"),
            ("by_weight", "By Weight"),
            ("by_volume", "By Volume"),
        ],
        string="Cost Allocation Method",
        readonly=True,
    )
    delivery_remainder = fields.Float(
        string="Delivery Remainder", readonly=True
    )
    description = fields.Char(string="Description", readonly=True, store=False)
    exchange_rate = fields.Float(string="Exchange Rate")
    header_charges_allocated = fields.Boolean(
        string="Header Charges Allocated", readonly=True
    )
    indent_no = fields.Char(string="Indent No", readonly=True)
    invoice_qty = fields.Float(string="Invoice Qty.")
    many2many_field_ZvmKu = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_many2many_field_ZvmKu_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_ex_cd_ids",
    )
    order_remainder = fields.Float(
        string="Consignment Remainder", readonly=True
    )
    original_delivery_remainder = fields.Float(
        string="Original Delivery Remainder"
    )
    product_id = fields.Many2one("product.product", string="Product")
    accounting_purchase_id = fields.Many2one("purchase.order", string="Purchase Order")
    purchase_line_id = fields.Many2one(
        "purchase.order.line", string="Purchase Line Id"
    )
    received_qty = fields.Float(string="Received Qty.", readonly=True)
    sequence = fields.Integer(string="Sequence")
    status = fields.Selection(
        [
            ("Draft", "Draft"),
            ("In Transit", "In Transit"),
            ("Under Custom Clearance", "Under Custom Clearance"),
            ("Done", "Done"),
        ],
        string="Status",
        readonly=True,
    )
    stock_move_id = fields.Many2one("stock.move", string="Stock Move Id")
    tariff_code = fields.Many2one(
        "tariffmaster", string="Tariff Code", readonly=True, store=False
    )
    test1 = fields.Char(string="Test1", readonly=True)
    test2 = fields.Many2one(
        "consignment_header", string="Test2", readonly=True
    )
    tot_charge = fields.Float(string="Tot Charge")
    tot_charge_cd = fields.Float(string="Tot Charge Cd")
    tot_charge_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_charge_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_charge_cd_ids",
    )
    tot_charge_ex = fields.Float(string="Tot Charge Ex")
    tot_charge_ex_cd = fields.Float(string="Tot Charge Ex Cd")
    tot_charge_ex_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_charge_ex_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_charge_ex_cd_ids",
    )
    tot_charge_ex_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_charge_ex_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_charge_ex_ids",
    )
    tot_charge_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_charge_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_charge_ids",
    )
    tot_duty = fields.Float(string="Tot Duty")
    tot_duty_cd = fields.Float(string="Tot Duty Cd")
    tot_duty_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_duty_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_duty_cd_ids",
    )
    tot_duty_ex = fields.Float(string="Tot Duty Ex")
    tot_duty_ex_cd = fields.Float(string="Tot Duty Ex Cd")
    tot_duty_ex_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_duty_ex_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_duty_ex_cd_ids",
    )
    tot_duty_ex_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_duty_ex_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_duty_ex_ids",
    )
    tot_duty_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_duty_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_duty_ids",
    )
    tot_tax = fields.Float(string="Tot Tax")
    tot_tax_cd = fields.Float(string="Tot Tax Cd")
    tot_tax_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_tax_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_cd_ids",
    )
    tot_tax_ex = fields.Float(string="Tot Tax Ex")
    tot_tax_ex_cd = fields.Float(string="Tot Tax Ex Cd")
    tot_tax_ex_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_tax_ex_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_ex_cd_ids",
    )
    tot_tax_ex_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_tax_ex_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_ex_ids",
    )
    tot_tax_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_tax_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_ids",
    )
    unit_price = fields.Float(string="Unit Price")
    valid_charge = fields.Boolean(string="Valid Charge")
    valid_charge_cd = fields.Boolean(string="Valid Charge Cd")
    valid_charge_ex = fields.Boolean(string="Valid Charge Ex")
    valid_charge_ex_cd = fields.Boolean(string="Valid Charge Ex Cd")
    valid_duty = fields.Boolean(string="Valid Duty")
    valid_duty_cd = fields.Boolean(string="Valid Duty Cd")
    valid_duty_ex = fields.Boolean(string="Valid Duty Ex")
    valid_duty_ex_cd = fields.Boolean(string="Valid Duty Ex Cd")
    valid_tax = fields.Boolean(string="Valid Tax")
    valid_tax_cd = fields.Boolean(string="Valid Tax Cd")
    valid_tax_ex = fields.Boolean(string="Valid Tax Ex")
    valid_tax_ex_cd = fields.Boolean(string="Valid Tax Ex Cd")
    volume = fields.Float(string="Volume")
    warehouse = fields.Many2one(
        "stock.warehouse", string="Warehouse", readonly=True
    )
    weight = fields.Float(string="Weight")


class XConsignmentLineGap(models.Model):
    _inherit = "consignment_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    currency_id = fields.Many2one(
        comodel_name="res.currency", string="Currency", readonly=True
    )
    name = fields.Char(string="Name")
