# -*- coding: utf-8 -*-
from odoo import models, fields

class XConsignmentHeaderGap(models.Model):
    _inherit = 'x_consignment_header'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Invoice Reference')
