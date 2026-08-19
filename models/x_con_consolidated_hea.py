# -*- coding: utf-8 -*-
"""Sentinel declaration for x_con_consolidated_hea."""
from odoo import fields, models


class XConConsolidatedHea(models.Model):
    _name = 'x_con_consolidated_hea'
    _description = 'X Con Consolidated Hea'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Con. Reference')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    # TODO: x_studio_con_line_ids = fields.One2many('x_con_consolidated_lin', <inverse>, string='Con. Line Ids')
    x_studio_description = fields.Char(string='Description')
    x_studio_lines_copied = fields.Boolean(string='Lines Copied')
    x_studio_pipeline_status_bar = fields.Selection([], string='Pipeline Status Bar')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_status = fields.Selection([], string='Status')
