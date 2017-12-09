# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from openerp import tools
from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import openerp.addons.decimal_precision as dp
import time


class res_partner(osv.osv):
    _inherit = "res.partner"
    _columns = {
        'facebook_url': fields.char('Facebook'),
        'twitter_url': fields.char('Twitter'),
        'youtube_url': fields.char('Youtube'),
        'instagram_url': fields.char('instagram'),
        'googleplus_url': fields.char('Google+'),
    }

    _defaults = {
    }





