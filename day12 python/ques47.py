##function to find nth Fibonacci number
def fibonacci(n):
    a=0 ##initializing a to 0
    b=1 ##initializing b to 1
    if n == 0: ##return 0 for position 1
        return a
    if n==2: ##return 1 for position 2
        return b
    ## calculate from position 3 onwards 
    for i in range(3,n+1): ##looping from 3 to n
        c = a + b ##calculating the next Fibonacci number
        a = b ##updating a to b
        b = c ##updating b to c
    return c ##returning the nth Fibonacci number
##take input from user
n = int(input("Enter the position of Fibonacci number: "))
print("fibonacci term=",fibonacci(n))