##character frequency
# Input string from the user
text = input("Enter a string: ")

# Initialize an empty dictionary
frequency = {}

# Loop through each character in the string
for char in text:
    if char in frequency:
        frequency[char] += 1  # Increment count if character exists
    else:
        frequency[char] = 1   # Initialize count to 1 if character is new

# Print the result
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
