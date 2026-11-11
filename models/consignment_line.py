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

    active = fields.Boolean()
    currency_id = fields.Many2one("res.currency", readonly=True)
    name = fields.Char()
    allocate_amount = fields.Float(readonly=True)
    amount = fields.Float(readonly=True)  # was Monetary (no currency_field)
    boolean_field_Gbd5Y = fields.Boolean(string="Valid Duty")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    concessional_rate = fields.Boolean()
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
        readonly=True,
    )
    delivery_remainder = fields.Float(readonly=True)
    description = fields.Char(readonly=True, store=False)
    exchange_rate = fields.Float()
    header_charges_allocated = fields.Boolean(readonly=True)
    indent_no = fields.Char(readonly=True)
    invoice_qty = fields.Float(string="Invoice Qty.")
    many2many_field_ZvmKu = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_many2many_field_ZvmKu_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_ex_cd_ids",
    )
    order_remainder = fields.Float(string="Consignment Remainder", readonly=True)
    original_delivery_remainder = fields.Float()
    product_id = fields.Many2one("product.product")
    accounting_purchase_id = fields.Many2one("purchase.order", string="Purchase Order")
    purchase_line_id = fields.Many2one("purchase.order.line", string="Purchase Line Id")
    received_qty = fields.Float(string="Received Qty.", readonly=True)
    sequence = fields.Integer()
    status = fields.Selection(
        [
            ("Draft", "Draft"),
            ("In Transit", "In Transit"),
            ("Under Custom Clearance", "Under Custom Clearance"),
            ("Done", "Done"),
        ],
        readonly=True,
    )
    stock_move_id = fields.Many2one("stock.move", string="Stock Move Id")
    tariff_code = fields.Many2one("tariffmaster", readonly=True, store=False)
    test1 = fields.Char(readonly=True)
    test2 = fields.Many2one("consignment_header", readonly=True)
    tot_charge = fields.Float()
    tot_charge_cd = fields.Float()
    tot_charge_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_charge_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_charge_cd_ids",
    )
    tot_charge_ex = fields.Float()
    tot_charge_ex_cd = fields.Float()
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
    tot_duty = fields.Float()
    tot_duty_cd = fields.Float()
    tot_duty_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_duty_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_duty_cd_ids",
    )
    tot_duty_ex = fields.Float()
    tot_duty_ex_cd = fields.Float()
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
    tot_tax = fields.Float()
    tot_tax_cd = fields.Float()
    tot_tax_cd_ids = fields.Many2many(
        "misc_charge_codes",
        "x_consignment_line_x_studio_tot_tax_cd_ids_rel",
        "x_id",
        "x_misc_charge_codes_id",
        string="tot_tax_cd_ids",
    )
    tot_tax_ex = fields.Float()
    tot_tax_ex_cd = fields.Float()
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
    unit_price = fields.Float()
    valid_charge = fields.Boolean()
    valid_charge_cd = fields.Boolean()
    valid_charge_ex = fields.Boolean()
    valid_charge_ex_cd = fields.Boolean()
    valid_duty = fields.Boolean()
    valid_duty_cd = fields.Boolean()
    valid_duty_ex = fields.Boolean()
    valid_duty_ex_cd = fields.Boolean()
    valid_tax = fields.Boolean()
    valid_tax_cd = fields.Boolean()
    valid_tax_ex = fields.Boolean()
    valid_tax_ex_cd = fields.Boolean()
    volume = fields.Float()
    warehouse = fields.Many2one("stock.warehouse", readonly=True)
    weight = fields.Float()


class XConsignmentLineGap(models.Model):
    _inherit = "consignment_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    currency_id = fields.Many2one(comodel_name="res.currency", readonly=True)
    name = fields.Char()
