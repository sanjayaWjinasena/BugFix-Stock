from odoo import fields, models


class StockLocation(models.Model):
    _inherit = "stock.location"

    color = fields.Integer(string="Color")
    finished_good_location = fields.Boolean(string="Finished Good Location")
    many2many_field_7kpUe = fields.Many2many(
        "res.users",
        "stock_location_x_studio_many2many_field_7kpUe_rel",
        "stock_id",
        "res_users_id",
        string="Users (Cell Visibility)",
    )
    repair_factory_location = fields.Boolean(string="Repair Factory Location")
    repair_return_location = fields.Boolean(string="Repair Return Location")
    return_receipt_location = fields.Many2one(
        "stock.location", string="Return Receipt Location"
    )
    return_sequence = fields.Many2one("ir.sequence", string="Return Sequence")
    temp_location = fields.Boolean(string="Temp Location")
    users_internal_transfer = fields.Many2many(
        "res.users",
        "stock_location_x_studio_users_internal_transfer_rel",
        "stock_id",
        "res_users_id",
        string="Users (Internal Transfer)",
    )
    users_stock_location = fields.Many2many(
        "res.users",
        "stock_location_x_studio_users_stock_location_rel",
        "stock_id",
        "res_users_id",
        string="Users (Stock Location)",
    )


class StockLocationGap(models.Model):
    _inherit = "stock.location"

    color = fields.Integer(string="Color")
