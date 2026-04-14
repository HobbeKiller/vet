# -*- coding: utf-8 -*-
{
    'name': 'Gestió veterinària',
    'summary': 'Gestiona els animals que visiten la teva clínica veterinària',
    'description': """
Gestió veterinària per a Odoo 18 Community.

Característiques:
- Fitxes d'animals
- Propietaris i mascotes vinculades
- Visites
- Medicaments, vacunes, al·lèrgies, cirurgies i assegurances
- Pressupostos i factures del propietari
""",
    'author': 'Anatoly Lutaev',
    'website': '',
    'license': '',
    'category': 'Services',
    'version': '18.0.1.0.0',
    'depends': ['base', 'mail', 'contacts', 'account', 'sale_management'],
    'data': [
        'security/groups.xml',          
        'security/ir.model.access.csv',
        'security/rules.xml',
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
