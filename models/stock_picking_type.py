from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    mj_in = fields.Boolean(string="MJ IN")
    mj_out = fields.Boolean(string="MJ OUT")
    movement_journal = fields.Boolean()
