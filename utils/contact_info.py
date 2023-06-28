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

        self.address1 = StringVar()
        ttk.Label(self.contact_info_frame, text="Address1").grid(column=0, row=1, sticky=W, padx=15)
        self.address1_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.address1)
        self.address1_entry.grid(column=1, row=1, sticky=(W, E))

        self.address2 = StringVar()
        ttk.Label(self.contact_info_frame, text="Address2").grid(column=2, row=1, sticky=W, padx=15)
        self.address2_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.address2)
        self.address2_entry.grid(column=3, row=1, sticky=(W, E))

        self.city = StringVar()
        ttk.Label(self.contact_info_frame, text="City").grid(column=0, row=2, sticky=W, padx=15)
        self.city_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.city)
        self.city_entry.grid(column=1, row=2, sticky=(W, E))

        self.state = StringVar()
        ttk.Label(self.contact_info_frame, text="State").grid(column=2, row=2, sticky=W, padx=15)
        self.state_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.state)
        self.state_entry.grid(column=3, row=2, sticky=(W, E))

        self.zip = StringVar()
        ttk.Label(self.contact_info_frame, text="Zip").grid(column=0, row=3, sticky=W, padx=15)
        self.zip_entry = ttk.Entry(self.contact_info_frame, width=15, textvariable=self.zip)
        self.zip_entry.grid(column=1, row=3, sticky=(W, E))

        self.contact_info_frame.pack(fill='x')
