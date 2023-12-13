import sqlite3

#opens connection and creates cursor
conn = sqlite3.connect('filler.db')
cursor = conn.cursor()

#wayptID Input
while True:
    try:
        wayptID = input("Enter a Waypoint ID(Must Be An Integer): ")
        wayptID = int(wayptID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
wayptID = str(wayptID)
print('Waypoint ID is: ' + wayptID)


#wayptName Input
while True:
    try:
        wayptName = input("Enter a Waypoint Name(Must Be A String): ")
        wayptName = str(wayptName)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Waypoint Name is: ' + wayptName)


#latitude Input
while True:
    try:
        latitude = input("Enter A Latitude(Must Be A Float): ")
        latitude = float(latitude)
        break
    except ValueError:
        print("Value Must Be A Float!")
latitude =str(latitude)
print('Latitude is: ' + latitude)


#Longitude Input
while True:
    try:
        longitude = input("Enter A Longitude(Must Be A Float): ")
        longitude = float(longitude)
        break
    except ValueError:
        print("Value Must Be A Float!")
longitude =str(longitude)
print('Latitude Is: ' + longitude)


#Northing Input
while True:
    try:
        northing = input("Enter A Northing Value(Must Be A Float): ")
        northing = float(northing)
        break
    except ValueError:
        print("Value Must Be A Float!")
northing =str(northing)
print('Northing Is: ' + northing)


#Zone1 Input
while True:
    try:
        zone1 = input("Enter UMTZone1 (Must Be An Integer): ")
        zone1 = int(zone1)
        break
    except ValueError:
        print("Value Must Be An Integer!")
zone1 = str(zone1)
print('UMTZone1 Is: ' + zone1)


#Zone2 Input
while True:
    try:
        zone2 = input("Enter Zone 2 Value(Must Be A String): ")
        zone2 = str(zone2)
        break
    except ValueError:
        print("Value Must Be A String!")
print('UMTZone2 Is: ' + zone2)


#Datum Input
while True:
    try:
        datum = input("Enter Datum (Must Be A String): ")
        datum = str(datum)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Datum Is: ' + datum)


#Projection Input
while True:
    try:
        projection = input("Enter Projection (Must Be A String): ")
        projection = str(projection)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Projection Is: ' + projection)


#Fieldbook Input
while True:
    try:
        fieldBook = input("Enter Fieldbook(Must Be A String): ")
        fieldBook = str(fieldBook)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Fieldbook Is: ' + fieldBook)


#Page Input
while True:
    try:
        page = input("Enter Fieldbook Page(Must Be An Integer): ")
        page = int(page)
        break
    except ValueError:
        print("Value Must Be An Integer!")
page = str(page)
print('The Fieldbook Page Is: ' + page)


#Formation Input
while True:
    try:
        formation = input("Enter Formation(Must Be A String): ")
        formation = str(formation)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Formation Is: ' + formation)


#Site Name Input
while True:
    try:
        siteName = input("Enter Site Name(Must Be A String): ")
        siteName = str(siteName)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Site Name Is: ' + siteName)


#Date Collected Input
while True:
    try:
        dateCollected = input("Enter Date Collected(Format: Month-Day-Year/XX-XX-XXXX): ")
        dateCollected = str(dateCollected)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Date Collected is: ' + dateCollected)

#Elevation Input
while True:
    try:
        elevation = input("Enter the Elevation(Must Be A Float): ")
        elevation = float(elevation)
        break
    except ValueError:
        print("Value Must Be A Float!")
elevation = str(elevation)
print('Elevation is: ' + elevation)

#Project Input
while True:
    try:
        project = input("Enter Project(Must Be A String):")
        project = str(project)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Project is: ' + project)

#Measured Section Input
measuredSection = ''
while measuredSection.upper() not in ['Y', 'N', 'y', 'n']:
    measuredSection = input("Is The Section Measured? (Y/N)")
measuredSection = measuredSection.upper() == 'Y'
print("The Section Is Measured:", measuredSection)

#Section Name Input
while True:
    try:
        sectionName = input("Enter Section Name(Must Be A String): ")
        sectionName = str(sectionName)
        break
    except ValueError:
        print("Value Must Be A String!")
print('Section Name Is: ' + sectionName)

#Section Comments
comments = input("Add any comments if neccessary and press enter:")

#Query String for execute
addWaypointQuery = '''
    INSERT INTO your_table_name (
        wayptID, wayptName, latitude, longitude, northing, zone1, zone2,
        datum, projection, fieldBook, page, formation, siteName, dateCollected,
        elevation, project, measuredSection, sectionName, comments
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

#executes the cursor that is setup
cursor.execute(addWaypointQuery, (wayptID, wayptName, latitude, longitude, northing, zone1, zone2,
                           datum, projection, fieldBook, page, formation, siteName, dateCollected,
                           elevation, project, measuredSection, sectionName, comments))

#commits and closes connection
conn.commit()
conn.close()

print(addWaypointQuery)
