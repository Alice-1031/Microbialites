import sqlite3

#opens connection and creates cursor
conn = sqlite3.connect('filler.db')
cursor = conn.cursor()

while True:
    try:
        MacroStructureTypesID = input("Enter What Macrostructure Type ID Info You Want:")
        MacroStructureTypesID = int(MacroStructureTypesID)
        break
    except ValueError:
        print("Entry Must Be An Integer!")

MacroStructureTypesID = str(MacroStructureTypesID)
print("You Entered: " + MacroStructureTypesID)

qry = '''
SELECT
    MacroStructureTypesID,
    MacroStructureName,
    FormDescription
FROM
    MacroStructureTypes
ORDER BY
    MacroStructureTypesID;
'''

cursor.execute(qry)

for row in cursor.fetchall():
    print(row)
    #print(", ".join(map(str, row)))

cursor.close()
