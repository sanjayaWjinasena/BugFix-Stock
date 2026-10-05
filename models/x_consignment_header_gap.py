# -*- coding: utf-8 -*-
from odoo import models, fields

class XConsignmentHeaderGap(models.Model):
    _inherit = 'x_consignment_header'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Invoice Reference')
