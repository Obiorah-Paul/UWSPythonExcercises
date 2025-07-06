# 1. Initialize the variable
sum_of_squares = 0

# 2. Use a for loop to iterate through numbers 1 to 5
for number in range(1, 6):  # range(1, 6) includes 1 to 5
    # 3. Add the square of the current number to sum_of_squares
    sum_of_squares += number ** 2

# 4. Print the final result
print("The sum of squares from 1 to 5 is:", sum_of_squares)