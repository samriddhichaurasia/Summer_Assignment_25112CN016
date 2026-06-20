# Function to find the second largest element
def second_largest(arr):

    # Remove duplicate values using set()
    unique_arr = list(set(arr))

    # Sort the array in ascending order
    unique_arr.sort()

    # Second largest element will be at second last position
    return unique_arr[-2]


# Input array from user
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
result = second_largest(arr)

# Display result
print("Second Largest Element =", result)