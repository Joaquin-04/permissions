{
    'name': 'custom_sales_permissions',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Control de accesos para el equipo de ventas',
    'depends': [
        'sale', 
        'sales_team',
        'stock'
    ],
    'data': [
        'security/groups.xml',  # Cargar el archivo XML
        'views/menus.xml',
        'views/sale_order_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}