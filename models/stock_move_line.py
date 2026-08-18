# -*- coding: utf-8 -*-
from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    x_studio_pr_type = fields.Selection([], string='PR Type', readonly=True)
    x_studio_report_type_production_summary_split = fields.Many2one('x_sales_report_type', string='Report Type - Production Summary Split')
    x_studio_report_type_sales_prod_purch = fields.Many2one('x_sales_report_type', string='Report Type - Sales prod. purch.')
    x_studio_report_type_slow_moving_items = fields.Many2one('x_sales_report_type', string='Report Type - Slow Moving Items')
