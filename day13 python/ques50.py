##sum and average using functions
## Take size and elements
n = int(input("Enter size: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Calculate sum
total = 0
for i in range(n):
    total = total + arr[i]  # add each element

# Calculate average
average = total / n         # sum divide by count

print("Sum =", total)
print("Average =", average)