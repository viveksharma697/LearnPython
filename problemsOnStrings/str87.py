# Write a Python program find the common values that appear in two given strings. 
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python

def common_val(str1, str2):
    result = ""
    for ch in str1:
        if ch in str2:
            result += ch

    return result

