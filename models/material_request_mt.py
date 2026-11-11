"""Studio-ported custom model material_request_mt."""

from odoo import fields, models


class XMaterialRequestMt(models.Model):
    _name = "material_request_mt"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Material Request MT"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Description", required=True)
    accounting_company_id = fields.Many2one("res.company", string="Company")
    created_by = fields.Char(string="Created by")
    created_on = fields.Char(string="Created on")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    date = fields.Date(string="Date")
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="End Date")
    department = fields.Char(string="Department")
    image = fields.Binary(string="Image")
    journal_type = fields.Char(string="Journal Type")
    kanban_state = fields.Selection(
        [("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")],
        string="Kanban State",
    )
    maintenance_request_no = fields.Char(string="Maintenance Request No")
    many2one_field_32i_1j8i1f37m = fields.Many2one("hr.department", string="Department")
    notes = fields.Html(string="Notes")
    notes_1 = fields.Char(string="Notes")
    partner_email = fields.Char(string="Email")
    partner_id = fields.Many2one("res.partner", string="Contact")
    partner_phone = fields.Char(string="Phone")
    custom_reports_priority = fields.Boolean(string="High Priority")
    request_reference = fields.Char(string="Request Reference")
    requested_by = fields.Char(string="Requested By")
    requested_date = fields.Char(string="Requested Date")
    sequence = fields.Integer(string="Sequence")
    stage_id = fields.Many2one(
        "material_request_mt_stage", string="Stage", required=True
    )
    status = fields.Char(string="Status")
    tag_ids = fields.Many2many(
        "material_request_mt_tag",
        relation="x_material_request_mt_x_material_request_mt_tag_rel",
        column1="x_material_request_mt_id",
        column2="x_material_request_mt_tag_id",
        string="Tags",
    )
    user_id = fields.Many2one("res.users", string="Responsible")
    value = fields.Monetary(string="Value", currency_field="accounting_currency_id")
    warehouse = fields.Char(string="Warehouse")
    # Fields gap D.2 REVERT v0.81: O2M inverse causes registry-setup KeyError
    # on module-load-order edge cases (comodel is in BugFix-Studio-Misc,
    # cross-module _fields lookup fragile). Deferred as permanent skip.


class XMaterialRequestMtGap(models.Model):
    _inherit = "material_request_mt"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    # STRIPPED material_request_mt_line_ids_7737e: O2M inverse lives in another repo
    # (load-order risk)
    name = fields.Char(string="Description", required=True)
