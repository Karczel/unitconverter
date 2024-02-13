"""Converter UI"""
import tkinter as tk
from tkinter import ttk, messagebox

import unittype
from unittype import UnitType
from converter import *


class ConverterUI(tk.Tk):
    """User Interface for a unit converter.

    The UI displays units and handles user interaction.  It invokes
    a UnitConverter object to perform actual unit conversions.
    """

    def __init__(self, converter: UnitConverter):
        """initialize ui"""
        super().__init__()
        self.converter = converter
        self.init_components()

    def init_components(self):
        """Create components and layout the UI."""
        # menu
        self.unit, unitchooser = self.load_units(unittype.UnitType, self.update_combobox)
        self.unit_type = Area
        # self.unit_type = Length
        # self.unit_type = Time
        # self.unit_type = Volume
        # self.unit_type = Weight

        self.leftinput = tk.StringVar()
        self.rightinput = tk.StringVar()

        # left input field
        leftfield = tk.Entry(self, width=20, textvariable=self.leftinput)
        # combobox
        self.leftunit, self.leftchooser = self.load_units(self.unit_type,self.do_nothing)
        # label '='
        label = tk.Label(self, text="=")
        # right input field
        rightfield = tk.Entry(self, width=20, textvariable=self.rightinput)
        # combobox
        self.rightunit, self.rightchooser = self.load_units(self.unit_type, self.do_nothing)
        # convert button
        convert_button = tk.Button(self, text="Convert", command=self.convert_handler)
        # clear button
        clear_button = tk.Button(self, text="Clear", command=self.clear_handler)

        # Enter bind
        leftfield.bind('<Return>', self.convert_handler)
        rightfield.bind('<Return>', self.convert_handler)
        unitchooser.bind('<<Combobox>>', self.update_unit)

        # layout
        padding = {'padx': 10, 'pady': 10}
        # position & size the components
        unitchooser.pack(**padding, anchor=tk.NW)
        leftfield.pack(side=tk.LEFT, **padding, expand=True, fill=tk.X)
        self.leftchooser.pack(side=tk.LEFT, **padding, expand=True, fill=tk.X)
        label.pack(side=tk.LEFT, **padding)
        rightfield.pack(side=tk.LEFT, **padding, expand=True, fill=tk.X)
        self.rightchooser.pack(side=tk.LEFT, **padding, expand=True, fill=tk.X)
        clear_button.pack(side=tk.RIGHT, **padding)
        convert_button.pack(side=tk.RIGHT, **padding)

    def load_units(self, unittype: UnitType, function):
        """Load units of the requested unittype into the comboboxes."""
        units = self.converter.get_units(unittype)
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(self, textvariable=selected, postcommand=function)
        # and select which unit to display
        chooser['values'] = units
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>', function)
        return selected, chooser

    def convert_handler(self, *args):
        """An event handler for conversion actions.
        You should call the unit converter to perform actual conversion.
        """
        try:
            # 1. Convert from left side to right side
            unit_1 = self.leftunit.get()
            unit_2 = self.rightunit.get()
            if self.leftinput.get() != "":
                self.converter.set_number(float(self.leftinput.get()))
                self.converter.set_unit(unit_1)
                self.rightinput.set(self.converter.convert(unit_2).number)

            # 2. When that works, intelligently decide to convert
            #        left-to-right or right-to-left
            # in this case, left side must be empty,
            # otherwise will use left side value
            # and output in right side instead
            else:
                self.converter.set_number(float(self.rightinput.get()))
                self.converter.set_unit(unit_2)
                self.leftinput.set(self.converter.convert(unit_1).number)
        except ValueError:
            messagebox.showerror(message="Only number input are accepted")
            # change to red input and clear other, return to black when re-input

    def do_nothing(self, *args):
        pass

    def clear_handler(self, *args):
        """clears both input fields"""
        self.leftinput.set("")
        self.rightinput.set("")

    def update_unit(self,*args):
        if self.unit.get() == "Area":
            self.unit_type = Area
        elif self.unit.get() == "Temperature":
            self.unit_type = Temperature
        elif self.unit.get() == "Time":
            self.unit_type = Time
        elif self.unit.get() == "Volume":
            self.unit_type = Volume
        elif self.unit.get() == "Weight":
            self.unit_type = Weight
        else:
            self.unit_type = Length
        lst = self.converter.get_units(self.unit_type)
        return lst

    def update_combobox(self, *args):
        self.leftchooser['values'] = self.update_unit()
        self.rightchooser['values'] = self.update_unit()

    def run(self):
        """start the app, wait for events"""
        self.mainloop()
