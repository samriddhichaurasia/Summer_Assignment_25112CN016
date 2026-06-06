##find x^n without pow()
a= int(input("Enter the base (x): "))
b= int(input("Enter the exponent (n): "))
result=1
for i in range(b):
    result*=a
print(f"{a} raised to the power of {b} is: {result}")

    