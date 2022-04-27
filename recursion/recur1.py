# convert a number to a binary string

def bin_str(n):
    if n == 0:
        return ''
    else:
        return bin_str(n // 2) + str(n % 2)

n = input("Enter the number : ")
print(n)
print("Binary number is : " + bin_str(n))

