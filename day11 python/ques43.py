##function to check prime number
def is_prime(n):
    if n < 2: ## 0 and 1 are not prime numbers
        return False ##checking if n is less than 2
    for i in range(2, int(n**0.5) + 1): ##looping from 2 to square root of n
        if n % i == 0: ##checking if n is divisible by i
            return False ##returning false if it is divisible
    return True ##returning true if it is not divisible by any number
##take input from user
n = int(input("Enter a number: "))
##call the function and print the result
if is_prime(n):
    print(n, "is a prime number") ##printing if n is prime  
else:
    print(n, "is not a prime number") ##printing if n is not prime
    