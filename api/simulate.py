from fastapi import APIRouter
from app.logic.drop_planner import plan_drop
from app.logic.shipment_summary import generate_shipment_summary

router = APIRouter()

@router.post("/simulate-drop")
def simulate_drop(ddus: list):
    pallets = plan_drop(ddus)
    summary = generate_shipment_summary(pallets)
    return {
        "pallets": pallets,
        "shipment_summary": summary
    }
