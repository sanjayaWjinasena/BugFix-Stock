# -*- coding: utf-8 -*-
"""Studio-ported custom model x_material_request_mt."""
from odoo import fields, models


class XMaterialRequestMt(models.Model):
    _name = 'x_material_request_mt'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Material Request MT'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Description', required=True)
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_created_by = fields.Char(string='Created by')
    x_studio_created_on = fields.Char(string='Created on')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_date = fields.Date(string='Date')
    x_studio_date_start = fields.Datetime(string='Start Date')
    x_studio_date_stop = fields.Datetime(string='End Date')
    x_studio_department = fields.Char(string='Department')
    x_studio_image = fields.Binary(string='Image')
    x_studio_journal_type = fields.Char(string='Journal Type')
    x_studio_kanban_state = fields.Selection([], string='Kanban State')
    x_studio_maintenance_request_no = fields.Char(string='Maintenance Request No')
    x_studio_many2one_field_32i_1j8i1f37m = fields.Many2one('hr.department', string='Department')
    x_studio_notes = fields.Html(string='Notes')
    x_studio_notes_1 = fields.Char(string='Notes')
    x_studio_partner_email = fields.Char(string='Email')
    x_studio_partner_id = fields.Many2one('res.partner', string='Contact')
    x_studio_partner_phone = fields.Char(string='Phone')
    x_studio_priority = fields.Boolean(string='High Priority')
    x_studio_request_reference = fields.Char(string='Request Reference')
    x_studio_requested_by = fields.Char(string='Requested By')
    x_studio_requested_date = fields.Char(string='Requested Date')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_stage_id = fields.Many2one('x_material_request_mt_stage', string='Stage', required=True)
    x_studio_status = fields.Char(string='Status')
    x_studio_tag_ids = fields.Many2many('x_material_request_mt_tag', string='Tags')
    x_studio_user_id = fields.Many2one('res.users', string='Responsible')
    x_studio_value = fields.Monetary(string='Value')
    x_studio_warehouse = fields.Char(string='Warehouse')

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   x_material_request_mt_line_ids_7737e (one2many rel='x_material_request_mt_line_9a011' not safe)
