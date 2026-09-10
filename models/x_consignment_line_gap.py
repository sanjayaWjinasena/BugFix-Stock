# -*- coding: utf-8 -*-
from odoo import models, fields

class XConsignmentLineGap(models.Model):
    _inherit = 'x_consignment_line'

    x_active = fields.Boolean(string='Active')
    x_currency_id = fields.Many2one(comodel_name='res.currency', string='Currency', readonly=True)
    x_name = fields.Char(string='Name')
