def most_frequent_chars(input_string):
    """
    This function takes a string as input and returns the most frequent characters in it.
    """
    # Create an empty dictionary to store the count of each character
    char_count = {}
    # Iterate over each character in the input string
    for char in input_string:
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_count[char] = 1
    # Find the maximum count of any character in the dictionary
    max_count = max(char_count.values())
    # Create a list of the characters with the maximum count
    most_frequent_chars = [char for char, count in char_count.items() if count == max_count]
    # Return the list of most frequent characters
    return most_frequent_chars

# Test the function with the given input string
input_string = "ranjith and co"
most_frequent_chars = most_frequent_chars(input_string)

# Print the results
print(f"The input string is: {input_string}")
if len(most_frequent_chars) == 1:
    print(f"The most frequent character in the input string is: {most_frequent_chars[0]}")
else:
    print("The most frequent characters in the input string are:")
    for char in most_frequent_chars:
        print(char)