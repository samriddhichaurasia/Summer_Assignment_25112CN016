##function to check perfect number 
def is_perfect(n):
    total=0
##add all factors from 1 to n-1
for i in range (1,n):
    if n%i==0:
## i is a factor of n
          total=total+i
##if sum of factors equals n,it is perfect
     return total==n
##take input
n=int(input("Enter number:"))
if is_perfect(n):
    print("Perfect number")
else:
    print("Not perfect number")