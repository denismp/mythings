from tkinter import *
from tkinter import ttk

from utils.thing_info import ThingInfo

root = Tk(screenName="My Things", baseName="main window")
root.title("My Things To Remember")
root.geometry("500x350")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# thing_name = StringVar()
# thing_entry = ttk.Entry(mainframe, width=15, textvariable=thing_name)
# thing_entry.grid(column=2, row=1, sticky=(W, E))
# ttk.Label(mainframe, text="Name").grid(column=0, row=1, sticky=W)

# thing_type = StringVar()
# thing_type_label = ttk.Label(mainframe, text="Type")
# thing_type_combobox = ttk.Combobox(mainframe, values=["Bank", "Life Insurance"])
# thing_type_label.grid(row=1, column=3)
# thing_type_combobox.grid(row=1, column=4)
name_obj = ThingInfo(mainframe,"Name", "Type")



root.mainloop()

