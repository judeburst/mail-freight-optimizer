import math

HOUSEHOLD_WEIGHT_LB = 0.15
MAX_PALLET_WEIGHT = 2000
PALLET_DIMENSIONS_IN = (48, 40)


def calculate_pallets(destinations):
    """
    Handles:
    - Individual DDU shipments
    - Grouped SCF shipments (list of DDUs)
    - Splits overweight shipments into multiple pallets
    """

    pallets = []

    for dest in destinations:

        # SCF GROUP
        if isinstance(dest, list):
            total_households = sum(d.households for d in dest)
            total_weight = total_households * HOUSEHOLD_WEIGHT_LB

            # Check if we need to split into multiple pallets
            if total_weight > MAX_PALLET_WEIGHT:
                num_pallets = math.ceil(total_weight / MAX_PALLET_WEIGHT)
                households_per_pallet = math.ceil(total_households / num_pallets)
                
                # Create multiple pallets
                remaining_households = total_households
                pallet_num = 1
                
                for i in range(num_pallets):
                    pallet_households = min(households_per_pallet, remaining_households)
                    weight = pallet_households * HOUSEHOLD_WEIGHT_LB
                    
                    pallets.append({
                        "destination": f"{dest[0].scf_code} (Part {pallet_num}/{num_pallets})",
                        "type": "SCF",
                        "weight_lbs": round(weight, 2),
                        "dimensions_in": PALLET_DIMENSIONS_IN,
                        "households": pallet_households,
                        "included_ddus": [d.ddu_code for d in dest],
                        "pallet_number": pallet_num,
                        "total_pallets": num_pallets
                    })
                    
                    remaining_households -= pallet_households
                    pallet_num += 1
            else:
                # Single pallet for SCF group
                pallets.append({
                    "destination": dest[0].scf_code,
                    "type": "SCF",
                    "weight_lbs": round(total_weight, 2),
                    "dimensions_in": PALLET_DIMENSIONS_IN,
                    "households": total_households,
                    "included_ddus": [d.ddu_code for d in dest]
                })

        # SINGLE DDU
        else:
            total_weight = dest.households * HOUSEHOLD_WEIGHT_LB
            
            # Check if single DDU needs multiple pallets
            if total_weight > MAX_PALLET_WEIGHT:
                num_pallets = math.ceil(total_weight / MAX_PALLET_WEIGHT)
                households_per_pallet = math.ceil(dest.households / num_pallets)
                
                remaining_households = dest.households
                pallet_num = 1
                
                for i in range(num_pallets):
                    pallet_households = min(households_per_pallet, remaining_households)
                    weight = pallet_households * HOUSEHOLD_WEIGHT_LB
                    
                    pallets.append({
                        "destination": f"{dest.ddu_code} (Part {pallet_num}/{num_pallets})",
                        "type": "DDU",
                        "weight_lbs": round(weight, 2),
                        "dimensions_in": PALLET_DIMENSIONS_IN,
                        "households": pallet_households,
                        "included_ddus": [dest.ddu_code],
                        "pallet_number": pallet_num,
                        "total_pallets": num_pallets
                    })
                    
                    remaining_households -= pallet_households
                    pallet_num += 1
            else:
                # Single pallet for DDU
                pallets.append({
                    "destination": dest.ddu_code,
                    "type": "DDU",
                    "weight_lbs": round(total_weight, 2),
                    "dimensions_in": PALLET_DIMENSIONS_IN,
                    "households": dest.households,
                    "included_ddus": [dest.ddu_code]
                })

    return pallets
