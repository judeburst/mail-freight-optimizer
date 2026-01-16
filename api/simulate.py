from fastapi import APIRouter
from app.logic.drop_planner import plan_drop

router = APIRouter()

@router.post("/simulate-drop")
def simulate_drop(ddus: list):
    return plan_drop(ddus)
