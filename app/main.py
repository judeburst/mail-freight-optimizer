from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import simulate, campaign_simulate

# Create FastAPI app
app = FastAPI(
    title="Mail & Freight Optimizer",
    description="Optimizes USPS drop planning and freight palletization",
    version="1.0.0"
)

# Add CORS middleware (optional, useful if connecting to a frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from api folder
app.include_router(simulate.router, prefix="/simulate-drop", tags=["Simulate Drop"])
app.include_router(campaign_simulate.router, prefix="/simulate-campaign", tags=["Simulate Campaign"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Mail & Freight Optimizer API is running!"}
