import tkinter as tk

class TemperatureConverter:
    ABS_ZERO_C = -273.15
    ABS_ZERO_F = -459.67
    
    def fahrenheit_to_celsius(self, f_str):
        try:
            f_temp = float(f_str)
        except ValueError:
            return "Please enter a number"
        
        if f_temp < self.ABS_ZERO_F:
            return "Temperature too low"
        
        c_temp = (f_temp - 32) * 5 / 9
        return f"{c_temp:.2f} °C"
    
    def celsius_to_fahrenheit(self, c_str):
        try:
            c_temp = float(c_str)
        except ValueError:
            return "Please enter a number"
        
        if c_temp < self.ABS_ZERO_C:
            return "Temperature too low"
        
        f_temp = c_temp * 9 / 5 + 32
        return f"{f_temp:.2f} °F"


class ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x350")
        
        self.converter = TemperatureConverter()
        self.colors = {'bg': '#f0f0f0', 'yellow': '#fffacd', 'pink': '#ffc0cb', 'green': '#98fb98'}
        
        self.container = tk.Frame(root, bg=self.colors['bg'])
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        self.create_main_frame()
        self.create_to_c_frame()
        self.create_to_f_frame()
        self.show_frame("main")
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
    
    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_forget()
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
    
    def create_main_frame(self):
        frame = tk.Frame(self.container, bg=self.colors['bg'])
        self.frames["main"] = frame
        
        for i in range(5):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        tk.Label(frame, text="Temperature Converter", font=("Arial", 16, "bold"), 
                bg=self.colors['bg']).grid(row=1, column=0, pady=20)
        
        tk.Button(frame, text="Fahrenheit to Celsius", font=("Arial", 12),
                 bg=self.colors['yellow'], width=18, height=2,
                 command=lambda: self.show_frame("to_c")).grid(row=2, column=0, pady=10)
        
        tk.Button(frame, text="Celsius to Fahrenheit", font=("Arial", 12),
                 bg=self.colors['pink'], width=18, height=2,
                 command=lambda: self.show_frame("to_f")).grid(row=3, column=0, pady=10)
        
        return frame
    
    def create_to_c_frame(self):
        frame = tk.Frame(self.container, bg=self.colors['bg'])
        self.frames["to_c"] = frame
        
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        
        tk.Label(frame, text="Fahrenheit to Celsius", font=("Arial", 14, "bold"),
                bg=self.colors['bg']).grid(row=0, column=0, columnspan=2, pady=15)
        
        tk.Label(frame, text="Enter Fahrenheit:", font=("Arial", 11),
                bg=self.colors['bg']).grid(row=1, column=0, columnspan=2, pady=5)
        self.f_entry = tk.Entry(frame, font=("Arial", 11), width=18)
        self.f_entry.grid(row=2, column=0, columnspan=2, pady=5, padx=20)
        
        self.c_result = tk.Label(frame, text="", font=("Arial", 11), bg=self.colors['bg'])
        self.c_result.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(frame, text="Calculate", font=("Arial", 11), bg=self.colors['green'],
                 width=12, command=self.calc_f_to_c).grid(row=4, column=0, pady=15, padx=5)
        
        tk.Button(frame, text="Reset", font=("Arial", 11), bg="#ffb6c1",
                 width=12, command=lambda: self.reset(self.f_entry, self.c_result)
                 ).grid(row=4, column=1, pady=15, padx=5)
        
        tk.Button(frame, text="Back to Main", font=("Arial", 11), bg="#d3d3d3",
                 width=15, command=lambda: self.show_frame("main")
                 ).grid(row=5, column=0, columnspan=2, pady=10)
        
        return frame
    
    def create_to_f_frame(self):
        frame = tk.Frame(self.container, bg=self.colors['bg'])
        self.frames["to_f"] = frame
        
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        
        tk.Label(frame, text="Celsius to Fahrenheit", font=("Arial", 14, "bold"),
                bg=self.colors['bg']).grid(row=0, column=0, columnspan=2, pady=15)
        
        tk.Label(frame, text="Enter Celsius:", font=("Arial", 11),
                bg=self.colors['bg']).grid(row=1, column=0, columnspan=2, pady=5)
        self.c_entry = tk.Entry(frame, font=("Arial", 11), width=18)
        self.c_entry.grid(row=2, column=0, columnspan=2, pady=5, padx=20)
        
        self.f_result = tk.Label(frame, text="", font=("Arial", 11), bg=self.colors['bg'])
        self.f_result.grid(row=3, column=0, columnspan=2, pady=10)
        
        tk.Button(frame, text="Calculate", font=("Arial", 11), bg=self.colors['green'],
                 width=12, command=self.calc_c_to_f).grid(row=4, column=0, pady=15, padx=5)
        
        tk.Button(frame, text="Reset", font=("Arial", 11), bg="#ffb6c1",
                 width=12, command=lambda: self.reset(self.c_entry, self.f_result)
                 ).grid(row=4, column=1, pady=15, padx=5)
        
        tk.Button(frame, text="Back to Main", font=("Arial", 11), bg="#d3d3d3",
                 width=15, command=lambda: self.show_frame("main")
                 ).grid(row=5, column=0, columnspan=2, pady=10)
        
        return frame
    
    def calc_f_to_c(self):
        result = self.converter.fahrenheit_to_celsius(self.f_entry.get())
        # Updated condition to catch 'too low' error message styling
        self.c_result.config(text=result, fg="red" if any(x in result.lower() for x in ["low", "please"]) else "black")
    
    def calc_c_to_f(self):
        result = self.converter.celsius_to_fahrenheit(self.c_entry.get())
        # Updated condition to catch 'too low' error message styling
        self.f_result.config(text=result, fg="red" if any(x in result.lower() for x in ["low", "please"]) else "black")
    
    def reset(self, entry_widget, result_label):
        entry_widget.delete(0, tk.END)
        result_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()
