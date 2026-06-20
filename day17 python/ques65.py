# Function to merge two arrays
def merge_arrays(arr1, arr2):

    # + operator joins both arrays
    merged = arr1 + arr2

    # Return merged array
    return merged


# Input first array
arr1 = list(map(int, input("Enter first array elements: ").split()))

# Input second array
arr2 = list(map(int, input("Enter second array elements: ").split()))

# Function call
result = merge_arrays(arr1, arr2)

# Display merged array
print("Merged Array:")
print(result)