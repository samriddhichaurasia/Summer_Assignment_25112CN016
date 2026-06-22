##convert lowercase to uppercase
# Take input from the user
user_input = input("Enter a lowercase string: ")

uppercase_result = ""

# Loop through each character in the string
for char in user_input:
    # Check if the character is lowercase
    if 'a' <= char <= 'z':
        # Convert to uppercase by subtracting 32 from its ASCII value
        uppercase_result += chr(ord(char) - 32)
    else:
        # Keep non-lowercase characters (spaces, numbers, symbols) as they are
        uppercase_result += char

# Display the output
print("Uppercase String:", uppercase_result)
