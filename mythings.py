from tkinter import N, W, E, S, Frame, Tk, ttk
from utils.contact_info import ContactInfo

from utils.thing_info import ThingInfo

root: Tk = Tk(screenName="My Things", baseName="main window")
root.title("My Things To Remember")
root.geometry("515x350")

mainframe: Frame = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name_obj: ThingInfo = ThingInfo(mainframe,"Name", "Type")
contact_obj: ContactInfo = ContactInfo(mainframe)


root.mainloop()

