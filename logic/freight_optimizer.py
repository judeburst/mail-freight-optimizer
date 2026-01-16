CARRIER_PRIORITY = {
    "DDU": ["Old Dominion", "FedEx Freight"],
    "SCF": ["R+L", "XPO"]
}

def recommend_carriers(pallet_type):
    return CARRIER_PRIORITY.get(pallet_type, [])
