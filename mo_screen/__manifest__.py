# -*- coding: utf-8 -*-
{
    'name': "Size of Pieces",

    'summary': """
        Adds the Size of Pieces field in the Produce & Transfer Screens""",

    'description': """
        Adds the Size of Pieces field in the Produce & Transfer Screens
    """,

    'author': "Egymentors",
    'website': "http://www.egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'mrp', 'sale_management', 'stock', 'stock_picking_batch', 'sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_view_changes.xml',
        'views/manufacturing_order_screen.xml',
        
        'wizard/mrp_product_produce_view_changes.xml',
    ],

}
