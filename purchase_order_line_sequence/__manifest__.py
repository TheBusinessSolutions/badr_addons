# Copyright 2017 Camptocamp SA - Damien Crier, Alexandre Fayolle
# Copyright 2017-23 ForgeFlow S.L.
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Purchase Order Line Sequence",
    "summary": "Adds sequence to PO lines and propagates it to"
    "Invoice lines and Stock Moves",
    "version": "13.0.1.1.1",
    "category": "Purchase Management",
    "author": "Camptocamp, "
    "ForgeFlow, "
    "Serpent CS, "
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "depends": ["purchase_stock", "stock_picking_line_sequence"],
    "data": [
        "views/purchase_view.xml",
        "views/report_purchaseorder.xml",
        "views/report_purchasequotation.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "auto_install": False,
    "license": "AGPL-3",
}
