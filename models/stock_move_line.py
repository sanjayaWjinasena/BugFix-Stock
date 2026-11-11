from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    pr_type = fields.Selection(
        [("Local", "Local"), ("Import", "Import")], string="PR Type", readonly=True
    )
    report_type_production_summary_split = fields.Many2one(
        "sales_report_type", string="Report Type - Production Summary Split"
    )
    report_type_sales_prod_purch = fields.Many2one(
        "sales_report_type", string="Report Type - Sales prod. purch."
    )
    report_type_slow_moving_items = fields.Many2one(
        "sales_report_type", string="Report Type - Slow Moving Items"
    )
