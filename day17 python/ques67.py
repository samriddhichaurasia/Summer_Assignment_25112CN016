# Function to find intersection of two arrays
def intersection_arrays(arr1, arr2):

    # Empty list to store common elements
    intersection = []

    # Check each element of first array
    for num in arr1:

        # Element should be present in second array
        # and should not be repeated in result
        if num in arr2 and num not in intersection:
            intersection.append(num)

    return intersection


# Input arrays
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

# Function call
result = intersection_arrays(arr1, arr2)

# Display result
print("Intersection:", result)