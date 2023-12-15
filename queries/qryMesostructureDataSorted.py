import mysql.connector

def qryMesoDataSorted():

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
        p.PhotoID,
        msph.MesoStructureID,
        msp.ThinSectionMade,
        tsp.PriorityType, -- from ThinSectionPriority
        mst.Mesostructure, -- from MesoStructureType
        tt.MesoStructureTextureType, -- from TextureType
        msp.MacroStructureID,
        msp.SampleSize,
        msp.FieldDescription,
        msp.RockDescription,
        mgt.GrainType, -- from MesoGrainType
        msp.LaminaThickness,
        msr.SynopticRelief, -- from MesoSynopticRelief
        msp.Wavelength,
        msp.AmplitudeOrHeight
    FROM 
        MesoStructurePhotos msph
    RIGHT JOIN Photos p ON msph.PhotoID = p.PhotoID
    RIGHT OUTER JOIN MesoStructureProperties msp ON msp.MesoStructureID = msp.MesoStructureID
    RIGHT OUTER JOIN MesoStructureType mst ON msp.MesoStructureTypeID = mst.MesoStructureTypeID
    RIGHT OUTER JOIN MesoStructureTextureTypes mstt ON msp.MesoStructureID = mstt.MesoStructureID
    RIGHT OUTER JOIN TextureType tt ON mstt.TextureTypeID = tt.TextureTypeID
    RIGHT OUTER JOIN MesoGrainType mgt ON msp.GrainTypeID = mgt.GrainTypeID
    LEFT OUTER JOIN MesoSynopticRelief msr ON msp.MesoSynopticReliefID = msr.MesoSynopticReliefID
    RIGHT OUTER JOIN ThinSectionPriority tsp ON msp.ThinSectionPriorityID = tsp.ThinSectionPriorityID
    ORDER BY
        msp.MesoStructureID;
    '''

    cursor.execute(qry)

    for row in cursor.fetchall():
        print(row)
        #print(", ".join(map(str, row)))

    cursor.close()
