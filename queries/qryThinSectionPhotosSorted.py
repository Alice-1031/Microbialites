import mysql.connector
from prettytable import PrettyTable

def qryThinSectionPhotosSorted():

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
        ms.MesoStructureID,
        p.PhotoLinkName, -- from Photos
        msph.OutcropPhoto, -- from MesoStructurePhotos
        msph.Photomicrograph, -- from MesoStructurePhotos
        msph.CLImage, -- from MesoStructurePhotos
        msph.OtherDocument -- from MesoStructurePhotos
    FROM
        MesoStructure ms
    JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msph.MesoStructureID
    JOIN Photos p ON msph.PhotoID = p.PhotoID
    ORDER BY
        ms.MesoStructureID;
    '''

    cursor.execute(qry)

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["MesoStructureID", "PhotoLinkName", "OutcropPhoto", "Photomicrograph", "CLImage", "OtherDocument"]
    table.max_width = 50  # Set max width of columns
    table.align = "l"     # Align text to the left

    for row in cursor.fetchall():
        table.add_row(row)

    cursor.close()
    conn.close()

    print(table)