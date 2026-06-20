# Function to perform Binary Search
def binary_search(arr, key):

    low = 0
    high = len(arr) - 1

    while low <= high:

        # Find middle index
        mid = (low + high) // 2

        # Element found
        if arr[mid] == key:
            return mid

        # Search in right half
        elif arr[mid] < key:
            low = mid + 1

        # Search in left half
        else:
            high = mid - 1

    return -1


# Input sorted array
arr = list(map(int, input("Enter sorted array: ").split()))

# Input element to search
key = int(input("Enter element to search: "))

# Function call
result = binary_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")