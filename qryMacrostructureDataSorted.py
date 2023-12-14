import sqlite3

#opens connection and creates cursor
#conn = sqlite3.connect('filler.db')
#cursor = conn.cursor()

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

while True:
    try:
        MacrostructureID = input("Enter What MacrostructureID Info You Want:")
        MacrostructureID = int(MacrostructureID)
        break
    except ValueError:
        print("Entry Must Be An Integer!")

MacrostructureID = str(MacrostructureID)
print("You Entered: " + MacrostructureID)

qry = '''
SELECT
    MS.MacrostructureID,
    MS.WayptID,  -- Getting WayptID from MacroStructure table
    MST.MacroStructureName,
    MSP.SectionHeight,
    MSP.Comments
FROM
    MacroStructureProperties MSP
    JOIN MacroStructureTypes MST ON MSP.MacrostructureTypesID = MST.MacroStructureTypesID
    JOIN MacroStructure MS ON MSP.MacrostructureID = MS.MacrostructureID  -- Added JOIN for MacroStructure

ORDER BY
    MS.WayptID;
'''

cursor.execute(qry)


for row in cursor.fetchall():
    print(row)
    #print(", ".join(map(str, row)))

cursor.close()
