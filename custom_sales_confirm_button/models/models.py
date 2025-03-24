# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder,self).action_confirm()
        for rec in self:
            if rec.state == 'sale':
                for line in rec.order_line:
                    if line:
                        # line.product_id.lst_price = line.price_unit
                        line.product_id.product_tmpl_id.list_price = line.price_unit
        return res
