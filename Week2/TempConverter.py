print("Welcome to the Temperature Converter!")

# Ask the user what unit they want to convert from
unit = input("Enter the temperature unit you want to convert from (C, F, or K): ").strip().upper()

# Ask for the temperature value
temp = float(input("Enter the temperature value: "))

# Convert based on input unit
if unit == "C":
    degree_f = (temp * 9/5) + 32           # Celsius to Fahrenheit
    degree_k = temp + 273.15               # Celsius to Kelvin

    print(f"\nYou entered {temp}°C.")
    print(f"{temp}°C is equal to {degree_f:.2f}°F.")
    print(f"{temp}°C is equal to {degree_k:.2f}K.")

elif unit == "F":
    degree_c = (temp - 32) * 5/9           # Fahrenheit to Celsius
    degree_k = degree_c + 273.15           # Convert Celsius result to Kelvin

    print(f"\nYou entered {temp}°F.")
    print(f"{temp}°F is equal to {degree_c:.2f}°C.")
    print(f"{temp}°F is equal to {degree_k:.2f}K.")

elif unit == "K":
    degree_c = temp - 273.15               # Kelvin to Celsius
    degree_f = (degree_c * 9/5) + 32       # Convert Celsius result to Fahrenheit

    print(f"\nYou entered {temp}K.")
    print(f"{temp}K is equal to {degree_c:.2f}°C.")
    print(f"{temp}K is equal to {degree_f:.2f}°F.")

else:
    print("Invalid unit entered. Please use C, F, or K.")

print("\nThank you for using the Temperature Converter!")