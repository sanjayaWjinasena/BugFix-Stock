# -*- coding: utf-8 -*-
from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    x_studio_melt_item = fields.Boolean(string='Melt Item', readonly=True, store=False)
    x_studio_melt_item_2 = fields.Boolean(string='Melt Item 2', readonly=True, store=False)
    x_studio_melt_item_3 = fields.Boolean(string='Melt Item 3', readonly=True, store=False)
    x_studio_original_qty = fields.Float(string='Original Qty', readonly=True)
    x_studio_pr_type = fields.Selection([], string='PR Type', readonly=True)
    x_studio_report_type_production_job_variance = fields.Many2one('x_sales_report_type', string='Report Type - Production Job Variance')
    x_studio_update_consignment = fields.Boolean(string='Update Consignment', readonly=True)
    x_studio_variance = fields.Float(string='Variance', readonly=True, store=False)
