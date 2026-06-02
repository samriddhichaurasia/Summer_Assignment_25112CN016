# Take input from the user
num = int(input("Enter a number: "))

# Initialize sum variable
digit_sum = 0

# Store original number for absolute processing
n = abs(num)

# Loop to extract and sum digits
while n > 0:
    digit_sum += n % 10  # Extract the last digit
    n //= 10             # Remove the last digit

print(f"The sum of digits of {num} is: {digit_sum}")
