import mysql.connector
from mysql.connector import Error

try:
    # JawsDB MySQL connection details
    db_config = {
        'user': 'izgrmlgwk70csp9l',  # Your JawsDB username
        'password': 'qpmikh9t3n3a2ekg',  # Your JawsDB password
        'host': 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  # Your JawsDB host
        'database': 'h762lahe056bge13',  # Your JawsDB database name
        'port': 3306
    }

    # Open connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()


    #wayptName Input
    while True:
        try:
            WayptName = input("Enter a Waypoint Name(Must Be A String): ")
            WayptName = str(WayptName)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Waypoint Name is: ' + WayptName)


    #latitude Input
    while True:
        try:
            Latitude = input("Enter A Latitude(Must Be A Float): ")
            Latitude = float(Latitude)
            break
        except ValueError:
            print("Value Must Be A Float!")
    Latitude =str(Latitude)
    print('Latitude is: ' + Latitude)


    #Longitude Input
    while True:
        try:
            Longitude = input("Enter A Longitude(Must Be A Float): ")
            Longitude = float(Longitude)
            break
        except ValueError:
            print("Value Must Be A Float!")
    Longitude =str(Longitude)
    print('Latitude Is: ' + Longitude)

    #Zone1 Input
    while True:
        try:
            UTMZone1 = input("Enter UMTZone1 (Must Be An Integer): ")
            UTMZone1 = int(UTMZone1)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    UTMZone1 = str(UTMZone1)
    print('UMTZone1 Is: ' + UTMZone1)


    #Zone2 Input
    while True:
        try:
            UTMZone2 = input("Enter Zone 2 Value(Must Be A String): ")
            UTMZone2 = str(UTMZone2)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('UMTZone2 Is: ' + UTMZone2)


    #Datum Input
    while True:
        try:
            Datum = input("Enter Datum (Must Be A String): ")
            Datum = str(Datum)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Datum Is: ' + Datum)


    #Projection Input
    while True:
        try:
            Projection = input("Enter Projection (Must Be A String): ")
            Projection = str(Projection)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Projection Is: ' + Projection)


    #Fieldbook Input
    while True:
        try:
            Fieldbook = input("Enter Fieldbook(Must Be A String): ")
            Fieldbook = str(Fieldbook)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Fieldbook Is: ' + Fieldbook)


    #Page Input
    while True:
        try:
            FieldbookPage = input("Enter Fieldbook Page(Must Be An Integer): ")
            FieldbookPage = int(FieldbookPage)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    FieldbookPage = str(FieldbookPage)
    print('The Fieldbook Page Is: ' + FieldbookPage)


    #Formation Input
    while True:
        try:
            Formation = input("Enter Formation(Must Be A String): ")
            Formation = str(Formation)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Formation Is: ' + Formation)


    #Site Name Input
    while True:
        try:
            SiteOrLocationName = input("Enter Site Name(Must Be A String): ")
            SiteOrLocationName = str(SiteOrLocationName)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Site Name Is: ' + SiteOrLocationName)


    #Date Collected Input
    while True:
        try:
            DateCollected = input("Enter Date Collected(Format: Month-Day-Year/XX-XX-XXXX): ")
            DateCollected = str(DateCollected)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Date Collected is: ' + DateCollected)

    #Elevation Input
    while True:
        try:
            Elevation = input("Enter the Elevation(Must Be A Float): ")
            Elevation = float(Elevation)
            break
        except ValueError:
            print("Value Must Be A Float!")
    Elevation = str(Elevation)
    print('Elevation is: ' + Elevation)

    #Project Input
    while True:
        try:
            ProjectName = input("Enter Project(Must Be A String):")
            ProjectName = str(ProjectName)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Project is: ' + ProjectName)

    #Measured Section Input
    MeasuredSection = ''
    while MeasuredSection.upper() not in ['Y', 'N', 'y', 'n']:
        MeasuredSection = input("Is The Section Measured? (Y/N)")
    if MeasuredSection.upper() == 'Y': 
        MeasuredSection = '1'
    else:
        MeasuredSection = '0'
        
    print("The Section Is Measured:", MeasuredSection)

    #Section Name Input
    while True:
        try:
            SectionName = input("Enter Section Name(Must Be A String): ")
            SectionName = str(SectionName)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('Section Name Is: ' + SectionName)

    #Section Comments
    Comments = input("Add any comments if neccessary and press enter:")
    Comments = str(Comments)

    #Query String for execute
    addWaypointQuery = '''
    INSERT INTO Waypoint (
         WayptName, Latitude, Longitude, UTMZone1, UTMZone2,
        Datum, Projection, FieldBook, FieldbookPage, Formation, SiteOrLocationName, DateCollected,
        Elevation, ProjectName, MeasuredSection, SectionName, Comments
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    #executes the cursor that is setup
    cursor.execute(addWaypointQuery, (WayptName, Latitude, Longitude, UTMZone1, UTMZone2,
                            Datum, Projection, Fieldbook, FieldbookPage, Formation, SiteOrLocationName, DateCollected,
                            Elevation, ProjectName, MeasuredSection, SectionName, Comments))

    conn.commit()
    print("Data inserted successfully.")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
    
