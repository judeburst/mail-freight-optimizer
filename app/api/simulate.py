from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from types import SimpleNamespace

from app.logic.drop_planner import plan_drop
from app.logic.shipment_summary import generate_shipment_summary
from app.ai.assistant import explain_campaign

router = APIRouter()

# Pydantic model for a single drop
class DropItem(BaseModel):
    ddu_code: str = Field(..., min_length=1, description="DDU code identifier")
    scf_code: str = Field(..., min_length=1, description="SCF code identifier")
    households: int = Field(..., ge=0, description="Number of households (must be non-negative)")

# Request model with optional AI explanation
class SimulateDropRequest(BaseModel):
    drops: List[DropItem]
    explain: bool = Field(False, description="Include AI-generated explanation")

# Endpoint for simulating a drop
@router.post("/")
def simulate_drop(request: SimulateDropRequest):
    """
    Simulate a mail drop with USPS routing optimization.
    
    - Applies DDU-first logic (3000+ households go direct to DDU)
    - Groups smaller DDUs to SCF facilities
    - Calculates palletization and weights
    - Recommends freight carriers
    - Optionally generates AI explanation
    """
    try:
        # Validate input
        if not request.drops:
            raise HTTPException(status_code=400, detail="At least one drop is required")
        
        # Convert Pydantic models to SimpleNamespace for logic layer
        ddus = [SimpleNamespace(
            ddu_code=d.ddu_code,
            scf_code=d.scf_code,
            households=d.households
        ) for d in request.drops]
        
        # Run planning logic
        pallets = plan_drop(ddus)
        
        # Generate summary
        summary = generate_shipment_summary(pallets)
        
        # Build response
        response = {
            "pallets": pallets,
            "summary": summary,
            "total_pallets": len(pallets),
            "total_households": sum(p["households"] for p in pallets)
        }
        
        # Add AI explanation if requested
        if request.explain:
            try:
                response["ai_explanation"] = explain_campaign(summary)
            except Exception as e:
                response["ai_explanation"] = f"AI explanation unavailable: {str(e)}"
        
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Simulation failed: {str(e)}")
