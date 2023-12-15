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

    macroStructureQuery = '''
    INSERT INTO MacroStructure (
        WayptID
    ) VALUES (%s)
    '''
    cursor.execute(macroStructureQuery, (WayptID,))
    connection.commit()

    selectMacroStructureIDQuery = '''
    SELECT MAX(MacroStructureID) FROM macrostructure
    '''

    cursor.execute(selectMacroStructureIDQuery)

    #MacrostructureID
    MacrostructureID = cursor.fetchone()[0]
    print(MacrostructureID)

    #MegaStructureTypeID
    while True:
        try:
            MegaStructureTypeID = input("Enter MegaStructureTypeID (Must Be An Integer): ")
            MegaStructureTypeID = int(MegaStructureTypeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MegaStructureTypeID = str(MegaStructureTypeID)
    print('MegaStructureTypeID Is: ' + MegaStructureTypeID)

    #Section Height
    while True:
        try:
            SectionHeight = input("Enter Section Height (Must Be A Float): ")
            SectionHeight = float(SectionHeight)
            break
        except ValueError:
            print("Value Must Be A Float!")
    SectionHeight = str(SectionHeight)
    print('Section Height Is: ' + SectionHeight)

    #comments input
    Comments = input("Add any short comments:")
    Comments = str(Comments)

    #MegastructureShapeID
    while True:
        try:
            MegastructureShapeID = input("Enter Megastructure ShapeID (Must Be An Integer): ")
            MegastructureShapeID = int(MegastructureShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MegastructureShapeID = str(MegastructureShapeID)
    print('MegastructureShapeID Is: ' + MegastructureShapeID)

    #MegaStructureSizeID
    while True:
        try:
            MegaStructureSizeID = input("Enter MegaStructure SizeID (Must Be An Integer): ")
            MegaStructureSizeID = int(MegaStructureSizeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MegaStructureSizeID = str(MegaStructureSizeID)
    print('MegaStructureSizeID Is: ' + MegaStructureSizeID)

    #SubstrateID
    while True:
        try:
            SubstrateID = input("Enter Substrate ID(Must Be An Integer): ")
            SubstrateID = int(SubstrateID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    SubstrateID = str(SubstrateID)
    print('SubstrateID Is: ' + SubstrateID)


    #InitiationID
    while True:
        try:
            InitiationID  = input("Enter Initiation ID(Must Be An Integer): ")
            InitiationID  = int(InitiationID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    InitiationID  = str(InitiationID )
    print('InitiationID  Is: ' + InitiationID)


    #PlanViewID
    while True:
        try:
            PlanViewID  = input("Enter PlanView ID(Must Be An Integer): ")
            PlanViewID  = int(PlanViewID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    PlanViewID = str(PlanViewID)
    print('PlanViewID  Is: ' + PlanViewID)


    #LinkageID
    while True:
        try:
            LinkageID  = input("Enter LinkageID(Must Be An Integer): ")
            LinkageID  = int(LinkageID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    LinkageID = str(LinkageID)
    print('LinkageID  Is: ' + LinkageID)


    #SpacingID
    while True:
        try:
            SpacingID  = input("Enter SpacingID(Must Be An Integer): ")
            SpacingID  = int(SpacingID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    SpacingID = str(SpacingID)
    print('PlanViewID  Is: ' + SpacingID)


    #ShapeID
    while True:
        try:
            ShapeID  = input("Enter ShapeID(Must Be An Integer): ")
            ShapeID  = int(ShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ShapeID = str(ShapeID)
    print('ShapeID  Is: ' + ShapeID)


    #ShapeLayeringID
    while True:
        try:
            ShapeLayeringID  = input("Enter ShapeLayeringID(Must Be An Integer): ")
            ShapeLayeringID  = int(ShapeLayeringID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ShapeLayeringID = str(ShapeLayeringID)
    print('ShapeLayeringID  Is: ' + ShapeLayeringID)


    #ShapeDomeID
    while True:
        try:
            ShapeDomeID  = input("Enter ShapeDomeID(Must Be An Integer): ")
            ShapeDomeID  = int(ShapeDomeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ShapeDomeID = str(ShapeDomeID)
    print('ShapeDomeID  Is: ' + ShapeDomeID)


    #ConicalShapeID
    while True:
        try:
            ConicalShapeID  = input("Enter ConicalShapeID(Must Be An Integer): ")
            ConicalShapeID  = int(ConicalShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ConicalShapeID = str(ConicalShapeID)
    print('ConicalShapeID  Is: ' + ConicalShapeID)


    #AspectRatioID
    while True:
        try:
            AspectRatioID  = input("Enter AspectRatioID(Must Be An Integer): ")
            AspectRatioID  = int(AspectRatioID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    AspectRatioID = str(AspectRatioID)
    print('AspectRatioID  Is: ' + AspectRatioID)

    #GrowthVariabilityID
    while True:
        try:
            GrowthVariabilityID  = input("Enter GrowthVariabilityID(Must Be An Integer): ")
            GrowthVariabilityID  = int(GrowthVariabilityID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    GrowthVariabilityID = str(GrowthVariabilityID)
    print('GrowthVariabilityID  Is: ' + GrowthVariabilityID)

    #AttitudeID
    while True:
        try:
            AttitudeID  = input("Enter AttitudeID(Must Be An Integer): ")
            AttitudeID  = int(AttitudeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    AttitudeID = str(AttitudeID)
    print('AttitudeID  Is: ' + AttitudeID)

    #BranchingStyleID
    while True:
        try:
            BranchingStyleID  = input("Enter BranchingStyleID(Must Be An Integer): ")
            BranchingStyleID  = int(BranchingStyleID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    BranchingStyleID = str(BranchingStyleID)
    print('BranchingStyleID  Is: ' + BranchingStyleID)

    #BranchingModeID
    while True:
        try:
            BranchingModeID  = input("Enter BranchingModeID(Must Be An Integer): ")
            BranchingModeID  = int(BranchingModeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    BranchingModeID = str(BranchingModeID)
    print('BranchingModeID  Is: ' + BranchingModeID)

    #BranchingAngleID
    while True:
        try:
            BranchingAngleID  = input("Enter BranchingAngleID(Must Be An Integer): ")
            BranchingAngleID  = int(BranchingAngleID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    BranchingAngleID = str(BranchingAngleID)
    print('BranchingAngleID  Is: ' + BranchingAngleID)

    #ColumnShapeID
    while True:
        try:
            ColumnShapeID  = input("Enter PlanView ID(Must Be An Integer): ")
            ColumnShapeID  = int(ColumnShapeID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    ColumnShapeID = str(ColumnShapeID)
    print('ColumnShapeID  Is: ' + ColumnShapeID)

    #MacrostructureTypesID
    while True:
        try:
            MacrostructureTypesID  = input("Enter MacrostructureTypesID(Must Be An Integer): ")
            MacrostructureTypesID  = int(MacrostructureTypesID)
            break
        except ValueError:
            print("Value Must Be An Integer!")
    MacrostructureTypesID = str(MacrostructureTypesID)
    print('MacrostructureTypesID  Is: ' + MacrostructureTypesID)

    macroStructurePropertiesQuery = '''
    INSERT INTO MacroStructureProperties (
        MacrostructureID, MegaStructureTypeID, SectionHeight, Comments, MegastructureShapeID,
        MegaStructureSizeID, SubstrateID, InitiationID, PlanViewID, LinkageID, SpacingID, ShapeID,
        ShapeLayeringID, ShapeDomeID, ConicalShapeID, AspectRatioID, GrowthVariabilityID, AttitudeID,
        BranchingStyleID, BranchingModeID, BranchingAngleID, ColumnShapeID, MacroStructureTypesID
    ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    # Executing the query
    cursor.execute(macroStructurePropertiesQuery, (MacrostructureID, MegaStructureTypeID, SectionHeight, Comments, MegastructureShapeID,
        MegaStructureSizeID, SubstrateID, InitiationID, PlanViewID, LinkageID, SpacingID, ShapeID,
        ShapeLayeringID, ShapeDomeID, ConicalShapeID, AspectRatioID, GrowthVariabilityID, AttitudeID,
        BranchingStyleID, BranchingModeID, BranchingAngleID, ColumnShapeID, MacrostructureTypesID))

    # Committing the transaction

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
