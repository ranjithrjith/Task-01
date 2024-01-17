def remove_vowels(input_string: str) -> str:
    """
    This function takes a string as input and returns a new string with all the vowels removed.
    """
    # Define a string containing all vowels
    vowels = "AEIOUaeiou"
    # Remove all vowels from the input string
    output_string = "".join([char for char in input_string if char not in vowels])
    # Return the output string
    return output_string

# Test the function with the given input string
input_string = "Guvi Geeks Network Private Limited"
output_string = remove_vowels(input_string)

# Print the results
print(f"The input string is: {input_string}")
print(f"The output string with all vowels removed is: {output_string}")