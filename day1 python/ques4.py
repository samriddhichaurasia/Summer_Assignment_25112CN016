# Take input from the user
num = int(input("Enter a number: "))

# Use abs() to handle negative numbers, convert to string, and get length
digit_count = len(str(abs(num)))

print(f"The number of digits is: {digit_count}")
