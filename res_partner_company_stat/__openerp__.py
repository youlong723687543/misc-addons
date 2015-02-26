{
    'name' : 'Fix stat buttons for companies',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Sale',
    'website' : 'https://yelizariev.github.io',
    'description': """
Collects statistic information from all company's contacts.

Tested on Odoo 8.0 ab7b5d7732a7c222a0aea45bd173742acd47242d

Further information and discussion: https://yelizariev.github.io/odoo/module/2015/02/26/company-contacts.html
    """,
    'depends' : ['crm', 'sale', 'account', 'project'],
    'data':[
        'views.xml',
        ],
    'installable': True
}
