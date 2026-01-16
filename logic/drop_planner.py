from app.logic.usps_rules import assign_destination
from app.logic.palletization import palletize_ddus, palletize_scf_group
from app.logic.freight_optimizer import recommend_carriers

def plan_drop(ddus):
    ddu_shipments, scf_group = assign_destination(ddus)

    pallets = palletize_ddus(ddu_shipments)

    if scf_group:
        pallets.extend(palletize_scf_group(scf_group))

    carriers = recommend_carriers()

    for pallet in pallets:
        pallet["available_carriers"] = carriers

    return pallets
