# Function to find the frequency of a given element in the array
def frequency(arr, key):

    # count() returns how many times the element appears
    return arr.count(key)


# Taking array input from the user
arr = list(map(int, input("Enter array elements: ").split()))

# Taking the element whose frequency is to be found
key = int(input("Enter element to find frequency: "))

# Calling the function
freq = frequency(arr, key)

# Displaying the result
print("Frequency of", key, "=", freq)