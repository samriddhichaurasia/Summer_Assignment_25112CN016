##find common characters in string
# Accept two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Initialize an empty list to store unique common characters
common_characters = []

# Loop through each character of the first string
for char in string1:
    # Check if the character exists in the second string 
    # and has not been added to our common list yet
    if char in string2 and char not in common_characters:
        common_characters.append(char)

# Display the results
if common_characters:
    print("Common characters found:", common_characters)
else:
    print("No common characters found.")
