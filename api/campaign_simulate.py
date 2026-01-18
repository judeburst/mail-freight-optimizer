from fastapi import APIRouter
from app.logic.drop_planner import plan_drop
from app.logic.shipment_summary import generate_shipment_summary

router = APIRouter()

@router.post("/simulate-campaign")
def simulate_campaign(campaign: dict):
    results = {}

    for drop in campaign["drops"]:
        pallets = plan_drop(drop["ddus"])
        results[f"Drop {drop['drop_number']}"] = {
            "pallets": pallets,
            "shipment_summary": generate_shipment_summary(pallets)
        }

    return results
