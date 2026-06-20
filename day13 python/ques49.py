## Take size of array
n = int(input("Enter size: "))
arr = []                # empty list

# Take n elements from user
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)     # add element to list

# Display array
print("Array =", arr)