{
    'name': 'Compare Client Price with Product Price',
    'version': '1.0',
    'category': 'Sales',
	'author': 'Business Solutions',
    'summary': 'check the client price in the PO if it matches with the offered pricein the sale quotation',
	'description': """
This module adds a new 'Client Price' in the sale order line to compare the price in the CLient PO with the original sale price
if there are a difference the quotation will not be confirmed
""",
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}