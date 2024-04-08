def main():
    print("TEMPERATURE CONVERTER")
    print("\nEnter the temperature value")
    print("\nEnter the unit of measurement: \nC. Celsius \nF. Fahrenheit \nK. Kelvin")
    
    temp = float(input("\nTemperature: "))
    unit = input("Temperature system: ").upper()
    
    if unit == 'C':
        print("Fahrenheit:", 9.0/5.0 * temp + 32)
        print("Kelvin:", temp + 273.15)
    elif unit == 'F':
        print("Celsius:", 5.0/9.0 * (temp - 32))
        print("Kelvin:", (temp + 459.67) * 5.0/9.0)
    elif unit == 'K':
        print("Celsius:", temp - 273.15)
        print("Fahrenheit:", temp * 9.0/5.0 - 459.67)

if __name__ == "__main__":
    main()