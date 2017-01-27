# -*- coding: utf-8 -*-
{
    'name': "partner_wireless",

    'summary': """
        Wireless network credentials from partner
        SSID, KEY, ROUTER, ROUTERPASSWORD""",

    'description': """
        Safe the wireless networks of your partners
    """,

    'author': "BRUDER Datentechnik",
    'website': "http://www.bruder-datentechnik.de",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'partner_wireless.xml',
    ],
    'qweb':[
    ],
    "auto_install": false
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: