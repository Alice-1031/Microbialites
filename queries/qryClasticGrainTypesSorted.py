import mysql.connector
from prettytable import PrettyTable

# Method to run the database query
def qryClasticGrainsTypesSorted():

    # JawsDB MySQL connection details
    db_config = {
        'user': 'izgrmlgwk70csp9l',  # Your JawsDB username
        'password': 'qpmikh9t3n3a2ekg',  # Your JawsDB password
        'host': 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  # Your JawsDB host
        'database': 'h762lahe056bge13',  # Your JawsDB database name
        'port': 3306
    }

    # Open connection and create cursor
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    qry = '''
    SELECT
        ClasticGrainsID,
        ClasticGrainType
    FROM
        ClasticGrains
    ORDER BY
        ClasticGrainsID;
    '''

    cursor.execute(qry)

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["ClasticGrainsID", "ClasticGrainType"]
    table.max_width = 50  # Set max width of columns
    table.align = "l"     # Align text to the left

    for row in cursor.fetchall():
        table.add_row(row)

    cursor.close()
    conn.close()

    print(table)