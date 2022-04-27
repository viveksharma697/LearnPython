# Write a function to print all the fibonacci numbers

def fibo(n):

    a = 0
    b = 1

    if n == 1:
        print(a)

    elif n <= 0:
        print("Please enter a valid number")
    
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)

n = input("Enter the number of fabonacci you want : ")
print(n, " fibonacci are :")
fibo(n)
