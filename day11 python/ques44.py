##function to find factorial of a number
def find_factorial(n):
    fact=1 ##initializing factorial to 1
    for i in range(1,n+1): ##looping from 1 to n
        fact *= i
        ##multiplying fact with i
    return fact
 ##returning the factorial
##take input from user
n = int(input("Enter a number: "))
##call the function and print the result
print("factorial=",find_factorial(n))
