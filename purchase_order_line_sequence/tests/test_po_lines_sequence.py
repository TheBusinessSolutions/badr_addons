# Copyright 2017 Camptocamp SA - Damien Crier, Alexandre Fayolle
# Copyright 2017-23 ForgeFlow S.L
# Copyright 2017 Serpent Consulting Services Pvt. Ltd.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from datetime import datetime

from odoo.tests import common
from odoo.tests.common import Form
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class TestPurchaseOrder(common.TransactionCase):
    def setUp(self):
        super(TestPurchaseOrder, self).setUp()
        # Useful models
        self.PurchaseOrder = self.env["purchase.order"]
        self.PurchaseOrderLine = self.env["purchase.order.line"]
        self.partner_id = self.env.ref("base.res_partner_1")
        self.product_id_1 = self.env.ref("product.product_product_8")
        self.product_id_2 = self.env.ref("product.product_product_11")

        self.AccountInvoice = self.env["account.move"]
        self.AccountInvoiceLine = self.env["account.move.line"]

        self.category = self.env.ref("product.product_category_1").copy(
            {
                "name": "Test category",
                "property_valuation": "real_time",
                "property_cost_method": "fifo",
            }
        )

        account_type = self.env["account.account.type"].create(
            {"name": "RCV type", "type": "other", "internal_group": "expense"}
        )
        self.account_expense = self.env["account.account"].create(
            {
                "name": "Expense",
                "code": "EXP00",
                "user_type_id": account_type.id,
                "reconcile": True,
            }
        )
        self.account_payable = self.env["account.account"].create(
            {
                "name": "Payable",
                "code": "PAY00",
                "user_type_id": account_type.id,
                "reconcile": True,
            }
        )

        self.category.property_account_expense_categ_id = self.account_expense

        self.category.property_stock_journal = self.env["account.journal"].create(
            {"name": "Stock journal", "type": "sale", "code": "STK00"}
        )
        self.product_id_1.categ_id = self.category
        self.product_id_2.categ_id = self.category
        self.partner_id.property_account_payable_id = self.account_payable

    def _create_purchase_order(self):
        po_vals = {
            "partner_id": self.partner_id.id,
            "order_line": [
                (
                    0,
                    0,
                    {
                        "name": self.product_id_1.name,
                        "product_id": self.product_id_1.id,
                        "product_qty": 5.0,
                        "product_uom": self.product_id_1.uom_po_id.id,
                        "price_unit": 500.0,
                        "date_planned": datetime.today().strftime(
                            DEFAULT_SERVER_DATETIME_FORMAT
                        ),
                    },
                ),
                (
                    0,
                    0,
                    {
                        "name": self.product_id_2.name,
                        "product_id": self.product_id_2.id,
                        "product_qty": 5.0,
                        "product_uom": self.product_id_2.uom_po_id.id,
                        "price_unit": 250.0,
                        "date_planned": datetime.today().strftime(
                            DEFAULT_SERVER_DATETIME_FORMAT
                        ),
                    },
                ),
            ],
        }

        return self.PurchaseOrder.create(po_vals)

    def test_purchase_order_line_sequence(self):

        self.po = self._create_purchase_order()
        self.po.button_confirm()

        move1 = self.env["stock.move"].search(
            [("purchase_line_id", "=", self.po.order_line[0].id)]
        )
        move2 = self.env["stock.move"].search(
            [("purchase_line_id", "=", self.po.order_line[1].id)]
        )

        self.assertEqual(
            self.po.order_line[0].sequence,
            move1.sequence,
            "The Sequence of the Purchase Order Lines does not "
            "match to the Stock Moves",
        )
        self.assertEqual(
            self.po.order_line[1].sequence,
            move2.sequence,
            "The Sequence of the Purchase Order Lines does not "
            "match to the Stock Moves",
        )

        self.po2 = self.po.copy()
        self.assertEqual(
            self.po.order_line[0].sequence,
            self.po2.order_line[0].sequence,
            "The Sequence is not copied properly",
        )
        self.assertEqual(
            self.po.order_line[1].sequence,
            self.po2.order_line[1].sequence,
            "The Sequence is not copied properly",
        )

    def test_purchase_order_line_sequence_with_section_note(self):
        """
            Verify that the sequence is correctly assigned to the move associated
            with the purchase order line it references.
        """
        po = self._create_purchase_order()
        self.PurchaseOrderLine.create(
            {
                "name": "Section 1",
                "display_type": "line_section",
                "order_id": po.id,
                "product_qty": 0,
            }
        )
        self.PurchaseOrderLine.create(
            {
                "name": self.product_id_1.name,
                "product_id": self.product_id_1.id,
                "product_qty": 15.0,
                "product_uom": self.product_id_1.uom_po_id.id,
                "price_unit": 150.0,
                "date_planned": datetime.today().strftime(
                    DEFAULT_SERVER_DATETIME_FORMAT
                ),
                "order_id": po.id,
            }
        )
        self.PurchaseOrderLine.create(
            {
                "name": "Note 1",
                "display_type": "line_note",
                "order_id": po.id,
                "product_qty": 0,
            }
        )
        self.PurchaseOrderLine.create(
            {
                "name": self.product_id_2.name,
                "product_id": self.product_id_2.id,
                "product_qty": 1.0,
                "product_uom": self.product_id_2.uom_po_id.id,
                "price_unit": 50.0,
                "date_planned": datetime.today().strftime(
                    DEFAULT_SERVER_DATETIME_FORMAT
                ),
                "order_id": po.id,
            }
        )
        po.button_confirm()

        moves = po.picking_ids[0].move_ids_without_package
        self.assertNotEquals(len(po.order_line), len(moves))

        for move in moves:
            self.assertEqual(move.sequence, move.purchase_line_id.sequence)

    def test_write_purchase_order_line(self):
        po = self._create_purchase_order()
        po.button_confirm()

        po.write(
            {
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product_id_2.name,
                            "product_id": self.product_id_2.id,
                            "product_qty": 2,
                            "product_uom": self.product_id_2.uom_id.id,
                            "price_unit": 30,
                            "date_planned": datetime.today().strftime(
                                DEFAULT_SERVER_DATETIME_FORMAT
                            ),
                        },
                    )
                ]
            }
        )

        moves = po.picking_ids[0].move_ids_without_package
        for move in moves:
            self.assertEqual(move.sequence, move.purchase_line_id.sequence)

    def test_invoice_sequence(self):

        po = self._create_purchase_order()
        po.button_confirm()
        po.order_line.qty_received = 5
        result = po.action_view_invoice()
        self.invoice = Form(
            self.env["account.move"].with_context(result["context"])
        ).save()
        self.assertEqual(
            po.order_line[0].sequence,
            self.invoice.invoice_line_ids[0].sequence,
            "The Sequence is not copied properly",
        )
        self.assertEqual(
            po.order_line[1].sequence,
            self.invoice.invoice_line_ids[1].sequence,
            "The Sequence is not copied properly",
        )
