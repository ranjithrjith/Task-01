def count_unique_chars(input_string):
    """
    This function takes a string as input and returns the number of unique characters in it.
    """
    # Convert the input string to a set to remove duplicates
    unique_chars = set(input_string)
    # Return the length of the set
    return len(unique_chars)

# Test the function with the given input string
input_string = "Ranjith and co"
unique_char_count = count_unique_chars(input_string)

# Print the results
print(f"The input string is: {input_string}")
print(f"The number of unique characters in the input string is: {unique_char_count}")