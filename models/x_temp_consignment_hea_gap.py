# -*- coding: utf-8 -*-
from odoo import models, fields

class XTempConsignmentHeaGap(models.Model):
    _inherit = 'x_temp_consignment_hea'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
