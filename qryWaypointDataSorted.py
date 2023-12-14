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
        WayptID = input("Enter What Waypoint ID Info You Want:")
        WayptID = int(WayptID)
        break
    except ValueError:
        print("Entry Must Be An Integer!")

WayptID = str(WayptID)
print("You Entered: " + WayptID)

qry = '''
SELECT
    WayptID,
    DateCollected,
    WayptName,
    ProjectName,
    SiteOrLocationName,
    Formation,
    Fieldbook,
    FieldbookPage,
    MeasuredSection,
    SectionName,
    Comments,
    Latitude,
    Longitude,
    Elevation,
    UTMZone1,
    UTMZone2,
    Datum,
    Projection
FROM
    Waypoint
ORDER BY
    DateCollected DESC;
'''

cursor.execute(qry)

for row in cursor.fetchall():
    print(row)
    #print(", ".join(map(str, row)))

cursor.close()
