from odoo import fields, models


class StockLot(models.Model):
    _inherit = "stock.lot"

    currency_id = fields.Many2one("res.currency", string="Currency")
    cost = fields.Float(readonly=True)
    no_of_days = fields.Char(string="No of Days", readonly=True, store=False)
    no_of_days_2 = fields.Integer(string="No of Days 2", readonly=True)
    price_1 = fields.Char(readonly=True, store=False)
    price_2 = fields.Char(readonly=True, store=False)
    production_id = fields.Many2one("mrp.production", string="Production Order")
    production_order = fields.Char()
    related_field_IlrRW = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_KzAMe = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_Vz7B8 = fields.Char(string="New Related Field", readonly=True)
    related_field_bz0VM = fields.Boolean(string="New Related Field", readonly=True)
    related_field_e2LSH = fields.Integer(string="New Related Field", readonly=True)
    related_field_fTaKf = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    related_field_jS93T = fields.Integer(string="New Related Field", readonly=True)
    related_field_vTORT = fields.Char(
        string="New Related Field", readonly=True, store=False
    )
    sequence_size = fields.Integer()
    serial_no_prefix = fields.Char()
    starting_serial_no = fields.Integer()
    warehouse = fields.Char(readonly=True)


class StockLotGap(models.Model):
    _inherit = "stock.lot"

    currency_id = fields.Many2one(
        string="Currency", related="product_id.stock_valuation_layer_ids.currency_id"
    )
