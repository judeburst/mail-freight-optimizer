DDU_MIN_HOUSEHOLDS = 3000

def assign_destination(ddus):
    """
    Applies your locked rule:
    - DDU always first priority
    - If DDU < 3000 households → SCF group
    """
    ddu_shipments = []
    scf_group = []

    for ddu in ddus:
        if ddu.households >= DDU_MIN_HOUSEHOLDS:
            ddu_shipments.append(ddu)
        else:
            scf_group.append(ddu)

    return ddu_shipments, scf_group
