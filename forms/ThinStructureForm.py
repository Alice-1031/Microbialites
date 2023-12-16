import mysql.connector
from mysql.connector import Error

def insertThin_method():

    # Replace with your connection details
    db_config = {
            'user': 'izgrmlgwk70csp9l',  # Your JawsDB username
            'password': 'qpmikh9t3n3a2ekg',  # Your JawsDB password
            'host': 'nnsgluut5mye50or.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',  # Your JawsDB host
            'database': 'h762lahe056bge13',  # Your JawsDB database name
            'port': 3306
    }

    try:
        try:
            # Establishing the connection
            connection = mysql.connector.connect(**db_config)

            # Creating a cursor object to interact with the database
            cursor = connection.cursor()

            # WaypointID input
            while True:
                try:
                    WaypointID = input("What WaypointID would you like this ThinStructure To Be A Part Of?")
                    WaypointID = int(WaypointID)
                    break
                except ValueError:
                    print("Value Must Be An Integer!")
            WaypointID = str(WaypointID)
            print('Waypoint ID ' + WaypointID)

            # MacroStructureID input
            while True:
                try:
                    MacroStructureID = input("Enter MacroStructureID (Must Be An Integer): ")
                    MacroStructureID = int(MacroStructureID)
                    break
                except ValueError:
                    print("Value Must Be An Integer!")
            MacroStructureID = str(MacroStructureID)
            print('MacroStructureID Is: ' + MacroStructureID)

            # MesoStructureID input
            while True:
                try:
                    MesoStructureID = input("Enter MesoStructureID (Must Be An Integer): ")
                    MesoStructureID = int(MesoStructureID)
                    break
                except ValueError:
                    print("Value Must Be An Integer!")
            MesoStructureID = str(MesoStructureID)
            print('MesoStructureID Is: ' + MesoStructureID)

            # ThinStructureID input
            while True:
                try:
                    ThinStructureID = input("Enter ThinStructureID (Must Be An Integer): ")
                    ThinStructureID = int(ThinStructureID)
                    break
                except ValueError:
                    print("Value Must Be An Integer!")
            ThinStructureID = str(ThinStructureID)
            print('ThinStructureID Is: ' + ThinStructureID)

            # ThinStructure query
            thinStructureQuery = '''
            INSERT INTO ThinStructure (
                WaypointID, MacroStructureID, MesoStructureID, ThinStructureID
            ) VALUES (%s, %s, %s, %s)
            '''

            # Executing the query
            cursor.execute(thinStructureQuery, (WaypointID, MacroStructureID, MesoStructureID))
            connection.commit()

            # ThinStructureProperties input
            while True:
                try:
                    PorosityPercentEst = input("Enter PorosityPercentEst (Must Be A Decimal): ")
                    PorosityPercentEst = float(PorosityPercentEst)
                    break
                except ValueError:
                    print("Value Must Be A Decimal!")
            PorosityPercentEst = str(PorosityPercentEst)
            print('PorosityPercentEst Is: ' + PorosityPercentEst)

            # CementFilledPorosity input
            while True:
                try:
                    CementFilledPorosity = input("Enter CementFilledPorosity (Must Be A Decimal): ")
                    CementFilledPorosity = float(CementFilledPorosity)
                    break
                except ValueError:
                    print("Value Must Be A Decimal!")
            CementFilledPorosity = str(CementFilledPorosity)
            print('CementFilledPorosity Is: ' + CementFilledPorosity)

            # ThinStructureProperties query and execution
            thinStructurePropertiesQuery = '''
            INSERT INTO ThinStructureProperties (
                ThinStructureID, PorosityPercentEst, CementFilledPorosity
            ) VALUES (%s, %s, %s)
            '''

            # Executing the query
            cursor.execute(thinStructurePropertiesQuery, (ThinStructureID, PorosityPercentEst, CementFilledPorosity))
            connection.commit()
            print("Data inserted successfully")

        except mysql.connector.Error as e:
            # Handle database errors
            print(f"Database error occurred: {e}")

        # ThinStructurePhotos input
        InReport = ''
        while InReport.upper() not in ['Y', 'N']:
            InReport = input("Is this photo included in the report? (Y/N)")
        InReport = InReport.upper() == 'Y'

        OutcropPhoto = ''
        while OutcropPhoto.upper() not in ['Y', 'N']:
            OutcropPhoto = input("Is this photo an outcrop photo? (Y/N)")
        OutcropPhoto = OutcropPhoto.upper() == 'Y'

        Photomicrograph = ''
        while Photomicrograph.upper() not in ['Y', 'N']:
            Photomicrograph = input("Is this a photomicrograph? (Y/N)")
        Photomicrograph = Photomicrograph.upper() == 'Y'

        # PhotoID input
        PhotoID = ''
        while PhotoID.upper() not in ['Y', 'N']:
            PhotoID = input("Is this a PhotoID? (Y/N)")
        PhotoID = PhotoID.upper() == 'Y'
        print("PhotoID Is:", PhotoID)

        # Use a similar format for OtherImage, CLImage, and OtherDocument
        # OtherImage input
        OtherImage = ''
        while OtherImage.upper() not in ['Y', 'N']:
            OtherImage = input("Is this an OtherImage? (Y/N)")
        OtherImage = OtherImage.upper() == 'Y'
        print("OtherImage Is:", OtherImage)

        # CLImage input
        CLImage = ''
        while CLImage.upper() not in ['Y', 'N']:
            CLImage = input("Is this a CLImage? (Y/N)")
        CLImage = CLImage.upper() == 'Y'
        print("CLImage Is:", CLImage)

        # OtherDocument input
        OtherDocument = ''
        while OtherDocument.upper() not in ['Y', 'N']:
            OtherDocument = input("Is this an OtherDocument? (Y/N)")
        OtherDocument = OtherDocument.upper() == 'Y'
        print("OtherDocument Is:", OtherDocument)

        # ReferenceLink input
        ReferenceLink = input("Enter the reference link (VARCHAR, max 255 characters): ")
        ReferenceLink = str(ReferenceLink)

        # ThinStructurePhotos query and execution
        thinStructurePhotosQuery = '''
        INSERT INTO ThinStructurePhotos (
            ThinStructureID, PhotoID, WaypointID, InReport, OutcropPhoto, Photomicrograph, OtherImage,
            CLImage, OtherDocument, ReferenceLink
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        # Executing the query
        cursor.execute(thinStructurePhotosQuery, (ThinStructureID, PhotoID, WaypointID, InReport, OutcropPhoto,
                                                Photomicrograph, OtherImage, CLImage, OtherDocument, ReferenceLink))
        connection.commit()
        print("ThinStructurePhotos data inserted successfully")

        # ThinStructureTextureTypes input
        while True:
            try:
                TextureTypeID = input("Enter TextureTypeID (Must Be An Integer): ")
                TextureTypeID = int(TextureTypeID)
                break
            except ValueError:
                print("Value Must Be An Integer!")
        TextureTypeID = str(TextureTypeID)
        print('TextureTypeID Is: ' + TextureTypeID)

        # ThinStructureTextureTypes query and execution
        thinStructureTextureTypesQuery = '''
        INSERT INTO ThinStructureTextureTypes (
            ThinStructureID, TextureTypeID
        ) VALUES (%s, %s)
        '''

        # Executing the query
        cursor.execute(thinStructureTextureTypesQuery, (ThinStructureID, TextureTypeID))
        connection.commit()
        print("ThinStructureTextureTypes data inserted successfully")

        # ThinStructureClasticGrains input
        while True:
            try:
                ClasticGrainsID = input("Enter ClasticGrainsID (Must Be An Integer): ")
                ClasticGrainsID = int(ClasticGrainsID)
                break
            except ValueError:
                print("Value Must Be An Integer!")
        ClasticGrainsID = str(ClasticGrainsID)
        print('ClasticGrainsID Is: ' + ClasticGrainsID)

        # ThinStructureClasticGrains query and execution
        thinStructureClasticGrainsQuery = '''
        INSERT INTO ThinStructureClasticGrains (
            ThinStructureID, ClasticGrainsID
        ) VALUES (%s, %s)
        '''

        # Executing the query
        cursor.execute(thinStructureClasticGrainsQuery, (ThinStructureID, ClasticGrainsID))
        connection.commit()
        print("ThinStructureClasticGrains data inserted successfully")

        # Don't forget to add the necessary input code and queries for each related table
        # ...

        # Closing the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

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