# Write a Python program to decapitalize the first letter of a given string.
# Sample Output:
# java Script
# python

def decapitalize_first_letter(s):
  return ''.join([s[:1].lower(), s[1:]]) 
print(decapitalize_first_letter('Java Script'))
print(decapitalize_first_letter('Python'))