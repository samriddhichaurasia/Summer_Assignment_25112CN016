# Take input from the user
num = int(input("Enter an integer: "))

# Initialize the reversed number variable
reversed_num = 0

# Store the sign for handling negative numbers
sign = -1 if num < 0 else 1
num = abs(num)

# Loop until all digits are extracted
while num > 0:
    # Get the last digit using modulo operator
    digit = num % 10
    
    # Append the digit to the reversed number
    reversed_num = (reversed_num * 10) + digit
    
    # Remove the last digit from the original number
    num = num // 10

# Reapply the original sign
reversed_num *= sign

print("Reversed Number:", reversed_num)
