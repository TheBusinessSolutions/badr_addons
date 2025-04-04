# Copyright 2019-21 ForgeFlow S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Purchase Manual Delivery",
    "summary": """
        Prevents pickings to be auto generated upon Purchase Order confirmation
        and adds the ability to manually generate them as the supplier confirms
        the different purchase order lines.
    """,
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "ForgeFlow S.L., Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "depends": ["purchase_stock"],
    "data": [
        "wizard/create_manual_stock_picking_views.xml",
        "views/purchase_order_views.xml",
        "views/res_config_view.xml",
    ],
}
