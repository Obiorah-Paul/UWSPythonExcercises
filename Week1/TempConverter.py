# Welcome message
print("Welcome to the Temperature Converter!\n")

# Get user input and convert it to a float
celsius_input = float(input("Please enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit: F = (C * 9/5) + 32
degree_f = (celsius_input * 9/5) + 32

# Convert Celsius to Kelvin: K = C + 273.15
degree_k = celsius_input + 273.15

# Output result
print(f"\nThe temperature you have entered is {celsius_input} degree Celsius.\n")

print("Converted Temperatures:")
print(f"{celsius_input} degree Celsius is equal to {degree_f} Fahrenheit.")
print(f"{celsius_input} degree Celsius is equal to {degree_k} Kelvin.\n")

# Goodbye message
print("Thank you for using the Temperature Converter!")