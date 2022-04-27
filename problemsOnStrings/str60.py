# Write a Python program to capitalize first and last letters of each word of a given string.

def first_capital(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(first_capital("python exercises practice solution"))
print(first_capital("capitalme"))