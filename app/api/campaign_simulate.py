from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Pydantic model for a campaign
class CampaignItem(BaseModel):
    campaign_name: str
    drops: List[dict]

# Endpoint for simulating a campaign
@router.post("/")
def simulate_campaign(campaigns: List[CampaignItem]):
    results = []
    for campaign in campaigns:
        results.append({
            "campaign_name": campaign.campaign_name,
            "drop_count": len(campaign.drops),
            "message": "Simulation completed successfully"
        })
    return {"campaigns": results}
