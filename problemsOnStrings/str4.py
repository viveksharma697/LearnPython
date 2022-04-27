# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

a = 'w3resource'
b = a[0:2]
c = a[-2:]
print(b + c)

e = 'w3'
print(e + e)

f = 'w'
def func(x):
    if len(x) < 2:
        return ''
print(func(f))

