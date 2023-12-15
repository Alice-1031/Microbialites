import mysql.connector
from mysql.connector import Error

# Replace with your connection details
db_config = {
        'user': 'izgrmlgwk70csp9l',  # Your JawsDB username
        'password': 'qpmikh9t3n3a2ekg',  # Your JawsDB password
        'host': 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  # Your JawsDB host
        'database': 'h762lahe056bge13',  # Your JawsDB database name
        'port': 3306
}

try:
    # Establishing the connection
    connection = mysql.connector.connect(**db_config)

    # Creating a cursor object to interact with the database
    cursor = connection.cursor()

    # MesoStructureID Input
    while True:
        try:
            MesoStructureID = input("Enter MesoStructure ID (Must Be An Integer): ")
            MesoStructureID = int(MesoStructureID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureID = str(MesoStructureID)
    print('MesoStructure ID is:', MesoStructureID)

    # WaypointID Input
    while True:
        try:
            WaypointID = input("Enter Waypoint ID (Must Be An Integer): ")
            WaypointID = int(WaypointID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    WaypointID = str(WaypointID)
    print('Waypoint ID is:', WaypointID)

    # MacroStructureID Input
    while True:
        try:
            MacroStructureID = input("Enter MacroStructure ID (Must Be An Integer): ")
            MacroStructureID = int(MacroStructureID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MacroStructureID = str(MacroStructureID)
    print('MacroStructure ID is:', MacroStructureID)

    # Query String for execute
    addMesoStructureQuery = '''
        INSERT INTO mesoStructure (
            MesoStructureID, WaypointID, MacroStructureID
        ) VALUES (?, ?, ?)
    '''

    # executes the cursor that is set up
    cursor.execute(addMesoStructureQuery, (
        MesoStructureID, WaypointID, MacroStructureID
    ))

    # commit and close connection
    conn.commit()
    conn.close()

    print(addMesoStructureQuery)

    #MesoStructureProperties

    #opens connection and creates cursor
    conn = sqlite3.connect('filler.db')
    cursor = conn.cursor()

    # MesoStructureID Input
    while True:
        try:
            MesoStructureID = input("Enter MesoStructure ID (Must Be An Integer): ")
            MesoStructureID = int(MesoStructureID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureID = str(MesoStructureID)
    print('MesoStructure ID is:', MesoStructureID)

    # GrainTypeID Input
    while True:
        try:
            GrainTypeID = input("Enter Grain Type ID (Must Be An Integer): ")
            GrainTypeID = int(GrainTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    GrainTypeID = str(GrainTypeID)
    print('Grain Type ID is:', GrainTypeID)

    # GeneralTypeID Input
    while True:
        try:
            GeneralTypeID = input("Enter General Type ID (Must Be An Integer): ")
            GeneralTypeID = int(GeneralTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    GeneralTypeID = str(GeneralTypeID)
    print('General Type ID is:', GeneralTypeID)

    # ThinSectionPriorityID Input
    while True:
        try:
            ThinSectionPriorityID = input("Enter Thin Section Priority ID (Must Be An Integer): ")
            ThinSectionPriorityID = int(ThinSectionPriorityID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ThinSectionPriorityID = str(ThinSectionPriorityID)
    print('Thin Section Priority ID is:', ThinSectionPriorityID)

    # MesoInheritanceID Input
    while True:
        try:
            MesoInheritanceID = input("Enter Meso Inheritance ID (Must Be An Integer): ")
            MesoInheritanceID = int(MesoInheritanceID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoInheritanceID = str(MesoInheritanceID)
    print('Meso Inheritance ID is:', MesoInheritanceID)

    # MesoStructureTypeID Input
    while True:
        try:
            MesoStructureTypeID = input("Enter Meso Structure Type ID (Must Be An Integer): ")
            MesoStructureTypeID = int(MesoStructureTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureTypeID = str(MesoStructureTypeID)
    print('Meso Structure Type ID is:', MesoStructureTypeID)

    # MesoStructureLaminaID Input
    while True:
        try:
            MesoStructureLaminaID = input("Enter Meso Structure Lamina ID (Must Be An Integer): ")
            MesoStructureLaminaID = int(MesoStructureLaminaID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureLaminaID = str(MesoStructureLaminaID)
    print('Meso Structure Lamina ID is:', MesoStructureLaminaID)

    # Query String for execute
    addMesoStructurePropertiesQuery = '''
        INSERT INTO MesoStructureProperties (
            MesoStructureID, GrainTypeID, GeneralTypeID, ThinSectionPriorityID,
            MesoInheritanceID, MesoStructureTypeID, MesoStructureLaminaID
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    '''

    # executes the cursor that is set up
    cursor.execute(addMesoStructurePropertiesQuery, (
        MesoStructureID, GrainTypeID, GeneralTypeID, ThinSectionPriorityID,
        MesoInheritanceID, MesoStructureTypeID, MesoStructureLaminaID
    ))

    # commit and close connection
    conn.commit()
    conn.close()

    print(addMesoStructurePropertiesQuery)

    #MesoStructurePhotos

    #opens connection and creates cursor
    conn = sqlite3.connect('filler.db')
    cursor = conn.cursor()

    # MesoStructureID Input
    while True:
        try:
            MesoStructureID = input("Enter MesoStructure ID (Must Be An Integer): ")
            MesoStructureID = int(MesoStructureID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureID = str(MesoStructureID)
    print('MesoStructure ID is:', MesoStructureID)

    # PhotoID Input
    while True:
        try:
            PhotoID = input("Enter Photo ID (Must Be An Integer): ")
            PhotoID = int(PhotoID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    PhotoID = str(PhotoID)
    print('Photo ID is:', PhotoID)

    # WaypointID Input
    while True:
        try:
            WaypointID = input("Enter Waypoint ID (Must Be An Integer): ")
            WaypointID = int(WaypointID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    WaypointID = str(WaypointID)
    print('Waypoint ID is:', WaypointID)

    # MacroStructureID Input
    while True:
        try:
            MacroStructureID = input("Enter MacroStructure ID (Must Be An Integer): ")
            MacroStructureID = int(MacroStructureID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MacroStructureID = str(MacroStructureID)
    print('MacroStructure ID is:', MacroStructureID)

    # InReport Input
    inReport = ''
    while inReport.upper() not in ['Y', 'N', 'y', 'n']:
        inReport = input("Is it in the Report? (Y/N)")
    inReport = inReport.upper() == 'Y'
    print("In Report:", inReport)

    # OutcropPhoto Input
    outcropPhoto = ''
    while outcropPhoto.upper() not in ['Y', 'N', 'y', 'n']:
        outcropPhoto = input("Is it an Outcrop Photo? (Y/N)")
    outcropPhoto = outcropPhoto.upper() == 'Y'
    print("Outcrop Photo:", outcropPhoto)

    # Photomicrograph Input
    photomicrograph = ''
    while photomicrograph.upper() not in ['Y', 'N', 'y', 'n']:
        photomicrograph = input("Is it a Photomicrograph? (Y/N)")
    photomicrograph = photomicrograph.upper() == 'Y'
    print("Photomicrograph:", photomicrograph)

    # OtherImage Input
    otherImage = ''
    while otherImage.upper() not in ['Y', 'N', 'y', 'n']:
        otherImage = input("Is it an Other Image? (Y/N)")
    otherImage = otherImage.upper() == 'Y'
    print("Other Image:", otherImage)

    # CLImage Input
    clImage = ''
    while clImage.upper() not in ['Y', 'N', 'y', 'n']:
        clImage = input("Is it a CL Image? (Y/N)")
    clImage = clImage.upper() == 'Y'
    print("CL Image:", clImage)

    # OtherDocument Input
    otherDocument = ''
    while otherDocument.upper() not in ['Y', 'N', 'y', 'n']:
        otherDocument = input("Is it an Other Document? (Y/N)")
    otherDocument = otherDocument.upper() == 'Y'
    print("Other Document:", otherDocument)

    # ReferenceLink Input
    referenceLink = input("Enter Reference Link (Must Be A String): ")

    # Query String for execute
    addMesoStructurePhotosQuery = '''
        INSERT INTO MesoStructurePhotos (
            MesoStructureID, PhotoID, WaypointID, MacroStructureID,
            InReport, OutcropPhoto, Photomicrograph, OtherImage,
            CLImage, OtherDocument, ReferenceLink
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # executes the cursor that is set up
    cursor.execute(addMesoStructurePhotosQuery, (
        MesoStructureID, PhotoID, WaypointID, MacroStructureID,
        inReport, outcropPhoto, photomicrograph, otherImage,
        clImage, otherDocument, referenceLink
    ))

    # commit and close connection
    conn.commit()

    print(addMesoStructurePhotosQuery)

except mysql.connector.Error as e:
    if e.errno == 1452:
        print("Foreign Key Constraint Error: The referenced key does not exist.")
        # Extract constraint name and referenced table name from the error message
        error_message = str(e)
        constraint_name_start = error_message.find('FOREIGN KEY (`') + len('FOREIGN KEY (`')
        constraint_name_end = error_message.find('`) REFERENCES')
        constraint_name = error_message[constraint_name_start:constraint_name_end]

        referenced_table_start = error_message.find('REFERENCES `' + db_config['database'] + '`.`') + len('REFERENCES `' + db_config['database'] + '`.`')
        referenced_table_end = error_message.find('` (`')
        referenced_table_name = error_message[referenced_table_start:referenced_table_end]

        print(f"Foreign Key Constraint Error: The referenced key in table '{referenced_table_name}' does not exist for constraint '{constraint_name}'.")
    else:
        print(f"Database error occurred: {e}")

finally:
    # Closing the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")