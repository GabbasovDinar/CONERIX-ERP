# -*- coding: utf-8 -*-

from openerp import models, fields, api

class datentechnik(models.Model):
    _name = 'datentechnik.datentechnik'
    _description = 'Datentechnik'
    wireless     = fields.Char('Wireless', required=True)
    encryption   = fields.Char('Encryption', required=True)
    description  = fields.Char('Description')
