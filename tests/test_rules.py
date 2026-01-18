from types import SimpleNamespace
from app.logic.usps_rules import assign_destination

def test_assign_destination():
    ddus = [
        SimpleNamespace(ddu_code="DDU1", scf_code="SCF1", households=4000),
        SimpleNamespace(ddu_code="DDU2", scf_code="SCF1", households=1500),
    ]

    ddu_shipments, scf_group = assign_destination(ddus)

    assert len(ddu_shipments) == 1
    assert len(scf_group) == 1
