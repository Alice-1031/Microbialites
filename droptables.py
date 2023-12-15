import mysql.connector

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
        elif choice == '2':
            delete_mesostructure()
        elif choice == '3':
            delete_macrostructure()
        elif choice == '4':
            delete_thin_structure()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter 1-5.")

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