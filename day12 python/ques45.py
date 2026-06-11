##function to check palindrome 
def is_palindrome(n):
    original = n ##storing the original number
    reverse = 0 ##initializing reverse to 0
    ##reverse the number
    while n > 0: ##looping until n is greater than 0
        digit = n % 10 ##getting the last digit of n
        reverse = reverse * 10 + digit ##adding the digit to reverse
        n //= 10 ##removing the last digit from n
    return original == reverse ##checking if original and reverse are equal
##take input from user
n = int(input("Enter a number: "))
##call the function and print the result
if is_palindrome(n):
    print(n, "is a palindrome number") ##printing if n is palindrome    
else:
    print(n, "is not a palindrome number") ##printing if n is not palindrome
