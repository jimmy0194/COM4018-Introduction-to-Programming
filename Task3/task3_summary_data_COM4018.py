# Task 3 - Display Property Rental Summary
# Module: COM4018 - Introduction to Programming
# ---------------------------------------------------

# --- Reuse from Task 2 ---
property_details = {
    "B12-3AB": {"original_cost": 153450, "mortgage": 112345},
    "B13-4CD": {"original_cost": 212130, "mortgage": 180234},
    "B14-5GH": {"original_cost": 120100, "mortgage": 85980},
    "B15-6JK": {"original_cost": 135230, "mortgage": 101321},
    "B16-7MO": {"original_cost": 183230, "mortgage": 130234}
}

property_transactions = {
    "B12-3AB": [],
    "B13-4CD": [],
    "B14-5GH": [],
    "B15-6JK": [],
    "B16-7MO": []
}

# For testing:

property_transactions["B12-3AB"] = [("Rent received", 760), ("Rent received", 760), ("Boiler serviced", -80)]
property_transactions["B13-4CD"] = [("Rent received", 1060), ("Replaced radiator", -150)]
property_transactions["B14-5GH"] = [("Rent received", 600), ("Leak repair", -70), ("Flooring", -210)]
property_transactions["B15-6JK"] = [("Rent received", 690), ("Boiler serviced", -80)]
property_transactions["B16-7MO"] = [("Rent received", 920), ("Washer repair", -120)]

# Subroutine to display summary
def summary_data():
    print("\n--- Property Summary Table ---\n")
    print("{:<10} {:>10} {:>10} {:>12} {:>12} {:>10}".format(
        "Property", "Original", "Repairs", "Amended", "Mortgage", "Rent %"))
    print("{:<10} {:>10} {:>10} {:>12} {:>12} {:>10}".format(
        "", "Cost", "", "Cost", "", "of Mortg."))

    total_original = 0
    total_repairs = 0
    total_amended = 0
    total_mortgage = 0
    total_rents = 0

    for prop_id, details in property_details.items():
        original_cost = details["original_cost"]
        mortgage = details["mortgage"]

        total_rent = 0
        total_repair = 0

        for desc, amount in property_transactions[prop_id]:
            if amount >= 0:
                total_rent += amount
            else:
                total_repair += abs(amount)  # Make repair positive for display

        amended_cost = original_cost + total_repair
        rent_percent = (total_rent / mortgage * 100) if mortgage else 0

        print("{:<10} {:>10} {:>10} {:>12} {:>12} {:>9.2f}%".format(
            prop_id, original_cost, total_repair, amended_cost, mortgage, rent_percent))

        # Totals
        total_original += original_cost
        total_repairs += total_repair
        total_amended += amended_cost
        total_mortgage += mortgage
        total_rents += total_rent

    # Final total row
    total_rent_percent = (total_rents / total_mortgage * 100) if total_mortgage else 0
    print("-" * 70)
    print("{:<10} {:>10} {:>10} {:>12} {:>12} {:>9.2f}%".format(
        "TOTAL", total_original, total_repairs, total_amended, total_mortgage, total_rent_percent))

# Entry point to test
if __name__ == "__main__":
    summary_data()
