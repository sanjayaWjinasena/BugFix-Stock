from odoo import fields, models


class StockReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    repair_normal_with_serial_no = fields.Boolean(
        string="Repair Normal With Serial No", readonly=True, store=False
    )
    repair_normal_without_serial_no = fields.Boolean(
        string="Repair Normal Without Serial No", readonly=True
    )
    repair_rug = fields.Boolean(string="Repair RUG", readonly=True, store=False)
    suggested_location_id = fields.Many2one(
        "stock.location", string="Suggested Return Location", readonly=True
    )
    suggested_location_id_1 = fields.Many2one(
        "stock.location", string="Suggested Return Location", readonly=True
    )
