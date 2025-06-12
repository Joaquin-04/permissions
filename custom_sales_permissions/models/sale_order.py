from odoo import models, fields, api, exceptions

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    

    # Sobrescribir el método create para asignar el vendedor
    @api.model
    def create(self, vals):
        # Verificar si el usuario está en el grupo XML
        if self.env.user.has_group('custom_sales_permissions.grupo_vendedores_personalizados'):
            vals['user_id'] = self.env.user.id
        return super().create(vals)

    