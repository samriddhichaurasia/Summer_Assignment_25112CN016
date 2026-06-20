# Function to remove duplicate elements
def remove_duplicates(arr):

    # Convert list to set
    # Set automatically removes duplicates
    unique_elements = set(arr)

    # Convert set back to list
    return list(unique_elements)


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
result = remove_duplicates(arr)

# Display result
print("Array after removing duplicates:")
print(result)