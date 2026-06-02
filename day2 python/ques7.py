# Function to calculate product of digits
def get_digit_product(num):
    # Handle negative numbers by converting to absolute value
    num = abs(num)
    
    # Base case for zero
    if num == 0:
        return 0
        
    product = 1
    
    while num > 0:
        # Extract the last digit
        digit = num % 10
        # Multiply it with the running product
        product *= digit
        # Remove the last digit from the number
        num = num // 10
        
    return product

# Take user input
try:
    user_input = int(input("Enter an integer number: "))
    result = get_digit_product(user_input)
    print(f"The product of the digits of {user_input} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
