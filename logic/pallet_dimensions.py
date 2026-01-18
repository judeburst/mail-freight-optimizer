HOUSEHOLD_WEIGHT_LB = 0.15
MAX_PALLET_WEIGHT = 2000
PALLET_DIMENSIONS_IN = (48, 40)


def calculate_pallets(destinations):
    """
    Handles:
    - Individual DDU shipments
    - Grouped SCF shipments (list of DDUs)
    """

    pallets = []

    for dest in destinations:

        # SCF GROUP
        if isinstance(dest, list):
            total_households = sum(d.households for d in dest)
            weight = total_households * HOUSEHOLD_WEIGHT_LB

            pallets.append({
                "destination": dest[0].scf_code,
                "type": "SCF",
                "weight_lbs": round(weight, 2),
                "dimensions_in": PALLET_DIMENSIONS_IN,
                "households": total_households,
                "included_ddus": [d.ddu_code for d in dest]
            })

        # SINGLE DDU
        else:
            weight = dest.households * HOUSEHOLD_WEIGHT_LB

            pallets.append({
                "destination": dest.ddu_code,
                "type": "DDU",
                "weight_lbs": round(weight, 2),
                "dimensions_in": PALLET_DIMENSIONS_IN,
                "households": dest.households,
                "included_ddus": [dest.ddu_code]
            })

    return pallets
