# Copyright 2023 ForgeFlow SL.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    @api.model
    def create(self, vals):
        warehouse = super().create(vals)
        self.env["stock.reserve.area"].sudo().create(
            {
                "name": warehouse.name,
                "location_ids": [(6, 0, [warehouse.view_location_id.id])],
            }
        )
        return warehouse
