# 1. Create a new variable called my_string and store the given text
my_string = "This class covers OOP. COMP11124 Object Oriented Programming  5 Practical Lab Exercises - Week 1 v1.0 – 2024/2025"

# 2. Print the my_string variable
print("Original String:")
print(my_string)

# 3a. Convert my_string to uppercase
my_uppercase_string = my_string.upper()

# 3b. Convert my_string to lowercase
my_lowercase_string = my_string.lower()

# 3c. Replace "OOP" with "Object Oriented Programming"
my_new_string = my_string.replace("OOP", "Object Oriented Programming")

# 3d. Store the length of my_string
my_string_length = len(my_string)

# Print results
print("\nUppercase String:")
print(my_uppercase_string)

print("\nLowercase String:")
print(my_lowercase_string)

print("\nModified String with replacement:")
print(my_new_string)

print("\nLength of the original string:")
print(my_string_length)