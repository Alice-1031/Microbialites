import sqlite3

#opens connection and creates cursor
conn = sqlite3.connect('filler.db')
cursor = conn.cursor()


# MacrostructureID Input
while True:
    try:
        macrostructureID = input("Enter Macrostructure ID (Must Be An Integer): ")
        macrostructureID = int(macrostructureID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
macrostructureID = str(macrostructureID)
print('Macrostructure ID is: ' + macrostructureID)

# MegaStructureTypeID Input
while True:
    try:
        MegaStructureTypeID = input("Enter MegaStructure Type ID (Must Be An Integer): ")
        MegaStructureTypeID = int(MegaStructureTypeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
MegaStructureTypeID = str(MegaStructureTypeID)
print('MegaStructure Type ID is: ' + MegaStructureTypeID)

# SectionHeight Input
while True:
    try:
        SectionHeight = input("Enter Section Height (Must Be A Decimal): ")
        SectionHeight = float(SectionHeight)
        break
    except ValueError:
        print("Value Must Be A Decimal!")
SectionHeight = str(SectionHeight)
print('Section Height is: ' + SectionHeight)

# Comments Input
Comments = input("Enter Comments: ")

# MegastructureShapeID Input
while True:
    try:
        MegastructureShapeID = input("Enter MegaStructure Shape ID (Must Be An Integer): ")
        MegastructureShapeID = int(MegastructureShapeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
MegastructureShapeID = str(MegastructureShapeID)
print('MegaStructure Shape ID is: ' + MegastructureShapeID)

# MegaStructureSizeID Input
while True:
    try:
        MegaStructureSizeID = input("Enter MegaStructure Size ID (Must Be An Integer): ")
        MegaStructureSizeID = int(MegaStructureSizeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
MegaStructureSizeID = str(MegaStructureSizeID)
print('MegaStructure Size ID is: ' + MegaStructureSizeID)

# SubstrateID Input
while True:
    try:
        SubstrateID = input("Enter Substrate ID (Must Be An Integer): ")
        SubstrateID = int(SubstrateID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
SubstrateID = str(SubstrateID)
print('Substrate ID is: ' + SubstrateID)

# InitiationID Input
while True:
    try:
        InitiationID = input("Enter Initiation ID (Must Be An Integer): ")
        InitiationID = int(InitiationID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
InitiationID = str(InitiationID)
print('Initiation ID is: ' + InitiationID)

# PlanViewID Input
while True:
    try:
        PlanViewID = input("Enter PlanView ID (Must Be An Integer): ")
        PlanViewID = int(PlanViewID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
PlanViewID = str(PlanViewID)
print('PlanView ID is: ' + PlanViewID)

# LinkageID Input
while True:
    try:
        LinkageID = input("Enter Linkage ID (Must Be An Integer): ")
        LinkageID = int(LinkageID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
LinkageID = str(LinkageID)
print('Linkage ID is: ' + LinkageID)

# SpacingID Input
while True:
    try:
        SpacingID = input("Enter Spacing ID (Must Be An Integer): ")
        SpacingID = int(SpacingID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
SpacingID = str(SpacingID)
print('Spacing ID is: ' + SpacingID)

# ShapeID Input
while True:
    try:
        ShapeID = input("Enter Shape ID (Must Be An Integer): ")
        ShapeID = int(ShapeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
ShapeID = str(ShapeID)
print('Shape ID is: ' + ShapeID)

# ShapeLayeringID Input
while True:
    try:
        ShapeLayeringID = input("Enter ShapeLayering ID (Must Be An Integer): ")
        ShapeLayeringID = int(ShapeLayeringID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
ShapeLayeringID = str(ShapeLayeringID)
print('ShapeLayering ID is: ' + ShapeLayeringID)

# ShapeDomeID Input
while True:
    try:
        ShapeDomeID = input("Enter ShapeDome ID (Must Be An Integer): ")
        ShapeDomeID = int(ShapeDomeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
ShapeDomeID = str(ShapeDomeID)
print('ShapeDome ID is: ' + ShapeDomeID)

# ConicalShapeID Input
while True:
    try:
        ConicalShapeID = input("Enter ConicalShape ID (Must Be An Integer): ")
        ConicalShapeID = int(ConicalShapeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
ConicalShapeID = str(ConicalShapeID)
print('ConicalShape ID is: ' + ConicalShapeID)

# AspectRatioID Input
while True:
    try:
        AspectRatioID = input("Enter AspectRatio ID (Must Be An Integer): ")
        AspectRatioID = int(AspectRatioID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
AspectRatioID = str(AspectRatioID)
print('AspectRatio ID is: ' + AspectRatioID)

# GrowthVariabilityID Input
while True:
    try:
        GrowthVariabilityID = input("Enter GrowthVariability ID (Must Be An Integer): ")
        GrowthVariabilityID = int(GrowthVariabilityID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
GrowthVariabilityID = str(GrowthVariabilityID)
print('GrowthVariability ID is: ' + GrowthVariabilityID)

# AttitudeID Input
while True:
    try:
        AttitudeID = input("Enter Attitude ID (Must Be An Integer): ")
        AttitudeID = int(AttitudeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
AttitudeID = str(AttitudeID)
print('Attitude ID is: ' + AttitudeID)

# BranchingStyleID Input
while True:
    try:
        BranchingStyleID = input("Enter BranchingStyle ID (Must Be An Integer): ")
        BranchingStyleID = int(BranchingStyleID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
BranchingStyleID = str(BranchingStyleID)
print('BranchingStyle ID is: ' + BranchingStyleID)

# BranchingModeID Input
while True:
    try:
        BranchingModeID = input("Enter BranchingMode ID (Must Be An Integer): ")
        BranchingModeID = int(BranchingModeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
BranchingModeID = str(BranchingModeID)
print('BranchingMode ID is: ' + BranchingModeID)

# BranchingAngleID Input
while True:
    try:
        BranchingAngleID = input("Enter BranchingAngle ID (Must Be An Integer): ")
        BranchingAngleID = int(BranchingAngleID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
branchingAngleID = str(BranchingAngleID)
print('BranchingAngle ID is: ' + BranchingAngleID)

# ColumnShapeID Input
while True:
    try:
        ColumnShapeID = input("Enter ColumnShape ID (Must Be An Integer): ")
        ColumnShapeID = int(ColumnShapeID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
columnShapeID = str(ColumnShapeID)
print('ColumnShape ID is: ' + columnShapeID)

# MacrostrucutreTypesID Input
while True:
    try:
        MacrostructureTypesID = input("Enter MacrostructureTypes ID (Must Be An Integer): ")
        MacrostructureTypesID = int(MacrostructureTypesID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
macrostructureTypesID = str(MacrostructureTypesID)
print('MacrostructureTypes ID is: ' + macrostructureTypesID)

# Query String for execute
addMacroStructureQuery = '''
    INSERT INTO MacroStructureProperties (
        MegaStructureTypeID, SectionHeight, Comments,
        MegastructureShapeID, MegaStructureSizeID, SubstrateID, InitiationID,
        PlanViewID, LinkageID, SpacingID, ShapeID, ShapeLayeringID, ShapeDomeID,
        ConicalShapeID, AspectRatioID, GrowthVariabilityID, AttitudeID,
        BranchingStyleID, BranchingModeID, BranchingAngleID, ColumnShapeID,
        MacrostrucutreTypesID
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

# executes the cursor that is set up
cursor.execute(addMacroStructureQuery, (
    MegaStructureTypeID, SectionHeight, Comments,
    MegastructureShapeID, MegaStructureSizeID, SubstrateID, InitiationID,
    PlanViewID, LinkageID, SpacingID, ShapeID, ShapeLayeringID, ShapeDomeID,
    ConicalShapeID, AspectRatioID, GrowthVariabilityID, AttitudeID,
    BranchingStyleID, BranchingModeID, BranchingAngleID, ColumnShapeID,
    MacrostructureTypesID
))

# commit and close connection
conn.commit()
conn.close()

print(addMacroStructureQuery)


conn = sqlite3.connect('filler.db')
cursor = conn.cursor()

# MacrostructureID Input
while True:
    try:
        MacrostructureID = input("Enter Macrostructure ID (Must Be An Integer): ")
        MacrostructureID = int(MacrostructureID)
        break
    except ValueError:
        print("Value Must Be An Integer!")
MacrostructureID = str(MacrostructureID)
print('Macrostructure ID is:', MacrostructureID)

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

# InReport Input
InReport = ''
while InReport.upper() not in ['Y', 'N', 'y', 'n']:
    InReport = input("Is it in the report? (Y/N): ")
InReport = InReport.upper() == 'Y'
print("In the Report:", InReport)

# OutcropPhoto Input
OutcropPhoto = ''
while OutcropPhoto.upper() not in ['Y', 'N', 'y', 'n']:
    OutcropPhoto = input("Is it an outcrop photo? (Y/N): ")
OutcropPhoto = OutcropPhoto.upper() == 'Y'
print("Outcrop Photo:", OutcropPhoto)

# Photomicrograph Input
Photomicrograph = ''
while Photomicrograph.upper() not in ['Y', 'N', 'y', 'n']:
    Photomicrograph = input("Is it a photomicrograph? (Y/N): ")
Photomicrograph = Photomicrograph.upper() == 'Y'
print("Photomicrograph:", Photomicrograph)

# OtherImage Input
OtherImage = ''
while OtherImage.upper() not in ['Y', 'N', 'y', 'n']:
    OtherImage = input("Is it another type of image? (Y/N): ")
OtherImage = OtherImage.upper() == 'Y'
print("Other Image:", OtherImage)

# CLImage Input
CLImage = ''
while CLImage.upper() not in ['Y', 'N', 'y', 'n']:
    CLImage = input("Is it a CL image? (Y/N): ")
CLImage = CLImage.upper() == 'Y'
print("CL Image:", CLImage)

# OtherDocument Input
OtherDocument = ''
while OtherDocument.upper() not in ['Y', 'N', 'y', 'n']:
    OtherDocument = input("Is it another type of document? (Y/N): ")
OtherDocument = OtherDocument.upper() == 'Y'
print("Other Document:", OtherDocument)

# ReferenceLink Input
ReferenceLink = input("Enter Reference Link (Must Be A String): ")
ReferenceLink = str(ReferenceLink)
print('Reference Link is:', ReferenceLink)

# Query String for execute
addMacrostructurePhotoQuery = '''
    INSERT INTO MacroStructurePhotos (
        MacrostructureID, PhotoID, WaypointID, InReport, OutcropPhoto,
        Photomicrograph, OtherImage, CLImage, OtherDocument, ReferenceLink
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

# executes the cursor that is set up
cursor.execute(addMacrostructurePhotoQuery, (
    MacrostructureID, PhotoID, WaypointID, InReport, OutcropPhoto,
    Photomicrograph, OtherImage, CLImage, OtherDocument, ReferenceLink
))

# commit and close connection
conn.commit()
conn.close()

print(addMacrostructurePhotoQuery)