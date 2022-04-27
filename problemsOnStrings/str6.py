# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def mixing(a, b):
    amix = b[:2] + a[-1]
    bmix = a[:2] + b[-1]

    return amix + ' ' + bmix


print(mixing('abc', 'xyz'))
