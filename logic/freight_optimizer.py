from app.logic.carriers import AVAILABLE_CARRIERS

def recommend_carriers():
    """
    Returns all supported carriers.
    No filtering by DDU / SCF / drop timing.
    Final carrier choice is made by the user.
    """
    return AVAILABLE_CARRIERS
