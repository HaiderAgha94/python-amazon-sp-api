from setuptools import setup

setup(
    name='python-amazon-sp-api',
    version='0.5.2',
    install_requires=[
        "requests",
        "six~=1.15.0",
        "boto3~=1.16.39",
        "cachetools~=4.2.0",
        "pycryptodome",
        "pytz",
        "confuse~=1.4.0",
    ],
    packages=['tests', 'tests.api', 'tests.api.orders', 'tests.api.sellers', 'tests.api.finances',
              'tests.api.product_fees', 'tests.api.notifications', 'tests.api.reports', 'tests.client',
              'sp_api',
              'sp_api.api',
              'sp_api.api.orders',
              'sp_api.api.sellers',
              'sp_api.api.finances',
              'sp_api.api.product_fees',
              'sp_api.api.products',
              'sp_api.api.feeds',
              'sp_api.api.sales',
              'sp_api.api.catalog',
              'sp_api.api.notifications',
              'sp_api.api.reports',
              'sp_api.api.inventories',
              'sp_api.api.messaging',
              'sp_api.api.upload',
              'sp_api.api.merchant_fulfillment',
              'sp_api.api.fulfillment_inbound',
              'sp_api.auth',
              'sp_api.base',
                ##### DO NOT DELETE ########## INSERT PACKAGE HERE #######
              'sp_api.api.catalog_items',
    
              'sp_api.api.product_type_definitions',
    
              'sp_api.api.listings_items',
    
              'sp_api.api.vendor_transaction_status',
    
              'sp_api.api.vendor_shipments',
    
              'sp_api.api.vendor_orders',
    
              'sp_api.api.vendor_invoices',
    
              'sp_api.api.vendor_direct_fulfillment_transactions',
    
              'sp_api.api.vendor_direct_fulfillment_shipping',
    
              'sp_api.api.vendor_direct_fulfillment_payments',
    
              'sp_api.api.vendor_direct_fulfillment_orders',
    
              'sp_api.api.vendor_direct_fulfillment_inventory',
    
              'sp_api.api.tokens',
    
              'sp_api.api.solicitations',
    
              'sp_api.api.shipping',
    
              'sp_api.api.services',
    
              'sp_api.api.fba_small_and_light',
    
              'sp_api.api.fba_inbound_eligibility',
    
              'sp_api.api.authorization',
    
              'sp_api.api.aplus_content',
    
              'sp_api.api.fulfillment_outbound',
    

              ],
    url='https://github.com/saleweaver/python-amazon-sp-api',
    license='MIT',
    author='Michael',
    author_email='info@saleweaver.com',
    description='Python wrapper for the Amazon Selling-Partner API'
)
