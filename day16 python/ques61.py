# Function to find the missing number
def find_missing(arr):

    # If one number is missing from 1 to n,
    # then total numbers should be len(arr)+1
    n = len(arr) + 1

    # Sum of first n natural numbers
    expected_sum = n * (n + 1) // 2

    # Actual sum of array elements
    actual_sum = sum(arr)

    # Difference gives the missing number
    return expected_sum - actual_sum


# Input array
arr = list(map(int, input("Enter elements (one number missing): ").split()))

# Function call
missing = find_missing(arr)

# Display result
print("Missing Number =", missing)