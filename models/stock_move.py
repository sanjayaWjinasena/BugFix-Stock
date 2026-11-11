from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    melt_item = fields.Boolean(readonly=True, store=False)
    melt_item_2 = fields.Boolean(readonly=True, store=False)
    melt_item_3 = fields.Boolean(readonly=True, store=False)
    original_qty = fields.Float(readonly=True)
    pr_type = fields.Selection(
        [("Local", "Local"), ("Import", "Import")], string="PR Type", readonly=True
    )
    report_type_production_job_variance = fields.Many2one(
        "sales_report_type", string="Report Type - Production Job Variance"
    )
    update_consignment = fields.Boolean(readonly=True)
    variance = fields.Float(readonly=True, store=False)
