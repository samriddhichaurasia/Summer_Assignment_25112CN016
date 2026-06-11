##write function to find sum of two numbers
def find_sum(a,b):
    result = a + b ##adding two numbers
    return a+b ##returning the result
##take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
##call the function and print the result
print("sum=",find_sum(a,b))