def convert_temperature():
    print("Temperature Converter")
    choice = input("Convert from (C)elsius or (F)ahrenheit? ")

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")
        
convert_temperature()
