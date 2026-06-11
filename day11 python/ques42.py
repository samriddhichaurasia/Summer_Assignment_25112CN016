##function to find maximum of two numbers
def find_max(a,b):
    if a > b: ##checking if a is greater than b
        return a ##returning a if it is greater
    else:
        return b ##returning b if it is greater
##take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
##call the function and print the result
print("maximum=",find_max(a,b))