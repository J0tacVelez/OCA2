# 2016 Akretion (http://www.akretion.com)
# David BEAL <david.beal@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "MRP Workcenter Hierarchical",
    "version": "16.0.1.0.0",
    "author": "Akretion,Odoo Community Association (OCA)",
    "summary": "Organise Workcenters by section",
    "category": "Manufacturing",
    "maintainers": ["florian-dacosta"],
    "depends": [
        "mrp",
    ],
    "website": "https://github.com/OCA/manufacture",
    "data": [
        "security/ir.model.access.csv",
        "views/workcenter_view.xml",
        "wizards/switch_workcenter.xml",
        "wizards/res_config_settings_views.xml",
    ],
    "demo": [
        "data/mrp_demo.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
}
