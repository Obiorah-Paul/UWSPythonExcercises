# This function takes a list of names and prints a greeting for each one

def greet_friends(names):  # Define the function 'greet_friends' that accepts one parameter called 'names'
    for name in names:  # Loop through each item in the list 'names'
        print(f"Hello {name}!")  # Print a personalized greeting using an f-string

# List of names to be passed into the function
friend_list = ["John", "Jane", "Jack"]

# Calling the function with the list of friends
greet_friends(friend_list)



def calculate_tax(income, tax_rate):
    # Calculate and return the tax amount
    tax = income * tax_rate
    return tax

# call the function with an income of £50,000 and tax rate of 0.2
tax1 = calculate_tax(50000, 0.2)
print("Tax on £50,000 with 20% rate:", tax1)

# different incomes and tax rates
tax2 = calculate_tax(35000, 0.15)
print("Tax on £35,000 with 15% rate:", tax2)

tax3 = calculate_tax(80000, 0.25)
print("Tax on £80,000 with 25% rate:", tax3)

tax4 = calculate_tax(100000, 0.3)
print("Tax on £100,000 with 30% rate:", tax4)


# define the function with the parameters: principal, duration, and interest_rate
def compound_interest(principal, duration, interest_rate):
    # check if interest_rate is valid (between 0 and 1)
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None  # exit the function early if rate is invalid

    # check if the duration is a valid positive number
    if duration < 0:
        print("Please enter a positive number of years")
        return None  # exit the function early if duration is invalid

    # calculating compound interest each year using for loop
    for year in range(1, duration + 1):
        # formula to calculate compound interest for the year
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {int(total_for_the_year)} £")

    # return the final amount as an integer
    return int(total_for_the_year)

# test the function with the given example
compound_interest(1000, 5, 0.03)

print("Hello, World!") 

favorite_color = "Blue"

print("My favorite color is", favorite_color)

# Convert number1 from string to integer
number1 = "5"
number2 = 3

# Use int() to convert string to integer before addition
result = int(number1) + number2

# Print the result
print("The sum is:", result)

fruits = ["apple", "banana", "cherry"]

# Access and print the second element (index 1)
print(fruits[1])