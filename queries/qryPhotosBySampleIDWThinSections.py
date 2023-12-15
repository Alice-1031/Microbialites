import mysql.connector

def qryPhotosbySampleIDWThin():

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
        msp.ThinSectionMade, -- from MesoStructureProperties
        mst.Mesostructure, -- from MesoStructureType
        msp.AnalysisPriority -- from MesoStructureProperties
    FROM 
        MesoStructure ms
    JOIN MesoStructurePhotos msph ON ms.MesoStructureID = msph.MesoStructureID
    JOIN Photos p ON msph.PhotoID = p.PhotoID
    JOIN MesoStructureProperties msp ON ms.MesoStructureID = msp.MesoStructureID
    JOIN MesoStructureType mst ON msp.MesoStructureTypeID = mst.MesoStructureTypeID
    ORDER BY
        msp.MesoStructureTypeID;
    '''

    cursor.execute(qry)

    for row in cursor.fetchall():
        print(row)
        #print(", ".join(map(str, row)))

    cursor.close()
