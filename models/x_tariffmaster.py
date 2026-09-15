# -*- coding: utf-8 -*-
"""Sentinel declaration for x_tariffmaster so cross-references resolve."""
from odoo import fields, models


class XTariffmaster(models.Model):
    _name = 'x_tariffmaster'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'TariffMaster'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Tarrif Code')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_description = fields.Char(string='Description')
    x_studio_sequence = fields.Integer(string='Sequence')
    # x_studio_tariff_master_ids O2M cannot be shipped: CDB names the O2M
    # AND its inverse M2O identically, causing Odoo setup_nonrelated to
    # KeyError. Would need renaming the inverse on x_tariff_date (destructive).
    # Deferred as permanent skip.
