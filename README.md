# Mail & Freight Optimizer

Internal AI-assisted system for USPS multi-drop campaigns.

## Features
- DDU-first USPS logic
- SCF grouping for DDUs under 3000 households
- Per-drop palletization
- Flexible carrier selection
- Campaign-level simulation
- Copy-paste shipment summaries
- AI explanations (optional)

## Run
uvicorn app.main:app --reload
