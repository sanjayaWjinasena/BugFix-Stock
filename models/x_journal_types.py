# -*- coding: utf-8 -*-
"""Sentinel declaration for x_journal_types so cross-references resolve."""
from odoo import fields, models


class XJournalTypes(models.Model):
    _name = 'x_journal_types'
    _description = 'X Journal Types'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Journal Type')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_offset_account = fields.Many2one('account.account', string='Offset Account')
    x_studio_sequence = fields.Integer(string='Sequence')
