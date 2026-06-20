# Function to find union of two arrays
def union_arrays(arr1, arr2):

    # Combine both arrays and convert to set
    # Set automatically removes duplicate elements
    union = list(set(arr1 + arr2))

    return union


# Input first array
arr1 = list(map(int, input("Enter first array elements: ").split()))

# Input second array
arr2 = list(map(int, input("Enter second array elements: ").split()))

# Function call
result = union_arrays(arr1, arr2)

# Display result
print("Union of arrays:", result)