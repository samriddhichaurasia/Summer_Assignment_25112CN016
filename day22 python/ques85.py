##check palindrome number
def is_palindrome_math(num):
    # Negative numbers cannot be palindromes due to the minus sign
    if num < 0:
        return False
        
    original_num = num
    reversed_num = 0
    
    # Loop to reverse the digits mathematically
    while num > 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num = num // 10  # Remove the last digit
        
    return original_num == reversed_num

# Get user input
user_input = int(input("Enter a number: "))

# Check and display results
if is_palindrome_math(user_input):
    print(f"{user_input} is a palindrome number.")
else:
    print(f"{user_input} is not a palindrome number.")
