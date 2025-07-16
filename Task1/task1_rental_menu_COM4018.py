# Task 1 - Rental Management Menu System
# Module: COM4018 - Introduction to Programming
# ----------------------------------------------

# Function to handle Option 1: Enter property details
def property_data():
    print("\n--- Enter Property Details ---")
    print("This is a placeholder for entering property rental and repair data.")

# Function to handle Option 2: Display summary
def summary_data():
    print("\n--- Property Summary ---")
    print("This is a placeholder for displaying property summary.")

# Mainmenu
def display_menu():
    while True:
        print("\nRental Management Menu")
        print("1. Enter rental property details")
        print("2. Display summary for rentals")
        print("3. Exit")

        choice = input("Enter your choice : ")

        # Inputvalidation
        if choice == "1":
            property_data()
        elif choice == "2":
            summary_data()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

display_menu()
