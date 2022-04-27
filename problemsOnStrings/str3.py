# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def func(a):
   dict = {}
   for n in a:
       keys = dict.keys()
       if n in keys:
           dict[n] += 1
       else:
           dict[n] = 1
   return dict
print(func('google.com'))