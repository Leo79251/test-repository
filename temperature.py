class TemperatureConverter:
    '''Responsible for verifying temperature values ​​and converting between Celsius and Fahrenheit'''
    ABS_ZERO_F = -459.67
    ABS_ZERO_C = -273.15
    
    def convert_fahrenheit_to_celsius(fahrenheit_str):
        '''Convert Fahrenheit to Celsius'''
        try:
            fahrenheit = float(fahrenheit_str)
        except ValueError:
            return "Please enter a number", "error"  # Return results and status

        if fahrenheit < TemperatureConverter.ABSOLUTE_ZERO_F:
            return "Temperature too low", "error"

        celsius = (fahrenheit - 32) * 5 / 9
        return f"{celsius:.2f} °C", "success"
    
    def convert_celsius_to_fahrenheit(celsius_str):
        '''Convert Celsius to Fahrenheit'''
        try:
            celsius = float(celsius_str)
        except ValueError:
            return "Please enter a number", "error"

        if celsius < TemperatureConverter.ABSOLUTE_ZERO_C:
            return "Temperature too low", "error"

        fahrenheit = (celsius * 9 / 5) + 32
        return f"{fahrenheit:.2f} °F", "success" 
    
    
import tkinter as tk
from tkinter import ttk
from TemperatureConverter import TemperatureConverter

class ConverterGUI:
    '''Temperature converter graphical user interface class'''
    def __init__(self, root):
        
            self.root = root
            self.root.title("Temperature Converter")
            self.root.geometry("500x400")
            
            self.converter = TemperatureConverter()
            
            self.STYLES = {
                        "bg_color": "#f0f0f0",
                        "button_bg": "#4a7a8c",
                        "button_fg": "white",
                        "error_color": "red",
                        "success_color": "green",
                        "main_button_yellow": "#ffcc00",
                        "main_button_pink": "#ff66b2"
                    }            

            

            self.root.configure(bg=self.STYLES["bg_color"])
            # Create a container frame to stack all screens
            self.container = ttk.Frame(root)
            self.container.pack(side="top", fill="both", expand=True)
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)            
            
                    
