# python program to find the fibonacci series by recursion method

def fibo(n):
    if(n <= 1):
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
n = int(input("Enter the term: "))
print("The ", n,"th term of fibonacci series is :")
print(fibo(n))
