# Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]



def extracted_num(str):
    result = [int(str1) for str1 in str1.split() if str1.isdigit()]
    return result


str1 = 'red 12 black 45 green'
print('Original String: ' + str1)
print('Extract numbers from the said string: ')
print(extracted_num(str1))
