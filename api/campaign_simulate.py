from fastapi import APIRouter
from app.logic.drop_planner import plan_drop
from app.logic.shipment_summary import generate_shipment_summary

router = APIRouter()

@router.post("/simulate-campaign")
def simulate_campaign(campaign: dict):
    """
    Input example:
    {
        "campaign_name": "Dealer XYZ Sale",
        "drops": [
            {"drop_number": 1, "ddus": [ ... ]},
            {"drop_number": 2, "ddus": [ ... ]}
        ]
    }
    """
    results = {}
    for drop in campaign["drops"]:
        pallets = plan_drop(drop["ddus"])
        summary = generate_shipment_summary(pallets)
        results[f"Drop {drop['drop_number']}"] = summary
    return results
