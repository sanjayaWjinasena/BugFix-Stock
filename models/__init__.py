from . import stock_location
from . import stock_lot
from . import stock_move
from . import stock_move_line
from . import stock_picking
from . import stock_picking_type
from . import stock_valuation_layer
from . import con_consolidated_hea
from . import con_consolidated_lin
from . import consignment_charge_h
from . import consignment_charge_l
from . import consignment_header
from . import consignment_line
from . import journal_types
from . import mr_config
from . import material_request
from . import misc_charge_codes

# sales_report_type sentinel removed: Jinasena_Masterdata_Reporting
# now owns the model. Many2one refs on stock.move + stock.move.line
# resolve at load time via the new dep.
from . import tariffmaster
from . import temp_consignment_hea
from . import temp_consignment_lin
from . import material_request_mt
from . import material_request_tes
from . import temp_con_conso_line
from . import temp_con_consolidate
from . import temp_structure_detai
from . import temp_structure_maste
from . import material_request_mt_tag
from . import material_request_mt_stage
from . import material_request_tes_stage
from . import material_request_tes_tag

from . import product_product
from . import hide_dev_extras
