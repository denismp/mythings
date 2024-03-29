from tkinter import *
from tkinter import E, W, Frame, StringVar, ttk
import tkinter


class ThingInfo:
    
    def __init__(self, frame: Frame, name_label: str, type_label: str):
        self.frame = frame
        self.thing_info_frame = tkinter.LabelFrame(self.frame, text="Thing Information",padx=5)
        #self.thing_info_frame.grid(row=0, column=0, padx=20, pady=10)
        self.thing_name = StringVar()
        ttk.Label(self.thing_info_frame, text=name_label).grid(column=0, row=0, sticky=W, padx=15)
        self.thing_entry = ttk.Entry(self.thing_info_frame, width=15, textvariable=self.thing_name)
        self.thing_entry.grid(column=1, row=0, sticky=(W, E))

        self.thing_type = StringVar()
        self.thing_type_label = ttk.Label(self.thing_info_frame, text=type_label)
        self.thing_type_label.grid(row=0, column=2, sticky=(E), padx=15)
        self.thing_type_combobox = ttk.Combobox(self.thing_info_frame, values=["Bank", "Life Insurance"])
        self.thing_type_combobox.grid(row=0, column=3)
        self.thing_info_frame.pack(fill='x')