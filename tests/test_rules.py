import unittest
from app.logic.usps_rules import assign_destination
from types import SimpleNamespace

class TestDDU_SCFRules(unittest.TestCase):
    def test_ddu_scf_assignment(self):
        ddus = [
            SimpleNamespace(ddu_code="DDU1", scf_code="SCF1", households=4000),
            SimpleNamespace(ddu_code="DDU2", scf_code="SCF1", households=1500),
            SimpleNamespace(ddu_code="DDU3", scf_code="SCF1", households=2000),
        ]
        ddu_shipments, scf_group = assign_destination(ddus)
        self.assertEqual(len(ddu_shipments), 1)
        self.assertEqual(len(scf_group), 2)
