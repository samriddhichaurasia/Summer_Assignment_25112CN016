##to check armstrong number in a given range
lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
print(f"Armstrong numbers between {lower} and {upper} are: ")
for num in range(lower, upper+1):
    ## to include upper limit in the range we use upper+1
    length=len(str(num)) ##for knowing the power of individual digits
    temp=num
    sum=0
    while temp>0:   
        digit=temp%10
        sum+=digit**length
        temp = temp//10
    if num==sum:
        print(num)