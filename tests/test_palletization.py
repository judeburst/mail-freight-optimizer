from types import SimpleNamespace
from app.logic.pallet_dimensions import calculate_pallets

def test_calculate_pallets():
    ddu = SimpleNamespace(ddu_code="DDU1", scf_code="SCF1", households=5000)
    pallets = calculate_pallets([ddu])

    assert pallets[0]["weight_lbs"] == 750.0
