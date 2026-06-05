##findin largest prime factor of a number
num=int(input("Enter a number: "))
original=num
largest_factor=0
for i in range(2,original+1):
    while num%i==0:
        largest_factor=i
        num//=i
if largest_factor==0:
    print(f"{original} is a prime number and its largest prime factor is itself.")
else:
    print(f"The largest prime factor of {original} is: {largest_factor}")