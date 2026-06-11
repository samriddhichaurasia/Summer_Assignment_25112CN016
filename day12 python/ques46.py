##function to check armstrong number
def is_armstrong(n):
    original = n ##storing the original number
    digits = len(str(n)) ##getting the number of digits in n
    total = 0 ##initializing total to 0
    ##raise each digit to the power of number of digits and add to total
    while n!= 0: ##looping until n is not equal to 0
        last_digit = n % 10 ##getting the last digit of n
        total += last_digit ** digits ##adding the last digit raised to the power of digits to total
        n //= 10 ##removing the last digit from n
        ##if sum equals original number, then it is an armstrong number
    return total == original ##checking if total and original are equal
##take input from user
n = int(input("Enter a number: "))
##call the function and print the result
if is_armstrong(n):
    print(n, "is an armstrong number") ##printing if n is armstrong
else:
    print(n, "is not an armstrong number") ##printing if n is not armstrong