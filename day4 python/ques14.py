##nth fibonacci term
def fib(n):
    if (n==0 or n==1):
        return n
    else:
        return (fib(n-1) + fib(n-2))
n=int(input("Enter a number: "))
print(f"The {n}th term of the fibonacci series is: {fib(n)}")