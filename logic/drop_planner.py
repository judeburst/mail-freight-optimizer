from app.logic.usps_rules import assign_destination
from app.logic.pallet_dimensions import calculate_pallets
from app.logic.freight_optimizer import recommend_carriers


def plan_drop(ddus):
    """
    Plans palletization and freight options for a single drop.

    Rules enforced:
    - DDU is always first priority
    - DDUs with <3000 households are grouped and shipped to SCF
    - Palletization is done per drop
    - Any carrier can be used for any shipment
    """

    # Apply USPS DDU / SCF rules
    ddu_shipments, scf_group = assign_destination(ddus)

    # Combine all DDUs that need to be palletized for this drop
    all_destinations = []

    # DDU-level pallets
    for ddu in ddu_shipments:
        all_destinations.append(ddu)

    # SCF-level pallet (grouped DDUs)
    if scf_group:
        all_destinations.append(scf_group)

    # Calculate pallets (weight + dimensions)
    pallets = calculate_pallets(all_destinations)

    # Attach available carriers to every pallet
    available_carriers = recommend_carriers()
    for pallet in pallets:
        pallet["available_carriers"] = available_carriers

    return pallets
