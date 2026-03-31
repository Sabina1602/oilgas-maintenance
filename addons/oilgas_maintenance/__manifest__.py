{
    'name': 'Oil and Gas Maintenance',
    'version': '18.0.1.0.0',
    'summary': 'Oil and Gas Maintenance',
    'author': 'Sabina',
    'category': 'Services',
    'license': 'LGPL-3',

    'depends' : ['mail', 'base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/equipment_views.xml',
        'views/maintenance_request_views.xml',
        'views/res_partner_views.xml',
        'views/menu.xml',
    ],

    'installable': True,
    'application': True,
}
