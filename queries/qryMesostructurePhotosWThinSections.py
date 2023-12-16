import mysql.connector
from prettytable import PrettyTable

def qryMesoPhotosWThinSections():

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
        mst.Mesostructure, -- from MesoStructureType
        msp.ThinSectionMade,
        p.PhotoLinkName, -- from Photos
        c.Northing, -- from Coordinates
        c.Easting, -- from Coordinates
        tt.MesoStructureTextureType -- from TextureType
    FROM 
        MesoStructure ms
    JOIN MesoStructureProperties msp ON ms.MesoStructureID = msp.MesoStructureID
    JOIN MesoStructureType mst ON msp.MesoStructureTypeID = mst.MesoStructureTypeID
    JOIN MesoStructureTextureTypes mstt ON ms.MesoStructureID = mstt.MesoStructureID
    JOIN TextureType tt ON mstt.TextureTypeID = tt.TextureTypeID
    JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msp.MesoStructureID
    JOIN Photos p ON msph.PhotoID = p.PhotoID
    JOIN Coordinates c ON ms.WayptID = c.WayptID
    ORDER BY
        msp.MesoStructureTypeID;
    '''

    cursor.execute(qry)

    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["MesoStructureID", "Mesostructure", "ThinSectionMade", "PhotoLinkName", "Northing", "Easting", "MesoStructureTextureType"]
    table.max_width = 20  # Set max width of columns
    table.align = "l"     # Align text to the left

    for row in cursor.fetchall():
        # Format boolean values for better readability
        formatted_row = [
            row[0], 
            row[1], 
            'Yes' if row[2] else 'No',
            row[3],
            row[4],
            row[5],
            row[6]
        ]
        table.add_row(formatted_row)

    cursor.close()
    conn.close()

    print(table)