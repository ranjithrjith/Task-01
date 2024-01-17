def is_anagram(str1, str2):
    """
    This function takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
    """
    # Remove all spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Check if the length of the strings is the same
    if len(str1) != len(str2):
        return False
    # Sort the characters in each string
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    # Check if the sorted strings are equal
    return sorted_str1 == sorted_str2

# Test the function with the given input strings
str1 = "ranjith and co"
str2 = "co and ranjith"
is_anagram = is_anagram(str1, str2)

# Print the results
print(f"The first string is: {str1}")
print(f"The second string is: {str2}")
if is_anagram:
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.")