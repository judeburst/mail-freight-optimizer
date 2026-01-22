from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
from types import SimpleNamespace

from app.logic.drop_planner import plan_drop
from app.logic.shipment_summary import generate_shipment_summary
from app.ai.assistant import explain_campaign

router = APIRouter()

# Pydantic models
class DropData(BaseModel):
    ddu_code: str
    scf_code: str
    households: int = Field(..., ge=0)

class CampaignItem(BaseModel):
    campaign_name: str = Field(..., min_length=1)
    drops: List[DropData]
    explain: bool = Field(False, description="Include AI explanation")

class CampaignRequest(BaseModel):
    campaigns: List[CampaignItem]

# Endpoint for simulating multiple campaigns
@router.post("/")
def simulate_campaign(request: CampaignRequest):
    """
    Simulate one or more mail campaigns with multiple drops.
    
    - Each campaign can have multiple drops (mailings)
    - Applies USPS routing optimization to each drop
    - Calculates total costs and logistics across all drops
    - Optionally generates AI explanation per campaign
    """
    try:
        if not request.campaigns:
            raise HTTPException(status_code=400, detail="At least one campaign is required")
        
        results = []
        
        for campaign in request.campaigns:
            if not campaign.drops:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Campaign '{campaign.campaign_name}' has no drops"
                )
            
            # Convert drops to SimpleNamespace
            ddus = [SimpleNamespace(
                ddu_code=d.ddu_code,
                scf_code=d.scf_code,
                households=d.households
            ) for d in campaign.drops]
            
            # Run planning logic
            pallets = plan_drop(ddus)
            summary = generate_shipment_summary(pallets)
            
            # Calculate campaign totals
            total_weight = sum(p["weight_lbs"] for p in pallets)
            total_households = sum(p["households"] for p in pallets)
            ddu_count = sum(1 for p in pallets if p["type"] == "DDU")
            scf_count = sum(1 for p in pallets if p["type"] == "SCF")
            
            campaign_result = {
                "campaign_name": campaign.campaign_name,
                "drop_count": len(campaign.drops),
                "total_pallets": len(pallets),
                "total_weight_lbs": round(total_weight, 2),
                "total_households": total_households,
                "shipment_breakdown": {
                    "ddu_shipments": ddu_count,
                    "scf_shipments": scf_count
                },
                "pallets": pallets,
                "summary": summary
            }
            
            # Add AI explanation if requested
            if campaign.explain:
                try:
                    campaign_result["ai_explanation"] = explain_campaign(summary)
                except Exception as e:
                    campaign_result["ai_explanation"] = f"AI explanation unavailable: {str(e)}"
            
            results.append(campaign_result)
        
        return {
            "campaigns": results,
            "total_campaigns": len(results)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Campaign simulation failed: {str(e)}")
