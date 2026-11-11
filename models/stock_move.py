from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    melt_item = fields.Boolean(string="Melt Item", readonly=True, store=False)
    melt_item_2 = fields.Boolean(
        string="Melt Item 2", readonly=True, store=False
    )
    melt_item_3 = fields.Boolean(
        string="Melt Item 3", readonly=True, store=False
    )
    original_qty = fields.Float(string="Original Qty", readonly=True)
    pr_type = fields.Selection(
        [("Local", "Local"), ("Import", "Import")], string="PR Type", readonly=True
    )
    report_type_production_job_variance = fields.Many2one(
        "sales_report_type", string="Report Type - Production Job Variance"
    )
    update_consignment = fields.Boolean(
        string="Update Consignment", readonly=True
    )
    variance = fields.Float(string="Variance", readonly=True, store=False)
