from odoo import api, fields, models, exceptions
class MyModule(models.Model):
   
    _inherit = 'mrp.workorder'

    @api.depends('reservation_state')
    def button_start(self):
        for workorder in self:
            if workorder.production_id.reservation_state != 'assigned':
                raise exceptions.UserError("Cannot start work order: production order is not in 'ready' state.")
            elif workorder.state != 'ready':
                raise exceptions.UserError("Cannot start work order: work order status is not 'Ready'.")
        # Return value outside of loop
        return super().button_start()