# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Website Customer Social Network",
    "version" : "1.0",
    "author": "BrowseInfo",
    "description": """
        This Module add social networks detail on Partner and shows them on website
    """,
    "website" : "www.browseinfo.in",
    'summary': 'Website Customer/Partner Social Network',
    "depends" : ['base','sale','crm_partner_assign','website','website_crm_partner_assign','website_partner'],
    "data" :[
			'partner_social_network.xml',
            'views/template.xml',
    ],
    'qweb':[
    ],
    "auto_install": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
