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

    # The SQL query (as an example)

    while True:
        try:
            WayptID = input("What WaypointID would you like this Macrostructure To Be A Part Of?")
            WayptID = int(WayptID)
            break
        except ValueError:
            print("Value Must Be A Integer!")
    WayptID = str(WayptID)
    print('Waypoint ID ' + WayptID)

    while True:
        try:
            MacroStructureID = input("What MacroStructureID would you like this MesoStructure To Be A Part Of?")
            MacroStructureID = int(MacroStructureID)
            break
        except ValueError:
            print("Value Must Be A Integer!")
    MacroStructureID = str(MacroStructureID)
    print('MacroStructureID is: ' + MacroStructureID)

    mesoStructureQuery = '''
    INSERT INTO MesoStructure (
        WayptID, MacroStructureID
    ) VALUES (%s, %s)
    '''

    cursor.execute(mesoStructureQuery, (WayptID, MacroStructureID))
    connection.commit()



    selectMacroStructureIDQuery = '''
    SELECT MAX(MacroStructureID) FROM MacroStructure
    '''
    cursor.execute(selectMacroStructureIDQuery)

    #MacrostructureID
    MacrostructureID = cursor.fetchone()[0]
    print(MacrostructureID)

    selectMesoStructureIDQuery = '''
    SELECT MAX(MesoStructureID) FROM MesoStructure
    '''
    cursor.execute(selectMesoStructureIDQuery)

    #MesostructureID
    MesoStructureID = cursor.fetchone()[0]
    print(MesoStructureID)

    #GrainTypeID
    while True:
        try:
            GrainTypeID = input("Enter GrainTypeID (Must Be An Integer): ")
            GrainTypeID = int(GrainTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    GrainTypeID = str(GrainTypeID)
    print('GrainTypeID Is: ' + GrainTypeID)

    #ThinSectionPriorityID
    while True:
        try:
            ThinSectionPriorityID = input("Enter ThinSectionPriorityID (Must Be An Integer): ")
            ThinSectionPriorityID = int(ThinSectionPriorityID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ThinSectionPriorityID = str(ThinSectionPriorityID)
    print('ThinSectionPriorityID Is: ' + ThinSectionPriorityID)

    #MesoInheritanceID
    while True:
        try:
            MesoInheritanceID = input("Enter MesoInheritanceID (Must Be An Integer): ")
            MesoInheritanceID = int(MesoInheritanceID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoInheritanceID = str(MesoInheritanceID)
    print('MesoInheritanceID Is: ' + MesoInheritanceID)

    #MesoStructureTypeID
    while True:
        try:
            MesoStructureTypeID = input("Enter MegaStructureTypeID (Must Be An Integer): ")
            MesoStructureTypeID = int(MesoStructureTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureTypeID = str(MesoStructureTypeID)
    print('MesoStructureTypeID Is: ' + MesoStructureTypeID)

    #MesoStructureLaminaPatternID
    while True:
        try:
            MesoStructureLaminaPatternID = input("Enter MesoStructureLaminaPatternID (Must Be An Integer): ")
            MesoStructureLaminaPatternID = int(MesoStructureLaminaPatternID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStructureLaminaPatternID = str(MesoStructureLaminaPatternID)
    print('MesoStructureLaminaPatternID Is: ' + MesoStructureLaminaPatternID)

    #MesoStackingOverlapID
    while True:
        try:
            MesoStackingOverlapID = input("Enter MesoStackingOverlapID (Must Be An Integer): ")
            MesoStackingOverlapID = int(MesoStackingOverlapID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoStackingOverlapID = str(MesoStackingOverlapID)
    print('MesoStackingOverlapID Is: ' + MesoStackingOverlapID)

    #MesoAlterationID
    while True:
        try:
            MesoAlterationID = input("Enter MesoAlterationID (Must Be An Integer): ")
            MesoAlterationID = int(MesoAlterationID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoAlterationID = str(MesoAlterationID)
    print('MesoAlterationID Is: ' + MesoAlterationID)

    #MesoWavinessID
    while True:
        try:
            MesoWavinessID = input("Enter MesoWavinessID (Must Be An Integer): ")
            MesoWavinessID = int(MesoWavinessID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoWavinessID = str(MesoWavinessID)
    print('MesoWavinessID Is: ' + MesoWavinessID)

    #MesoModalityID
    while True:
        try:
            MesoModalityID = input("Enter MesoModalityID (Must Be An Integer): ")
            MesoModalityID = int(MesoModalityID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoModalityID = str(MesoModalityID)
    print('MesoModalityID Is: ' + MesoModalityID)

    #MesoLaminaProfileID
    while True:
        try:
            MesoLaminaProfileID = input("Enter MesoLaminaProfileID (Must Be An Integer): ")
            MesoLaminaProfileID = int(MesoLaminaProfileID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoLaminaProfileID = str(MesoLaminaProfileID)
    print('MesoLaminaProfileID Is: ' + MesoLaminaProfileID)

    #LaminaThickness
    while True:
        try:
            LaminaThickness = input("Enter LaminaThickness (Must Be A Float): ")
            LaminaThickness = float(LaminaThickness)
            break
        except ValueError:
            print("Value Must Be A Float!")
    LaminaThickness = str(LaminaThickness)
    print('MegaStructureTypeID Is: ' + LaminaThickness)

    #MesoSynopticReliefID
    while True:
        try:
            MesoSynopticReliefID = input("Enter MesoSynopticReliefID (Must Be An Integer): ")
            MesoSynopticReliefID = int(MesoSynopticReliefID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoSynopticReliefID = str(MesoSynopticReliefID)
    print('MesoSynopticReliefID Is: ' + MesoSynopticReliefID)

    #MesoLaminaInheritanceID
    while True:
        try:
            MesoLaminaInheritanceID = input("Enter MesoLaminaInheritanceID (Must Be An Integer): ")
            MesoLaminaInheritanceID = int(MesoLaminaInheritanceID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoLaminaInheritanceID = str(MesoLaminaInheritanceID)
    print('MesoLaminaInheritanceID Is: ' + MesoLaminaInheritanceID)

    #MesoLateralContinuityID
    while True:
        try:
            MesoLateralContinuityID = input("Enter MesoLateralContinuityID (Must Be An Integer): ")
            MesoLateralContinuityID = int(MesoLateralContinuityID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoLateralContinuityID = str(MesoLateralContinuityID)
    print('MesoLateralContinuityID Is: ' + MesoLateralContinuityID)

    #MesoWallsID
    while True:
        try:
            MesoWallsID = input("Enter MesoWallsID (Must Be An Integer): ")
            MesoWallsID = int(MesoWallsID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoWallsID = str(MesoWallsID)
    print('MesoWallsID Is: ' + MesoWallsID)

    #MesoMacroLaminaeID
    while True:
        try:
            MesoMacroLaminaeID = input("Enter MesoMacroLaminaeID (Must Be An Integer): ")
            MesoMacroLaminaeID = int(MesoMacroLaminaeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoMacroLaminaeID = str(MesoMacroLaminaeID)
    print('MesoMacroLaminaeID Is: ' + MesoMacroLaminaeID)

    #MesoLaminaShapeID
    while True:
        try:
            MesoLaminaShapeID = input("Enter MesoLaminaShapeID (Must Be An Integer): ")
            MesoLaminaShapeID = int(MesoLaminaShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoLaminaShapeID = str(MesoLaminaShapeID)
    print('MesoLaminaShapeID Is: ' + MesoLaminaShapeID)

    #MesoClotShapeID
    while True:
        try:
            MesoClotShapeID = input("Enter MesoClotShapeID (Must Be An Integer): ")
            MesoClotShapeID = int(MesoClotShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoClotShapeID = str(MesoClotShapeID)
    print('MesoClotShapeID Is: ' + MesoClotShapeID)

    #MesoClotShapeID
    while True:
        try:
            MesoClotShapeID = input("Enter MesoClotShapeID (Must Be An Integer): ")
            MesoClotShapeID = int(MesoClotShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoClotShapeID = str(MesoClotShapeID)
    print('MesoClotShapeID Is: ' + MesoClotShapeID)

    #MesoClotSize
    while True:
        try:
            MesoClotSize = input("Enter MesoClotSize (Must Be A Float): ")
            MesoClotSize = float(MesoClotSize)
            break
        except ValueError:
            print("Value Must Be A Float!")
    MesoClotSize = str(MesoClotSize)
    print('MesoClotSize Is: ' + MesoClotSize)

    #InTheFRUInterval
    InTheFRUInterval = ''
    while InTheFRUInterval.upper() not in ['Y', 'N', 'y', 'n']:
        InTheFRUInterval = input("Is it in the FRU Interval? (Y/N)")
    if InTheFRUInterval.upper() == 'Y': 
        InTheFRUInterval = '1'
    else:
        InTheFRUInterval = '0'

    #AnalysisPriority
    while True:
        try:
            AnalysisPriority = input("Enter AnalysisPriority (Must Be An Integer): ")
            AnalysisPriority = int(AnalysisPriority)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    AnalysisPriority = str(AnalysisPriority)
    print('AnalysisPriority Is: ' + AnalysisPriority)

    #FieldDescription
    while True:
        try:
            FieldDescription = input("Enter FieldDescription(Must Be A String): ")
            FieldDescription = str(FieldDescription)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('FieldDescription Is: ' + FieldDescription)

    #Lithology
    while True:
        try:
            Lithology = input("Enter Lithology (Must Be An Integer): ")
            Lithology = int(Lithology)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    Lithology = str(Lithology)
    print('Lithology Is: ' + Lithology)

    #RockDescription
    while True:
        try:
            RockDescription = input("Enter RockDescription(Must Be A String): ")
            RockDescription = str(RockDescription)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('RockDescription Is: ' + RockDescription)

    #SampleSize
    while True:
        try:
            SampleSize = input("Enter SampleSize(Must Be A String): ")
            SampleSize = str(SampleSize)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('SampleSize Is: ' + SampleSize)

    #PeelAndSEMPriority
    while True:
        try:
            PeelAndSEMPriority = input("Enter PeelAndSEMPriority (Must Be An Integer): ")
            PeelAndSEMPriority = int(PeelAndSEMPriority)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    PeelAndSEMPriority = str(PeelAndSEMPriority)
    print('PeelAndSEMPriority Is: ' + PeelAndSEMPriority)

    #ThinSectionMade
    while True:
        try:
            ThinSectionMade = input("Enter ThinSectionMade (Must Be An Integer): ")
            ThinSectionMade = int(ThinSectionMade)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ThinSectionMade = str(ThinSectionMade)
    print('MegaStructureTypeID Is: ' + ThinSectionMade)

    #C_N_Priority
    while True:
        try:
            C_N_Priority = input("Enter C_N_Priority (Must Be An Integer): ")
            C_N_Priority = int(C_N_Priority)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    C_N_Priority = str(C_N_Priority)
    print('C_N_Priority Is: ' + C_N_Priority)

    #Wavelength
    while True:
        try:
            Wavelength = input("Enter Wavelength (Must Be An Integer): ")
            Wavelength = float(Wavelength)
            break
        except ValueError:
            print("Value Must Be A Float!")
    Wavelength = str(Wavelength)
    print('Wavelength Is: ' + Wavelength)

    #AmplitudeOrHeight
    while True:
        try:
            AmplitudeOrHeight = input("Enter AmplitudeOrHeight (Must Be A Float): ")
            AmplitudeOrHeight = float(AmplitudeOrHeight)
            break
        except ValueError:
            print("Value Must Be A Float!")
    AmplitudeOrHeight = str(AmplitudeOrHeight)
    print('AmplitudeOrHeight Is: ' + AmplitudeOrHeight)

    #MicrobialiteType
    while True:
        try:
            MicrobialiteType = input("Enter MicrobialiteType (Must Be An Integer): ")
            MicrobialiteType = int(MicrobialiteType)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MicrobialiteType = str(MicrobialiteType)
    print('MicrobialiteType Is: ' + MicrobialiteType)

    #BriefNotes
    while True:
        try:
            BriefNotes = input("Enter BriefNotes(Must Be A String): ")
            BriefNotes = str(BriefNotes)
            break
        except ValueError:
            print("Value Must Be A String!")
    print('BriefNotes Is: ' + BriefNotes)

    #MesoClotTypeID
    while True:
        try:
            MesoClotTypeID = input("Enter MesoClotTypeID (Must Be An Integer): ")
            MesoClotTypeID = int(MesoClotTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MesoClotTypeID = str(MesoClotTypeID)
    print('MesoClotTypeID Is: ' + MesoClotTypeID)

    mesoStructurePropertiesQuery = '''
    INSERT INTO mesostructureproperties (
        GrainTypeID, ThinSectionPriorityID, MesoInheritanceID, MesoStructureTypeID,
        MesoStructureLaminaPatternID, MesoStackingOverlapID, MesoAlterationID, MesoWavinessID, MesoModalityID, MesoLaminaProfileID, LaminaThickness,
        MesoSynopticReliefID, MesoLaminaInheritanceID, MesoLateralContinuityID, MesoWallsID, MesoMacroLaminaeID, MesoLaminaShapeID,
        MesoClotShapeID, MesoClotSize, InTheFRUInterval, AnalysisPriority, MacroStructureID, FieldDescription, Lithology, RockDescription,
        SampleSize, PeelAndSEMPriority, ThinSectionMade, C_N_Priority, Wavelength, AmplitudeOrHeight, MicrobialiteType, BriefNotes, MesoClotTypeID     
    ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    # Executing the query
    cursor.execute(mesoStructurePropertiesQuery, (GrainTypeID, ThinSectionPriorityID, MesoInheritanceID, MesoStructureTypeID,
        MesoStructureLaminaPatternID, MesoStackingOverlapID, MesoAlterationID, MesoWavinessID, MesoModalityID, MesoLaminaProfileID, LaminaThickness,
        MesoSynopticReliefID, MesoLaminaInheritanceID, MesoLateralContinuityID, MesoWallsID, MesoMacroLaminaeID, MesoLaminaShapeID,
        MesoClotShapeID, MesoClotSize, InTheFRUInterval, AnalysisPriority, MacroStructureID, FieldDescription, Lithology, RockDescription,
        SampleSize, PeelAndSEMPriority, ThinSectionMade, C_N_Priority, Wavelength, AmplitudeOrHeight, MicrobialiteType, BriefNotes, MesoClotTypeID))

    # Committing the transaction
    connection.commit()
    print("Data inserted successfully")

    loop = input("How Many Texture Types Would You Like To Add?")
    loop = int(loop)
    counter = 0
    while counter < loop:
        while True:
            try:
                textureInsert = input("Enter Texture Type ID (Must Be An Integer)")
                textureInsert = int(textureInsert)
                break
            except ValueError:
                print("Value Must Be A Integer!")
        textureInsert = str(textureInsert)
        print('TextureID: ' + textureInsert)
        mesoTextureQuery = '''
        INSERT INTO MesoStructureTextureTypes(
        MesoStructureID, TextureTypeID
        ) VALUES (%s, %s)
        '''
        cursor.execute(mesoTextureQuery, (MesoStructureID, textureInsert))
        counter += 1

    loop = input("How Many Meso Architectures Would You Like To Add?")
    loop = int(loop)
    counter = 0
    while counter < loop:
        while True:
            try:
                ArchitectureID = input("Enter ArchitectureID (Must Be An Integer)")
                ArchitectureID = int(ArchitectureID)
                break
            except ValueError:
                print("Value Must Be A Integer!")
        ArchitectureID = str(ArchitectureID)
        print('ArchitectureID: ' + ArchitectureID)
        mesoArchitectureQuery = '''
        INSERT INTO MesoStructureArchitecture(
        MesoStructureID, ArchitectureID
        ) VALUES (%s, %s)
        '''
        cursor.execute(mesoArchitectureQuery, (MesoStructureID, ArchitectureID))
        counter += 1

    print("Data inserted successfully")
except mysql.connector.Error as e:
    if e.errno == 1452:
        print("Foreign Key Constraint Error: The referenced key does not exist.")
    else:
        print(f"Database error occurred: {e}")

finally:
    # Closing the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
