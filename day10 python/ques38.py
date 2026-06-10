##print inverted pyramid pattern of stars
rows=int(input("Enter the number of rows for the pattern: "))
for i in range(rows,0,-1):
##-1 is used to decrement the value of i in each iteration, starting from rows and ending at 1.
    for j in range(rows-i):
        print(end=" ")
    ## j is used for spaces
    for k in range(1,i+1):
    ##k is used for stars
        print("*", end=" ")
    print()