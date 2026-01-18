from app.logic.carriers import AVAILABLE_CARRIERS

def recommend_carriers():
    """
    Any carrier can be used for any shipment.
    No filtering or prioritization.
    """
    return AVAILABLE_CARRIERS
