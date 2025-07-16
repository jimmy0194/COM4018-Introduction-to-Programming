# Task 2 - Entering Property Rental and Repair Details
# Module: COM4018 - Introduction to Programming
# ---------------------------------------------------

# Global data structure for property details hardcoded from Table 1
property_details = {
    "B12-3AB": {"original_cost": 153450, "mortgage": 112345},
    "B13-4CD": {"original_cost": 212130, "mortgage": 180234},
    "B14-5GH": {"original_cost": 120100, "mortgage": 85980},
    "B15-6JK": {"original_cost": 135230, "mortgage": 101321},
    "B16-7MO": {"original_cost": 183230, "mortgage": 130234}
}

# Data structure to store rent/repair entries per property
property_transactions = {
    "B12-3AB": [],
    "B13-4CD": [],
    "B14-5GH": [],
    "B15-6JK": [],
    "B16-7MO": []
}

# Subroutine to accept user input for rental and maintenance transactions
def property_data():
    print("\n--- Enter Property Rental or Repair Details ---")
    while True:
        # InputPropertyID
        property_id = input("Enter property ID (or press Enter to return to menu): ").strip().upper()
        if property_id == "":
            print("Returning to main menu.")
            break

        if property_id not in property_details:
            print("Invalid property ID. Please try again.")
            continue

        #Inputdescription
        description = input("Enter description (e.g., Rent received or Boiler repair): ")

        #Inputamount with validation
        try:
            amount = float(input("Enter amount (positive for rent, negative for expense): "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        #Save
        property_transactions[property_id].append((description, amount))
        print(f"Entry saved for {property_id}.")

        #continue
        another = input("Add another transaction? (y/n): ").strip().lower()
        if another != 'y':
            break

# Entrypoint
if __name__ == "__main__":
    property_data()

    #Print all entries to verify data storage
    print("\n--- Stored Transactions Summary ---")
    for prop, entries in property_transactions.items():
        if entries:
            print(f"\n{prop}:")
            for desc, amt in entries:
                print(f"  - {desc} : {amt}")
