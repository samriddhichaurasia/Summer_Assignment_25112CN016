# Function to find duplicate elements
def find_duplicates(arr):

    # Empty list to store duplicate elements
    duplicates = []

    # Check every element in the array
    for num in arr:

        # If element appears more than once
        # and is not already added to duplicates list
        if arr.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    # Return duplicate elements
    return duplicates


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Function call
result = find_duplicates(arr)

# Print duplicate elements
print("Duplicate Elements:", result)