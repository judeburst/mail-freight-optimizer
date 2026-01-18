import unittest
from types import SimpleNamespace
from app.logic.pallet_dimensions import calculate_pallets

class TestPalletization(unittest.TestCase):
    def test_calculate_pallets(self):
        ddus = [SimpleNamespace(ddu_code="DDU1", scf_code="SCF1", households=5000)]
        pallets = calculate_pallets(ddus)
        self.assertEqual(len(pallets), 1)
        self.assertEqual(pallets[0]["weight_lbs"], 5000 * 0.15)
