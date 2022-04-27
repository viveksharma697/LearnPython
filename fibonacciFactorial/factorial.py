# Write a function to print first n number of factorials

def facto(n):

    a = 1
    b = 2

    if n == 1:
        print(a)

    elif n <= 0:
        print("Please enter a valid number")
    
    else:
        print(a)

        for i in range(2, n):
            a = a * b
            b = b + 1
            print(a)

n = input("Enter the number : ")
print(n, " factorial is :")
facto(n)