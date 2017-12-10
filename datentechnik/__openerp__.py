# -*- coding: utf-8 -*-
{
    'name': "BRUDER Datentechnik",
    'version': '0.0.1',
    'author': 'Erik Bruder',
    'category': 'Custom',
    'website': 'http://www.bruder-datentechnik.de',
    'description': '''Main Modul for BRUDER Datentechnik extension,
    Site structure''',
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
	'templates.xml',
	'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
