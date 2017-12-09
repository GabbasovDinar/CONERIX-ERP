# -*- encoding: utf-8 -*-
from openerp import http
from openerp.addons.website_sale.controllers.main import website_sale
from openerp.addons.web import http
from openerp.http import request
from openerp import models, fields, api

import openerp.addons.website_sale.controllers.main

class WebsiteSale(website_sale):
    @http.route(
        ['/shop',
         '/shop/page/<int:page>',
         '/shop/category/<model("product.public.category"):category>',
         '/shop/category/<model("product.public.category"):category>/'
         'page/<int:page>'],
        type='http', auth="public", website=True)
    
    def shop(self, page=0, category=None, search='', **post):
        parent_category_ids = []
        if category:
            parent_category_ids = [category.id]
            current_category = category
            while current_category.parent_id:
                parent_category_ids.append(current_category.parent_id.id)
                current_category = current_category.parent_id
        response = super(WebsiteSale, self).shop(
            page=page, category=category, search=search, **post)
        response.qcontext['parent_category_ids'] = parent_category_ids
        return response

class website_config_settings(models.TransientModel):

    _inherit = 'website.config.settings'

    @api.one
    def action_copy_shop_images(self):
        self.env['product.template'].search([]).action_copy_image_to_images()


class product_image(models.Model):
    _name = 'product.image'
    _order = 'sequence, id DESC'

    name = fields.Char('Name')
    description = fields.Text('Description')
    sequence = fields.Integer('Sequence')
    image_alt = fields.Text('Image Label')
    image = fields.Binary('Image')
    image_small = fields.Binary('Small Image')
    product_tmpl_id = fields.Many2one('product.template', 'Product', select=True)
    from_main_image = fields.Boolean('From Main Image', default=False)


class product_product(models.Model):
    _inherit = 'product.product'

    images = fields.One2many('product.image', related='product_tmpl_id.images',
                             string='Images', store=False)


class product_template(models.Model):
    _inherit = 'product.template'

    images = fields.One2many('product.image', 'product_tmpl_id',
                             string='Images')

    @api.one
    def action_copy_image_to_images(self):
        if not self.image:
            return
        image = None
        for r in self.images:
            if r.from_main_image:
                image = r
                break

        if image:
            image.image = self.image
        else:
            vals = {'image': self.image,
                    'name': self.name,
                    'product_tmpl_id': self.id,
                    'from_main_image': True, }
            self.env['product.image'].create(vals)





class cart_WebsiteSale(openerp.addons.website_sale.controllers.main.website_sale):

    @http.route(['/shop/cart'], type='http', auth="public", website=True)
    def cart(self, **post):
        res = super(WebsiteSale, self).cart(**post)
        if post.get('type') == 'popover':
            # two qweb responses will be rendered in this case, the one by
            # super and this one, but there is no way around it if
            # we don't want to break inheritance
            return request.website.render(
                "Ornate_Plus.cart_popover", res.qcontext)
        return res
