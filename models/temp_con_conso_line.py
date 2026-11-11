"""Studio-ported custom model temp_con_conso_line."""

from odoo import fields, models


class XTempConConsoLine(models.Model):
    _name = "temp_con_conso_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Temp Con. Conso. Line"

    name = fields.Char(string="Name")
    consignment_id = fields.Many2one(
        "consignment_header", string="Consignment Id"
    )
    container_no = fields.Char(string="Container No")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    custom_clearance_no = fields.Char(string="Custom Clearance No")
    accounting_invoice_date = fields.Date(string="Invoice Date")
    accounting_select = fields.Boolean(string="Select")
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
            ("In Transit", "In Transit"),
            ("Under Custom Clearance", "Under Custom Clearance"),
            ("Done", "Done"),
            ("TP Invoice", "TP Invoice"),
        ],
        string="Status",
    )
    supplier_id = fields.Many2one("res.partner", string="Vendor")
    supplier_invoice_no = fields.Char(string="Supplier Invoice No")
    temp_consolidated_header_id = fields.Many2one(
        "temp_con_consolidate",
        string="Temp Consolidated Header Id",
        ondelete="cascade",
    )

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   delivery_term (many2one rel='delivery_terms' not safe)


class XTempConConsoLineGap(models.Model):
    _inherit = "temp_con_conso_line"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
