from fastapi import FastAPI
from app.api.simulate import router as simulate_router
from app.api.campaign_simulate import router as campaign_router

app = FastAPI(title="Mail & Freight Optimizer")

app.include_router(simulate_router)
app.include_router(campaign_router)
