from openerp import api, fields, models
from urlparse import urlparse
import openerp



class ornate_ecommerce_product(models.Model):
    _inherit = 'product.template'
    is_recommended_product = fields.Boolean('Recommended')
   


class ornate_website(models.Model):
    _inherit = 'website'
    


    def get_recommended_length(self):
        r_length = []
        r_items_is = []
        count = 1
        
        recommended_products_ids = self.env['product.template'].search([('is_recommended_product', '=', True)])
        for record in recommended_products_ids:
            con = count % 3
            r_length.append(record)
            if con == 0:
                r_items_is.append(r_length)
                r_length = []

            count = count + 1

        return r_items_is