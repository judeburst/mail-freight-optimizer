# Example assumptions:
# - each household = 0.15 lbs of mail
# - max pallet weight = 2000 lbs
# - standard pallet footprint: 48x40 inches

HOUSEHOLD_WEIGHT_LB = 0.15
MAX_PALLET_WEIGHT = 2000
PALLET_FOOTPRINT = (48, 40)  # inches

def calculate_pallets(ddus):
    """
    Returns list of pallets with weight, dimensions, and assigned DDUs
    """
    pallets = []
    for ddu in ddus:
        weight = ddu.households * HOUSEHOLD_WEIGHT_LB
        num_pallets = max(1, int((weight + MAX_PALLET_WEIGHT - 1) // MAX_PALLET_WEIGHT))  # ceil

        for i in range(num_pallets):
            pallets.append({
                "destination": getattr(ddu, "ddu_code", getattr(ddu, "scf_code", "UNKNOWN")),
                "weight_lbs": min(weight, MAX_PALLET_WEIGHT),
                "dimensions_in": PALLET_FOOTPRINT,
                "households": ddu.households,
                "included_ddus": [getattr(ddu, "ddu_code", "SCF")],
            })
    return pallets
