def palletize_ddus(ddu_list):
    pallets = []
    for ddu in ddu_list:
        pallets.append({
            "destination": ddu.ddu_code,
            "households": ddu.households,
            "type": "DDU"
        })
    return pallets


def palletize_scf_group(scf_ddus):
    total_households = sum(d.households for d in scf_ddus)

    return [{
        "destination": scf_ddus[0].scf_code if scf_ddus else None,
        "households": total_households,
        "type": "SCF",
        "included_ddus": [d.ddu_code for d in scf_ddus]
    }]
