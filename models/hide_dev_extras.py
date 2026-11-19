# -*- coding: utf-8 -*-
"""Hide fields/buttons of apps Jinasena doesn't use on the transfer form.

Replaces views/stock_picking_hide_dev_extras.xml (v0.0.123). That view used
one hard <xpath> per element; when an app providing an element is not
installed (or gets uninstalled) the xpath cannot be located and Odoo refuses
to render the whole transfer form. Here the elements are hidden in
_get_view, only if they are present.
"""
from odoo import models

STOCK_PICKING_EXTRAS = [
    ('field', 'is_subcontract'), ('field', 'show_subcontracting_details_visible'),
    ('field', 'subcontracting_source_purchase_count'), ('field', 'eway_bill_number'),
    ('button', 'action_record_components'), ('button', 'action_show_subcontract_details'),
    ('button', 'action_view_subcontracting_source_purchase'), ('button', 'action_retry_amazon_sync'),
]


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super()._get_view(view_id, view_type, **options)
        if view_type == 'form' and view == self.env.ref('stock.view_picking_form', raise_if_not_found=False):
            for tag, name in STOCK_PICKING_EXTRAS:
                node = next((n for n in arch.iter(tag) if n.get('name') == name), None)
                if node is not None:   # the old view hid the first match only
                    node.set('invisible', '1')
        return arch, view
