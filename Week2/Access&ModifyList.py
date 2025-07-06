# Create a list named colours with three colour names
colours = ["blue", "green", "yellow"]

# Print the entire list
print("Original colours list:", colours)

# Access the second element (index 1) and print it
print("Second colour in the list:", colours[1])

# Modify the first element (index 0) to a new colour
colours[0] = "purple"

# Print the modified list
print("Modified colours list:", colours)

# Print the length of the colours list using len()
print("Length of colours list:", len(colours))

# Check if "red" is in the list and print a message if it is
if "red" in colours:
    print("Red is in the list.")
else:
    print("Red is not in the list.")

# Use slicing to create a new list with the second and third elements
selected_colours = colours[1:3]

# Print the selected_colours list
print("Selected colours (2nd and 3rd):", selected_colours)