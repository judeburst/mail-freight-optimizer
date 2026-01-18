def generate_shipment_summary(pallets):
    summary = []
    for idx, p in enumerate(pallets, start=1):
        summary.append(
            f"Shipment {idx}:\n"
            f"- Destination: {p['destination']}\n"
            f"- Weight: {p['weight_lbs']} lbs\n"
            f"- Dimensions: {p['dimensions_in'][0]}x{p['dimensions_in'][1]} in\n"
            f"- Households: {p['households']}\n"
            f"- Included DDUs: {', '.join(p['included_ddus'])}\n"
            f"- Available Carriers: {', '.join(p['available_carriers'])}\n"
        )
    return "\n".join(summary)
