import mysql.connector

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
    t.MesoStructureTextureType,
    msp.MesoStructureID,
    msp.ThinSectionMade,
    msph.InReport,  -- from MesoStructurePhotos
    msp.FieldDescription,
    msp.RockDescription,
    msp.MacroStructureID,
    msp.LaminaThickness,
    msr.SynopticRelief, -- from MesoSynopticRelief
    msp.Wavelength,
    msp.AmplitudeOrHeight,
    gt.GrainType, -- from MesoGrainType
    msph.OutcropPhoto, -- from MesoStructurePhotos
    p.PhotoLinkName -- from Photos
FROM 
    MesoStructureProperties msp
LEFT JOIN MesoStructureTextureTypes mstt ON msp.MesoStructureID = mstt.MesoStructureID
LEFT JOIN TextureType t ON mstt.TextureTypeID = t.TextureTypeID
LEFT JOIN MesoGrainType gt ON msp.GrainTypeID = gt.GrainTypeID
LEFT JOIN MesoSynopticRelief msr ON msp.MesoSynopticReliefID = msr.MesoSynopticReliefID
LEFT JOIN MesoStructurePhotos msph ON msp.MesoStructureID = msph.MesoStructureID
LEFT JOIN Photos p ON msph.PhotoID = p.PhotoID
ORDER BY
    msp.MesoStructureTypeID;
'''

cursor.execute(qry)

for row in cursor.fetchall():
    print(row)
    #print(", ".join(map(str, row)))

cursor.close()
