from tkinter import E, W, Frame, StringVar, ttk
import tkinter


class ContactInfo:

    def __init__(self, frame: Frame):
        self.frame = frame
        self.contact_info_frame = tkinter.LabelFrame(self.frame, text="Contact Information",padx=5)
        self.phone1 = StringVar()
        ttk.Label(self.contact_info_frame, text="Phone1").grid(column=0, row=0, sticky=W, padx=15)
        self.phone1_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.phone1)
        self.phone1_entry.grid(column=1, row=0, sticky=(W, E))

        self.phone2 = StringVar()
        ttk.Label(self.contact_info_frame, text="Phone2").grid(column=2, row=0, sticky=W, padx=15)
        self.phone2_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.phone2)
        self.phone2_entry.grid(column=3, row=0, sticky=(W, E))
        self.contact_info_frame.pack(fill='x')
