# Function to find all pairs having the required sum
def pair_sum(arr, target):

    # Variable to check whether pair exists
    found = False

    # Compare every element with every other element
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):

            # Check if pair sum equals target
            if arr[i] + arr[j] == target:
                print(arr[i], "+", arr[j], "=", target)
                found = True

    # If no pair found
    if not found:
        print("No pair found.")


# Input array
arr = list(map(int, input("Enter array elements: ").split()))

# Input target sum
target = int(input("Enter target sum: "))

# Function call
pair_sum(arr, target)