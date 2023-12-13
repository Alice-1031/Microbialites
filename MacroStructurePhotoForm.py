import sqlite3

#opens connection and creates cursor
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
addMacrostructureQuery = '''
    INSERT INTO your_table_name (
        MacrostructureID, PhotoID, WaypointID, InReport, OutcropPhoto,
        Photomicrograph, OtherImage, CLImage, OtherDocument, ReferenceLink
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

# executes the cursor that is set up
cursor.execute(addMacrostructureQuery, (
    MacrostructureID, PhotoID, WaypointID, InReport, OutcropPhoto,
    Photomicrograph, OtherImage, CLImage, OtherDocument, ReferenceLink
))

# commit and close connection
conn.commit()
conn.close()