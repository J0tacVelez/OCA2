# Copyright 2021 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
"""Test data models to get a mapping between carrier and delivery packaging.

Add a new "test" value for 'delivery_type' field of carrier and
'package_carrier_type' field of packaging for test purpose because
Shopfloor do not depend on 'delivery_*' modules adding the different
delivery types.
"""
from odoo import fields, models


class DeliveryCarrierTest(models.Model):
    _inherit = "delivery.carrier"

    delivery_type = fields.Selection(
        selection_add=[("test", "TEST")], ondelete={"test": "set default"}
    )
    test_default_packaging_id = fields.Many2one(
        "stock.package.type", string="Default Package Type"
    )


class StockPackageType(models.Model):
    _inherit = "stock.package.type"

    package_carrier_type = fields.Selection(
        selection_add=[("test", "TEST")], ondelete={"test": "set default"}
    )
