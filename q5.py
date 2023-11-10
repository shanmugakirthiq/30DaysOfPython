temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

if unit == 'C' or unit == 'c':
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif unit == 'F' or unit == 'f':
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius)
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
