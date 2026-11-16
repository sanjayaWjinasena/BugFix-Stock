"""Move the scrap sequences past the scrap numbers already issued.

Up to 17.0.0.0.135, data/ir_sequence_data.xml (not noupdate) set number_next=1 on its three
stock.scrap sequences, so every module update set them back to SP/00001 and the next scrap orders
reused numbers already issued. The value is gone from the data file; this raises each of those
sequences above the highest SP/ number in use (scrap orders of the sequence's company, or of all
companies for a sequence without one). It is never lowered.
"""

import logging
import re

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)

SEQUENCES = ["seq_234_stock_scrap", "seq_560_stock_scrap", "seq_8_stock_scrap"]


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    for xmlid in SEQUENCES:
        seq = env.ref(f"BugFix-Stock.{xmlid}", raise_if_not_found=False)
        if not seq or seq.implementation != "standard" or seq.use_date_range:
            continue
        prefix, suffix = seq._get_prefix_suffix()
        domain = [("name", "=like", prefix.replace("%", r"\%").replace("_", r"\_") + "%")]
        if seq.company_id:
            domain.append(("company_id", "=", seq.company_id.id))
        pattern = re.compile(re.escape(prefix) + r"(\d+)" + re.escape(suffix or "") + "$")
        names = env["stock.scrap"].sudo().search(domain).mapped("name")
        used = [int(m.group(1)) for name in names if (m := pattern.match(name or ""))]
        if used and max(used) >= seq.number_next_actual:
            _logger.info(
                "[BugFix-Stock] %s: next number %s -> %s",
                xmlid,
                seq.number_next_actual,
                max(used) + 1,
            )
            seq.write({"number_next": max(used) + 1})
