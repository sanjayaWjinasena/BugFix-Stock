"""Sentinel declaration for material_request so cross-references resolve."""

from odoo import api, fields, models


class XMaterialRequest(models.Model):
    _name = "material_request"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "X Material Request"

    active = fields.Boolean(default=True)
    name = fields.Char(string="Request Reference")
    done = fields.Boolean(compute="_compute_done", store=True, readonly=True)
    done_stage_updated = fields.Boolean()
    journal_type = fields.Many2one("journal_types")
    many2one_field_6f0Gc = fields.Many2one("hr.department", string="Department")
    many2one_field_THFu6 = fields.Many2one(
        "maintenance.request", string="Maintenance Request No"
    )
    many2one_field_W3qKf = fields.Many2one("stock.warehouse", string="Warehouse-1")
    purchase_new = fields.Char(string="NEW")
    notes = fields.Char()
    # Both O2Ms share the same inverse many2one_field_6yqbk on
    # mr_config — Studio-created redundancy preserved for CDB fidelity.
    one2many_field_9DTZS = fields.One2many(
        "mr_config", "many2one_field_6yqbk", string="New One2many"
    )
    request_lines = fields.One2many("mr_config", "many2one_field_6yqbk")
    requested_by = fields.Many2one("res.users", string="Requested by")
    requested_date = fields.Date()
    selection_field_BupKG = fields.Selection(
        [
            ("Draft", "Draft"),
            ("Confirmed", "Confirmed"),
            ("To Be Approved", "To Be Approved"),
            ("Approved", "Approved"),
            ("Rejected", "Rejected"),
            ("Done", "Done"),
        ],
        string="Status",
    )
    selection_field_X1Bue = fields.Selection(
        [("status1", "Create MR"), ("status2", "Create PR")],
        string="Pipeline status bar",
    )
    sequence = fields.Integer()
    test = fields.Char()
    type = fields.Selection([("Local", "Local"), ("Import", "Import")])
    warehouse = fields.Many2one("stock.location")
    created_from_material_request_no_stock_picking_count = fields.Integer(
        string="Created from Material Request No count",
        compute="_compute_related_stock_picking_count",
        store=False,
    )
    material_request_ref__x_pr_non_inventory_count = fields.Integer(
        string="Material Request ref count",
        compute="_compute_related_x_pr_non_inventory_count",
        store=False,
    )
    material_request_ref__x_purchase_request_count = fields.Integer(
        string="Material Request ref count",
        compute="_compute_related_x_purchase_request_count",
        store=False,
    )

    @api.depends("done_stage_updated")
    def _compute_done(self):
        # Ported from CDB Studio compute. Side-effects (writing status +
        # done_stage_updated) preserved verbatim — original Studio behavior
        # advances status to 'Done' when all deliveries complete and no
        # transfer remainder is left.
        SP = self.env["stock.picking"]
        for rec in self:
            task_status = False
            if not rec.id:
                rec.done = False
                continue
            delivery = SP.search(
                [("created_from_material_request_no", "=", rec.id)], limit=1
            )
            if delivery:
                open_delivery = SP.search(
                    [
                        ("created_from_material_request_no", "=", rec.id),
                        ("state", "not in", ["done", "cancel"]),
                    ],
                    limit=1,
                )
                task_status = not open_delivery
            for line in rec.request_lines:
                if line.transfer_remainder > 0:
                    task_status = False
                    break
            if task_status and not rec.done_stage_updated:
                rec.selection_field_BupKG = "Done"
                rec.done_stage_updated = True
            rec.done = task_status

    def _compute_related_stock_picking_count(self):
        SP = self.env["stock.picking"]
        has_field = "created_from_material_request_no" in SP._fields
        for rec in self:
            if has_field:
                rec.created_from_material_request_no_stock_picking_count = (
                    SP.search_count([("created_from_material_request_no", "=", rec.id)])
                )
            else:
                rec.created_from_material_request_no_stock_picking_count = 0

    def _compute_related_x_pr_non_inventory_count(self):
        for rec in self:
            rec.material_request_ref__x_pr_non_inventory_count = self.env[
                "pr_non_inventory"
            ].search_count([("material_request_ref", "=", rec.id)])

    def _compute_related_x_purchase_request_count(self):
        for rec in self:
            rec.material_request_ref__x_purchase_request_count = self.env[
                "purchase_request"
            ].search_count([("material_request_ref", "=", rec.id)])
