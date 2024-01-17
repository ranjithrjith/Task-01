# Define the number of rows in the pyramid
num_rows = 5

# Define a variable to keep track of the current number
current_num = 1

# Iterate over each row in the pyramid
for row in range(num_rows):
    # Print the spaces before the numbers
    print(" " * (num_rows - row - 1), end="")
    # Iterate over each number in the row
    for col in range(row + 1):
        # Print the current number
        print(current_num, end=" ")
        # Increment the current number
        current_num += 1
    # Print a new line after each row
    print()