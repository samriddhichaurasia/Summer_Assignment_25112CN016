##check strong number or not
num=int(input("Enter a number: "))
sum=0       
temp=num
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    temp//=10
  
if sum==num:
    print("The number is a strong number")
else:
    print("The number is not a strong number")  