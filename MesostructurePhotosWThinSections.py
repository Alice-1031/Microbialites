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

for row in cursor.fetchall():
    print(row)
    #print(", ".join(map(str, row)))

cursor.close()
