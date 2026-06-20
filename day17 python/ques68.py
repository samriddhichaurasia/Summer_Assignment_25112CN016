# Function to find common elements
def common_elements(arr1, arr2):

    common = []

    for num in arr1:
        if num in arr2 and num not in common:
            common.append(num)

    return common


# Input arrays
arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

# Function call
result = common_elements(arr1, arr2)

print("Common Elements:", result)