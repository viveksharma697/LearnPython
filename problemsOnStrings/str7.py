# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def ingly(a):
    if len(a) < 3:
        return a

    elif a[-3:] == 'ing':
        return a + 'ly'

    else:
        return a + 'ing'


print(ingly('abc'))
print(ingly('ab'))
print(ingly('string'))
