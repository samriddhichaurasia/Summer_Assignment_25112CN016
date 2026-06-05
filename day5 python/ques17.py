##check whether the given number is a perfect number or not
num=int(input("Enter a number: "))
sum=0
for i in range(1,int(num/2)+1):
 ##for loop repeats till stop-1
 ##factor is given by num/2
    if (num%i==0):
        sum+=i
if sum==num:
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")