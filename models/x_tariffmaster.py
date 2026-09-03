# -*- coding: utf-8 -*-
"""Sentinel declaration for x_tariffmaster so cross-references resolve."""
from odoo import fields, models


class XTariffmaster(models.Model):
    _name = 'x_tariffmaster'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'X Tariffmaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    # TODO: x_studio_tariff_master_ids = fields.One2many('x_tariff_date', <inverse>, string='Date Range')
