# Mail & Freight Optimizer

Internal AI-assisted system for USPS multi-drop campaigns and palletized freight planning.

## Features
- Multi-drop campaigns per sale
- DDU first, SCF grouping for small DDUs (<3000 households)
- Palletization with weight/dimensions
- Flexible carrier recommendations (any carrier for any drop)
- Copy-paste shipment summaries
- AI-assisted explanation (optional GPT layer)

## Installation
```bash
git clone <repo>
cd mail-freight-optimizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
