# Copyright 2023 ooops404
# Copyright 2023 Simone Rubino - Aion Tech
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale Commission Product Criteria Domain",
    "version": "16.0.1.0.2",
    "author": "Ilyas," "Ooops404," "Odoo Community Association (OCA)",
    "contributors": ["Ilyas"],
    "maintainers": ["ilyasProgrammer"],
    "website": "https://github.com/OCA/commission",
    "category": "Sales Management",
    "license": "AGPL-3",
    "depends": [
        "sale_commission_product_criteria",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "data": [
        "views/views.xml",
        "security/ir.model.access.csv",
    ],
    "application": False,
    "installable": True,
    "auto_install": False,
}
