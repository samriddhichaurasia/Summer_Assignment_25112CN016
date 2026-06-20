# Function to sort array in descending order
def descending_sort(arr):

    # Sort array in reverse order
    arr.sort(reverse=True)

    return arr


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
result = descending_sort(arr)

print("Descending Order:", result)