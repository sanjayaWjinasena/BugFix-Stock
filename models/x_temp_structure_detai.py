# -*- coding: utf-8 -*-
"""Studio-ported custom model x_temp_structure_detai."""
from odoo import fields, models


class XTempStructureDetai(models.Model):
    _name = 'x_temp_structure_detai'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Temp Structure Details'

    x_name = fields.Char(string='Name')
    x_studio_charge_group = fields.Selection([('None', 'None'), ('Charges', 'Charges'), ('Duty', 'Duty'), ('Taxes', 'Taxes'), ('Assessable Value', 'Assessable Value')], string='Charge Group')
    x_studio_charge_name = fields.Char(string='Charge Name')
    x_studio_select = fields.Boolean(string='Select')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_temp_structure_master_id = fields.Many2one('x_temp_structure_maste', string='Temp Structure Master Id')

    # TODO: skipped fields (unresolvable comodel or O2M inverse):
    #   x_studio_structure_details_line_ids (many2one rel='x_structure_details' not safe)
