# The main menu our users will use to interact with the Database

# Main menu to choose what to do
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Add/Insert data")
        print("2. Run a Query")
        print("3. Customer Support")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            if login():
                add_menu()
            else:
                print("Invalid login. Access denied.")
        elif choice == '2':
            query_menu()
        elif choice == '3':
            print("Please visit TDx and create a ticket")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


# User credentials (username: password)
user_credentials = {
    'user1': 'Password123',
    'admin': 'adminPass',
    # Add more users as needed
}

# User must log in to change the data
def login():
    username = input("Enter username: ").lower()  # Lowercase for non-case sensitive comparison
    password = input("Enter password: ")  # Case sensitive
    return user_credentials.get(username) == password


# Add and insert data menu
def add_menu():
    while True:
        print("\nAdd/Insert Sub-Menu")
        print("1. Waypoint")
        print("2. Mesostructure")
        print("3. Macrostructure")
        print("4. Thin Structure")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            insertWaypoint_method()
        elif choice == '2':
            insertMacro_method()
        elif choice == '3':
            insertMeso_method()
        elif choice == '4':
            insertThin_method()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter 1-5.")


# Queries menu
def query_menu():
    while True:
        print("\nQuery Sub-Menu")
        print("1. Clastic Grains Types Sorted")
        print("2. Image Report")
        print("3. Macrostructure Data Sorted")
        print("4. Macrostructure Photo Report")
        print("5. Macrostructure Photos Sorted")
        print("6. Macrostructure Types Sorted")
        print("7. Make A Mesostructure Report")
        print("8. Mesostructure Data Sorted")
        print("9. Mesostructure Photos With Thin Sections")
        print("10. Mesostructure Textures Sorted")
        print("11. Mesostructure Types Sorted")
        print("12. Photo Links Data Sorted")
        print("13. Photos by Sample ID")
        print("14. Photos by Sample ID with Thin Sections")
        print("15. Priority List for Analysis")
        print("16. Thin Section Photos Sorted")
        print("17. Waypoint Data Sorted")
        print("18. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            qryClasticGrainsTypesSorted()
        elif choice == '2':
            qryImageReport()
        elif choice == '3':
            qryMacroDataSorted()
        elif choice == '4':
            qryMacroPhotoReport()
        elif choice == '5':
            qryMacroPhotosSorted()
        elif choice == '6':
            qryMacroTypesSorted()
        elif choice == '7':
            qryMakeAMesoReport()
        elif choice == '8':
            qryMesoDataSorted()
        elif choice == '9':
            qryMesoPhotosWThinSections()
        elif choice == '10':
            qryMesoTexturesSorted()
        elif choice == '11':
            qryMesoTypesSorted()
        elif choice == '12':
            qryPhotoLinksDataSorted()
        elif choice == '13':
            qryPhotosbySampleID()
        elif choice == '14':
            qryPhotosbySampleIDWThin()
        elif choice == '15':
            qryPriorityListforAnalysis()
        elif choice == '16':
            qryThinSectionPhotosSorted()
        elif choice == '17':
            qryWaypointDataSorted()
        elif choice == '18':
            break
        else:
            print("Invalid choice. Please enter 1-18.")

# Run the main menu
main_menu()
