from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    client_price = fields.Float(string='Client Price')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for line in self.order_line:
            if line.client_price != line.price_unit:
                raise ValidationError('Client Price does not match Product Unit Price for product %s' % line.product_id.name)
        return super(SaleOrder, self).action_confirm()