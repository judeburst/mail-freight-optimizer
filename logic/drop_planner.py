from app.logic.usps_rules import assign_destination
from app.logic.pallet_dimensions import calculate_pallets
from app.logic.freight_optimizer import recommend_carriers


def plan_drop(ddus):
    """
    Full drop planning logic.
    """

    ddu_shipments, scf_group = assign_destination(ddus)

    destinations = []

    for ddu in ddu_shipments:
        destinations.append(ddu)

    if scf_group:
        destinations.append(scf_group)

    pallets = calculate_pallets(destinations)

    carriers = recommend_carriers()
    for pallet in pallets:
        pallet["available_carriers"] = carriers

    return pallets
