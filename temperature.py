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

        