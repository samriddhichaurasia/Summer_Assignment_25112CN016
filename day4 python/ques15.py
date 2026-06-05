##to check armstrong number
num=int(input("Enter a number: "))
length=len(str(num)) ##for knowing the power of individual digits
temp=num
sum=0
while temp>0:
  digit=temp%10
  sum+=digit**length
  temp = temp//10
if num==sum:
  print("Armstrong number")
else:  print("Not an armstrong number")

