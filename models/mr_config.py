"""mr_config declared in BugFix-Stock so material_request's O2M
inverse + notebook page arch validate at Stock load time.

mr_config is also declared in BugFix-Purchase with the same fields.
Odoo's _name-based class union merges the two declarations at
Purchase-load time. Field declarations MUST match between the two
modules (same ttype, same string, same store, same compute/related, etc.)
or Odoo logs a warning and the later declaration wins.

Load order at runtime:
  base -> stock -> BugFix-Stock (this file)
    -> purchase_stock -> purchase -> BugFix-Purchase (equivalent file)
"""

from odoo import api, fields, models


class XMrConfig(models.Model):
    _name = "mr_config"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "MR config"
    _rec_name = "name"
    _order = "sequence asc, id asc"

    active = fields.Boolean(string="Active", default=True, copy=True)
    currency_id = fields.Many2one(
        "res.currency", string="Currency", ondelete="set null", copy=True
    )
    name = fields.Char(string="Name", copy=True)
    available_qty_to_transfer = fields.Float(
        string="Available Qty. to Transfer",
        store=False,
        compute="_compute_available_qty_to_transfer",
        readonly=True,
    )
    description = fields.Html(
        string="Description",
        store=False,
        related="product.description",
        readonly=True,
    )
    description_1 = fields.Char(
        string="Description",
        store=False,
        related="product.name",
        readonly=True,
    )
    inventory_location = fields.Many2one(
        "stock.location",
        string="Inventory Location ",
        store=False,
        ondelete="set null",
        related="many2one_field_02S0w.property_stock_inventory",
        readonly=True,
    )
    inventory_location_1 = fields.Many2one(
        "stock.location",
        string="Inventory Location ",
        store=False,
        ondelete="set null",
        related="many2one_field_2LV9q.property_stock_inventory",
        readonly=True,
    )
    many2one_field_02S0w = fields.Many2one(
        "product.product", string="Product-1", ondelete="set null", copy=True
    )
    many2one_field_2LV9q = fields.Many2one(
        "product.product", string="Product-2", ondelete="set null", copy=True
    )
    many2one_field_6cvHX = fields.Many2one(
        "maintenance.request",
        string="Maintenance Request",
        ondelete="set null",
        copy=True,
    )
    many2one_field_6yqbk = fields.Many2one(
        "material_request", string="Material Request", ondelete="set null", copy=True
    )
    on_hand_qty = fields.Float(
        string="On Hand Qty",
        store=False,
        related="many2one_field_02S0w.qty_available",
        readonly=True,
    )
    on_hand_qty_1 = fields.Float(
        string="On Hand Qty",
        store=False,
        related="many2one_field_02S0w.qty_available",
        readonly=True,
    )
    on_hand_qty_2 = fields.Float(
        string="On Hand Qty",
        store=False,
        compute="_compute_on_hand_qty_2",
        readonly=True,
    )
    product = fields.Many2one(
        "product.product", string="Product", ondelete="set null", copy=True
    )
    qty = fields.Integer(string="Qty", copy=True)
    qty_1 = fields.Integer(copy=True)
    qty_to_transfer = fields.Float(string="Qty. to Transfer", copy=True)
    qty_transfered = fields.Float(string="Qty. Transferred", copy=True)
    quantity = fields.Float(string="Quantity", copy=True)
    requested_by = fields.Many2one(
        "res.users", string="Requested by", ondelete="set null", copy=True
    )
    sequence = fields.Integer(string="Sequence", copy=True)
    status = fields.Selection(
        string="Status",
        related="many2one_field_6yqbk.selection_field_BupKG",
        readonly=True,
    )
    text = fields.Char(string="Text", copy=True)
    text_1 = fields.Char(string="Notes", copy=True)
    transfer_remainder = fields.Float(
        string="Transfer Remainder",
        store=False,
        compute="_compute_transfer_remainder",
        readonly=True,
    )
    uom = fields.Many2one(
        "uom.uom",
        string="UoM",
        store=False,
        ondelete="set null",
        related="many2one_field_02S0w.uom_id",
        readonly=True,
    )
    uom_1 = fields.Many2one(
        "uom.uom",
        string="UoM",
        store=False,
        ondelete="set null",
        related="many2one_field_2LV9q.uom_id",
        readonly=True,
    )
    uom_1_1 = fields.Char(
        string="UOM-1",
        store=False,
        related="product.uom_id.display_name",
        readonly=True,
    )
    uom_2 = fields.Char(
        string="UOM", related="product.uom_id.name", readonly=True
    )
    warehouse = fields.Many2one(
        "stock.location",
        string="Warehouse",
        ondelete="set null",
        related="many2one_field_6yqbk.warehouse",
        readonly=True,
    )

    @api.depends("quantity", "qty_transfered")
    def _compute_transfer_remainder(self):
        for rec in self:
            rec.transfer_remainder = rec.quantity - rec.qty_transfered

    @api.depends("quantity", "on_hand_qty_2", "qty_transfered")
    def _compute_available_qty_to_transfer(self):
        # Ported from CDB Studio compute - preserves the branch logic
        # despite unusual conditions.
        for rec in self:
            onhand_qty = 0
            if rec.qty_transfered == 0:
                if rec.quantity <= rec.on_hand_qty_2:
                    onhand_qty = rec.quantity
                else:
                    onhand_qty = rec.on_hand_qty_2
            else:
                if (
                    rec.quantity - rec.qty_transfered
                ) <= rec.on_hand_qty_2:
                    onhand_qty = (rec.quantity - rec.qty_transfered) - (
                        rec.quantity - rec.on_hand_qty_2
                    )
                else:
                    onhand_qty = rec.on_hand_qty_2
            rec.available_qty_to_transfer = onhand_qty

    @api.depends("product", "warehouse")
    def _compute_on_hand_qty_2(self):
        # Ported from CDB Studio compute. Original code had a loop that
        # overwrote onhand_qty each iteration - preserved verbatim to
        # match CDB behavior. If warehouse is unset, guards
        # against False comparison.
        SQ = self.env["stock.quant"]
        for rec in self:
            onhand_qty = 0.0
            if rec.product and rec.warehouse:
                quants = SQ.search(
                    [
                        ("product_id", "=", rec.product.id),
                        ("location_id", "=", rec.warehouse.id),
                    ]
                )
                if quants:
                    onhand_qty = (
                        quants.available_quantity
                    )  # verbatim CDB - reads .available_quantity on the recordset
            rec.on_hand_qty_2 = onhand_qty
