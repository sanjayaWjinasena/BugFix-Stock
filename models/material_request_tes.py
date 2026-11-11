"""Studio-ported custom model material_request_tes."""

from odoo import fields, models


class XMaterialRequestTes(models.Model):
    _name = "material_request_tes"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Material Request Test"

    color = fields.Integer(string="Color")
    name = fields.Char(string="Description", required=True)
    accounting_company_id = fields.Many2one("res.company", string="Company")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    date = fields.Date(string="Date")
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="End Date")
    image = fields.Binary(string="Image")
    kanban_state = fields.Selection(
        [("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")],
        string="Kanban State",
    )
    notes = fields.Html(string="Notes")
    partner_email = fields.Char(string="Email")
    partner_id = fields.Many2one("res.partner", string="Contact")
    partner_phone = fields.Char(string="Phone")
    custom_reports_priority = fields.Boolean(string="High Priority")
    sequence = fields.Integer(string="Sequence")
    user_id = fields.Many2one("res.users", string="Responsible")
    value = fields.Monetary(string="Value", currency_field="accounting_currency_id")

    # Fields gap D.2 REVERT v0.81: O2M inverse causes registry-setup KeyError
    # on module-load-order edge cases (comodel is in BugFix-Studio-Misc,
    # cross-module _fields lookup fragile). Deferred as permanent skip.
    # Still deferred (comodels not on dev):
    #   stage_id (many2one rel='material_request_tes_stage')
    #   tag_ids (many2many rel='material_request_tes_tag')


class XMaterialRequestTesGap(models.Model):
    _inherit = "material_request_tes"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    # STRIPPED material_request_tes_line_ids_661d3: O2M inverse lives in another repo
    # (load-order risk)
    name = fields.Char(string="Description", required=True)
    stage_id = fields.Many2one(
        comodel_name="material_request_tes_stage", string="Stage", required=True
    )
    tag_ids = fields.Many2many(
        comodel_name="material_request_tes_tag",
        relation="x_material_request_tes_x_material_request_tes_tag_rel",
        column1="x_material_request_tes_id",
        column2="x_material_request_tes_tag_id",
        string="Tags",
    )
