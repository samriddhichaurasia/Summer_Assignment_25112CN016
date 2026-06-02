# Take input from the user
num = int(input("Enter a number: "))

# Store the original number in a temporary variable
temp = num
reverse_num = 0

# Loop to reverse the number
while temp > 0:
    digit = temp % 10
    reverse_num = (reverse_num * 10) + digit
    temp //= 10

# Compare original number with the reversed number
if num == reverse_num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
