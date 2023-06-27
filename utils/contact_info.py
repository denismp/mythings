from tkinter import E, W, Frame, StringVar, ttk


class ContactInfo:

    def __init__(self, frame: Frame):
        self.frame = frame
        self.phone1 = StringVar()
        self.phone1_entry = ttk.Entry(self.frame, width=15, textvariable=self.phone1)
        self.phone1_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(self.frame, text="Phone1").grid(column=0, row=1, sticky=W)

        self.phone2 = StringVar()
        self.phone2_entry = ttk.Entry(self.frame, width=15, textvariable=self.phone2)
        self.phone2_entry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(self.frame, text="Phone1").grid(column=0, row=1, sticky=W)
