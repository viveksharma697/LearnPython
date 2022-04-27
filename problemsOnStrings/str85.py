# Write a Python program to convert a given Bytearray to Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d

def bytearray_to_hexadecimal(list_val):
     result = ''.join('{:02x}'.format(x) for x in list_val)  
     return(result)

list_val = [111, 12, 45, 67, 109] 
print("Original Bytearray :")
print(list_val)
print("\nHexadecimal string:")
print(bytearray_to_hexadecimal(list_val))