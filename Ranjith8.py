def count_words(input_string):
    """
    This function takes a string as input and returns the number of words in it.
    """
    # Split the input string into words
    words = input_string.split()
    # Return the number of words
    return len(words)

# Test the function with the given input string
input_string = "Ranjith and co"
word_count = count_words(input_string)

# Print the results
print(f"The input string is: {input_string}")
print(f"The number of words in the input string is: {word_count}")