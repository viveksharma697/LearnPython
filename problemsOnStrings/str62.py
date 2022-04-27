# Write a Python program to compute sum of digits of a given string. 

def digitSum(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit
     
print(digitSum("123abcd45"))
print(digitSum("abcd1234"))