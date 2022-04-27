# write a python program to find the prime numbers

def primeNo(num):
    prime = False
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                prime = True
                break
    if prime:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

num = int(input("Enter a Number: "))
primeNo(num)

