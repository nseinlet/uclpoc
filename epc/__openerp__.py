# -*- coding: utf-8 -*-
{
    'name': "epc",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Your Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/res.groups.csv',
        'security/ir.model.access.csv',
        'views/entite.xml',
        'views/cahiercharge.xml',
        'views/activite.xml',
        'views/modifactivite.xml',
        'views/activiteinfo.xml',
        'views/menu.xml',
        'views/respartner.xml',
        'views/resusers.xml',
        'views/WS.xml',
        'reports/activiteinfo.xml',
    ],
}
