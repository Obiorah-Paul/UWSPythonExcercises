# Week Practical 
## Week 2 Report

### Section 1: Comparisons and Conditions

#### Exercise 1: Comparison Operators
This exercise helped me understand how Python uses Boolean logic to compare values, returning True or False.
```python
x = 8
y = 8

print(x == y)   # returns True because 8 is equal to 8

x = 3
y = 3

print(x != y)   # returns False because 3 is equal to 3

x = 2
y = 5

print(x > y)    # returns False because 2 is not greater than 5

x = 6
y = 7

print(x < y)   # returns True because 6 is less than 7

x = 4
y = 5

print(x >= y)   # returns False because 4 is less, or equal, to 5

x = 6
y = 8

print(x <= y)   # returns True because 6 is neither greater than or equal to 8
```
#### Output when run:
```python
True
False
False
True 
False
True 
```
### Logical Operators
#### Exercise 2
```python
# AND Operator
x = 10

print(x > 5 and x < 15)  # returns True because 10 is greater than 5 AND 10 is less than 15

# OR Operator
x = 8

print(x > 4 or x < 7)   # returns True because one of the conditions are true (8 is greater than 4, but 8 is not less than 7)

# NOT Operator
x = 6

print(not(x > 3 and x < 10))    # returns False because not is used to reverse the result
```
#### Outcome when run:
```python
True
True
False
```
### If Statements
#### Exercise 3
```python
age = 19
age_group = "child"

# Checks if the age is greater than 18
if age > 18:
    age_group = "adult"  # If the condition is true, reassign age_group to 'adult'

# Prints the final age group result using an f-string
print(f"The age group is {age_group}")
```
#### Outcome when run:
```python
The age group is adult
```

#### Second program
```python
age = 17
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")
```
#### output when run:
```python
The age group is child
```

## If-Else Statements
Using 'else' condition helped me control two possible outcomes from a single condition.

```python
wind_speed = 30

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```

### Task: 
Run this program twice, once with the given wind speed and once when you change the speed to something below 10. Observe the output and you will see that depending on the wind speed, different parts will be executed.

```python
# Task 1: When wind_speed = 30, above 10
wind_speed = 30

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

```
#### Output when run:
```python
It is a windy day
```
```python
# Task 2: When wind_speed = 5, below 10
wind_speed = 5

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```
#### Output when run:
```python
It is a calm day
```
### Observation:
The program uses an if-else statement to decide what message to show based on the wind speed. When you change the value of wind_speed, the output changes to match the weather condition either a calm or a windy day.

## If-Elif-Else Conditions
### Exercise 6
#### Task:
- Create two variables, temperature1 and temperature2, and assign different values to them.
- Use an if statement to check if the temperatures are equal and print a corresponding message.
- Use an else statement to print a message if the temperatures are not equal.
- Run the code and see if your statement has been built correctly. 

### Code:
```python
temperature1 = 23
temperature2 = 25

if temperature1 == temperature2:
    print("Temperatures are equal")  # This helped reinforce comparison logic using real-life examples like temperatures.
else:
    print("Temperatures are not equal")

```

### Output when run:
```python
Temperatures are not equal
```
## Python Lists
### Exercise 1: Creating a List 
#### Task: Create a list in the variable city_list. It should contain the following items in this order: "Glasgow", "London", "Edinburgh”. 
```python
city_list = ["Glasgow", "London", "Edinburgh"]
```

### Exercise 2: Accessing a List
#### Task: Print the third item in the city_list list. Then print the last two items in the city_list list as well using slicing. 
```python
print(city_list[2])
print(city_list[1:])
```
### output when run:
```python
Edinburgh
['London', 'Edinburgh']
```
### Exercise 3: Modifying a List
#### Task: Add the item "Manchester" to the end of the city_list list. Then change the second item in the city_list list to "Birmingham". 
```python
city_list.append("Manchester")
city_list[1] = "Birmingham"

print(city_list) # Being able to add and update list items makes them really flexible for data storage.
```

### output when run:
```python
['Glasgow', 'Birmingham', 'Edinburgh', 'Manchester']
```
### Exercise 4: Summary Task
#### Task Create, Access and Modify Lists:
- Write Python code to create a list named colours containing the names of three colours as strings.
- Print the entire list.
- Access the second element of the colours list and print it. 
- Modify the first element of the list to a new colour of your choice. 
- Print the modified list.
- Check and print the length of the colours list using the len() method. This is similar to using the similar to using the type() method from before.
- Use a conditional to check if "red" is in the colours list. If yes, print that “Red is in the list”.
- Use slicing to create a new list named selected_colours containing the second and third elements from the colours list.
- Print the selected_colours list. 
### Code
```python
# Create a list of colours
colours = ["red", "blue", "green"]

# Print the entire list
print(colours)

# Access and print the second element in the list
print(colours[1])  # Output: blue

# Modify the first element of the list
colours[0] = "yellow"

# Print the modified list
print(colours)

# Check the length of the list using len()
print("Length of list:", len(colours))

# Check if "red" is in the list
if "red" in colours:
    print("Red is in the list")
else:
    print("Red is not in the list")

# Create a new list with the second and third items using slicing
selected_colours = colours[1:3]

# Print the sliced list
print("Selected colours:", selected_colours)
```
### Output when run:
```python
['red', 'blue', 'green']
blue
['yellow', 'blue', 'green']
Length of list: 3
Red is not in the list
Selected colours: ['blue', 'green']
```
### Python Loops
Task: Create a for loop that prints each item in the city_list list.
```python
city_list = ["Glasgow", "London", "Edinburgh"]

# Loop through each city in the list and print it
for city in city_list:
    print(city)
```
### Output when run:
```python
Glasgow
London
Edinburgh
```
This loop goes through each city in the list one at a time and prints it out. It’s like saying, “Hey, give me the next city,” and then showing it, until the list is finished.
```python
for i in range(5): 
    if i == 2: 
        break 
    print(i)
```

Task: Modify the above code to print the numbers 0 through 4, but stop the loop when i is equal to 3. 
```python
for i in range(5):
    if i == 3:
        break
    print(i)
```
### Output when run:
```python
0
1
2
```
This loop starts at 0 and goes up to 4, but as soon as i becomes 3, it stops the loop and doesn’t print anything after that. So it will print 0, 1, and 2 then break out of the loop before printing 3.

## Summary Task
### Task 1: Even Numbers
- Create a list called numbers which contains the integers from 1 to 10.
- Use a for loop to iterate through the list and only print the even numbers. (Hint: use the modulo % operator) 
```python
# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop through each number in the list
for number in numbers:
    # Check if the number is even
    if number % 2 == 0:
        print(number)
```
### Output when run:
```python
2
4
6
8
10
```
We first make a list of numbers from 1 to 10. Then, for each number, we check if it’s even by using % 2 == 0. If it is, we print it. This way, only the even numbers come out.

### Task 2: Sum of Squares
- Create a variable sum_of_squares and initialize it to 0.
- Use a for loop to iterate through the numbers from 1 to 5 (inclusive) using the range() function.
- Add the square of each number to sum_of_squares.
- Print the final value of sum_of_squares. (Hint: if you do it correctly, the result should be 55) 
```python
# Step 1: Initialize the variable
sum_of_squares = 0

# Step 2 & 3: Loop through numbers 1 to 5 and add their squares to sum_of_squares
for i in range(1, 6):  # range(1, 6) includes numbers 1 to 5
    sum_of_squares += i ** 2  # Square the number and add it to the total

# Step 4: Print the result
print("The sum of squares from 1 to 5 is:", sum_of_squares)
```
### Output when run:
```python
The sum of squares from 1 to 5 is: 55
```
### Task 3: Countdown:
- Create a variable countdown and initialize it to 10.
- Use a while loop to print a countdown from the value of countdown to 1.
- After the countdown, print "Liftoff!" 
```python
# Step 1: Initialize the countdown variable
countdown = 10

# Step 2: Use a while loop to count down to 1
while countdown > 0:
    print(countdown)
    countdown -= 1  # Decrease the value by 1 each time

# Step 3: Print "Liftoff!" after the loop ends
print("Liftoff!")
```
### Output when run:
```python
10
9
8
7
6
5
4
3
2
1
Liftoff!
```
## Obtaining User Input 
### Task: User Input and Conditional Statements 
Write a code that takes the user's age as input. If the age is less than 18, print "You are a minor." If the age is between 18 and 65 (inclusive), print "You are an adult." If the age is greater than 65, print "You are a senior citizen." 
```python
# User enter their age
age = int(input("Enter your age: "))

# conditionals to determine the age group
if age < 18:
    print("You are a minor.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```
### Task: Temperature Converter 
Modify the temperature converter from last’s week lab class to also take a user input. The user should be able to enter a value in degrees Celsius and your converter should convert this to Fahrenheit and Kelvin.  As an extra task, (if you are finished before the class is over or want to practice a bit more Python) you should allow the user of the program to enter what temperature they want to convert (C, K or F) and then print out the conversions. Use conditionals for this.
```python
# Welcome message
print("Welcome to the Temperature Converter!")

# User input what unit they want to convert from
unit = input("Enter the temperature unit you want to convert from (C, F, or K): ").strip().upper()

# Ask user for the temperature value
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

# Goodbye message
print("\nThank you for using the Temperature Converter!")
```
### Output when run:
```python
Welcome to the Temperature Converter!
Enter the temperature unit you want to convert from (C, F, or K): c
Enter the temperature value: 40

You entered 40.0°C.
40.0°C is equal to 104.00°F.
40.0°C is equal to 313.15K.

Thank you for using the Temperature Converter!
```