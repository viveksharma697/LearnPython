# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def func(a):
    b = a.find('not')
    c = a.find('poor')

    if c > b and b > 0 and c > 0:
        a = a.replace(a[b:(c+4)], 'good')
        return a
    else:
        return a
    


print(func('The lyrics is not that poor!'))
print(func('The lyrics is poor!'))
