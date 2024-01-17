def longest_common_substring(str1, str2):
    """
    This function takes two strings as input and returns the longest common substring between them.
    """
    # Initialize variables to store the length and starting index of the longest common substring
    max_len = 0
    start_index = 0

    # Create a 2D array to store the lengths of common substrings
    lengths = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # Iterate over each character in the first string
    for i in range(1, len(str1) + 1):
        # Iterate over each character in the second string
        for j in range(1, len(str2) + 1):
            # If the characters match
            if str1[i - 1] == str2[j - 1]:
                # Update the length of the common substring
                lengths[i][j] = lengths[i - 1][j - 1] + 1
                # If the length of the common substring is greater than the current maximum
                if lengths[i][j] > max_len:
                    # Update the maximum length and starting index
                    max_len = lengths[i][j]
                    start_index = i - max_len
            else:
                # If the characters do not match, reset the length of the common substring
                lengths[i][j] = 0

    # Return the longest common substring
    return str1[start_index:start_index + max_len]

# Test the function with the given input strings
str1 = "Ranjith and co"
str2 = "Ranjith and co is a foodchain company"
longest_common_substring = longest_common_substring(str1, str2)

# Print the results
print(f"The longest common substring between '{str1}' and '{str2}' is '{longest_common_substring}'.")