# -*- coding: utf-8 -*-
{
    'name': "custom_sales_confirm_button",
    'summary': """ When confirm sales order the price in order line move to his product """,
    'description': """
        When user confirm a Sale Order, Product price is Updated as per the Price in the Sale Order Line
    """,
    'author': "Business Solutions",
    'website': "https://www.theBusinessSolutions.net",
    'category': 'Sales',
    'version': '13.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale'],
    # always loaded
    'data': [
        # 'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
