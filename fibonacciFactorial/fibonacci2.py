# Write a program to print all the fibonacci numbers under 100


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
            if c <= n:
                print(c)
# n = input("Enter the value upto which you want to get the fibonacci no. : ")
fibo(100)



            
