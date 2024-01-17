def is_palindrome(input_string):
    """
    This function takes a string as input and returns True if it is a palindrome, and False otherwise.
    """
    # Remove all spaces and convert to lowercase
    input_string = input_string.replace(" ", "").lower()
    # Check if the input string is equal to its reverse
    return input_string == input_string[::-1]

# Test the function with the given input string
input_string = "madam"
is_input_string_palindrome = is_palindrome(input_string)

# Print the results
print(f"The input string is: {input_string}")
if is_input_string_palindrome:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")