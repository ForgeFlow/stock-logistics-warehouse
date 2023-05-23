# Copyright 2023 ForgeFlow SL.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    """
    This post-init-hook will create a Reserve Area for each existing WH.
    """
    env = api.Environment(cr, SUPERUSER_ID, dict())
    warehouse_obj = env["stock.warehouse"]
    warehouses = warehouse_obj.search([])
    reserve_area_obj = env["stock.reserve.area"]
    for warehouse_id in warehouses.ids:
        warehouse = warehouse_obj.browse(warehouse_id)
        all_locations = env["stock.location"].search(
            [("id", "child_of", warehouse.view_location_id.id)]
        )
        reserve_area_obj.create(
            {
                "name": warehouse.name,
                "location_ids": [(6, 0, all_locations.ids)],
                "company_id": warehouse.company_id.id,
            }
        )
