## binary to decimal
n = input("Enter a binary number: ")
l=list(n)
sum=0
l.reverse()
for i in range(len(l)):
    sum+=int(l[i])*(2**i)
print(f"The decimal equivalent of {n} is: {sum}")

