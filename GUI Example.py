import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

#opens connection and creates cursor
conn = sqlite3.connect('filler.db')
cursor = conn.cursor()



def submit_macrostructure():
    # Get values from the form
    macrostructureID = macrostructure_id_entry.get()
    # Get other macrostructure attributes in a similar way...

    # Insert the data into the database
    addMacrostructureQuery = '''
        INSERT INTO your_macrostructure_table_name (
            macrostructureID
        ) VALUES (?)
    '''
    cursor.execute(addMacrostructureQuery, (macrostructureID))
    conn.commit()
    conn.close()

# Create main window
root = tk.Tk()
root.title("Macrostructure Data Entry")

# Create and place form elements
macrostructure_id_label = ttk.Label(root, text="Macrostructure ID:")
macrostructure_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")

macrostructure_id_entry = ttk.Entry(root)
macrostructure_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

# Add other form elements (labels and entry fields) for macrostructure attributes...
macrostructure_test_label = ttk.Label(root, text="Macrostructure test:")
macrostructure_test_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")

macrostructure_test_entry = ttk.Entry(root)
macrostructure_test_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

#dropdown menu
combo = ttk.Combobox(
        #state="readonly",
        values=["Test1", "Test2", "Test3"])
combo.grid(row=1, column=1, padx=10, pady=5)


measured = tk.BooleanVar()

def checkBoxChecked():
    print(measured.get())


check_L1 = Checkbutton(root, text = "Section is measured", command=checkBoxChecked, variable = measured, onvalue = True, offvalue= False)
check_L1.grid(row=2, column=0)




# Create a submit button
submit_button = ttk.Button(root, text="Submit", command=submit_macrostructure)
submit_button.grid(row=5, column=1, pady=20)



# Run the Tkinter event loop
root.mainloop()