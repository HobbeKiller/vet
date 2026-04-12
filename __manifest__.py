# -*- coding: utf-8 -*-
{
    'name': 'Veterinary management',
    'summary': 'Manage the animals that visit your veterinary clinic',
    'description': """
Veterinary management for Odoo 18 Community.

Features:
- Animal records
- Owners and linked pets
- Visits
- Medicines, vaccines, allergies, surgeries and insurances
- Quotes and invoices from the owner
""",
    'author': 'JD Solutions / Adapted for Odoo 18',
    'website': 'https://javierdiez.netlify.app/',
    'license': 'AGPL-3',
    'category': 'Services',
    'version': '18.0.1.0.0',
    'depends': ['base', 'mail', 'contacts', 'account', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/animals_views.xml',
        'views/medicines_views.xml',
        'views/allergies_views.xml',
        'views/surgeries_views.xml',
        'views/vaccines_views.xml',
        'views/insurances_views.xml',
        'views/visits_views.xml',
        'views/species_views.xml',
        'views/breeds_views.xml',
        'views/tags_views.xml',
        'views/animal_partner_views.xml',
        'views/animals_menus.xml',
        'views/visit_sequence.xml',
        'views/animals_identification.xml',
    ],
    'images': ['static/images/banner.png', 'static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
