import mysql.connector

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

    for row in cursor.fetchall():
        print(row)
        #print(", ".join(map(str, row)))

    cursor.close()