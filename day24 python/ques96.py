##remove duplicate characters
# Accept string input from the user
user_input = input("Enter a string: ")

# Initialize an empty string to store unique characters
result = ""

# Loop through each character in the user input
for char in user_input:
    # Append the character only if it is not already in the result
    if char not in result:
        result += char

# Display the final output
print("String after removing duplicates:", result)
