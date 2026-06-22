##count string length 
# Take input from the user
user_string = input("Enter a string: ")

# Initialize a counter variable
counter = 0

# Loop through each character in the string and it will count the number of string 
for character in user_string:
    counter += 1

# Display the result
print(f"The length of the string is: {counter}")
