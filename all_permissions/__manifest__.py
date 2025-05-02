{
    'name': 'all_permissions',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'Control de accesos para módulos generales',
    'depends': [
        'purchase',
        'purchase_requisition'
    ],
    'data': [
        'security/all_users.xml',
        'views/menus.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}