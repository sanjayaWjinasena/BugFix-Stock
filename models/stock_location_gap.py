from odoo import fields, models


class StockLocationGap(models.Model):
    _inherit = "stock.location"

    x_color = fields.Integer(string="Color")
