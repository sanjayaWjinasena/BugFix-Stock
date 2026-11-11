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

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    name = fields.Char(string="Invoice Reference")
    account_charge = fields.Many2one(
        "account.account", string="Account Charge"
    )
    account_duty = fields.Many2one("account.account", string="Account Duty")
    account_tax = fields.Many2one("account.account", string="Account Tax")
    allocate_header_charges = fields.Boolean(string="Allocate Header Charges")
    bill_of_lading = fields.Binary(string="Bill of Lading")
    bill_of_lading_filename = fields.Char(
        string="Filename for x_studio_binary_field_LzgTH"
    )
    cargo_arrival_notice = fields.Binary(string="Cargo Arrival Notice")
    cargo_arrival_notice_filename = fields.Char(
        string="Filename for x_studio_binary_field_M4Ehh"
    )
    accounting_company_id = fields.Many2one("res.company", string="Company")
    con_validated = fields.Boolean(string="Con. Validated")
    confirm_invoice = fields.Boolean(string="Confirm Invoice")
    consignment_line_ids = fields.One2many(
        "consignment_line",
        "consignment_header_id",
        string="Consignment Line Ids",
    )
    consolidated = fields.Boolean(string="Consolidated")
    consolidation_confirmed = fields.Boolean(string="Consolidation Confirmed")
    container_no = fields.Char(string="Container No")
    cost_allocation_method = fields.Selection(
        [
            ("equal", "Equal"),
            ("by_quantity", "By Quantity"),
            ("by_current_cost_price", "By Current Cost"),
            ("by_weight", "By Weight"),
            ("by_volume", "By Volume"),
        ],
        string="Cost Allocation Method",
    )
    create_header_charges = fields.Boolean(string="Create Header Charges")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    custom_clearance = fields.Boolean(string="Custom Clearance")
    custom_clearance_exchange_rate = fields.Float(
        string="Custom Clearance Exchange Rate"
    )
    custom_clearance_no = fields.Char(string="Custom Clearance No")
    custom_cleared_date = fields.Date(string="Custom Cleared Date")
    description = fields.Char(string="Description")
    header_charges_allocated = fields.Boolean(
        string="Header Charges Allocated"
    )
    accounting_invoice_date = fields.Date(string="Supplier's Invoice Date (Bill Date)")
    lines_copied = fields.Boolean(string="Lines Copied")
    offset_account = fields.Many2one(
        "account.account", string="Offset Account"
    )
    packing_list = fields.Binary(string="Packing List")
    packing_list_filename = fields.Char(
        string="Filename for x_studio_binary_field_xDIyn"
    )
    sequence = fields.Integer(string="Sequence")
    shipment_start_date = fields.Date(string="Shipment Start Date")
    shipping_mode = fields.Selection(
        [("Air", "Air"), ("Sea", "Sea"), ("Road", "Road"), ("Courier", "Courier")],
        string="Shipping Mode",
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
        string="Status",
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
        string="Status Bar",
    )
    supplier_document = fields.Binary(string="Purchase Invoice")
    supplier_document_filename = fields.Char(
        string="Filename for x_studio_binary_field_KSsMR"
    )
    supplier_id = fields.Many2one("res.partner", string="Vendor")
    supplier_invoice_number = fields.Char(
        string="Supplier's Invoice No (Bill Reference)"
    )
    total_allocate_amount = fields.Float(
        string="Total Allocate Amount", readonly=True
    )
    total_amount = fields.Float(string="Total Amount", readonly=True)
    total_amount_cost_allocation_method = fields.Float(
        string="Total Amount Cost Allocation Method", readonly=True
    )
    vend_dispatch_status = fields.Text(string="Vend. Dispatch Status")
    vendor_dispatch = fields.Boolean(string="Vendor Dispatch")
    vendor_dispatch_exchange_rate = fields.Float(
        string="Vendor Dispatch Exchange Rate"
    )
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

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    name = fields.Char(string="Invoice Reference")
