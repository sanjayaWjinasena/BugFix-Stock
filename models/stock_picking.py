from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    analytic_account = fields.Many2one(
        "account.analytic.account", string="Analytic Account", readonly=True
    )
    budget_created = fields.Boolean(readonly=True)
    cancelled = fields.Boolean(readonly=True)
    cash_full_payment_made = fields.Boolean(readonly=True, store=False)
    consignment_no = fields.Many2one("consignment_header")
    created_from_help_ticket = fields.Many2one(
        "helpdesk.ticket", string="Created from Help Ticket"
    )
    created_from_material_request_no = fields.Many2one(
        "material_request", string="Created from Material Request No"
    )
    custom_clearance_no = fields.Char(readonly=True)
    factory_repair = fields.Boolean()
    fsm_task_done = fields.Boolean(string="FSM Task Done", readonly=True, store=False)
    fully_paid_so = fields.Boolean(string="Fully Paid SO", readonly=True, store=False)
    gl_account_status = fields.Selection(
        [("Pending", "Pending"), ("Updated", "Updated")], string="G/L Account Status"
    )
    helpdesk_ticket_id = fields.Many2one("helpdesk.ticket", string="Helpdesk Ticket Id")
    journal_type = fields.Many2one("journal_types")
    maintenance_request_ = fields.Many2one(
        "maintenance.request", string="Maintenance Request #"
    )
    # Clear-DB: related to the operation type (stored, readonly). The port had dropped related=, so the
    # Movement Journal flags stayed False and the Journal Type field never showed on Movement Journal transfers.
    mj_in = fields.Boolean(
        string="MJ IN",
        related="picking_type_id.mj_in",
        store=True,
        readonly=True,
    )
    mj_out = fields.Boolean(
        string="MJ OUT",
        related="picking_type_id.mj_out",
        store=True,
        readonly=True,
    )
    movement_journal = fields.Boolean(
        string="Movement Journal",
        related="picking_type_id.movement_journal",
        store=True,
        readonly=True,
    )
    need_approval = fields.Boolean(readonly=True, store=False)
    offset_account_updated = fields.Boolean()
    picking_count = fields.Boolean()
    pr_type = fields.Selection(
        [("Local", "Local"), ("Import", "Import")], string="PR Type", readonly=True
    )
    quotation_type = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
        string="Quotation Type",
        readonly=True,
    )
    quotation_type_2 = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
        string="Quotation Type-2",
        readonly=True,
    )
    received_at_centre = fields.Boolean(string="Received at Centre")
    related_field_zZDiA = fields.Selection(
        [("Sales", "Sales"), ("Project", "Project"), ("Repair", "Repair")],
        string="New Related Field",
        readonly=True,
    )
    repair_payment_made = fields.Boolean(readonly=True, store=False)
    repair_return_location = fields.Boolean(readonly=True)
    return_receipt_location = fields.Many2one("stock.location", readonly=True)
    return_sequence = fields.Many2one("ir.sequence", readonly=True)
    sales_order = fields.Many2one("sale.order", string="Sales Order")
    sequence_code = fields.Char(
        string="Sequence Code",
        related="picking_type_id.sequence_code",
        store=True,
        readonly=True,
    )
    supplier_invoice_number = fields.Char()
    supplier_invoice_number_1 = fields.Char(
        string="Supplier Invoice Number", readonly=True
    )
    task_status = fields.Boolean(readonly=True, store=False)
    ticket_sales_order = fields.Many2one(
        "sale.order", string="Ticket Sales Order", readonly=True, store=False
    )
    transfer_approval = fields.Boolean()
    transfer_approved = fields.Boolean()
    transfer_rejected = fields.Boolean()
    transfer_request_sent = fields.Boolean()
    ttt = fields.Boolean(string="TTT")
    type_of_operation = fields.Selection(
        string="Type of Operation",
        readonly=True,
        related="picking_type_id.code",
        store=True,
    )
    update_consignment = fields.Boolean()
    user_location_validation = fields.Boolean(readonly=True, store=False)
    user_location_validation_2 = fields.Boolean()
    valid_factory_repair = fields.Boolean(readonly=True, store=False)
    valid_transfer_lines = fields.Boolean(readonly=True, store=False)
    validation = fields.Char()
    xxx = fields.Boolean(string="XXX")
    create_from_transfer_1__account_move_count = fields.Integer(
        string="Create From Transfer count", store=False
    )
    created_from_transfer__account_move_count = fields.Integer(
        string="Created From Transfer count", store=False
    )

    def _action_done(self):
        res = super()._action_done()
        for picking in self.filtered(
            lambda p: p.state == "done" and p.movement_journal
        ):
            picking._apply_movement_journal_offset_account()
        return res

    def _apply_movement_journal_offset_account(self):
        """Post the valuation of a Movement IN/OUT to the offset account of the Journal Type
        (replaces the interim Received / Delivered account line)."""
        self.ensure_one()
        offset = self.journal_type.offset_account
        if not offset or not (self.mj_in or self.mj_out):
            return
        for move in self.move_ids:
            categ = move.product_id.categ_id
            interim = (
                categ.property_stock_account_output_categ_id
                if self.mj_out
                else categ.property_stock_account_input_categ_id
            )
            if not interim or interim == offset:
                continue
            account_moves = move.stock_valuation_layer_ids.account_move_id
            lines = account_moves.line_ids.filtered(lambda l: l.account_id == interim)
            if lines:
                lines.write({"account_id": offset.id})
        self.write(
            {
                "offset_account_updated": True,
                "gl_account_status": "Updated",
            }
        )
