import math

def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
        
    # Check for factors from 2 up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # Factor found, so it's not prime
            
    return True  # No factors found, it is prime

# --- Example Usage ---
user_input = int(input("Enter a number to check: "))

if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")
