# -*- coding: utf-8 -*-
"""Studio-ported custom model x_material_request_tes."""
from odoo import fields, models


class XMaterialRequestTes(models.Model):
    _name = 'x_material_request_tes'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Material Request Test'

    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Description', required=True)
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_date = fields.Date(string='Date')
    x_studio_date_start = fields.Datetime(string='Start Date')
    x_studio_date_stop = fields.Datetime(string='End Date')
    x_studio_image = fields.Binary(string='Image')
    x_studio_kanban_state = fields.Selection([('normal', 'In Progress'), ('done', 'Ready'), ('blocked', 'Blocked')], string='Kanban State')
    x_studio_notes = fields.Html(string='Notes')
    x_studio_partner_email = fields.Char(string='Email')
    x_studio_partner_id = fields.Many2one('res.partner', string='Contact')
    x_studio_partner_phone = fields.Char(string='Phone')
    x_studio_priority = fields.Boolean(string='High Priority')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_user_id = fields.Many2one('res.users', string='Responsible')
    x_studio_value = fields.Monetary(string='Value', currency_field='x_studio_currency_id')

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   x_material_request_tes_line_ids_661d3 (one2many rel='x_material_request_tes_line_3301b' not safe)
    #   x_studio_stage_id (many2one rel='x_material_request_tes_stage' not safe)
    #   x_studio_tag_ids (many2many rel='x_material_request_tes_tag' not safe)
