# -*- coding: utf-8 -*-
"""Studio-ported custom model x_temp_con_consolidate."""
from odoo import fields, models


class XTempConConsolidate(models.Model):
    _name = 'x_temp_con_consolidate'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Temp Con. Consolidated Header'

    x_name = fields.Char(string='Name')
    x_studio_consolidated_header_id = fields.Many2one('x_con_consolidated_hea', string='Consolidated Header Id')
    x_studio_select_all = fields.Boolean(string='Select All')
    x_studio_sequence = fields.Integer(string='Sequence')

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   x_studio_con_lines (one2many rel='x_temp_con_conso_line' needs inverse)
