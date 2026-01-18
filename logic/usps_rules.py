DDU_MIN_HOUSEHOLDS = 3000

def assign_destination(ddus):
    """
    Locked rules:
    - DDU is always first priority
    - DDUs under 3000 households are grouped to SCF
    """

    ddu_shipments = []
    scf_group = []

    for ddu in ddus:
        if ddu.households >= DDU_MIN_HOUSEHOLDS:
            ddu_shipments.append(ddu)
        else:
            scf_group.append(ddu)

    return ddu_shipments, scf_group
