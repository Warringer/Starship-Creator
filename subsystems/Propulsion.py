"""Propulsion Class."""

from widgets.MultiEntry import MultiEntry
from widgets.MultiDisplay import MultiDisplay
from tkinter import DoubleVar, IntVar
from subsystems.Subsystem import Subsystem


class Propulsion(Subsystem):
    """Contains the Propulsion Data."""

    def __init__(self, data):
        """Init the Propulsion."""
        self.data = data
        self.propulsion = data.propulsion
        self.max_acceleration = DoubleVar()
        self.no_thrusters = IntVar(value=2)
        self.power_thruster = DoubleVar(value=750)
        self.power_total_thruster = DoubleVar()
        self.mass_total_thruster = DoubleVar()
        self.waste_power = DoubleVar()

        self.make_entry()
        self.make_display()

    def make_entry(self):
        """Make the Entry Form."""
        entry = {
            "Max Acceneration": {
                "value": self.max_acceleration,
                "unit": "m/s²"
            },
            "Thruster Power": {
                "value": self.power_thruster,
                "unit": "GW"
            },
            "Number of Thrusters": {
                "value": self.no_thrusters,
                "unit": ""
            },
        }
        self.entry = MultiEntry(self.data.main_frame, "Propulsion", entry)

    def make_display(self):
        """Make the Data Display."""
        data = {
            "Total Thruster Power": {
                "value": self.power_total_thruster,
                "unit": "GW"
            },
            "Total Thruster Mass": {
                "value": self.mass_total_thruster,
                "unit": "kg"
            },
            "Retained Waste Power": {
                "value": self.waste_power,
                "unit": "GW"
            }
        }
        self.data_display = MultiDisplay(self.data.main_frame, "Propulsion Data")
        self.data_display.make_display(data)

    def calculate(self):
        """Do the calculations."""
        power_thruster = self.power_thruster.get()
        # max_acceleration = self.max_acceleration.get()
        no_thrusters = self.no_thrusters.get()
        mass_thruster = power_thruster * self.propulsion["Thruster Mass"]
        power_total_thruster = power_thruster * no_thrusters
        mass_total_thruster = mass_thruster * no_thrusters
        waste_power = power_thruster * self.propulsion["Waste Factor"]

        self.mass_total_thruster.set(mass_total_thruster)
        self.power_total_thruster.set(power_total_thruster)
        self.waste_power.set(waste_power)