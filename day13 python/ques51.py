##largest and smallest using functions
# Program to find the largest and smallest element in an array

arr = list(map(int, input("Enter elements separated by space: ").split()))

largest = max(arr)      # Finds largest element
smallest = min(arr)     # Finds smallest element

print("Largest element:", largest)
print("Smallest element:", smallest)