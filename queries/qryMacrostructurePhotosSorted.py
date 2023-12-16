import mysql.connector
from prettytable import PrettyTable

def qryMacroPhotosSorted():

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
        msp.PhotoID,
        p.PhotoLinkName,
        msp.MacroStructureID,
        msp.OutcropPhoto,
        msp.Photomicrograph,
        msp.CLImage,
        msp.OtherImage,
        msp.OtherDocument
    FROM
        MacroStructurePhotos msp
    JOIN
        Photos p ON msp.PhotoID = p.PhotoID
    ORDER BY
        msp.MacroStructureID;
    '''

    cursor.execute(qry)

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["PhotoID", "PhotoLinkName", "MacroStructureID", "OutcropPhoto", "Photomicrograph", "CLImage", "OtherImage", "OtherDocument"]
    table.max_width = 50  # Set max width of columns
    table.align = "l"     # Align text to the left

    for row in cursor.fetchall():
        table.add_row(row)

    cursor.close()
    conn.close()

    print(table)