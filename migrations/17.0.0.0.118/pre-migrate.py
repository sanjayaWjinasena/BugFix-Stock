# -*- coding: utf-8 -*-
"""v0.0.118: hand the sticky-`_unknown` Many2one(s) below over to BugFix-Purchase v0.1.0.178.

Part of the 2026-10-02 ownership move: a Python Many2one whose comodel is owned
by a module that loads LATER is rewritten to comodel '_unknown' by Odoo 17 at
this module's setup pass and never recovers for the rest of an upgrade-mode
registry build (Jinasena_All cascade crashed on a MasterData CSV with
`relation "_unknown" does not exist`). The only load-order-proof fix is a
single declaration in the comodel-owning module, so the field declarations
left this module and now live in BugFix-Purchase v0.1.0.178.

This pre-migrate does two ORM-only things (no cr.execute):

1. Detaches this module's ir.model.data pointers for the moved fields.
   Otherwise ir.model.data._process_end would see xmlids that were not
   re-loaded and, if no other xmlid pointed at the same ir.model.fields row,
   UNLINK the field and DROP its column (live data). With the pointer gone
   the field row is never a cleanup candidate; BugFix-Purchase v0.1.0.178 re-attaches its own
   xmlids on reflection.

2. Unlinks the extension views of this module whose arch referenced the moved
   fields. Odoo rewrites a parent view first and validates the combined arch
   with the children AS STORED IN THE DB (old arch, field still referenced)
   -> "Field X does not exist in model Y". A dangling xmlid makes
   _load_records recreate the view from the new file arch (same xmlid, new
   id). None of these views has inheriting children (RPC-verified).

Idempotent: no-op on fresh installs (version is None) and when rows are gone.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

MODULE = 'BugFix-Stock'
MOVED_FIELDS = (
    ('x_consignment_charge_h', 'x_studio_structure_details_line_ids'),
    ('x_consignment_charge_h', 'x_studio_structure_master_id'),
    ('x_consignment_charge_l', 'x_studio_structure_details_line_ids'),
    ('x_consignment_charge_l', 'x_studio_structure_master_id'),
    ('x_consignment_header', 'x_studio_delivery_term'),
    ('x_consignment_header', 'x_studio_structure_name'),
    ('x_consignment_line', 'x_studio_payment_method'),
    ('x_consignment_line', 'x_studio_structure_name'),
    ('x_con_consolidated_lin', 'x_studio_delivery_term'),
    ('x_temp_consignment_lin', 'x_studio_payment_method'),
    ('x_temp_consignment_lin', 'x_studio_structure_name'),
    ('x_temp_con_conso_line', 'x_studio_delivery_term'),
    ('x_temp_structure_detai', 'x_studio_structure_details_line_ids'),
    ('x_temp_structure_maste', 'x_studio_temp_structure_details_id'),
)
STALE_VIEWS = (
    'BugFix-Stock.ported_view_2816_studio_form_x_consignment_header',
    'BugFix-Stock.ported_view_3073_odoo_studio_default_form_view_for_x_con_',
    'BugFix-Stock.ported_view_3074_odoo_studio_default_form_view_for_x_con_',
    'BugFix-Stock.ported_view_2941_odoo_studio_default_form_view_for_x_cons',
    'BugFix-Stock.ported_view_3018_odoo_studio_imp_copy_po_line_to_consignm',
)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    Fields = env['ir.model.fields'].sudo()
    IMD = env['ir.model.data'].sudo()

    field_ids = []
    for model, name in MOVED_FIELDS:
        field_ids += Fields.search([('model', '=', model), ('name', '=', name)]).ids
    if field_ids:
        imd = IMD.search([
            ('module', '=', MODULE),
            ('model', '=', 'ir.model.fields'),
            ('res_id', 'in', field_ids),
        ])
        if imd:
            names = imd.mapped('name')
            imd.unlink()
            _logger.info("%s v0.0.118: detached %d ir.model.data pointer(s) for moved "
                         "fields: %s", MODULE, len(names), names)

    View = env['ir.ui.view'].sudo().with_context(active_test=False)
    for xmlid in STALE_VIEWS:
        view = env.ref(xmlid, raise_if_not_found=False)
        if not view:
            continue
        view = View.browse(view.id)
        _logger.info("%s v0.0.118: unlinking stale extension view %s (id=%s, model=%s) "
                     "for recreation from the new file arch", MODULE, xmlid, view.id, view.model)
        view.unlink()
