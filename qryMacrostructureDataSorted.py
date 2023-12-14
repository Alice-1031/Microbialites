import sqlite3

#opens connection and creates cursor
conn = sqlite3.connect('filler.db')
cursor = conn.cursor()

while True:
    try:
        MacrostructureID = input("Enter What MacrostructureID Info You Want:")
        MacrostructureID = int(MacrostructureID)
        break
    except ValueError:
        print("Entry Must Be An Integer!")

MacrostructureID = str(MacrostructureID)
print("You Entered: " + MacrostructureID)

qry = '''
SELECT
    MSP.MacrostructureID,
    MSP.WaptID,
    MST.MacroStructureName,  -- Changed from MacroStructureTypeID to MacroStructureName
    MSP.SectionHeight,
    MSP.Comments
FROM
    MacroStructureProperties MSP
    JOIN MacroStructureTypes MST ON MSP.MacrostructureTypesID = MST.MacroStructureTypesID  -- Added JOIN clause
WHERE
    MSP.MacrostructureID = ?  -- Added a WHERE clause to filter by MacrostructureID
ORDER BY
    MSP.WayptID;
'''

cursor.execute(qry, (MacrostructureID,))

for row in cursor.fetchall():
    print(row)
    #print(", ".join(map(str, row)))

cursor.close()
