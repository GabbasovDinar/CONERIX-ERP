# -*- coding: utf-8 -*-
from openerp import http

# class PartnerWireless(http.Controller):
#     @http.route('/partner_wireless/partner_wireless/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_wireless/partner_wireless/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_wireless.listing', {
#             'root': '/partner_wireless/partner_wireless',
#             'objects': http.request.env['partner_wireless.partner_wireless'].search([]),
#         })

#     @http.route('/partner_wireless/partner_wireless/objects/<model("partner_wireless.partner_wireless"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_wireless.object', {
#             'object': obj
#         })