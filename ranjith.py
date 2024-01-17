# Define the input string
input_string = "Guvi Geeks Network Private Limited"

# Define a dictionary to store the vowel counts
vowel_counts = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}

# Loop through each character in the input string
for char in input_string:
    # Convert the character to uppercase
    char = char.upper()
    # Check if the character is a vowel
    if char in vowel_counts:
        # Increment the count for the vowel
        vowel_counts[char] += 1

# Calculate the total number of vowels
total_vowels = sum(vowel_counts.values())

# Print the results
print(f"The total number of vowels is {total_vowels}")
print("The count of each individual vowel is:")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")