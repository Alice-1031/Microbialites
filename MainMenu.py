import mysql.connector
from prettytable import PrettyTable
from mysql.connector import Error
from queries.qryClasticGrainTypesSorted import *
from queries.qryImagereport import *
from queries.qryMacrostructureDataSorted import *
from queries.qryMacrostructurePhotosSorted import *
from queries.qryMacrostructureTypesSorted import *
from queries.qryMakeAMesostructureReport import *
from queries.qryMesostructureDataSorted import *
from queries.qryMesostructurePhotosWThinSections import *
from queries.qryMesostructureTexturesSorted import *
from queries.qryMesostructureTypesSorted import *
from queries.qryPhotoLinksDataSorted import *
from queries.qryPhotosBySampleID import *
from queries.qryPhotosBySampleIDWThinSections import *
from queries.qryPriorityListForAnalysis import *
from queries.qryThinSectionPhotosSorted import *
from queries.qryWaypointDataSorted import *


db_config = {
        'user': 'izgrmlgwk70csp9l',  # Your JawsDB username
        'password': 'qpmikh9t3n3a2ekg',  # Your JawsDB password
        'host': 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  # Your JawsDB host
        'database': 'h762lahe056bge13',  # Your JawsDB database name
        'port': 3306
}


# The main menu our users will use to interact with the Database
def main_menu():
    while True:
        print("\n-------------Main Menu-------------")
        print("1. Add/Insert data")
        print("2. Run a Query")
        print("3. Customer Support")
        print("4. Drop Table")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            if login():
                add_menu()
            else:
                print("Invalid login. Access denied.")
        elif choice == '2':
            query_menu()
        elif choice == '3':
            create_support_ticket()
        elif choice == '4':
            if login():
                delete_menu()
            else:
                print("Invalid login. Access denied.")
        elif choice == '5':
            print("Exiting program.")
            exit()
        else:
            print("Invalid choice. Please enter 1-5.")


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
            from forms.WaypointForm import insertWaypoint_method
            insertWaypoint_method()
            main_menu()
        elif choice == '2':
            from forms.MacroStructureForm import insertMeso_method
            insertMeso_method()
            main_menu()
        elif choice == '3':
            from forms.MacroStructureForm import insertMacro_method
            insertMacro_method()
            main_menu()
        elif choice == '4':
            from forms.ThinStructureForm import insertThin_method
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


# Delete menu
def delete_menu():
    while True:
        print("\n-------------Delete Sub-Menu-------------")
        print("1. Delete Waypoint")
        print("2. Delete Mesostructure")
        print("3. Delete Macrostructure")
        print("4. Delete Thin Structure")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            delete_waypoint()
            main_menu()
        elif choice == '2':
            delete_mesostructure()
            main_menu()
        elif choice == '3':
            delete_macrostructure()
            main_menu()
        elif choice == '4':
            delete_thin_structure()
            main_menu()
        elif choice == '5':
            main_menu()
        else:
            print("Invalid choice. Please enter 1-5.")

# Delete
def delete_structure(table, id_column):
    try:
        structure_id = int(input(f"Enter the ID of the {table} to delete: "))
        query = f"DELETE FROM {table} WHERE {id_column} = %s"
        execute_query(query, (structure_id,))
        print(f"{table} with ID {structure_id} has been deleted.")
    except ValueError:
        print("Invalid ID. Please enter a number.")
    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")

def delete_waypoint():
    delete_structure('Waypoint', 'WayptID')

def delete_mesostructure():
    delete_structure('MesoStructure', 'MesoStructureID')

def delete_macrostructure():
    delete_structure('MacroStructure', 'MacrostructureID')

def delete_thin_structure():
    delete_structure('ThinStructures', 'ThinStructureID')

def execute_query(query, params):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")

#create ticket
def create_support_ticket():
    print("\n--- Customer Support Ticket Creation ---")
    user_name = input("Enter your name: ")
    contact_info = input("Enter your contact information: ")
    issue_description = input("Describe your issue: ")

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        insert_query = '''
        INSERT INTO SupportTickets (UserName, ContactInfo, IssueDescription)
        VALUES (%s, %s, %s)
        '''
        cursor.execute(insert_query, (user_name, contact_info, issue_description))
        conn.commit()
        print("Support ticket created successfully.")

    except mysql.connector.Error as err:
        print(f"Error occurred: {err}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Run the main menu
main_menu()
