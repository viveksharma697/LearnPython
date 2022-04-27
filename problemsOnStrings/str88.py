# Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length. 
# Sample Output:
# Input the string: W3resource
# ['Valid string.']

def check_string(s):
    messg = []
    if not any(x.isupper() for x in s):
        messg.append('String must have 1 upper case character.')
    if not any(x.islower() for x in s):
        messg.append('String must have 1 lower case character.')
    if not any(x.isdigit() for x in s):
        messg.append('String must have 1 number.')
    if len(s) < 8:
        messg.append('String length should be atleast 8.')    
    if not messg:
        messg.append('Valid string.')
    return messg
    
s = input("Input the string: ")
print(check_string(s))
