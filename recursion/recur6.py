# check with the help of the recursive methos wether the number is even or odd

def check(n):
    if n<2:
        return (n%2==0)
    else:
        return (check(n-2))

n = int(input("Enter your number: "))

if check(n) == True:
    print("The number is even  !!!")
else:
    print("The number is odd !!!")