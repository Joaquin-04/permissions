{
    'name': 'update_permissions',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Actualizando o removiendo permisos base del sistema, para asi tener un "lienzo ne blanco"',
    'depends': [
        'product',
        'stock'
    ],
    'data': [
        'security/only_read_access.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}