"""Studio-ported custom model material_request_mt."""

from odoo import fields, models


class XMaterialRequestMt(models.Model):
    _name = "material_request_mt"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Material Request MT"

    color = fields.Integer()
    name = fields.Char(string="Description", required=True)
    accounting_company_id = fields.Many2one("res.company", string="Company")
    created_by = fields.Char(string="Created by")
    created_on = fields.Char(string="Created on")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    date = fields.Date()
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="End Date")
    department = fields.Char()
    image = fields.Binary()
    journal_type = fields.Char()
    kanban_state = fields.Selection(
        [("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")],
    )
    maintenance_request_no = fields.Char()
    many2one_field_32i_1j8i1f37m = fields.Many2one("hr.department", string="Department")
    notes = fields.Html()
    notes_1 = fields.Char(string="Notes")
    partner_email = fields.Char(string="Email")
    partner_id = fields.Many2one("res.partner", string="Contact")
    partner_phone = fields.Char(string="Phone")
    custom_reports_priority = fields.Boolean(string="High Priority")
    request_reference = fields.Char()
    requested_by = fields.Char()
    requested_date = fields.Char()
    sequence = fields.Integer()
    stage_id = fields.Many2one("material_request_mt_stage", required=True)
    status = fields.Char()
    tag_ids = fields.Many2many(
        "material_request_mt_tag",
        relation="x_material_request_mt_x_material_request_mt_tag_rel",
        column1="x_material_request_mt_id",
        column2="x_material_request_mt_tag_id",
        string="Tags",
    )
    user_id = fields.Many2one("res.users", string="Responsible")
    value = fields.Monetary(currency_field="accounting_currency_id")
    warehouse = fields.Char()
    # Fields gap D.2 REVERT v0.81: O2M inverse causes registry-setup KeyError
    # on module-load-order edge cases (comodel is in BugFix-Studio-Misc,
    # cross-module _fields lookup fragile). Deferred as permanent skip.


class XMaterialRequestMtGap(models.Model):
    _inherit = "material_request_mt"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    color = fields.Integer()
    # STRIPPED material_request_mt_line_ids_7737e: O2M inverse lives in another repo
    # (load-order risk)
    name = fields.Char(string="Description", required=True)
