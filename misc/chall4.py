# write a function that accepts a number as a parameter. The function should return a number that is difference between the largest and smallest numbers that the digits can form in the number. For example, if the parameter is "213", the function should return "198", which is the result of 123 subtracted from 321.


x = []


def toString(List):
    return x == x.append(''.join(List))


def permute(a, l, r):
    if l == r:
        return toString(a)
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]


string = "123"
n = len(string)
a = list(string)
permute(a, 0, n-1)
y = [int(i) for i in x]
y.sort()
z = y[-1] - y[0]
print("The difference between the highest and the lowest of the permutations of number is : ", z)
