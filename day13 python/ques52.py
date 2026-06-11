# Program to count even and odd elements in an array

arr = list(map(int, input("Enter elements: ").split()))

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even elements:", even)
print("Odd elements:", odd)