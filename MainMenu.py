import mysql.connector
from mysql.connector import Error
from qryClasticGrainTypesSorted import *
from qryImagereport import *
from qryMacrostructureDataSorted import *
from qryMacrostructurePhotoReport import *
from qryMacrostructurePhotosSorted import *
from qryMacrostructureTypesSorted import *
from qryMakeAMesostructureReport import *
from qryMesostructureDataSorted import *
from qryMesostructurePhotosWThinSections import *
from qryMesostructureTexturesSorted import *
from qryMesostructureTypesSorted import *
from qryPhotoLinksDataSorted import *
from qryPhotosBySampleID import *
from qryPhotosBySampleIDWThinSections import *
from qryPriorityListForAnalysis import *
from qryThinSectionPhotosSorted import *
from qryWaypointDataSorted import *

# The main menu our users will use to interact with the Database
def main_menu():
    while True:
        print("\n-------------Main Menu-------------")
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
            print("Please visit TDx and create a ticket or give us a call and we \n"
                    + "will troubleshoot with you and create a ticket on your behalf")
        elif choice == '4':
            print("Exiting program.")
            exit()
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
        print("\n-------------Add/Insert Sub-Menu-------------")
        print("1. Waypoint")
        print("2. Mesostructure")
        print("3. Macrostructure")
        print("4. Thin Structure")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            from WaypointForm import insertWaypoint_method
            insertWaypoint_method()
            main_menu()
        elif choice == '2':
            insertMeso_method()
            main_menu()
        elif choice == '3':
            from MacroStructureForm import insertMacro_method
            insertMacro_method()
            main_menu()
        elif choice == '4':
            insertThin_method()
            main_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter 1-5.")


# Queries menu
def query_menu():
    while True:
        print("\n-------------Query Sub-Menu-------------")
        print("1. Clastic Grains Types Sorted")
        print("2. Image Report")
        print("3. Macrostructure Data Sorted")
        print("4. Macrostructure Photos Sorted")
        print("5. Macrostructure Types Sorted")
        print("6. Make A Mesostructure Report")
        print("7. Mesostructure Data Sorted")
        print("8. Mesostructure Photos With Thin Sections")
        print("9. Mesostructure Textures Sorted")
        print("10. Mesostructure Types Sorted")
        print("11. Photo Links Data Sorted")
        print("12. Photos by Sample ID")
        print("13. Photos by Sample ID with Thin Sections")
        print("14. Priority List for Analysis")
        print("15. Thin Section Photos Sorted")
        print("16. Waypoint Data Sorted")
        print("17. Back to Main Menu")
        choice = input("\nEnter choice: ")
        print("\n")

        if choice == '1':
            qryClasticGrainsTypesSorted()
            main_menu()
        elif choice == '2':
            qryImageReport()
            main_menu()
        elif choice == '3':
            qryMacroDataSorted()
            main_menu()
        elif choice == '4':
            qryMacroPhotosSorted()
            main_menu()
        elif choice == '5':
            qryMacroTypesSorted()
            main_menu()
        elif choice == '6':
            qryMakeAMesoReport()
            main_menu()
        elif choice == '7':
            qryMesoDataSorted()
            main_menu()
        elif choice == '8':
            qryMesoPhotosWThinSections()
            main_menu()
        elif choice == '9':
            qryMesoTexturesSorted()
            main_menu()
        elif choice == '10':
            qryMesoTypesSorted()
            main_menu()
        elif choice == '11':
            qryPhotoLinksDataSorted()
            main_menu()
        elif choice == '12':
            qryPhotosbySampleID()
            main_menu()
        elif choice == '13':
            qryPhotosbySampleIDWThin()
            main_menu()
        elif choice == '14':
            qryPriorityListforAnalysis()
            main_menu()
        elif choice == '15':
            qryThinSectionPhotosSorted()
            main_menu()
        elif choice == '16':
            qryWaypointDataSorted()
            main_menu()
        elif choice == '17':
            break
        else:
            print("Invalid choice. Please enter 1-17.")

# Run the main menu
main_menu()
