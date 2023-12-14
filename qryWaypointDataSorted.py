import sqlite3

#opens connection and creates cursor
conn = sqlite3.connect('filler.db')
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
    WaypointName,
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
    Northing,
    Easting,
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
