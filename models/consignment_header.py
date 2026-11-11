from odoo import fields, models

# NOTE (v0.0.118): the Many2one(s) delivery_term / structure_name were
# MOVED to BugFix-Purchase v0.1.0.178.
# Their comodel is owned by a DOWNSTREAM module; declared here they were
# `_unknown` for the whole upgrade-mode registry build (see BugFix-Purchase
# models/upstream_link_fields.py). Do NOT re-add them here.


class XConsignmentHeader(models.Model):
    """Studio-ported custom model consignment_header."""

    _name = "consignment_header"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Consignment Header"

    active = fields.Boolean()
    color = fields.Integer()
    name = fields.Char(string="Invoice Reference")
    account_charge = fields.Many2one("account.account")
    account_duty = fields.Many2one("account.account")
    account_tax = fields.Many2one("account.account")
    allocate_header_charges = fields.Boolean()
    bill_of_lading = fields.Binary(string="Bill of Lading")
    bill_of_lading_filename = fields.Char(
        string="Filename for x_studio_binary_field_LzgTH"
    )
    cargo_arrival_notice = fields.Binary()
    cargo_arrival_notice_filename = fields.Char(
        string="Filename for x_studio_binary_field_M4Ehh"
    )
    accounting_company_id = fields.Many2one("res.company", string="Company")
    con_validated = fields.Boolean(string="Con. Validated")
    confirm_invoice = fields.Boolean()
    consignment_line_ids = fields.One2many(
        "consignment_line",
        "consignment_header_id",
        string="Consignment Line Ids",
    )
    consolidated = fields.Boolean()
    consolidation_confirmed = fields.Boolean()
    container_no = fields.Char()
    cost_allocation_method = fields.Selection(
        [
            ("equal", "Equal"),
            ("by_quantity", "By Quantity"),
            ("by_current_cost_price", "By Current Cost"),
            ("by_weight", "By Weight"),
            ("by_volume", "By Volume"),
        ],
    )
    create_header_charges = fields.Boolean()
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    custom_clearance = fields.Boolean()
    custom_clearance_exchange_rate = fields.Float()
    custom_clearance_no = fields.Char()
    custom_cleared_date = fields.Date()
    description = fields.Char()
    header_charges_allocated = fields.Boolean()
    accounting_invoice_date = fields.Date(string="Supplier's Invoice Date (Bill Date)")
    lines_copied = fields.Boolean()
    offset_account = fields.Many2one("account.account")
    packing_list = fields.Binary()
    packing_list_filename = fields.Char(
        string="Filename for x_studio_binary_field_xDIyn"
    )
    sequence = fields.Integer()
    shipment_start_date = fields.Date()
    shipping_mode = fields.Selection(
        [("Air", "Air"), ("Sea", "Sea"), ("Road", "Road"), ("Courier", "Courier")],
    )
    status = fields.Selection(
        [
            ("Draft", "Draft"),
            ("Consignment", "Confirmed"),
            ("Consolidated", "Consolidated"),
            ("In Transit", "In Transit"),
            ("Under Custom Clearance", "Under Custom Clearance"),
            ("Done", "Done"),
            ("TP Invoice", "TP Invoice"),
        ],
    )
    status_bar = fields.Selection(
        [
            ("Draft", "Draft"),
            ("Consignment", "Confirmed"),
            ("Consolidated", "Consolidated"),
            ("In Transit", "In Transit"),
            ("Under Custom Clearance", "Under Custom Clearance"),
            ("Done", "Done"),
            ("TP Invoice", "TP Invoice"),
        ],
    )
    supplier_document = fields.Binary(string="Purchase Invoice")
    supplier_document_filename = fields.Char(
        string="Filename for x_studio_binary_field_KSsMR"
    )
    supplier_id = fields.Many2one("res.partner", string="Vendor")
    supplier_invoice_number = fields.Char(
        string="Supplier's Invoice No (Bill Reference)"
    )
    total_allocate_amount = fields.Float(readonly=True)
    total_amount = fields.Float(readonly=True)
    total_amount_cost_allocation_method = fields.Float(readonly=True)
    vend_dispatch_status = fields.Text(string="Vend. Dispatch Status")
    vendor_dispatch = fields.Boolean()
    vendor_dispatch_exchange_rate = fields.Float()
    voucher_date = fields.Date(string="Vendor Dispatch Voucher Date")
    con_no__x_tp_invoice_header_count = fields.Integer(
        string="Created From Consignment No count", store=False
    )
    consignment_id__x_consignment_charge_h_count = fields.Integer(
        string="Consignment Id count", store=False
    )
    consignment_id__x_consignment_charge_l_count = fields.Integer(
        string="Consignment Id count", store=False
    )
    created_from_consignment_1__account_move_count = fields.Integer(
        string="Created From Consignment count", store=False
    )
    created_from_consignment__account_move_count = fields.Integer(
        string="Created From Consignment count", store=False
    )


class XConsignmentHeaderGap(models.Model):
    _inherit = "consignment_header"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    color = fields.Integer()
    name = fields.Char(string="Invoice Reference")
